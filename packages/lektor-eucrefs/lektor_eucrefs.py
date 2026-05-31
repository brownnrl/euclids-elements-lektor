"""Mistune extension for Euclid's Elements citations.

Authoring syntax in markdown bodies:

    Inline:   @I.5  @I.Def.10  @I.Post.3  @C.N.1  @II.4  @XI.Def.2
    Block:    [!just I.3, I.46; I.31]

Both forms resolve a citation token to a URL under
`/elements/books/book{N}/{section}/{slug}/`. The block form renders as
`<div class="just">…<a/>, <a/><br><a/>…</div>` — same shape the proof
templates already expect.

Tokens recognized:
  - `{Roman}.{number}`          → proposition  e.g. I.5, II.13, XIII.18
  - `{Roman}.Def.{number}`      → definition   e.g. I.Def.10, XI.Def.2
  - `{Roman}.Post.{number}`     → postulate    e.g. I.Post.3
  - `C.N.{number}`              → common notion (Book I)  e.g. C.N.1

Anything else (typos, unrecognized prefix) becomes `<a href="#unresolved-…">`
so it surfaces visibly when proofreading the rendered page.

Reusability note: when adding Apollonius / Hilbert / Archimedes content
later, register a second resolver under a different prefix scheme
(e.g. `@Apol.II.4`) and dispatch on the prefix.
"""
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
_TOKEN_BARE = (
    rf"(?:(?:{_ROMAN_ALT})\.(?:Def\.|Post\.)?\d+|C\.N\.\d*)"
)
INLINE_RE = re.compile(rf"@({_TOKEN_BARE})")
BLOCK_RE = re.compile(r"\[!just\s+(.+?)\]")


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
            return f"/elements/books/book{book}/definitions/def{book}{n}/"
        if kind == "Post":
            return f"/elements/books/book{book}/postulates/post{n}/"
    return f"#unresolved-{token}"


def _link(token: str) -> str:
    return f'<a href="{resolve(token)}">{token}</a>'


def _sub_inline(text: str) -> str:
    return INLINE_RE.sub(lambda m: _link(m.group(1)), text)


def _render_just(content: str) -> str:
    """Render '[!just I.3, I.46; I.31]' content into a <div class="just">.

    Within the directive, `,` keeps refs on the same logical line
    (rendered with literal ", " between links). `;` breaks to a new
    line (rendered as `<br>`).
    """
    groups = []
    for line in content.split(";"):
        refs = [r.strip() for r in line.split(",") if r.strip()]
        if refs:
            groups.append(", ".join(_link(r) for r in refs))
    return '<div class="just">' + "<br>".join(groups) + "</div>"


class EucrefsRendererMixin:
    """Mixed into Lektor's Mistune Renderer via on_markdown_config."""

    def text(self, text):
        # The parent text() HTML-escapes its argument, so we can't just
        # substitute @TOKEN in-place and hand the result up — the <a>
        # we generated would become &lt;a. Instead, walk the text in
        # chunks: escape non-match spans via the parent, splice raw
        # link HTML for each @TOKEN.
        if "@" not in text:
            return super().text(text)
        parts = []
        last = 0
        for m in INLINE_RE.finditer(text):
            if m.start() > last:
                parts.append(super().text(text[last:m.start()]))
            parts.append(_link(m.group(1)))
            last = m.end()
        if last == 0:
            return super().text(text)
        if last < len(text):
            parts.append(super().text(text[last:]))
        return "".join(parts)

    def paragraph(self, text):
        # Extract any [!just …] directives that appear inside this
        # paragraph — they can be standalone (their own paragraph) or
        # embedded mid-sentence ("Describe the circle. [!just I.3]").
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
