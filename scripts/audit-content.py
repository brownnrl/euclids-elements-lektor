#!/usr/bin/env python3
"""Audit our Lektor content against Joyce's original HTML.

Walks `content/elements/books/` and `content/elements/prematter/`,
matches each leaf to its source HTML page (default: the local djoyce
mirror at /data-mirrored/projects/geometry/djoyce/mirror/...), extracts
the text and link sets from both sides, and reports differences in
markdown.

Output: `doc/journal/content-audit.md` by default.

Usage:
    python3 scripts/audit-content.py
    python3 scripts/audit-content.py --source http://aleph0.clarku.edu/~djoyce/elements
    python3 scripts/audit-content.py --output doc/journal/audit-2026-06.md

What's compared:
  - Statement (frontmatter `statement:` vs Joyce's <div class="statement">)
  - Proof (markdown `proof:` field vs the rest of <div class="theorem">)
  - Guide body (markdown `body:` field vs the post-<h2>Guide</h2> content)
  - Link set (display text + href target basename, ignoring our
    /elements/books/.../ vs Joyce's bookN/propNX.html URL skin)

Known intentional transformations (NOT flagged as differences):
  - eucref shortcodes `@I.5` rendered as <a href="…propI5/">I.5</a>
  - `[!just I.3]` directives rendered as <div class="just">…</div>
  - markdown `*x*` / `**x**` rendered as <em>/<strong>
  - HTML entities `&rsquo;` etc. → literal Unicode
  - U+00A0 (non-breaking space) replacement for `&nbsp;`
  - Joyce's `loadHeader()` / `loadFooter()` boilerplate stripped
  - Page-title <h1> dropped (we render from frontmatter)

Differences that ARE flagged for review:
  - Substantive text changes (added or removed sentences)
  - Different link display text or href target
  - Section structure mismatches (Joyce has a section we don't, etc.)
"""
from __future__ import annotations

import argparse
import dataclasses
import difflib
import pathlib
import re
import sys
import urllib.parse
import urllib.request
from typing import Iterable

from bs4 import BeautifulSoup, NavigableString


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = "file:///data-mirrored/projects/geometry/djoyce/mirror/aleph0.clarku.edu/~djoyce/elements"
# Fallback mirror for files that exist in the older Java applet version
# but were dropped from Joyce's modernised mirror (e.g. propII8, propVII32).
FALLBACK_SOURCE = "file:///data-mirrored/projects/geometry/djoyce/mirror/aleph0.clarku.edu/~djoyce/java/elements"
DEFAULT_OUTPUT = REPO_ROOT / "doc" / "journal" / "content-audit.md"


# ---------------------------------------------------------------------------
# Lektor .lr file parsing


def parse_lr(path: pathlib.Path) -> dict[str, str]:
    """Return the .lr file's fields as a dict.

    Frontmatter fields are separated by lines containing only `---`.
    Each field is `name: value` for short strings or `name:` followed
    by multi-line content until the next `---` separator.
    """
    text = path.read_text()
    fields: dict[str, str] = {}
    # Split on `---` lines.
    blocks = re.split(r"\n---\n", text)
    for block in blocks:
        block = block.strip("\n")
        if not block:
            continue
        # Field name = up to first colon on the first line
        first_line, _, rest = block.partition("\n")
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", first_line)
        if not m:
            continue
        name = m.group(1)
        first_value = m.group(2)
        if first_value and not rest:
            fields[name] = first_value
        else:
            fields[name] = (first_value + "\n" + rest).strip("\n") if first_value else rest
    return fields


# ---------------------------------------------------------------------------
# Text normalisation


# Strip eucref shortcodes (`@I.5`, `@I.Def.10`, `@X.Def.II.3`, `@VI.20.Cor`, `@C.N.1`)
_EUCREF_RE = re.compile(
    r"@(?:X\.Def\.(?:III|II|I)\.\d+"
    r"|(?:[IVX]+)\.\d+\.Cor"
    r"|(?:[IVX]+)\.(?:Def\.|Post\.)?\d+"
    r"|C\.N\.\d*)"
)
# Strip `[!just …]` margin directives
_JUST_RE = re.compile(r"\[!just\s+[^\]]+\]")
# Strip markdown emphasis pairs and headings
_MD_HEADING_RE = re.compile(r"^#+\s+", re.MULTILINE)
_MD_EMPHASIS_RE = re.compile(r"\*\*([^*]+)\*\*|\*([^*]+)\*")
_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
_MD_CODE_RE = re.compile(r"`([^`]+)`")
# Strip HTML tags
_HTML_TAG_RE = re.compile(r"<[^>]+>")
# Collapse repeated whitespace
_WS_RE = re.compile(r"\s+")


_FIGURE_BLOCK_RE = re.compile(
    r"<figure\b[^>]*>.*?</figure>", re.IGNORECASE | re.DOTALL,
)
_SCRIPT_BLOCK_RE = re.compile(
    r"<script\b[^>]*>.*?</script>", re.IGNORECASE | re.DOTALL,
)
_NOSCRIPT_BLOCK_RE = re.compile(
    r"<noscript\b[^>]*>.*?</noscript>", re.IGNORECASE | re.DOTALL,
)
_STYLE_BLOCK_RE = re.compile(
    r"<style\b[^>]*>.*?</style>", re.IGNORECASE | re.DOTALL,
)


def lex_to_words(text: str) -> list[str]:
    """Normalise to a comparable word stream.

    Keeps lowercase alphanumeric tokens (letters, digits, common
    punctuation). Drops markdown / HTML markup, eucref shortcodes,
    figure/script/noscript blocks, and Joyce header/footer chrome.
    """
    # Drop figure/canvas/script blocks first — they're equipment for
    # rendering, not content. Joyce's <applet>...</applet> blocks get
    # the same treatment via the existing HTML-tag stripper plus the
    # BeautifulSoup extraction for the Joyce side.
    text = _FIGURE_BLOCK_RE.sub(" ", text)
    text = _SCRIPT_BLOCK_RE.sub(" ", text)
    text = _NOSCRIPT_BLOCK_RE.sub(" ", text)
    text = _STYLE_BLOCK_RE.sub(" ", text)
    # Drop margin-citation blocks entirely. They slide around in position
    # (Joyce puts <div class="just"> before the sentence; we hoist
    # [!just ...] in source but the plugin pulls it before the <p>) — and
    # SequenceMatcher counts each repositioning as a delete+insert.
    # Link comparison catches citation accuracy separately.
    text = _JUST_RE.sub(" ", text)
    text = _EUCREF_RE.sub(" ", text)
    # Markdown markup
    text = _MD_HEADING_RE.sub("", text)
    text = _MD_EMPHASIS_RE.sub(lambda m: m.group(1) or m.group(2) or "", text)
    text = _MD_LINK_RE.sub(lambda m: m.group(1), text)
    text = _MD_CODE_RE.sub(lambda m: m.group(1), text)
    # HTML
    text = _HTML_TAG_RE.sub(" ", text)
    # Entities
    for src, dst in [
        ("&rsquo;", "'"), ("&lsquo;", "'"),
        ("&rdquo;", '"'), ("&ldquo;", '"'),
        ("&mdash;", "—"), ("&ndash;", "–"),
        ("&nbsp;", " "), (" ", " "),
        ("&deg;", "°"), ("&times;", "×"),
        ("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"),
    ]:
        text = text.replace(src, dst)
    # Lowercase, collapse whitespace
    text = text.lower()
    text = _WS_RE.sub(" ", text).strip()
    # Tokenize by whitespace, keep only word-like (letters / digits)
    words = re.findall(r"[a-z0-9.,;:!?'\"()/\-–—]+", text)
    return words


# ---------------------------------------------------------------------------
# Joyce HTML extraction


def _read(url: str) -> bytes | None:
    try:
        with urllib.request.urlopen(url) as r:
            return r.read()
    except Exception:
        return None


def fetch_joyce(source: str, rel_path: str) -> str | None:
    """Fetch a Joyce HTML page from the primary mirror, falling back
    to the older /java/ mirror if the file isn't in the modernised
    layout (propII8, propVII32 etc. live only in /java/).
    Returns None if neither has it."""
    candidates = [source.rstrip("/") + "/" + rel_path.lstrip("/")]
    if source == DEFAULT_SOURCE:
        candidates.append(FALLBACK_SOURCE.rstrip("/") + "/" + rel_path.lstrip("/"))
    for url in candidates:
        data = _read(url)
        if data is None:
            continue
        for enc in ("utf-8", "latin-1"):
            try:
                return data.decode(enc, errors="replace")
            except UnicodeDecodeError:
                continue
        return data.decode("latin-1", errors="replace")
    return None


def extract_joyce_prop_sections(html: str) -> dict[str, str]:
    """Pull statement / proof / guide blocks out of a Joyce proposition page.

    Returns a dict with keys: statement, proof, guide. Missing sections
    are empty strings.
    """
    soup = BeautifulSoup(html, "html.parser")
    # Drop loadHeader() / loadFooter() and any <script> boilerplate
    for tag in soup(["script", "style"]):
        tag.decompose()
    for div in soup.find_all("div", id=["header", "footer"]):
        div.decompose()

    sections = {"statement": "", "proof": "", "guide": ""}

    # The theorem block holds statement + proof. Multi-section pages
    # (X.17, X.29, X.111, etc.) have several sibling theorem boxes —
    # aggregate the first statement we see + every theorem box's
    # text. Mirrors our sections data model.
    stmts = []
    proofs = []
    for theorem in soup.find_all("div", class_="theorem"):
        stmt_div = theorem.find("div", class_="statement")
        if stmt_div:
            stmts.append(stmt_div.get_text(" ", strip=True))
            stmt_div.decompose()
        for h1 in theorem.find_all("h1"):
            h1.decompose()
        for just in theorem.find_all("div", class_="just"):
            just.decompose()
        for tag_name in ["applet", "figure", "canvas", "script", "noscript"]:
            for t in theorem.find_all(tag_name):
                t.decompose()
        proofs.append(theorem.get_text(" ", strip=True))
    sections["statement"] = " ".join(s for s in stmts if s)
    sections["proof"] = " ".join(p for p in proofs if p)

    # Guide section: everything after the <h2>Guide</h2> heading.
    # Joyce variously writes `<a name=guide><h2>Guide</h2></a>` or
    # `<h2>Guide</h2>` directly. The Guide content extends through to
    # the footer (which we already decomposed). We use `find_all_next`
    # so we pick up content from any depth, not just the heading's
    # immediate siblings.
    guide_h2 = None
    for h2 in soup.find_all("h2"):
        if "guide" in (h2.get_text() or "").lower():
            guide_h2 = h2
            break
    if guide_h2 is None:
        guide_anchor = soup.find("a", attrs={"name": "guide"})
        if guide_anchor:
            # The h2 may be inside the anchor or be a following sibling.
            guide_h2 = guide_anchor.find("h2") or guide_anchor.find_next("h2")
    if guide_h2:
        guide_parts = []
        for el in guide_h2.find_all_next():
            # Skip non-content (citation justs, applets, scripts).
            if el.name in ("script", "style", "noscript", "applet", "canvas"):
                continue
            if el.name == "div" and "just" in (el.get("class") or []):
                continue
            # Only collect leaf-text nodes via get_text on each top-level
            # block we hit. Using find_all_next plus get_text would
            # double-count nested content, so just keep the strings.
            pass
        # Simpler: take everything between the h2 and end of body, then
        # strip out the unwanted bits via BeautifulSoup decomposition on
        # a copy.
        from copy import copy as _copy
        # Reparse to get a fresh tree (since we mutated the original).
        soup2 = BeautifulSoup(html, "html.parser")
        for tag in soup2(["script", "style", "noscript"]):
            tag.decompose()
        for div in soup2.find_all("div", id=["header", "footer"]):
            div.decompose()
        for div in soup2.find_all("div", class_="just"):
            div.decompose()
        for tag_name in ["applet", "canvas"]:
            for t in soup2.find_all(tag_name):
                t.decompose()
        # Re-find the Guide heading on the cloned tree.
        guide_h2_clone = None
        for h2 in soup2.find_all("h2"):
            if "guide" in (h2.get_text() or "").lower():
                guide_h2_clone = h2
                break
        if guide_h2_clone is None:
            guide_anchor = soup2.find("a", attrs={"name": "guide"})
            if guide_anchor:
                guide_h2_clone = guide_anchor.find("h2") or guide_anchor.find_next("h2")
        if guide_h2_clone:
            # Walk forward in document order, collecting text until EOF.
            collected: list[str] = []
            for el in guide_h2_clone.find_all_next(string=True):
                collected.append(str(el))
            sections["guide"] = " ".join(c.strip() for c in collected if c.strip())

    return sections


def extract_joyce_def_sections(html: str) -> dict[str, str]:
    """For a definition / postulate / common-notion page, extract the
    statement + guide. The structure is the same theorem-then-guide
    shape as propositions.
    """
    return extract_joyce_prop_sections(html)


def extract_joyce_prose_sections(html: str) -> dict[str, str]:
    """Generic extractor for non-theorem pages (book intros + prematter).
    These pages don't have <div class="theorem">; they're just prose
    bodies between header and footer chrome. Treat everything as
    'body' so the text comparator gets a single big lump to match
    against our `body:` field.
    """
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    for div in soup.find_all("div", id=["header", "footer"]):
        div.decompose()
    for tag_name in ["applet", "canvas"]:
        for t in soup.find_all(tag_name):
            t.decompose()
    # Joyce's prematter pages often have <small> attribution footers; drop.
    for sm in soup.find_all("small"):
        sm.decompose()
    # Drop the page's own <h1> — we render it from frontmatter.
    for h1 in soup.find_all("h1"):
        h1.decompose()
    body = soup.find("body") or soup
    return {"statement": "", "proof": "", "guide": body.get_text(" ", strip=True)}


def extract_joyce_links(html: str) -> list[tuple[str, str]]:
    """Return a list of (display_text, href_basename) tuples for every
    link on a Joyce page. href_basename strips directory + .html so we
    can compare against our Lektor paths.
    """
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    for div in soup.find_all("div", id=["header", "footer"]):
        div.decompose()
    out = []
    for a in soup.find_all("a", href=True):
        display = a.get_text(" ", strip=True)
        href = a["href"]
        # Strip protocol + path, keep basename + fragment
        parsed = urllib.parse.urlparse(href)
        base = parsed.path.rsplit("/", 1)[-1]
        if parsed.fragment:
            base = base + "#" + parsed.fragment
        if display and base:
            out.append((display, base))
    return out


# ---------------------------------------------------------------------------
# Our content extraction


# Render markdown links + eucref shortcodes to plain (display, target) tuples
_MD_LINK_FULL_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_EUCREF_LINK_RE = re.compile(
    r"@((?:X\.Def\.(?:III|II|I)\.\d+"
    r"|(?:[IVX]+)\.\d+\.Cor"
    r"|(?:[IVX]+)\.(?:Def\.|Post\.)?\d+"
    r"|C\.N\.\d*))"
)
_HTML_A_RE = re.compile(r'<a\s+[^>]*href="([^"]+)"[^>]*>([^<]+)</a>', re.IGNORECASE)


_JUST_INNER_RE = re.compile(r"\[!just\s+([^\]]+)\]")


def extract_our_links(md_text: str) -> list[tuple[str, str]]:
    """Find every link reference in our markdown source. Each becomes a
    (display, target_token) tuple. For eucref shortcodes, the target
    token is the eucref itself (e.g. 'I.5'). `[!just I.3, I.46; I.31]`
    margin directives expand to one link per citation token — they
    render as `<div class="just"><a>I.3</a>, <a>I.46</a><br><a>I.31</a></div>`
    in the build, equivalent to Joyce's own margin <a href> citations."""
    out = []
    # Inline html <a href> tags inside markdown
    for m in _HTML_A_RE.finditer(md_text):
        href, display = m.group(1), m.group(2)
        parsed = urllib.parse.urlparse(href)
        base = parsed.path.rsplit("/", 1)[-1] or parsed.path
        if parsed.fragment:
            base = base + "#" + parsed.fragment
        out.append((display.strip(), base.strip()))
    # Markdown [text](url)
    for m in _MD_LINK_FULL_RE.finditer(md_text):
        display, href = m.group(1), m.group(2)
        parsed = urllib.parse.urlparse(href)
        base = parsed.path.rsplit("/", 1)[-1] or parsed.path
        if parsed.fragment:
            base = base + "#" + parsed.fragment
        out.append((display.strip(), base.strip()))
    # Eucref shortcodes @TOKEN
    for m in _EUCREF_LINK_RE.finditer(md_text):
        tok = m.group(1)
        out.append((tok, tok))
    # [!just X.Y, X.Z; X.W] — each comma/semicolon-separated token
    # becomes its own (display, target) tuple. Comma keeps refs on
    # the same logical line, semicolon breaks to a new line; both
    # render as <a> tags, equivalent for link comparison.
    for m in _JUST_INNER_RE.finditer(md_text):
        inner = m.group(1)
        for piece in re.split(r"[,;]", inner):
            tok = piece.strip()
            if tok:
                out.append((tok, tok))
    return out


# ---------------------------------------------------------------------------
# Page discovery + mapping


@dataclasses.dataclass
class PageMatch:
    our_path: pathlib.Path           # content/.../contents.lr
    joyce_rel: str                   # relative path under Joyce's elements/
    kind: str                        # 'proposition' | 'definition' | 'postulate'
                                     # | 'commonnotion' | 'prematter' | 'book' | 'bundle'


def discover_pages() -> list[PageMatch]:
    matches = []
    books_dir = REPO_ROOT / "content" / "elements" / "books"
    for book_dir in sorted(books_dir.iterdir()):
        if not book_dir.is_dir():
            continue
        book_name = book_dir.name  # bookI
        roman = book_name[4:]      # I
        # Propositions
        prop_dir = book_dir / "propositions"
        if prop_dir.exists():
            for leaf in sorted(prop_dir.iterdir()):
                if not leaf.is_dir():
                    continue
                # leaf.name like propI5 → bookI/propI5.html on Joyce
                joyce_rel = f"{book_name}/{leaf.name}.html"
                matches.append(PageMatch(leaf / "contents.lr", joyce_rel, "proposition"))
        # Definitions. Skip bundle MEMBER leaves — they carry empty
        # bodies (content lives on the bundle root page) and would
        # produce false positives against Joyce's source file that
        # combines several definitions. The member leaf has `group:
        # <bundle_slug>` in its frontmatter; bundle roots don't.
        def_dir = book_dir / "definitions"
        if def_dir.exists():
            for leaf in sorted(def_dir.iterdir()):
                if not leaf.is_dir():
                    continue
                cl = leaf / "contents.lr"
                if not cl.exists():
                    continue
                fields = parse_lr(cl)
                if fields.get("group"):
                    # Bundle member — skip
                    continue
                if fields.get("_model") == "definition_group":
                    # Bundle root → Joyce's source file. Books II and
                    # IV use unnumbered names (defII.html, defIV.html).
                    # Book X has three subsection sources (defX.I.html
                    # etc.). All other books use defN{firstmember}.html.
                    if book_name == "bookX":
                        joyce_rel = f"{book_name}/{leaf.name}.html"
                    elif book_name == "bookII":
                        joyce_rel = f"{book_name}/defII.html"
                    elif book_name == "bookIV":
                        joyce_rel = f"{book_name}/defIV.html"
                    else:
                        first = leaf.name.split("_", 1)[0]
                        joyce_rel = f"{book_name}/{first}.html"
                    matches.append(PageMatch(cl, joyce_rel, "bundle"))
                else:
                    # Single-def page (e.g. defI1 → defI1.html)
                    joyce_rel = f"{book_name}/{leaf.name}.html"
                    matches.append(PageMatch(cl, joyce_rel, "definition"))
        # Postulates (bookI only)
        post_dir = book_dir / "postulates"
        if post_dir.exists():
            for leaf in sorted(post_dir.iterdir()):
                if not leaf.is_dir():
                    continue
                # postN → bookI/postN.html
                num = re.match(r"post(\d+)", leaf.name)
                if num:
                    joyce_rel = f"{book_name}/post{num.group(1)}.html"
                    matches.append(PageMatch(leaf / "contents.lr", joyce_rel, "postulate"))
        # Common notions (bookI only; bundled in cn.html)
        cn_dir = book_dir / "commonnotions"
        if cn_dir.exists():
            cn_bundle = cn_dir / "cn1_5"
            if cn_bundle.exists():
                joyce_rel = f"{book_name}/cn.html"
                matches.append(PageMatch(cn_bundle / "contents.lr", joyce_rel, "bundle"))
        # Book intro pages skipped: Joyce's bookN.html is structurally
        # a TOC + per-prop list; ours is title + short_description
        # + (sometimes) an intro Guide rendered via the section_index
        # template. The two aren't comparable as prose — see
        # link-normalisation-patterns.md for the architectural pattern.

    # Prematter
    prem_dir = REPO_ROOT / "content" / "elements" / "prematter"
    prem_map = {
        "aboutText": "aboutText.html",
        "Euclid": "Euclid.html",
        "trip": "trip.html",
        "web": "web.html",
        "subjindex": "subjindex.html",
        "copyright": "copyright.html",
    }
    for slug, joyce_filename in prem_map.items():
        leaf = prem_dir / slug / "contents.lr"
        if leaf.exists():
            matches.append(PageMatch(leaf, joyce_filename, "prematter"))

    return matches


# ---------------------------------------------------------------------------
# Diff + report


def text_similarity(joyce_text: str, our_text: str) -> tuple[float, list[str]]:
    """Return (similarity_ratio, list of differing-passage snippets).

    The snippets are small windows of joyce vs our text where they
    diverge — useful for reading the diff at a glance without staring
    at the full 5kB of body text.
    """
    j_words = lex_to_words(joyce_text)
    o_words = lex_to_words(our_text)
    if not j_words and not o_words:
        return 1.0, []
    sm = difflib.SequenceMatcher(None, j_words, o_words, autojunk=False)
    ratio = sm.ratio()
    snippets = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        # Show a tiny snippet of each side.
        ours = " ".join(o_words[j1:j2]) if j1 < j2 else "(missing)"
        theirs = " ".join(j_words[i1:i2]) if i1 < i2 else "(missing)"
        # Trim long snippets
        if len(ours) > 200:
            ours = ours[:200] + "…"
        if len(theirs) > 200:
            theirs = theirs[:200] + "…"
        snippets.append(f"  - Joyce: {theirs}\n    Ours:  {ours}")
    return ratio, snippets


def link_diff(joyce_links: list[tuple[str, str]], our_links: list[tuple[str, str]]) -> dict:
    """Set-diff of (display, target_basename) tuples after some
    normalisation. Returns a dict with 'missing' (in Joyce not ours)
    and 'added' (in ours not Joyce)."""
    # Replace Joyce's `propXIII13.html` / `defXI3.html` style hrefs with
    # the eucref-equivalent token (`xiii.13`, `xi.def.3`). Longest Roman
    # numerals must match FIRST or `propx` would eat the start of `propxi`.
    _romans = ["xiii", "xii", "xi", "ix", "iv", "viii", "vii", "vi", "v", "x", "iii", "ii", "i"]
    _replacements: list[tuple[str, str]] = [(".html", "")]
    for r in _romans:
        _replacements.append((f"prop{r}", f"{r}."))
        _replacements.append((f"def{r}",  f"{r}.def."))
    _replacements.append(("post", "i.post."))

    def norm_display(d: str) -> str:
        # Squash whitespace, strip trailing punctuation, lowercase.
        d = re.sub(r"\s+", "", d).strip().lower()  # collapse `post. 1` → `post.1`
        d = d.rstrip(".,;:")
        # Joyce-variant → canonical eucref alias (mirrors the
        # transformations performed by scripts/normalize-citations.py).
        # Order matters: longer patterns first so `proposition i.5`
        # doesn't get half-matched.
        rules = [
            (r"^proposition\s*(xiii|xii|xi+|ix|viii|vii|vi|v|iv|iii|ii|i|x)\.(\d+)$",  r"\1.\2"),
            (r"^postulate\s*(\d+)$",     r"i.post.\1"),
            (r"^prop\.\s*(xiii|xii|xi+|ix|viii|vii|vi|v|iv|iii|ii|i|x)\.(\d+)$",  r"\1.\2"),
            (r"^def\.\s*(xiii|xii|xi+|ix|viii|vii|vi|v|iv|iii|ii|i|x)\.(\d+)$",   r"\1.def.\2"),
            (r"^post\.\s*(xiii|xii|xi+|ix|viii|vii|vi|v|iv|iii|ii|i|x)\.(\d+)$",  r"\1.post.\2"),
            (r"^post\.(\d+)$",           r"i.post.\1"),  # `post.4` → `i.post.4`
            (r"^def\.(\d+)$",            r"i.def.\1"),
            (r"^c\.n(?!\.)$",            r"c.n."),       # `c.n` → `c.n.`
            (r"^(xiii|xii|xi+|ix|viii|vii|vi|v|iv|iii|ii|i|x)\.(\d+)\.$", r"\1.\2"),  # trailing dot
            # Corollary: Joyce wrote `X.6,Cor` (comma) or `X.6,Cor.`
            # (comma + trailing dot). We canonicalised to `X.6.Cor`
            # (period).
            (r"^(xiii|xii|xi+|ix|viii|vii|vi|v|iv|iii|ii|i|x)\.(\d+),cor$", r"\1.\2.cor"),
            # Definition with subsection (Book X): `X.Def.I.3` etc. —
            # already canonical on both sides.
            # Common notion: Joyce sometimes wrote `C.N.` (no number)
            # as a section reference; we use `C.N.1` for the bundle root.
            (r"^c\.n\.?$",               r"c.n.1"),
        ]
        for pat, rep in rules:
            d = re.sub(pat, rep, d)
        return d

    def norm_target(b: str) -> str:
        b = b.lower()
        for token, alias in _replacements:
            b = b.replace(token, alias)
        return b

    # Compare by display text (counts of identical-display links should
    # match Joyce's). When a display text is present on one side but not
    # the other, flag it. The target is kept as diagnostic context.
    j_by_disp: dict[str, list[str]] = {}
    for d, b in joyce_links:
        j_by_disp.setdefault(norm_display(d), []).append(norm_target(b))
    o_by_disp: dict[str, list[str]] = {}
    for d, b in our_links:
        o_by_disp.setdefault(norm_display(d), []).append(norm_target(b))

    missing = []  # display text present on Joyce, not on ours
    added = []    # display text present on ours, not on Joyce
    for disp, targets in j_by_disp.items():
        if disp not in o_by_disp:
            missing.append((disp, ", ".join(sorted(set(targets)))))
    for disp, targets in o_by_disp.items():
        if disp not in j_by_disp:
            added.append((disp, ", ".join(sorted(set(targets)))))
    return {"missing": sorted(missing), "added": sorted(added)}


# Cross-page accumulator for every Joyce-display ↔ ours-display
# transformation observed in the audit. We bucket by (joyce_display →
# ours_equivalent_or_None) so the link-patterns report can show what
# canonicalisations are in play across the whole tree.
LINK_PATTERNS: dict[tuple[str, str], list[str]] = {}


_SECTION_BLOCK_RE = re.compile(r"^#### prop_section ####\s*$", re.MULTILINE)
_SECTION_FIELD_RE = re.compile(
    r"^(?P<key>kind|label|anchor|statement|proof|guide|red_highlight)"
    r":\s*\n?(?P<val>.*?)(?=^----\s*$|^#### prop_section ####|\Z)",
    re.MULTILINE | re.DOTALL,
)


def extract_section_text(sections_blob: str) -> str:
    """Pull statement + proof + guide text out of a `sections:` flow
    blob, dropping the metaformat scaffolding (#### prop_section ####
    markers, ---- separators, kind/anchor/label/red_highlight metadata).
    What remains is comparable to Joyce's flat HTML text."""
    parts = []
    for block in _SECTION_BLOCK_RE.split(sections_blob):
        block = block.strip()
        if not block:
            continue
        for m in _SECTION_FIELD_RE.finditer(block):
            key = m.group("key")
            if key in ("statement", "proof", "guide"):
                parts.append(m.group("val").strip())
    return "\n".join(p for p in parts if p)


def extract_our_text(cl_path: pathlib.Path, fields: dict) -> str:
    """Combine the content fields for one of our .lr files into a single
    text blob comparable to Joyce's rendered page text."""
    model = fields.get("_model", "")
    if model == "proposition":
        return extract_section_text(fields.get("sections", ""))
    if model == "definition_group":
        # Bundle root — collect the members' statement + guide IN
        # SOURCE ORDER, then the bundle's own (shared) guide last.
        # Mirrors Joyce's page layout: theorem boxes first, then
        # Guide commentary, so the similarity comparison isn't
        # penalised for reorderings the data model imposes.
        parts = []
        bundle_slug = cl_path.parent.name
        for sibling in sorted(cl_path.parent.parent.iterdir()):
            if not sibling.is_dir() or sibling.name == bundle_slug:
                continue
            sibling_cl = sibling / "contents.lr"
            if not sibling_cl.exists():
                continue
            sib_fields = parse_lr(sibling_cl)
            if sib_fields.get("group") != bundle_slug:
                continue
            parts.append(sib_fields.get("statement", ""))
            parts.append(sib_fields.get("guide", ""))
        parts.append(fields.get("guide", ""))
        return "\n".join(p for p in parts if p)
    # Definitions / postulates / common notions / books / pages.
    return "\n".join(
        fields.get(k, "") for k in ("statement", "guide", "body") if fields.get(k)
    )


def audit_page(match: PageMatch, source: str) -> dict:
    """Return a dict of audit findings for one page."""
    our_fields = parse_lr(match.our_path)
    our_text_combined = extract_our_text(match.our_path, our_fields)

    joyce_html = fetch_joyce(source, match.joyce_rel)
    if not joyce_html:
        return {"match": match, "error": f"could not fetch {match.joyce_rel}"}

    if match.kind in ("book", "prematter"):
        joyce_sections = extract_joyce_prose_sections(joyce_html)
    elif match.kind == "bundle":
        # Bundle pages have multiple <div class="theorem"> blocks
        # plus Guide-style commentary in between. Grab everything.
        joyce_sections = extract_joyce_prose_sections(joyce_html)
    else:
        joyce_sections = extract_joyce_prop_sections(joyce_html)
    joyce_text_combined = "\n".join([
        joyce_sections["statement"],
        joyce_sections["proof"],
        joyce_sections["guide"],
    ])

    text_ratio, text_diffs = text_similarity(joyce_text_combined, our_text_combined)

    joyce_links = extract_joyce_links(joyce_html)
    our_links = extract_our_links(our_text_combined)
    link_findings = link_diff(joyce_links, our_links)

    # Record link-pattern observations for the patterns report. A
    # "missing" entry means Joyce's display label has no equivalent
    # display label on our side — note it as `joyce_display → ?`.
    # Most of these will be canonicalisations (e.g. Joyce wrote
    # `Post.4` and our equivalent display is `I.Post.4`).
    rel = str(match.our_path.relative_to(REPO_ROOT))
    for disp, target in link_findings["missing"]:
        LINK_PATTERNS.setdefault((disp, "(missing)"), []).append(rel)
    for disp, target in link_findings["added"]:
        LINK_PATTERNS.setdefault(("(added)", disp), []).append(rel)

    return {
        "match": match,
        "text_ratio": text_ratio,
        "text_diffs": text_diffs,
        "joyce_link_count": len(joyce_links),
        "our_link_count": len(our_links),
        "links": link_findings,
    }


def write_link_patterns(output_path: pathlib.Path) -> None:
    """Write a markdown report bucketing every (Joyce display ↔ ours)
    pair observed during the audit. Use this to spot pattern-level
    canonicalisations that should be accepted globally vs one-off
    edits worth reviewing.
    """
    if not LINK_PATTERNS:
        return
    by_pages: list[tuple[int, str, str, list[str]]] = [
        (len(pages), j, o, pages) for (j, o), pages in LINK_PATTERNS.items()
    ]
    by_pages.sort(reverse=True)  # most-frequent first
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write("# Link-normalisation patterns observed in the audit\n\n")
        f.write(f"Generated alongside [`content-audit.md`](content-audit.md). "
                f"Each row is a Joyce-display-label ↔ ours-display-label\n"
                f"pair that was flagged as a link diff somewhere in the audit. "
                f"Sorted by frequency.\n\n"
                f"- `(missing)` in the right column means Joyce's display label "
                f"has no equivalent display in our version — usually a "
                f"canonicalisation: Joyce wrote `Post.4`, our normalized version "
                f"shows `I.Post.4`.\n"
                f"- `(added)` in the left column means we surfaced a display "
                f"label Joyce never wrote.\n"
                f"- The `audit-content.py` normaliser already accepts a baked-in "
                f"set of canonicalisations (`Post.N` → `I.Post.N`, "
                f"`Def.N` → `I.Def.N`, etc.). Patterns that show up here are "
                f"the ones the normaliser doesn't yet recognise.\n\n")
        f.write("| Count | Joyce display | Ours display | Pages |\n")
        f.write("|---|---|---|---|\n")
        for count, j, o, pages in by_pages:
            sample = ", ".join(f"`{p.split('/')[-2]}`" for p in pages[:3])
            if len(pages) > 3:
                sample += f", …(+{len(pages) - 3})"
            f.write(f"| {count} | `{j}` | `{o}` | {sample} |\n")


def write_report(reports: list[dict], output_path: pathlib.Path,
                 ratio_threshold: float) -> None:
    """Write a markdown report. Pages with similarity above threshold
    and no link issues are summarised under 'Clean'. Pages with anything
    flagged get a per-page section."""
    clean = []
    flagged = []
    errors = []
    for r in reports:
        if "error" in r:
            errors.append(r)
            continue
        is_clean = (
            r["text_ratio"] >= ratio_threshold
            and not r["links"]["missing"]
            and not r["links"]["added"]
        )
        (clean if is_clean else flagged).append(r)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write("# Content audit — our Lektor pages vs Joyce's original HTML\n\n")
        f.write(f"Audit run over {len(reports)} pages.\n\n")
        f.write(f"- ✅ Clean (≥ {ratio_threshold:.0%} text similarity + no link diffs): "
                f"**{len(clean)}**\n")
        f.write(f"- ⚠️  Flagged for review: **{len(flagged)}**\n")
        f.write(f"- ❌ Could not fetch Joyce source: **{len(errors)}**\n\n")
        f.write("## How to read this report\n\n"
                "- Text similarity is a token-based ratio (after stripping markdown / HTML "
                "markup, eucref shortcodes, and Joyce's header/footer chrome). 100% means "
                "every word matches in order; lower means there are insertions, deletions, "
                "or rewordings.\n"
                "- Link diffs report (display text, target) tuples present on Joyce's page "
                "but missing from ours, or vice versa. Joyce's `propI5.html` is normalised "
                "to `i.5.` for comparison against our `@I.5` shortcode rendering.\n"
                "- Already-catalogued intentional fixes "
                "(see [`doc/journal/mismatch-review.md`](mismatch-review.md)) will appear "
                "as link-diff entries here; cross-check before re-fixing.\n\n")

        if errors:
            f.write("## ❌ Could not fetch\n\n")
            for r in errors:
                f.write(f"- `{r['match'].our_path.relative_to(REPO_ROOT)}` → "
                        f"`{r['match'].joyce_rel}`: {r['error']}\n")
            f.write("\n")

        if flagged:
            f.write("## ⚠️ Pages flagged for review\n\n")
            flagged.sort(key=lambda r: r["text_ratio"])
            for r in flagged:
                rel = r["match"].our_path.relative_to(REPO_ROOT)
                f.write(f"### `{rel}` (vs `{r['match'].joyce_rel}`)\n\n")
                f.write(f"- Text similarity: **{r['text_ratio']:.1%}**\n")
                f.write(f"- Joyce link count: {r['joyce_link_count']}, "
                        f"ours: {r['our_link_count']}\n")
                if r["links"]["missing"]:
                    f.write(f"- Missing in our version: {len(r['links']['missing'])}\n")
                    for disp, base in r["links"]["missing"][:10]:
                        f.write(f"    - `{disp}` → `{base}`\n")
                    if len(r["links"]["missing"]) > 10:
                        f.write(f"    - …and {len(r['links']['missing']) - 10} more\n")
                if r["links"]["added"]:
                    f.write(f"- Added in our version: {len(r['links']['added'])}\n")
                    for disp, base in r["links"]["added"][:10]:
                        f.write(f"    - `{disp}` → `{base}`\n")
                    if len(r["links"]["added"]) > 10:
                        f.write(f"    - …and {len(r['links']['added']) - 10} more\n")
                if r["text_diffs"]:
                    f.write(f"- Text differences (first 5 passages):\n\n")
                    for snippet in r["text_diffs"][:5]:
                        f.write(snippet + "\n")
                    if len(r["text_diffs"]) > 5:
                        f.write(f"  - …and {len(r['text_diffs']) - 5} more passages\n")
                f.write("\n")

        if clean:
            f.write("## ✅ Clean pages\n\n")
            clean.sort(key=lambda r: str(r["match"].our_path))
            for r in clean:
                rel = r["match"].our_path.relative_to(REPO_ROOT)
                f.write(f"- `{rel}` ({r['text_ratio']:.0%})\n")
            f.write("\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", default=DEFAULT_SOURCE,
                    help="URL prefix for Joyce's elements/ directory "
                         "(file:// or http://). Default: local mirror.")
    ap.add_argument("--output", default=str(DEFAULT_OUTPUT),
                    help="Output markdown report path. "
                         f"Default: {DEFAULT_OUTPUT.relative_to(REPO_ROOT)}")
    ap.add_argument("--ratio-threshold", type=float, default=0.92,
                    help="Text-similarity threshold below which a page is flagged. "
                         "Default: 0.92")
    ap.add_argument("--filter", default=None,
                    help="Only audit pages whose path matches this regex (for debugging).")
    ap.add_argument("--limit", type=int, default=None,
                    help="Only audit the first N matching pages (for debugging).")
    args = ap.parse_args()

    pages = discover_pages()
    if args.filter:
        pat = re.compile(args.filter)
        pages = [p for p in pages if pat.search(str(p.our_path))]
    if args.limit:
        pages = pages[:args.limit]

    print(f"Auditing {len(pages)} pages against {args.source}", file=sys.stderr)
    reports = []
    for i, page in enumerate(pages, 1):
        if i % 25 == 0:
            print(f"  {i}/{len(pages)}…", file=sys.stderr)
        reports.append(audit_page(page, args.source))

    output_path = pathlib.Path(args.output)
    write_report(reports, output_path, args.ratio_threshold)
    print(f"Report written to {output_path}", file=sys.stderr)

    patterns_path = output_path.with_name("link-normalisation-patterns.md")
    write_link_patterns(patterns_path)
    print(f"Link patterns written to {patterns_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
