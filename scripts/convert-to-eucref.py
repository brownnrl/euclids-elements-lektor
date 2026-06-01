#!/usr/bin/env python3
"""Second-pass conversion: canonical citations → eucref shortcodes.

After scripts/normalize-citations.py has rewritten variant display
text to canonical form, this script does what the conversion agents
already did for the bulk of the source:

  1. [I.5](url) → @I.5    (and other eucref-grammar tokens) — only when
     the url matches the canonical Lektor leaf path that @I.5 would
     resolve to.
  2. <div class="just"><a>X</a>, <a>Y</a><br><a>Z</a></div>
     → [!just X, Y; Z]                     — only when every internal ref
     matches the eucref grammar and points at its canonical leaf.

Mismatches between display text and href (e.g. propI22's `I.Def.16`
that points at `defI15`) are left as raw HTML — those are real source
bugs the user needs to hand-review.

Usage:
    python3 scripts/convert-to-eucref.py            # dry-run
    python3 scripts/convert-to-eucref.py --write    # apply
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content" / "elements" / "books"

ROMAN = {"I", "II", "III", "IV", "V", "VI", "VII", "VIII",
         "IX", "X", "XI", "XII", "XIII"}
ROMAN_ALT = "|".join(sorted(ROMAN, key=len, reverse=True))

# Token grammar (must mirror lektor-eucrefs).
TOKEN_RE = re.compile(
    rf"\A(?:(?:{ROMAN_ALT})\.(?:Def\.|Post\.)?\d+|C\.N\.\d*)\Z"
)


def resolve(token: str) -> str | None:
    """Same logic as the plugin — returns canonical Lektor path or None."""
    if token.startswith("C.N."):
        n = token[4:]
        if not n:
            return "/elements/books/bookI/commonnotions/cn1/"
        return f"/elements/books/bookI/commonnotions/cn{n}/"
    parts = token.split(".")
    if len(parts) < 2 or parts[0] not in ROMAN:
        return None
    book = parts[0]
    if len(parts) == 2:
        return f"/elements/books/book{book}/propositions/prop{book}{parts[1]}/"
    if len(parts) == 3:
        kind, n = parts[1], parts[2]
        if kind == "Def":
            return f"/elements/books/book{book}/definitions/def{book}{n}/"
        if kind == "Post":
            return f"/elements/books/book{book}/postulates/post{n}/"
    return None


def url_matches_canonical(url: str, canonical: str) -> bool:
    """url may be absolute or relative; canonical is always absolute.
    A relative url is judged by its suffix matching the canonical path's
    suffix. We compare normalized tails so `../propI5/` matches
    `/elements/.../propositions/propI5/`."""
    if not url or not canonical:
        return False
    # Strip trailing slash from both
    url = url.rstrip("/")
    canonical = canonical.rstrip("/")
    if url == canonical:
        return True
    # The leaf folder name (last path segment) must match.
    return url.endswith("/" + canonical.split("/")[-1])


LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
JUST_RE = re.compile(r'<div class="just">(.+?)</div>')
ANCHOR_RE = re.compile(r'<a\b[^>]*href="([^"]+)"[^>]*>([^<]+)</a>')


def convert_inline(text: str) -> tuple[str, int, int]:
    """Convert [token](url) → @token where matchable. Returns (new, converted, skipped)."""
    converted = 0
    skipped = 0
    def sub(m: re.Match) -> str:
        nonlocal converted, skipped
        display, url = m.group(1), m.group(2)
        if not TOKEN_RE.match(display):
            return m.group(0)  # not eucref grammar — pass through
        canonical = resolve(display)
        if canonical is None or not url_matches_canonical(url, canonical):
            skipped += 1
            return m.group(0)
        converted += 1
        return f"@{display}"
    return LINK_RE.sub(sub, text), converted, skipped


def convert_just_blocks(text: str) -> tuple[str, int, int]:
    """Convert hand-rolled <div class="just">…</div> blocks to [!just …]
    when every internal ref is eucref-grammar with matching href."""
    converted = 0
    skipped = 0
    def sub(m: re.Match) -> str:
        nonlocal converted, skipped
        inner = m.group(1)
        # Split by <br> to get logical groups
        groups = inner.split("<br>")
        group_tokens: list[list[str]] = []
        for g in groups:
            tokens: list[str] = []
            ok = True
            # Each group should be a comma-separated list of <a> tags
            anchors = ANCHOR_RE.findall(g)
            if not anchors:
                ok = False
                break
            # Check punctuation isn't anything weird (only ", " between anchors)
            non_anchor = re.sub(r'<a\b[^>]*>[^<]+</a>', "", g).strip().strip(",")
            non_anchor_clean = re.sub(r"\s+", " ", non_anchor).strip().strip(",").strip()
            if non_anchor_clean not in ("", ","):
                ok = False
                break
            for href, display in anchors:
                if not TOKEN_RE.match(display):
                    ok = False
                    break
                canonical = resolve(display)
                if canonical is None or not url_matches_canonical(href, canonical):
                    ok = False
                    break
                tokens.append(display)
            if not ok or not tokens:
                break
            group_tokens.append(tokens)
        else:
            # All groups parsed cleanly
            converted += 1
            lines = ["; ".join([", ".join(g) for g in group_tokens])]
            return f"[!just {lines[0]}]"
        # Fall-through: any group failed → leave as-is
        skipped += 1
        return m.group(0)
    return JUST_RE.sub(sub, text), converted, skipped


def process_file(path: Path, write: bool) -> tuple[int, int, int, int]:
    text = path.read_text()
    new_text, n_inline, n_inline_skip = convert_inline(text)
    new_text, n_just, n_just_skip = convert_just_blocks(new_text)
    if new_text == text:
        return 0, 0, n_inline_skip, n_just_skip
    if write:
        path.write_text(new_text)
    return n_inline, n_just, n_inline_skip, n_just_skip


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    if not ROOT.exists():
        sys.exit(f"Content root not found: {ROOT}")

    total_inline = 0
    total_just = 0
    total_skip_inline = 0
    total_skip_just = 0
    files_modified = 0
    for path in sorted(ROOT.rglob("contents.lr")):
        ni, nj, si, sj = process_file(path, args.write)
        total_skip_inline += si
        total_skip_just += sj
        if ni or nj:
            files_modified += 1
            total_inline += ni
            total_just += nj
            rel = path.relative_to(ROOT)
            verb = "Modified" if args.write else "Would modify"
            print(f"{verb}: {rel}  ({ni} inline, {nj} just-block)")

    print()
    verb = "Modified" if args.write else "Would modify"
    print(f"{verb} {files_modified} file(s):")
    print(f"  {total_inline} inline citation(s) → @TOKEN form")
    print(f"  {total_just} hand-rolled just-block(s) → [!just …] directive")
    if total_skip_inline or total_skip_just:
        print(f"\nLeft as-is for hand-review:")
        if total_skip_inline:
            print(f"  {total_skip_inline} inline link(s) — display matches grammar but URL doesn't point at canonical leaf")
        if total_skip_just:
            print(f"  {total_skip_just} just-block(s) — display/href mismatch or unparseable shape")
    if not args.write:
        print("\n(dry-run — pass --write to apply.)")


if __name__ == "__main__":
    main()
