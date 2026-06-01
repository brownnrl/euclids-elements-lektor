#!/usr/bin/env python3
"""Walk Lektor content tree, find every <img src="*.gif"> reference inside
   any contents.lr, and copy the matching source file (if found) into the
   same content folder so it becomes a page attachment."""
import re
import pathlib
import shutil

LEKTOR = pathlib.Path("/data-mirrored/projects/geometry/euclids-elements-lektor/content/elements/books")
SOURCES = [
    pathlib.Path("/data-mirrored/projects/geometry/euclids-elements.org/elements/bookI"),
    pathlib.Path("/data-mirrored/projects/geometry/djoyce/converted/elements/bookI"),
    pathlib.Path("/data-mirrored/projects/geometry/djoyce/converted/elements/bookII"),
    pathlib.Path("/data-mirrored/projects/geometry/djoyce/converted/elements/bookIII"),
    pathlib.Path("/data-mirrored/projects/geometry/djoyce/converted/elements/bookIV"),
    pathlib.Path("/data-mirrored/projects/geometry/djoyce/converted/java/elements/bookI"),
    pathlib.Path("/data-mirrored/projects/geometry/djoyce/converted/java/elements/bookII"),
    pathlib.Path("/data-mirrored/projects/geometry/djoyce/converted/java/elements/bookIII"),
    pathlib.Path("/data-mirrored/projects/geometry/djoyce/converted/java/elements/bookIV"),
    pathlib.Path("/data-mirrored/projects/geometry/djoyce/mirror/aleph0.clarku.edu/~djoyce/elements/bookI"),
    pathlib.Path("/data-mirrored/projects/geometry/djoyce/mirror/aleph0.clarku.edu/~djoyce/elements/bookIII"),
    pathlib.Path("/data-mirrored/projects/geometry/djoyce/mirror/aleph0.clarku.edu/~djoyce/elements/bookIV"),
    pathlib.Path("/data-mirrored/projects/geometry/djoyce/mirror/aleph0.clarku.edu/~djoyce/java/elements/bookI"),
    pathlib.Path("/data-mirrored/projects/geometry/djoyce/mirror/aleph0.clarku.edu/~djoyce/java/elements/bookIII"),
    pathlib.Path("/data-mirrored/projects/geometry/djoyce/mirror/aleph0.clarku.edu/~djoyce/java/elements/bookIV"),
]

GIF_RE = re.compile(r'<img[^>]+src="([^"]+\.gif)"', re.IGNORECASE)

copied = 0
missing = []
skipped = 0

for lr in LEKTOR.rglob("contents.lr"):
    text = lr.read_text(errors="replace")
    refs = set(GIF_RE.findall(text))
    for gif in refs:
        # Skip refs that already have a path component — leave those alone
        if "/" in gif:
            skipped += 1
            continue
        target = lr.parent / gif
        if target.exists():
            skipped += 1
            continue
        # Find the source
        for src_dir in SOURCES:
            cand = src_dir / gif
            if cand.exists():
                shutil.copy2(cand, target)
                copied += 1
                break
        else:
            missing.append((lr.parent.name, gif))

print(f"Copied {copied} gif(s) as page attachments.")
print(f"Skipped {skipped} already-present or path-qualified.")
if missing:
    print(f"\nMissing in source mirrors ({len(missing)}):")
    for leaf, gif in missing[:20]:
        print(f"  {leaf}: {gif}")
    if len(missing) > 20:
        print(f"  ... and {len(missing)-20} more")
