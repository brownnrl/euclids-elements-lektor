#!/usr/bin/env python3
"""Side-by-side review of pages flagged by audit-content.py.

Reads `doc/journal/content-audit.md`, lists every page in the
"⚠️ Pages flagged for review" section, and walks you through them
one at a time. For each page it opens TWO browser tabs:

  1. Our local Lektor page (default: http://localhost:5000/...)
  2. Joyce's mirror (default: the local Apache directory mirror)

…and prompts you to mark the page as `accepted` (intentional change),
`flagged` (real issue, follow-up needed), or `skip` (revisit later).

Outcomes are appended to `doc/journal/audit-review-log.md` so the
review is resumable across sessions.

Usage:
    python3 scripts/audit-review.py                         # all flagged
    python3 scripts/audit-review.py --filter "propX"        # only Book X
    python3 scripts/audit-review.py --start 20              # resume from 20
    python3 scripts/audit-review.py --our-base http://localhost:8001
    python3 scripts/audit-review.py --joyce-base file:///path/to/mirror/...elements
    python3 scripts/audit-review.py --list                  # don't open, just list
"""
from __future__ import annotations

import argparse
import datetime
import pathlib
import re
import sys
import webbrowser


REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_AUDIT = REPO_ROOT / "doc" / "journal" / "content-audit.md"
DEFAULT_LOG   = REPO_ROOT / "doc" / "journal" / "audit-review-log.md"
DEFAULT_OUR   = "http://localhost:5000"
# Joyce's live site at Clark. The local file:// mirror is faster but
# unreachable from snap-confined browsers (Ubuntu/Debian's default
# Firefox install) — they can't read /data-mirrored/. The live URL
# is the universally-reachable default.
DEFAULT_JOYCE = "http://aleph0.clarku.edu/~djoyce/elements"


# A flagged entry parsed out of the audit report.
class Flagged:
    def __init__(self, our_path: str, joyce_rel: str, similarity: float,
                 link_missing: int, link_added: int):
        self.our_path = our_path
        self.joyce_rel = joyce_rel
        self.similarity = similarity
        self.link_missing = link_missing
        self.link_added = link_added

    def our_url(self, base: str) -> str:
        # content/elements/books/bookI/propositions/propI5/contents.lr
        # → /elements/books/bookI/propositions/propI5/
        p = self.our_path
        p = re.sub(r"^content", "", p)
        p = re.sub(r"/contents\.lr$", "/", p)
        return base.rstrip("/") + p

    def joyce_url(self, base: str) -> str:
        return base.rstrip("/") + "/" + self.joyce_rel.lstrip("/")


_HEADER_RE = re.compile(r"^### `([^`]+)` \(vs `([^`]+)`\)")
_SIM_RE    = re.compile(r"Text similarity: \*\*([\d.]+)%\*\*")
_MISS_RE   = re.compile(r"Missing in our version: (\d+)")
_ADD_RE    = re.compile(r"Added in our version: (\d+)")


def parse_audit(audit_path: pathlib.Path) -> list[Flagged]:
    """Yield Flagged entries from the report's "Flagged for review" section."""
    text = audit_path.read_text()
    in_flagged = False
    flagged: list[Flagged] = []
    current: dict | None = None
    for line in text.splitlines():
        if line.startswith("## ⚠️"):
            in_flagged = True
            continue
        if line.startswith("## ") and not line.startswith("## ⚠️"):
            in_flagged = False
        if not in_flagged:
            continue
        m = _HEADER_RE.match(line)
        if m:
            if current:
                flagged.append(Flagged(**current))
            current = {
                "our_path": m.group(1),
                "joyce_rel": m.group(2),
                "similarity": 100.0,
                "link_missing": 0,
                "link_added":   0,
            }
            continue
        if not current:
            continue
        ms = _SIM_RE.search(line)
        if ms:
            current["similarity"] = float(ms.group(1))
            continue
        mm = _MISS_RE.search(line)
        if mm:
            current["link_missing"] = int(mm.group(1))
            continue
        ma = _ADD_RE.search(line)
        if ma:
            current["link_added"] = int(ma.group(1))
            continue
    if current:
        flagged.append(Flagged(**current))
    return flagged


def load_log(log_path: pathlib.Path) -> dict[str, str]:
    """Return {our_path: outcome} for previously reviewed pages."""
    if not log_path.exists():
        return {}
    reviewed = {}
    for line in log_path.read_text().splitlines():
        m = re.match(r"^- `([^`]+)`\s+→\s+([a-z]+)", line)
        if m:
            reviewed[m.group(1)] = m.group(2)
    return reviewed


def append_log(log_path: pathlib.Path, our_path: str, outcome: str,
               note: str = "") -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    if not log_path.exists():
        log_path.write_text(
            "# Audit review log\n\n"
            "Each line records the outcome of a manual side-by-side review.\n"
            "Run `scripts/audit-review.py` to add to this log.\n\n"
        )
    line = f"- `{our_path}` → {outcome}"
    if note:
        line += f"  ({note})"
    line += f"  _{datetime.date.today().isoformat()}_\n"
    with open(log_path, "a") as f:
        f.write(line)


def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("--audit", default=str(DEFAULT_AUDIT),
                    help=f"Audit report path (default: {DEFAULT_AUDIT.relative_to(REPO_ROOT)})")
    ap.add_argument("--log", default=str(DEFAULT_LOG),
                    help=f"Review log path (default: {DEFAULT_LOG.relative_to(REPO_ROOT)})")
    ap.add_argument("--our-base", default=DEFAULT_OUR,
                    help=f"URL base for OUR Lektor build (default: {DEFAULT_OUR}). "
                         f"Use http://localhost:5000 with `lektor serve` running, "
                         f"or http://localhost:8001 with a static build served.")
    ap.add_argument("--joyce-base", default=DEFAULT_JOYCE,
                    help="URL base for Joyce's mirror. Default: local file:// mirror.")
    ap.add_argument("--filter", default=None,
                    help="Only review pages whose path matches this regex.")
    ap.add_argument("--start", type=int, default=0,
                    help="Start at the Nth flagged page (1-indexed).")
    ap.add_argument("--max-similarity", type=float, default=100.0,
                    help="Only review pages with similarity at or BELOW this percentage. "
                         "Useful for triaging the worst diffs first (e.g. --max-similarity 80).")
    ap.add_argument("--list", action="store_true",
                    help="List flagged pages and exit; don't open anything.")
    ap.add_argument("--include-reviewed", action="store_true",
                    help="Don't skip pages already in the log.")
    args = ap.parse_args()

    flagged = parse_audit(pathlib.Path(args.audit))
    if not flagged:
        print("No flagged pages found in audit report.", file=sys.stderr)
        sys.exit(0)
    flagged = [f for f in flagged if f.similarity <= args.max_similarity]
    if args.filter:
        pat = re.compile(args.filter)
        flagged = [f for f in flagged if pat.search(f.our_path)]
    reviewed = {} if args.include_reviewed else load_log(pathlib.Path(args.log))
    queue = [f for f in flagged if f.our_path not in reviewed]
    # Worst first.
    queue.sort(key=lambda f: f.similarity)

    if args.start:
        queue = queue[args.start - 1:]

    if args.list:
        print(f"{len(queue)} flagged pages awaiting review "
              f"({len(reviewed)} already in log):\n")
        for i, f in enumerate(queue, 1):
            note = f"sim {f.similarity:.0f}%"
            if f.link_missing or f.link_added:
                note += f", -{f.link_missing}/+{f.link_added} links"
            print(f"  {i:3d}. [{note}] {f.our_path}")
        return

    print(f"Reviewing {len(queue)} flagged pages "
          f"(already done: {len(reviewed)}). "
          f"Commands: y=accept, n=flag, s=skip, q=quit\n")

    for i, f in enumerate(queue, 1):
        our_url   = f.our_url(args.our_base)
        joyce_url = f.joyce_url(args.joyce_base)
        print(f"\n[{i}/{len(queue)}] {f.our_path}")
        print(f"   similarity {f.similarity:.0f}%, "
              f"-{f.link_missing}/+{f.link_added} links")
        print(f"   OURS:  {our_url}")
        print(f"   JOYCE: {joyce_url}")
        webbrowser.open(our_url, new=2)
        webbrowser.open(joyce_url, new=2)
        while True:
            ans = input("   action [y/n/s/q]? ").strip().lower()
            if ans in {"y", "n", "s", "q"}:
                break
            print("   (y=accept intentional, n=flag for follow-up, s=skip, q=quit)")
        if ans == "q":
            print("\nExiting. Resume any time — log is preserved.")
            return
        if ans == "s":
            continue
        outcome = "accepted" if ans == "y" else "flagged"
        note = input("   optional note (Enter for none): ").strip()
        append_log(pathlib.Path(args.log), f.our_path, outcome, note)

    print(f"\nReviewed {len(queue)} pages. See {args.log} for the running log.")


if __name__ == "__main__":
    main()
