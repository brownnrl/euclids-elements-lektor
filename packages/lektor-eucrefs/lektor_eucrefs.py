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

# Element-reference inline shortcode: {NAME}.
#   NAME — Joyce/Euclid label: letter-led, may carry digits, primes,
#          hyphens (e.g. A, AB, BCD, A', ABC'). Underscores are
#          deliberately excluded — mistune's inline lexer stops at `_`
#          (emphasis prefix), which would split the token.
#
# The leading `!` was tried first (`{!AB}`) but mistune also stops at
# `!`. Bare `{NAME}` arrives intact at the text() walker, no lexer
# patch required. The constrained NAME pattern (letter-led identifier
# with no underscores) keeps free-form `{...}` prose from matching.
#
# The explicit canvas selector (`{AB:canvas_2}`) is not supported
# inline: mistune splits `canvas_2` at the underscore. The browser-side
# JS falls back to the nearest in-section canvas, which covers the
# expected cases. For the rare edge case where a specific canvas must
# be targeted from prose, drop to raw inline HTML:
#   <span class="elem-ref" data-elem="AB" data-canvas="canvas_2">AB</span>
ELEM_REF_RE = re.compile(
    r"\{(?P<name>[A-Za-z][A-Za-z0-9'\-]*)\}"
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
    rf"|\{{(?P<elem>[A-Za-z][A-Za-z0-9'\-]*)\}}"
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


def _render_elem_ref(name: str) -> str:
    """Render a `{NAME}` inline shortcode as a span the browser-side JS
    binds hover/touch handlers to."""
    return f'<span class="elem-ref" data-elem="{name}">{name}</span>'


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
                parts.append(_render_elem_ref(m.group("elem")))
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
