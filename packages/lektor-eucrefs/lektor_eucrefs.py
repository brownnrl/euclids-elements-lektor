"""Mistune extension for Euclid's Elements citations + diagram element
references + proof markers.

Authoring syntax in markdown bodies:

    Inline:   @I.5  @I.Def.10  @I.Post.3  @C.N.1  @II.4  @XI.Def.2
              {AB}  {BCD}
    Block:    [!just I.3, I.46; I.31]
              [!qed]
              [!qef]
              [!title Lemma 1]

`@TOKEN` resolves to a URL under
`/elements/books/book{N}/{section}/{slug}/`. The `[!just …]` block
renders as `<div class="just">…<a/>, <a/><br><a/>…</div>` — same shape
the proof templates already expect.

`{NAME}` marks a geometric element reference. Rendered as
`<span class="elem-ref" data-elem="NAME">NAME</span>`. The browser-side
`elem-ref-highlight.js` binds hover/touch handlers that flip the
corresponding geomlib element's `shouldHighlight` flag. The JS resolves
the target slate by walking up to the enclosing `<div class="theorem">`
section, then picking the first canvas inside it with a matching
element (falling back to the first canvas on the page).

`[!qed]` / `[!qef]` emit `<div class="qed">Q.E.D.</div>` and
`<div class="qed">Q.E.F.</div>` proof-end markers. `[!title TEXT]`
emits `<div class="title">TEXT</div>` for lemma/sub-section titles.
These replace raw HTML in markdown source.

Tokens recognized for `@`:
  - `{Roman}.{number}`          → proposition  e.g. I.5, II.13, XIII.18
  - `{Roman}.Def.{number}`      → definition   e.g. I.Def.10, XI.Def.2
  - `{Roman}.Post.{number}`     → postulate    e.g. I.Post.3
  - `C.N.{number}`              → common notion (Book I)  e.g. C.N.1
  - `X.Def.{I|II|III}.{number}` → Book X subsection definition
                                  e.g. X.Def.I.3, X.Def.II.1, X.Def.III.6.
                                  Book X follows Heath/Joyce/Heiberg in
                                  restarting numbering per subsection:
                                  DefsI has 4, DefsII and DefsIII have 6
                                  each. The slug carries the Roman
                                  subsection: `defX.I.3`, `defX.II.1`,
                                  `defX.III.6`.

Anything else (typos, unrecognized prefix) becomes `<a href="#unresolved-…">`
so it surfaces visibly when proofreading the rendered page.

Reusability note: when adding Apollonius / Hilbert / Archimedes content
later, register a second resolver under a different prefix scheme
(e.g. `@Apol.II.4`) and dispatch on the prefix.
"""
import os
import re

from lektor.pluginsystem import Plugin


ROMAN_VALID = {
    "I", "II", "III", "IV", "V", "VI", "VII", "VIII",
    "IX", "X", "XI", "XII", "XIII",
}

# Two regexes — inline tokens (prefixed with @) and the block directive.
# The Roman-numeral alternation is built from the explicit set above so we
# don't accidentally match arbitrary uppercase letter runs.
_ROMAN_ALT = "|".join(sorted(ROMAN_VALID, key=len, reverse=True))
# Token grammar (order matters — longest match first):
#   X.Def.{I|II|III}.{N}    — Book X subsection notation
#   {Roman}.{N}.Cor         — corollary of proposition N
#   {Roman}.(Def|Post).{N}  — standard def/post citation
#   {Roman}.{N}             — proposition citation
#   C.N.{N?}                — common notion (Book I), optional number
_TOKEN_BARE = (
    rf"(?:X\.Def\.(?:III|II|I)\.\d+"
    rf"|(?:{_ROMAN_ALT})\.\d+\.Cor"
    rf"|(?:{_ROMAN_ALT})\.(?:Def\.|Post\.)?\d+"
    rf"|C\.N\.\d*)"
)
INLINE_RE = re.compile(rf"@({_TOKEN_BARE})")
BLOCK_RE = re.compile(r"\[!just\s+(.+?)\]")

# Element-reference inline shortcode: {NAME} or {DISPLAY|element}.
#   NAME — Joyce/Euclid label: letter-led, may carry digits, primes,
#          hyphens (e.g. A, AB, BCD, A', ABC'). Underscores are
#          deliberately excluded — mistune's inline lexer stops at `_`
#          (emphasis prefix), which would split the token.
#   The optional `|element` part (display override) renders DISPLAY
#   but binds the highlight to `element` — for prose names that
#   collide with another element's name, e.g. "the angle {ABC|angBint}"
#   where the bare token would resolve to the triangle ABC. The
#   element part may carry digits (angBint) but follows the same
#   no-underscore constraint.
#
# The leading `!` was tried first (`{!AB}`) but mistune also stops at
# `!`. Bare `{NAME}` arrives intact at the text() walker, no lexer
# patch required. The constrained NAME pattern (letter-led identifier
# with no underscores) keeps free-form `{...}` prose from matching.
#
# An optional trailing `:N` selector names the canvas the ref should
# light, for multi-canvas pages where the browser's fallback (nearest
# preceding canvas) is not what the prose means. N is the canvas INDEX:
#   {AB:1}            -> data-canvas="canvas_1"
#   {ABC:0,1}         -> data-canvases="canvas_0,canvas_1"
#   {ABC|angABC:1}    -> override AND selector
# Both attributes are already understood by elem-ref-highlight.js; the
# multi form drives the cross-canvas highlight (geomlib >= 0.13, #130).
#
# The selector is an INDEX, not the id, precisely because mistune splits
# inline text at `_`: a literal `{AB:canvas_1}` reaches the text()
# walker as two chunks, 'Sel {AB:canvas' + '_1} and ...', so the token
# can never match. (The rejoined output still *looks* intact, which
# makes this easy to misdiagnose.) Keeping digits-only sidesteps the
# lexer entirely — no lexer patch, same as bare `{NAME}`.

ELEM_REF_RE = re.compile(
    r"\{(?P<name>[A-Za-z][A-Za-z0-9'\-]*)"
    r"(?:\|(?P<target>[A-Za-z][A-Za-z0-9'\-]*))?"
    r"(?::(?P<canvas>\d+(?:,\d+)*))?\}"
)

# Standalone block directives that REPLACE the paragraph they sit in.
# `[!just …]` keeps the existing in-paragraph extraction (floats right
# alongside the prose); [!qed] / [!qef] / [!title …] are full-width
# blocks that stand on their own line.
BLOCK_REPLACE_RE = re.compile(
    r"^\s*\[!(?P<kind>qed|qef|title)(?:\s+(?P<arg>[^\]]+))?\]\s*$"
)

# Combined inline pattern: citations AND element refs in one walk. The
# named groups disambiguate which kind of token matched.
_INLINE_ANY_RE = re.compile(
    rf"@(?P<cite>{_TOKEN_BARE})"
    rf"|\{{(?P<elem>[A-Za-z][A-Za-z0-9'\-]*)"
    rf"(?:\|(?P<target>[A-Za-z][A-Za-z0-9'\-]*))?"
    rf"(?::(?P<canvas>\d+(?:,\d+)*))?\}}"
)


# Book X subsection-restart numbering: each batch has its own 1..N
# range, matching Heath/Joyce/Heiberg. Folder slugs carry the Roman
# subsection (defX.I.1 … defX.III.6).
_X_DEF_SUBSECTIONS = {"I", "II", "III"}


def resolve(token: str) -> str:
    """Map a bare citation token to a URL path."""
    if token.startswith("C.N."):
        n = token[4:]
        # Bare `C.N.` (no number) is a reference to the common-notions
        # group as a whole. Link to the first member — cn1 — since each
        # cn URL serves the combined-view template anyway. Display text
        # stays as the author wrote it.
        if not n:
            return "/elements/books/bookI/commonnotions/cn1/"
        return f"/elements/books/bookI/commonnotions/cn{n}/"
    parts = token.split(".")
    if len(parts) < 2 or parts[0] not in ROMAN_VALID:
        return f"#unresolved-{token}"
    book = parts[0]
    if len(parts) == 2:
        n = parts[1]
        return f"/elements/books/book{book}/propositions/prop{book}{n}/"
    if len(parts) == 3:
        kind, n = parts[1], parts[2]
        if kind == "Def":
            # Book X uses subsection-restart numbering (see 4-part
            # handler below); a 3-part global-form citation has no
            # well-defined target there. All Book X def citations
            # must spell out the Roman subsection.
            if book == "X":
                return f"#unresolved-{token}"
            return f"/elements/books/book{book}/definitions/def{book}{n}/"
        if kind == "Post":
            return f"/elements/books/book{book}/postulates/post{n}/"
        if kind.isdigit() and n == "Cor":
            return f"/elements/books/book{book}/propositions/prop{book}{kind}/#cor"
    if len(parts) == 4 and book == "X" and parts[1] == "Def" and parts[2] in _X_DEF_SUBSECTIONS:
        section, local_n = parts[2], parts[3]
        return f"/elements/books/bookX/definitions/defX.{section}.{local_n}/"
    return f"#unresolved-{token}"


def _link(token: str) -> str:
    return f'<a href="{resolve(token)}">{token}</a>'


def _sub_inline(text: str) -> str:
    return INLINE_RE.sub(lambda m: _link(m.group(1)), text)


# Each entry in a [!just ...] directive can carry a parenthesised plain
# text fragment that becomes literal text in the rendered output.
#
#   `VIII.26 (and converse)`  → <a>VIII.26</a> and converse
#   `(standalone note)`       → standalone note
#
# Use it for things Joyce renders as link-plus-trailing-prose (X.9's
# "VIII.26 and converse") or as a marginal annotation without an
# accompanying citation. The parens themselves never appear in output.
_ENTRY_RE = re.compile(r"^(?:(\S+)\s*)?(?:\(([^)]*)\))?$")


def _render_entry(entry: str) -> str:
    """Render one comma-separated entry inside [!just …]."""
    entry = entry.strip()
    m = _ENTRY_RE.match(entry)
    if not m or (not m.group(1) and not m.group(2)):
        # Doesn't match the (token) / token (text) / (text) shape;
        # fall back to treating the whole thing as a citation token —
        # surfaces as `#unresolved-…` so it's visible during review.
        return _link(entry)
    token, plain = m.group(1), m.group(2)
    parts = []
    if token:
        parts.append(_link(token))
    if plain:
        parts.append(plain)
    return " ".join(parts)


def _render_elem_ref(
    name: str, target: str | None = None, canvas: str | None = None
) -> str:
    """Render a `{NAME}` / `{DISPLAY|element}` / `{NAME:canvas_N}` inline
    shortcode as a span the browser-side JS binds hover/touch handlers to.

    With a display override the span shows NAME but binds to `target`.
    With a canvas selector it also pins which canvas to light. The selector
    is a canvas INDEX (or comma list of them) — `1` becomes `canvas_1` —
    because mistune splits inline text at `_`, so the id cannot be written
    literally. One index emits `data-canvas`, several emit `data-canvases`
    (the cross-canvas form, geomlib >= 0.13). Without a selector the browser
    falls back to the nearest preceding canvas.
    """
    elem = target or name
    attrs = f'class="elem-ref" data-elem="{elem}"'
    if canvas:
        ids = [f"canvas_{i.strip()}" for i in canvas.split(",")]
        attr = "data-canvases" if len(ids) > 1 else "data-canvas"
        attrs += f' {attr}="{",".join(ids)}"'
    return f"<span {attrs}>{name}</span>"


def _render_block_replace(kind: str, arg: str | None) -> str:
    """Render a `[!qed]` / `[!qef]` / `[!title TEXT]` directive."""
    if kind == "qed":
        return '<div class="qed">Q.E.D.</div>'
    if kind == "qef":
        return '<div class="qed">Q.E.F.</div>'
    if kind == "title":
        return f'<div class="title">{arg or ""}</div>'
    return ""


def _render_just(content: str) -> str:
    """Render '[!just I.3, I.46; I.31]' content into a <div class="just">.

    Within the directive, `,` keeps refs on the same logical line
    (rendered with ", " between entries). `;` breaks to a new line
    (rendered as `<br>`). Each entry can be a citation token, a
    parenthesised plain-text annotation, or a citation followed by a
    parenthesised trailer — see `_render_entry`.
    """
    groups = []
    for line in content.split(";"):
        refs = [r.strip() for r in line.split(",") if r.strip()]
        if refs:
            groups.append(", ".join(_render_entry(r) for r in refs))
    return '<div class="just">' + "<br>".join(groups) + "</div>"


# ----------------------------------------------------------------------
# Forward-reference table (phase 1).
#
# For a proposition page, collect the UNIQUE set of citations its proof
# makes via `[!just …]` directives, grouped by book. Exposed to templates
# as the Jinja global `forward_refs(*proof_sources)` — each argument is a
# proof field's raw markdown `.source` (the template passes one per
# section). Reuses BLOCK_RE, _ENTRY_RE and resolve() above; no global
# index needed since forward refs are per-page.
# ----------------------------------------------------------------------

_ROMAN_ORDER = {r: i for i, r in enumerate(
    ["I", "II", "III", "IV", "V", "VI", "VII", "VIII",
     "IX", "X", "XI", "XII", "XIII"], start=1)}


def _num(s):
    try:
        return int(s)
    except (ValueError, TypeError):
        return 0


def _token_group(token):
    """(group label, group sort key) for a citation token."""
    if token.startswith("C.N."):
        return ("Common Notions", 99)
    head = token.split(".", 1)[0]
    if head in _ROMAN_ORDER:
        return (f"Book {head}", _ROMAN_ORDER[head])
    return ("Other", 100)


def _item_sort(token):
    """Sort within a book: postulates, then definitions, then
    propositions, then common notions; by number within each."""
    parts = token.split(".")
    if token.startswith("C.N."):
        return (3, _num(parts[-1]))
    if len(parts) >= 2 and parts[1] == "Post":
        return (0, _num(parts[2]) if len(parts) > 2 else 0)
    if len(parts) >= 2 and parts[1] == "Def":
        return (1, _num(parts[-1]))
    return (2, _num(parts[1]) if len(parts) > 1 else 0)


def _entry_token(entry):
    """The citation token from one `[!just]` entry, dropping any
    parenthetical annotation; None for pure-annotation entries."""
    entry = entry.strip()
    m = _ENTRY_RE.match(entry)
    if m and m.group(1):
        return m.group(1)
    if entry and "(" not in entry:
        return entry
    return None


def forward_refs(*proof_sources):
    """Unique `[!just]` citations across the given proof markdown
    sources, grouped + sorted by book. Returns a list of
    {"label": str, "refs": [{"token": str, "url": str}, …]} for the
    template (key is `refs`, not `items`, to avoid Jinja's dict.items)."""
    if len(proof_sources) == 1 and isinstance(proof_sources[0], (list, tuple)):
        proof_sources = proof_sources[0]
    seen = set()
    ordered = []
    for src in proof_sources:
        if not src:
            continue
        for m in BLOCK_RE.finditer(str(src)):
            for line in m.group(1).split(";"):
                for entry in line.split(","):
                    tok = _entry_token(entry)
                    if tok and tok not in seen:
                        seen.add(tok)
                        ordered.append(tok)
    groups = {}
    for tok in ordered:
        label, gsort = _token_group(tok)
        groups.setdefault((gsort, label), []).append(
            {"token": tok, "url": resolve(tok)})
    out = []
    for key in sorted(groups):
        refs = sorted(groups[key], key=lambda d: _item_sort(d["token"]))
        out.append({"label": key[1], "refs": refs})
    return out


# ----------------------------------------------------------------------
# Reverse-reference ("Referenced by") index.
#
# The inverse of forward_refs: for a given page, which OTHER pages list it
# in a `[!just …]`. Needs one pass over the whole corpus, so it's built
# once (memoised) by walking `content/elements/**/contents.lr`, pulling
# each file's `[!just]` tokens, and recording the citing page under every
# target it resolves to. `referenced_by(record)` then looks up the
# record's own URL. (Built once per process — restart `lektor server`
# after editing citations for the index to refresh.)
# ----------------------------------------------------------------------

_SHORT_LABEL_RE = re.compile(r"^short_label:\s*(.+?)\s*$", re.MULTILINE)
_reverse_index = None


def _content_root():
    here = os.path.abspath(__file__)
    root = os.path.dirname(os.path.dirname(os.path.dirname(here)))
    return os.path.join(root, "content")


def _norm_url(u):
    if u and not u.endswith("/"):
        u += "/"
    return u


def _url_from_contents_path(fpath, content_root):
    rel = os.path.relpath(os.path.dirname(fpath), content_root)
    return "/" + rel.replace(os.sep, "/") + "/"


def _build_reverse_index():
    root = _content_root()
    rev = {}
    elements = os.path.join(root, "elements")
    for dirpath, _dirnames, filenames in os.walk(elements):
        if "contents.lr" not in filenames:
            continue
        fpath = os.path.join(dirpath, "contents.lr")
        try:
            with open(fpath, encoding="utf-8") as f:
                text = f.read()
        except OSError:
            continue
        tokens = set()
        for jm in BLOCK_RE.finditer(text):
            for line in jm.group(1).split(";"):
                for entry in line.split(","):
                    tok = _entry_token(entry)
                    if tok:
                        tokens.add(tok)
        if not tokens:
            continue
        lm = _SHORT_LABEL_RE.search(text)
        url = _norm_url(_url_from_contents_path(fpath, root))
        citer = {"label": lm.group(1).strip() if lm else url, "url": url}
        for tok in tokens:
            target = resolve(tok).split("#")[0]   # fold #cor onto the prop
            if not target.startswith("/"):
                continue                          # skip #unresolved-…
            rev.setdefault(_norm_url(target), []).append(citer)
    return rev


def referenced_by(record):
    """Pages whose `[!just]` lists `record`, grouped + sorted by book.
    Returns the same {"label", "refs":[{"label","url"}]} shape as
    forward_refs (here `refs[*].label` is the citing page's short label)."""
    global _reverse_index
    if _reverse_index is None:
        _reverse_index = _build_reverse_index()
    url = _norm_url(getattr(record, "url_path", None) or "")
    citers = _reverse_index.get(url, [])
    seen, uniq = set(), []
    for c in citers:
        if c["url"] not in seen:
            seen.add(c["url"])
            uniq.append(c)
    groups = {}
    for c in uniq:
        label, gsort = _token_group(c["label"])
        groups.setdefault((gsort, label), []).append(c)
    out = []
    for key in sorted(groups):
        refs = sorted(groups[key], key=lambda c: _item_sort(c["label"]))
        out.append({"label": key[1], "refs": refs})
    return out


class EucrefsRendererMixin:
    """Mixed into Lektor's Mistune Renderer via on_markdown_config."""

    def text(self, text):
        # The parent text() HTML-escapes its argument, so we can't just
        # substitute matched tokens in-place and hand the result up —
        # the <a>/<span> we generated would become &lt;a. Instead, walk
        # the text in chunks: escape non-match spans via the parent,
        # splice raw HTML for each `@TOKEN` citation or `{NAME}`
        # element reference.
        if "@" not in text and "{" not in text:
            return super().text(text)
        parts = []
        last = 0
        for m in _INLINE_ANY_RE.finditer(text):
            if m.start() > last:
                parts.append(super().text(text[last:m.start()]))
            if m.group("cite"):
                parts.append(_link(m.group("cite")))
            else:
                parts.append(_render_elem_ref(
                    m.group("elem"), m.group("target"), m.group("canvas")
                ))
            last = m.end()
        if last == 0:
            return super().text(text)
        if last < len(text):
            parts.append(super().text(text[last:]))
        return "".join(parts)

    def paragraph(self, text):
        # Standalone-block directives ([!qed]/[!qef]/[!title …]) live on
        # their own paragraph; replace the whole <p> with the rendered
        # div so we get full-width block layout rather than inline text.
        m = BLOCK_REPLACE_RE.match(text)
        if m:
            return _render_block_replace(m.group("kind"), m.group("arg")) + "\n"
        # Otherwise: extract any [!just …] directives that appear inside
        # this paragraph — they can be standalone (their own paragraph)
        # or embedded mid-sentence ("Describe the circle. [!just I.3]").
        # Either way, emit them BEFORE the surrounding <p> so the
        # float-right CSS lines them up alongside the paragraph they
        # accompany. Mistune passes the directive text through as
        # literal characters because no reflink matches.
        just_blocks = []
        def collect(m):
            just_blocks.append(_render_just(m.group(1)))
            return ""
        cleaned = BLOCK_RE.sub(collect, text).strip()
        if not just_blocks:
            return super().paragraph(text)
        head = "\n".join(just_blocks) + "\n"
        if cleaned:
            return head + super().paragraph(cleaned)
        return head


class EucrefsPlugin(Plugin):
    name = "Euclid citation refs"
    description = "@-prefixed inline citations and [!just …] margin-ref blocks for Euclid's Elements."

    def on_markdown_config(self, config, **extra):
        config.renderer_mixins.append(EucrefsRendererMixin)

    def on_setup_env(self, **extra):
        # Local-dev toggle: when EUCLIDS_GEOMLIB_LOCAL is truthy, the
        # layout swaps the unpkg @brownnrl/geomlib script tag for a
        # local /geomlib-dev.js (symlinked into assets/ at the geomlib
        # repo's dist/bundle.js). Templates read this as a global.
        val = os.environ.get("EUCLIDS_GEOMLIB_LOCAL", "").strip().lower()
        self.env.jinja_env.globals["geomlib_local"] = val in ("1", "true", "yes", "on")
        # Reference tables: forward_refs = what this page cites;
        # referenced_by = which pages cite this one (see above).
        self.env.jinja_env.globals["forward_refs"] = forward_refs
        self.env.jinja_env.globals["referenced_by"] = referenced_by
