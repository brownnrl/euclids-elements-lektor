#!/usr/bin/env python3
"""Validate the subject index's cross-references at build time.

The subject index is ~800 hand-written entries carrying ~800 citation links,
~85 internal "See ..." references and a few dozen anchors. Nothing checks any
of it: a renamed anchor or a mistyped citation surfaces as a 404 in production,
or worse as a link that resolves to the wrong proposition and says nothing.

Three checks:

  1. every  href="#x"  has a matching  id="x"  on the page;
  2. every  href="/elements/..."  resolves to a page that exists;
  3. the link TEXT agrees with the target page's own short_label — this is the
     one that catches a link reading "I.Def.12" that points at Definition 11.

KNOWN_DISCREPANCIES exists for mismatches that are Dr. Joyce's own, faithfully
carried over from his subjindex.html: this edition reproduces his text, and
quietly rewriting his cross-references would be a different editorial act from
fixing a conversion bug. It is empty, and that is the audit's finding rather
than an oversight.

The first run reported 136 mismatches, and every one turned out to be ours.
Joyce's files bundled several definitions each — bookIII had six files for
eleven definitions, defIII6.html holding Definitions 6 through 9 — so his
index linking defIII6.html for "III.Def.8" was correct on his own site. This
conversion split those bundles into a page per definition and left the index
pointing at the old bundle heads. Eleven of them addressed group pages that
are `_hidden` and therefore never built, so they were live 404s.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
DATABAG = os.path.join(ROOT, "databags/subject_index.json")

# (href, link text) pairs where Joyce's own page has the same mismatch.
# Verified against the mirror of aleph0.clarku.edu/~djoyce/elements/subjindex.html.
KNOWN_DISCREPANCIES = {
    # populated below, after the first audit
}

# Cross-references whose target does not answer them, where the fault is in
# Joyce's index rather than in this edition's handling of it. Recorded rather
# than rewritten: correcting them means editing his text, which is a different
# act from fixing a conversion artifact.
KNOWN_UNMET = {
    # "acute angle. See angle, acute." lands on the angle entry, whose
    # sub-entry for Euclid I.Def.12 — the definition of an ACUTE angle — is
    # labelled "obtuse angle". The entry below it, "obtuse angle I.Def.11",
    # is the correct one, so the first is a slip for "acute angle".
    ("acute angle", "acute"),
}


def url_of(path):
    rel = os.path.relpath(os.path.dirname(path), CONTENT)
    return "/" + rel.replace(os.sep, "/").rstrip("/") + "/"


def lr_fields(text):
    """Top-level fields of a .lr file. Splitting on lines of exactly three
    dashes and keying on each chunk's first line matters: a bare grep for
    `short_label:` also matches the worked example inside the colophon's
    <pre>, and would claim that page owns the label I.1."""
    out = {}
    for chunk in re.split(r"^---$", text, flags=re.M):
        chunk = chunk.lstrip("\n")
        m = re.match(r"([A-Za-z_][A-Za-z0-9_]*):[ \t]*(.*)", chunk)
        if m:
            out[m.group(1)] = m.group(2).strip()
    return out


def page_labels():
    """url -> short_label for every page that declares one. Hidden bundle
    guides are skipped: they hold a shared commentary, not a citable record."""
    out = {}
    for dirpath, _dirnames, filenames in os.walk(CONTENT):
        if "contents.lr" not in filenames:
            continue
        p = os.path.join(dirpath, "contents.lr")
        f = lr_fields(open(p, encoding="utf-8").read())
        if f.get("_hidden") == "yes":
            continue
        out[url_of(p)] = f.get("short_label") or None
    return out


# The index cites in a shorter form than a page's own label in a few places —
# "Post.4" for I.Post.4, "C.N." for C.N.1, "VII.Def.1-2" for a range whose
# first member is the target. These are Joyce's citation style, not errors.
def label_agrees(text, label):
    if text == label:
        return True
    bare = re.sub(r"^[IVX]+\.", "", label)          # I.Post.4 -> Post.4
    if text in (bare, label):
        return True
    first = text.split("-")[0].strip()               # VII.Def.1-2 -> VII.Def.1
    if first and (first == label or first == bare):
        return True
    if label.startswith(text) and text.endswith("."):  # "C.N." for C.N.1
        return True
    return False


DEFAULT_ANCHOR = {"proposition": "prop", "corollary": "cor", "lemma": "lemma",
                  "note": "note", "remark": "remark"}


def anchors_of(url):
    """The section anchors a page offers — explicit `anchor:` overrides, else
    the default for the section's kind."""
    p = os.path.join(CONTENT, url.strip("/").replace("/", os.sep), "contents.lr")
    try:
        text = open(p, encoding="utf-8").read()
    except OSError:
        return set()
    out = set()
    for blk in text.split("#### prop_section ####")[1:]:
        m = re.search(r"^anchor:\s*(\S+)", blk, re.M)
        if m:
            out.add(m.group(1))
            continue
        k = re.match(r"\s*kind:\s*(\w+)", blk)
        if k:
            out.add(DEFAULT_ANCHOR.get(k.group(1), k.group(1)))
    return out


def main():
    idx = json.load(open(DATABAG, encoding="utf-8"))
    labels = page_labels()

    anchors = {e["anchor"] for l in idx["letters"] for e in l["entries"]
               if e.get("anchor")}
    anchors |= {l["id"] for l in idx["letters"]}
    problems = []
    checked = 0
    section_anchors = {}

    def check_cite(c, where):
        nonlocal checked
        checked += 1
        href = c["href"]
        # labels may carry inline emphasis; compare the text
        label = " ".join(re.sub(r"<[^>]+>", "", c["label"]).split())
        if href.startswith("#"):
            if href[1:] not in anchors:
                problems.append(("dead-anchor", where, "%s matches no entry" % href))
            return
        path, _, fragment = href.partition("#")
        key = path if path.endswith("/") else path + "/"
        if key not in labels:
            problems.append(("missing-page", where, "%s — no such page" % href))
            return
        # Lektor drops the trailing slash on a slug containing a dot (Book X's
        # defX.I.1 and friends) and emits the page as a FILE of that name, so
        # the directory form is a 404 in production. Verified against the live
        # site: no-slash 200, trailing-slash 404.
        if path.endswith("/") and "." in key.rstrip("/").rsplit("/", 1)[-1]:
            problems.append(("trailing-slash", where,
                             "%s — dotted slug, drop the trailing slash" % href))
            return
        if fragment:
            if key not in section_anchors:
                section_anchors[key] = anchors_of(key)
            if fragment not in section_anchors[key]:
                problems.append(("dead-section", where,
                                 "%s — page has no section anchored #%s" % (href, fragment)))
                return
        want = labels[key]
        if want is None:
            return
        if fragment and label.startswith(want):
            return
        if label_agrees(label, want) or KNOWN_DISCREPANCIES.get(href) == label:
            return
        problems.append(("label-mismatch", where,
                         '%s reads "%s", target is %s' % (href, label, want)))

    # An entry keyed by anchor, so a "See X, y" can be checked for whether the
    # target actually offers a "y".
    by_anchor = {e["anchor"]: e for l in idx["letters"] for e in l["entries"]
                 if e.get("anchor")}

    def check_promise(rec, where, kind):
        """"See angle, acute" promises a sub-entry about `acute` under `angle`.
        Nothing else notices when the target does not have one — the link
        resolves, it just lands somewhere that does not answer the reference."""
        ref = rec.get(kind)
        if not ref or not ref.get("tail"):
            return
        tail = ref["tail"].lower().strip(" .,")
        for r in ref["refs"]:
            if not r["href"].startswith("#"):
                continue
            target = by_anchor.get(r["href"][1:])
            if target is None:
                continue
            hay = [target.get("term", "")] + [sub.get("term", "")
                                              for sub in target.get("subentries", [])]
            if (rec.get("term", ""), ref["tail"]) in KNOWN_UNMET:
                continue
            if not any(tail in (h or "").lower() for h in hay):
                problems.append(("unmet-reference", where,
                                 '%s names "%s" but %s has no such entry'
                                 % (kind.replace("_", " "), ref["tail"], r["href"])))

    def walk(rec, where):
        for c in rec.get("cites", []):
            check_cite(c, where)
        for kind in ("see", "see_also"):
            if rec.get(kind):
                for c in rec[kind]["refs"]:
                    check_cite(c, "%s (%s)" % (where, kind.replace("_", " ")))
                check_promise(rec, where, kind)
        if rec.get("href"):
            check_cite({"href": rec["href"], "label": rec["term"]}, where)
        # The index nests three deep, so this recurses rather than looking one
        # level down: 26 references live in the third level.
        for sub in rec.get("subentries", []):
            walk(sub, "%s / %s" % (where, sub.get("term", "")))

    for letter in idx["letters"]:
        for e in letter["entries"]:
            walk(e, "%s / %s" % (letter["id"], e.get("term", "")))

    entries = sum(len(l["entries"]) for l in idx["letters"])
    print("subject index      : %s" % os.path.relpath(DATABAG, ROOT))
    print("letters / entries  : %d / %d" % (len(idx["letters"]), entries))
    print("anchors            : %d" % len(anchors))
    print("references checked : %d" % checked)
    print("known discrepancies: %d label, %d unmet reference (Joyce's own)"
          % (len(KNOWN_DISCREPANCIES), len(KNOWN_UNMET)))
    print("problems           : %d" % len(problems))
    for kind, where, why in problems:
        print("    [%s] %s — %s" % (kind, where, why))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
