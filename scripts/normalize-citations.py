#!/usr/bin/env python3
"""Normalize variant citation forms to the canonical eucref tokens.

Joyce's source uses several variant spellings for the same citation:

    Post.4      → I.Post.4   (no book prefix; postulates only exist in Book I)
    Def.I.5     → I.Def.5    (alternate ordering)
    Def.5       → I.Def.5    (no book prefix; only ever appears in Book I context)
    I.5.        → I.5        (trailing period from prose punctuation)
    C.N         → C.N.       (missing trailing dot)
    Postulate N → I.Post.N   (verbose form)
    Proposition I.N → I.N    (verbose form)

For each `.lr` file under content/elements/books/ we scan two contexts:

  1. Inline markdown links:  [Post.4](url)   →   [I.Post.4](url)
  2. <a> text inside <div class="just"> blocks: same display-text rewrites.

After this pass the previously-skipped agent cases match the eucref
grammar and can be re-swept into @TOKEN / [!just …] form by a second
pass (left to the agents or to a follow-up script).

Usage:
    python3 scripts/normalize-citations.py                 # dry-run
    python3 scripts/normalize-citations.py --write         # apply
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content" / "elements" / "books"

# Display-text rewrite rules. Order matters: alternate-order Def.I.N is
# matched before bare Def.N so we don't double-rewrite. Anchored by `\b`
# so `Postulate` doesn't bite into `Postulates`.
TEXT_RULES = [
    ("Post.I.N → I.Post.N",      re.compile(r'\bPost\.I\.(\d+)\b'),                lambda m: f"I.Post.{m.group(1)}"),
    ("Def.I.N → I.Def.N",        re.compile(r'\bDef\.I\.(\d+)\b'),                 lambda m: f"I.Def.{m.group(1)}"),
    ("Prop.I.N → I.N",           re.compile(r'\bProp\.I\.(\d+)\b'),                lambda m: f"I.{m.group(1)}"),
    ("Post.N → I.Post.N",        re.compile(r'(?<![A-Za-z.])Post\.(\d+)\b'),       lambda m: f"I.Post.{m.group(1)}"),
    ("Def.N → I.Def.N",          re.compile(r'(?<![A-Za-z.])Def\.(\d+)\b'),        lambda m: f"I.Def.{m.group(1)}"),
    ("I.N. (trailing) → I.N",    re.compile(r'\b(I\.\d+)\.(?=\s|$|[<,;])'),        lambda m: m.group(1)),
    ("C.N (no dot) → C.N.",      re.compile(r'\bC\.N(?!\.)\b'),                    lambda m: "C.N."),
    ("Postulate N → I.Post.N",   re.compile(r'\bPostulate\s+(\d+)\b'),             lambda m: f"I.Post.{m.group(1)}"),
    ("Proposition I.N → I.N",    re.compile(r'\bProposition\s+(I+|IV|V|VI+|IX|XI+|XII|XIII)\.(\d+)\b'),
                                                                                  lambda m: f"{m.group(1)}.{m.group(2)}"),
]

# Markdown link form: [display](url)
LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
# Anchor text inside a <div class="just"> block (one-line form Joyce uses)
JUST_BLOCK_RE = re.compile(r'<div class="just">(.+?)</div>')
ANCHOR_TEXT_RE = re.compile(r'<a\b[^>]*>([^<]+)</a>')


def rewrite_text(text: str) -> tuple[str, list[str]]:
    """Apply text rules. Returns (new_text, list_of_rule_names_that_fired)."""
    fired = []
    for name, pattern, sub in TEXT_RULES:
        new_text, n = pattern.subn(sub, text)
        if n > 0:
            fired.append(f"{name} (x{n})")
            text = new_text
    return text, fired


def normalize_link_text(m: re.Match) -> str:
    display, url = m.group(1), m.group(2)
    new_display, _ = rewrite_text(display)
    return f"[{new_display}]({url})"


def normalize_just_block(m: re.Match) -> str:
    inner = m.group(1)
    def fix_anchor(am: re.Match) -> str:
        old = am.group(1)
        new, _ = rewrite_text(old)
        return am.group(0).replace(f">{old}<", f">{new}<", 1)
    new_inner = ANCHOR_TEXT_RE.sub(fix_anchor, inner)
    return f'<div class="just">{new_inner}</div>'


def process_file(path: Path, write: bool) -> tuple[int, list[str]]:
    text = path.read_text()
    new_text = LINK_RE.sub(normalize_link_text, text)
    new_text = JUST_BLOCK_RE.sub(normalize_just_block, new_text)
    if new_text == text:
        return 0, []
    # Build a diff-ish summary
    diff_lines = []
    for i, (old, new) in enumerate(zip(text.splitlines(), new_text.splitlines())):
        if old != new:
            diff_lines.append(f"  L{i+1}: - {old.strip()}")
            diff_lines.append(f"  L{i+1}: + {new.strip()}")
    if write:
        path.write_text(new_text)
    return len(diff_lines) // 2, diff_lines


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true",
                        help="Apply the changes (default is dry-run).")
    parser.add_argument("--show-diffs", action="store_true",
                        help="Print the line-by-line diff for each modified file.")
    args = parser.parse_args()

    if not ROOT.exists():
        sys.exit(f"Content root not found: {ROOT}")

    total_files = 0
    total_lines = 0
    for path in sorted(ROOT.rglob("contents.lr")):
        n, diff_lines = process_file(path, args.write)
        if n > 0:
            total_files += 1
            total_lines += n
            rel = path.relative_to(ROOT)
            verb = "Modified" if args.write else "Would modify"
            print(f"{verb}: {rel}  ({n} line edit{'s' if n > 1 else ''})")
            if args.show_diffs:
                for line in diff_lines:
                    print(line)

    print()
    verb = "Modified" if args.write else "Would modify"
    print(f"{verb} {total_files} file(s), {total_lines} line edit(s) total.")
    if not args.write:
        print("\n(dry-run — pass --write to apply.)")


if __name__ == "__main__":
    main()
