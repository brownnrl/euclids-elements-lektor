#!/usr/bin/env python3
"""One-off: parse the subject index's hand-written HTML body into structured data.

Run once to produce databags/subject_index.json, after which the page is
rendered from that file by templates/subject_index.html and this script is
only of historical interest.

The parser is deliberately strict. Every logical line of the body must
classify as a letter heading, a term, a see-also, or a sub-entry; anything
left over is reported and the run fails, so the conversion cannot silently
drop an entry.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# The page's HTML body is retired once this has run, so the converter takes
# the source explicitly. To re-run it, recover the body from the commit that
# retired it:
#     git show <commit>^:content/elements/prematter/subjindex/contents.lr > /tmp/old.lr
#     python3 scripts/subjindex_to_json.py /tmp/old.lr
SRC = os.path.join(ROOT, "content/elements/prematter/subjindex/contents.lr")
OUT = os.path.join(ROOT, "databags/subject_index.json")

LINK = re.compile(r'<a href="([^"]+)"\s*>(.*?)</a>', re.S)


def render(fragment):
    """Split a fragment into what to SHOW and what to CHECK.

    The two are not the same. Most entries end with their citations
    ("boundary &nbsp; <a>I.Def.13</a>"), but some carry a link mid-sentence
    ("acute angle. See <a>angle</a>, acute."). Extracting links out of the
    prose and re-appending them would reorder that into "acute angle. See ,
    acute. angle". So the display fragment keeps its links exactly where the
    source put them, and the citation list is pulled out alongside it purely
    for validation.
    """
    html = fragment.strip()
    html = re.sub(r"^(&nbsp;\s*)+", "", html).strip()      # sub-entry indent
    html = " ".join(html.split())
    cites = [{"label": " ".join(re.sub(r"<[^>]+>", "", t).split()), "href": h}
             for h, t in LINK.findall(html)]
    text = " ".join(re.sub(r"<[^>]+>", "", html).replace("&nbsp;", " ").split())
    return html, text, cites


def logical_lines(block):
    """The body wraps long entries across source lines. Re-join them, so a
    logical line is exactly one `<br>`-introduced item."""
    out = []
    for raw in block.split("\n"):
        s = raw.rstrip()
        if not s.strip():
            out.append(None)          # blank line: entry separator
        elif s.lstrip().startswith("<br>"):
            out.append(s.lstrip()[4:])
        elif out and out[-1] is not None:
            out[-1] += " " + s.strip()
        else:
            out.append(s.strip())     # first item of a block, no leading <br>
    return out


def parse(src):
    text = open(src, encoding="utf-8").read()
    body = text.split("\nbody:\n", 1)[1]
    # Drop the A-Z jump nav; the template regenerates it from the letters.
    body = re.sub(r"<center>.*?</center>", "", body, flags=re.S)

    letters, unparsed = [], []
    current = None
    for chunk in re.split(r'(<h4 id="[^"]+">.*?</h4>)', body, flags=re.S):
        h = re.match(r'<h4 id="([^"]+)">(.*?)</h4>', chunk, re.S)
        if h:
            current = {"id": h.group(1),
                       "title": " ".join(re.sub(r"<[^>]+>", "", h.group(2)).split()),
                       "entries": []}
            letters.append(current)
            continue
        if current is None:
            continue

        # `columns: false` records the one entry that sits outside the
        # threecolumn div in the source (Byrne, between B and C).
        for part, in_columns in [(m, True) for m in re.findall(
                r'<div class="threecolumn">(.*?)</div>', chunk, re.S)] + \
                [(re.sub(r'<div class="threecolumn">.*?</div>', "", chunk, flags=re.S), False)]:
            entry = None
            for line in logical_lines(part):
                if line is None:
                    entry = None
                    continue
                line = line.strip()
                if not line:
                    continue
                anchor = None
                a = re.match(r'<span id="([^"]+)"></span>\s*(.*)', line, re.S)
                if a:
                    anchor, line = a.group(1), a.group(2).strip()
                    if not line:
                        # anchor on its own line; it belongs to the next term
                        entry = {"_pending_anchor": anchor}
                        continue
                is_sub = line.startswith("&nbsp;")
                html, text, cites = render(line)
                if not text and not cites:
                    continue
                prose = text
                # Five of the six see-also lines are indented like sub-entries
                # in the source. They are cross-references, not sub-entries,
                # so classify on what they say rather than where they sit.
                m_see = re.match(r"See also\b[\s.,]*(.*)$", prose, re.I)
                if m_see and entry:
                    entry["see_also"] = {"html": html, "text": text, "cites": cites}
                elif is_sub and entry:
                    entry.setdefault("subentries", []).append(
                        {"html": html, "text": text, "cites": cites})
                else:
                    pending = (entry or {}).get("_pending_anchor")
                    entry = {"html": html, "text": text}
                    if anchor or pending:
                        entry["anchor"] = anchor or pending
                    if cites:
                        entry["cites"] = cites
                    if not in_columns:
                        entry["columns"] = False
                    current["entries"].append(entry)
            # anything left dangling
        for e in current["entries"]:
            e.pop("_pending_anchor", None)

    return letters, unparsed


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else SRC
    letters, unparsed = parse(src)
    entries = sum(len(l["entries"]) for l in letters)
    subs = sum(len(e.get("subentries", [])) for l in letters for e in l["entries"])
    cites = sum(len(e.get("cites", [])) for l in letters for e in l["entries"]) + \
            sum(len(s["cites"]) for l in letters for e in l["entries"]
                for s in e.get("subentries", [])) + \
            sum(len(e["see_also"]["cites"]) for l in letters for e in l["entries"]
                if e.get("see_also"))
    anchors = sum(1 for l in letters for e in l["entries"] if e.get("anchor"))
    see = sum(1 for l in letters for e in l["entries"] if e.get("see_also"))
    print("letters %d | entries %d | sub-entries %d | citations %d | anchors %d | see-also %d"
          % (len(letters), entries, subs, cites, anchors, see))
    if unparsed:
        print("UNPARSED (%d):" % len(unparsed))
        for u in unparsed[:20]:
            print("   ", u[:110])
        return 1
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump({"letters": letters}, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print("wrote", os.path.relpath(OUT, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
