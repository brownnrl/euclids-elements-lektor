"""Generate content/geomlib/constructions/contents.lr.

Signatures and descriptions are parsed out of the library's own
doc/constructions-reference.md rather than restated here, so the page cannot
drift from the source silently. The figures themselves live in specs.py.
"""
import sys, re, os, html, json
sys.path.insert(0, os.path.dirname(__file__))
import specs

REF = "/data-mirrored/projects/geometry/euclid/doc/constructions-reference.md"
OUT = "/data-mirrored/projects/geometry/euclids-elements-lektor/content/geomlib/constructions/contents.lr"


def parse_ref():
    """(type, name) -> (signature, description).

    The tables don't share a column layout — the polyhedra table has no
    signature column at all — so read the header row and look the columns up
    by name instead of by position.
    """
    txt = open(REF).read()
    out = {}
    for sec in re.split(r"^## ", txt, flags=re.M):
        head = sec.split("\n", 1)[0].strip().lower()
        if "constructions" not in head:
            continue
        typ = head.split()[0]
        typ = {"polyhedra": "polyhedron"}.get(typ, typ)
        rows = [r for r in sec.split("\n") if r.startswith("|")]
        if len(rows) < 3:
            continue
        cols = [c.strip().lower() for c in rows[0].strip("|").split("|")]
        try:
            i_sig = cols.index("post-expansion signature")
        except ValueError:
            i_sig = None
        i_desc = cols.index("description")
        for row in rows[2:]:
            cells = row.strip().strip("|").split("|")
            name = cells[0].strip().strip("`")
            if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9]*", name):
                continue
            sig = cells[i_sig].strip() if i_sig is not None else ""
            out[(typ, name)] = (sig, cells[i_desc].strip())
    return out


def inline(s):
    """The reference cells are markdown; the cards are raw HTML blocks, which
    mistune passes through untouched. So render the handful of inline forms
    that actually occur rather than leaving `backticks` visible on the page."""
    s = s.replace(r"\|", "|")
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    return s


def first_sentence(s):
    """A few descriptions (path, curvedTriangle) run to a full paragraph with
    issue links. A card wants the opening claim; the note beneath adds the
    rest in the page's own voice."""
    s = re.sub(r"\s*\(#\d+\)\s*", " ", s).strip()
    m = re.match(r"^(.+?[.!?])(?:\s+[A-Z(])", s)
    return (m.group(1) if m else s).strip().rstrip(".")


REFTBL = parse_ref()
GROUPS = [
    ("point", "Point", specs.POINT),
    ("line", "Line", specs.LINE),
    ("circle", "Circle", specs.CIRCLE),
    ("polygon", "Polygon", specs.POLYGON),
    ("sector", "Sector", specs.SECTOR),
    ("plane", "Plane", specs.PLANE),
    ("sphere", "Sphere", specs.SPHERE),
    ("polyhedron", "Polyhedron", specs.POLYHEDRON),
]


def canvas(cid, elements, w, h, opts=None):
    els = ",\n            ".join('"%s"' % e for e in elements)
    # Extra init options, e.g. showAngles for the angle-marker figures:
    # markers default to hidden because Euclid's own diagrams draw no angle
    # arcs, which is right for a proposition and wrong for a card whose
    # subject IS the marker.
    extra = "".join('        %s: %s,\n' % (k, json.dumps(v))
                    for k, v in sorted((opts or {}).items()))
    return (
        '<figure class="diagram block">\n'
        '<canvas id="%s" width="%d" height="%d" tabindex="0"></canvas>\n'
        '<script type="text/javascript">\n'
        "    geomlib.init({\n"
        '        canvasid: "%s",\n'
        '        background: "0,0,100",\n'
        "        elements: [\n"
        "            %s\n"
        "        ],\n"
        "%s"
        "    });\n"
        "</script>\n"
        "</figure>" % (cid, w, h, cid, els, extra)
    )


def card(typ, name, sig, desc, decl, fig, note):
    anchor = "%s-%s" % (typ, name)
    parts = ['<section class="ctor-card" id="%s">' % anchor,
             "<h3>%s;%s</h3>" % (typ, name)]
    if sig:
        parts.append('<p class="ctor-sig"><b>Signature</b> — %s</p>' % inline(sig))
    if desc:
        parts.append('<p class="ctor-desc">%s.</p>' % inline(first_sentence(desc)))
    if decl:
        parts.append("<pre><code>%s</code></pre>" % html.escape(decl, quote=False))
    parts.append(fig)
    if note:
        parts.append('<p class="ctor-note">%s</p>' % inline(note))
    # The overlay reads the figure back out of the card, so the button
    # carries no source of its own — see assets/js/ctor-source.js.
    parts.append('<div class="ctor-actions">'
                 '<button type="button" class="ctor-src" aria-haspopup="dialog">'
                 'Source</button></div>')
    parts.append("</section>")
    # No blank lines: a blank line inside a raw HTML block ends the block for
    # mistune, which would then parse the rest of the card as markdown.
    return "\n".join(parts)


body = []
body.append("""Every construction the library implements, each with a figure you can drag.

An element is declared as a single string:

```
name;type;construction;arguments;nameColor;vertexColor;edgeColor;faceColor
```

The four colour fields are optional; `0` means transparent. Each figure's
**Source** button gives the complete runnable file behind it, to copy or to open
in CodePen.

> **Signatures are written post-expansion.** A line's name in an argument list
> expands to its two endpoints, so `params: ["AB"]` arrives as two points rather
> than one. That is why some signatures below read as taking more points than
> you would write.
""")

# Index. Built from the same tables as the cards, so it can't list a
# construction the page doesn't show, or miss one it does.
idx = ['<nav class="ctor-index">']
for typ, label, table in GROUPS:
    if not table:
        continue
    links = ", ".join(
        '<a href="#%s-%s"><code>%s</code></a>' % (typ, n, n) for n in table
    )
    idx.append('<div class="ctor-index-group"><b>%s</b> — %s</div>' % (label, links))
idx.append("</nav>")
body.append("\n" + "\n".join(idx) + "\n")

n = 0
for typ, label, table in GROUPS:
    if not table:
        continue
    body.append("\n## %s constructions\n" % label)
    if typ in specs.GROUP_NOTES:
        body.append("\n%s\n" % specs.GROUP_NOTES[typ])
    cards = []
    for name, entry in table.items():
        elements, note = entry[0], entry[1]
        w, h = entry[2] if len(entry) > 2 else (260, 200)
        opts = entry[3] if len(entry) > 3 else None
        sig, desc = REFTBL.get((typ, name), ("", ""))
        n += 1
        # The declaration to show is this construction's own element — the
        # last one in the spec whose construction field matches.
        decl = ""
        for e in elements:
            f = e.split(";")
            if len(f) > 2 and f[1] == typ and f[2] == name:
                decl = e
        cards.append(card(typ, name, sig, desc,
                          decl, canvas("c_%s_%s" % (typ, name), elements, w, h, opts), note))
    body.append('\n<div class="ctor-grid">\n' + "\n".join(cards) + "\n</div>\n")

body.append("""
The library's own documentation — the API reference, the implementation model,
and the guides to adding a construction or an animation — is listed at the foot
of the [geomlib](/geomlib/) page.

- [**Quickstart**](/geomlib/quickstart/) — a first figure, built one
  construction at a time.
- [**Slide transitions**](/geomlib/animations/) — animating the step from one
  slide to the next.
""")


page = """_model: other_work
---
title: Constructions
---
order: 4
---
body:

%s""" % "".join(body)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w").write(page)
missing = [k for k in REFTBL if k[0] in dict((g[0], 1) for g in GROUPS)
           and k[1] not in dict(GROUPS)[k[0]]] if False else None
print("wrote %s: %d constructions, %d lines" % (OUT, n, len(page.splitlines())))

# Coverage report against the reference table, so a construction added to the
# library shows up here as a gap rather than silently missing from the page.
have = set()
for typ, label, table in GROUPS:
    for name in table:
        have.add((typ, name))
gaps = sorted(k for k in REFTBL if k not in have)
if gaps:
    print("NOT YET DEMONSTRATED (%d):" % len(gaps))
    for typ, name in gaps:
        print("  %s;%s" % (typ, name))
