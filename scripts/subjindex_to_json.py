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


SEE_ALSO = re.compile(r"^(?P<head>.*?)\bSee\s+also\b\s*(?P<rest>.*)$", re.S | re.I)
SEE = re.compile(r"^(?P<head>.*?)\bSee\b\s*(?P<rest>.*)$", re.S | re.I)
ONE_LINK = re.compile(r'^<a href="(?P<href>[^"]+)"\s*>(?P<label>.*?)</a>(?P<tail>.*)$', re.S)


def clean(fragment):
    """Normalise a source fragment: drop the sub-entry indent and the &nbsp;
    spacers, which were doing the job the stylesheet now does."""
    f = fragment.strip()
    f = re.sub(r"(?:<br>)+$", "", f).strip()
    f = re.sub(r"^(?:&nbsp;\s*)+", "", f)
    f = f.replace("&nbsp;", " ")
    return " ".join(f.split())


def plain(fragment):
    """Strip the anchors, keep the inline emphasis. The index italicises book
    titles and Latin phrases (<i>Elements</i>, <i>ex aequali</i>), so removing
    every tag would flatten those away."""
    f = re.sub(r"</?a\b[^>]*>", "", fragment)
    return " ".join(f.replace("&nbsp;", " ").split())


def cross_ref(rest):
    """A `See` / `See also` names one or more targets, sometimes with prose
    qualifying them ("See angle, acute" / "See tetrahedron, cube, ... and
    dodecahedron")."""
    rest = rest.strip()
    links = LINK.findall(rest)
    if not links:
        return None
    refs = [{"href": h, "label": plain(t)} for h, t in links]
    tail = plain(rest[rest.rindex("</a>") + 4:]).strip(" .,")
    ref = {"refs": refs}
    if tail:
        ref["tail"] = tail
    return ref


def decompose(fragment):
    """A fragment -> a record, or an error string if it cannot be modelled.

    Every fragment must decompose; the caller fails the run on anything left
    over, so the conversion cannot quietly flatten something it did not
    understand.
    """
    f = clean(fragment)
    if not f:
        return None, None

    # A "See" may follow a citation on the same entry:
    #     multilateral figure  <a>I.Def.19</a>.  See <a>polygon</a>.
    # so the head is decomposed in its own right rather than flattened.
    for pattern, key in ((SEE_ALSO, "see_also"), (SEE, "see")):
        m = pattern.match(f)
        if not m or "<a " not in m.group("rest"):
            continue
        ref = cross_ref(m.group("rest"))
        if not ref:
            continue
        head = m.group("head").strip().rstrip(".,").strip()
        rec = {}
        if head:
            sub, err = decompose(head)
            if err:
                return None, err
            if sub:
                rec.update(sub)
        rec[key] = ref
        return rec, None

    links = LINK.findall(f)
    if not links:
        return {"term": plain(f)}, None

    # A term that is itself a link, with prose after it (the Euclid entry).
    m = ONE_LINK.match(f)
    if m and m.group("tail").strip():
        return {"term": plain(m.group("label")), "href": m.group("href"),
                "tail": plain(m.group("tail"))}, None

    # The ordinary shape: a term followed by its citations.
    head = f[:f.index("<a ")]
    if "<a " in LINK.sub("", f):
        return None, f
    return {"term": plain(head).rstrip(" ,"),
            "cites": [{"label": plain(t), "href": h} for h, t in links]}, None


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
                rec, err = decompose(line)
                if err is not None:
                    unparsed.append(err)
                    continue
                if rec is None:
                    continue
                if is_sub and entry is not None and "term" in entry:
                    if "see_also" in rec and not rec.get("term"):
                        entry["see_also"] = rec["see_also"]
                    else:
                        entry.setdefault("subentries", []).append(rec)
                elif "see_also" in rec and not rec.get("term") and entry is not None:
                    entry["see_also"] = rec["see_also"]
                else:
                    pending = (entry or {}).get("_pending_anchor")
                    if anchor or pending:
                        rec["anchor"] = anchor or pending
                    if not in_columns:
                        rec["columns"] = False
                    entry = rec
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
    def refs(rec):
        n = len(rec.get("cites", []))
        n += len(rec["see"]["refs"]) if rec.get("see") else 0
        n += len(rec["see_also"]["refs"]) if rec.get("see_also") else 0
        n += 1 if rec.get("href") else 0
        return n
    cites = sum(refs(e) + sum(refs(s) for s in e.get("subentries", []))
                for l in letters for e in l["entries"])
    anchors = sum(1 for l in letters for e in l["entries"] if e.get("anchor"))
    see = sum(1 for l in letters for e in l["entries"] if e.get("see_also"))
    xref = sum(1 for l in letters for e in l["entries"]
               if e.get("see")) + sum(1 for l in letters for e in l["entries"]
               for s in e.get("subentries", []) if s.get("see"))
    print("letters %d | entries %d | sub-entries %d | references %d | anchors %d | "
          "see %d | see-also %d" % (len(letters), entries, subs, cites, anchors, xref, see))
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
