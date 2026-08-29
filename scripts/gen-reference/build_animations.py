"""Generate content/geomlib/animations/contents.lr from anims.py."""
import sys, os, html, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from anims import ANIMS

OUT = "/data-mirrored/projects/geometry/euclids-elements-lektor/content/geomlib/animations/contents.lr"


def inline(s):
    s = html.escape(s, quote=False)
    s = s.replace("`", "")
    return s


def slide_js(slides, all_names):
    out = []
    for text, visible, highlighted, anims in slides:
        vis = all_names if visible == "ALL" else visible
        parts = ['                { text: %s' % json.dumps(text),
                 '                  visible: %s' % json.dumps(vis)]
        if highlighted:
            parts.append('                  highlighted: %s' % json.dumps(highlighted))
        if anims:
            entries = []
            for elem, name, args in anims:
                e = '{ elem: %s, name: geomlib.A.%s' % (json.dumps(elem), name)
                if args:
                    e += ', args: %s' % args
                entries.append(e + ' }')
            parts.append('                  transition: { animations: [\n                      '
                         + ',\n                      '.join(entries) + ' ] }')
        out.append(',\n'.join(parts) + ' }')
    return ',\n'.join(out)


def card(entry):
    (name, target, args, dur, desc, note, elements, slides, wh) = entry
    w, h = wh
    cid = "a_" + name.replace(".", "_")
    all_names = [e.split(";")[0] for e in elements]
    # Anything a slide withholds must start hidden, or it is on screen before
    # the slide that introduces it.
    first = slides[0][1]
    first = all_names if first == "ALL" else first
    hidden = [n for n in all_names if n not in first]

    els = ",\n            ".join('"%s"' % e for e in elements)
    init = ['    geomlib.init({',
            '        canvasid: "%s",' % cid,
            '        background: "35,19,100",',
            '        title: "A.%s",' % name,
            '        elements: [',
            '            ' + els,
            '        ],']
    if hidden:
        init.append('        initiallyHidden: %s,' % json.dumps(hidden))
    init.append('        slides: [')
    init.append(slide_js(slides, all_names))
    init.append('        ],')
    init.append('    });')

    fig = ('<figure class="diagram block">\n'
           '<canvas id="%s" width="%d" height="%d" tabindex="0"></canvas>\n'
           '<script type="text/javascript">\n' % (cid, w, h)
           + "\n".join(init) + '\n</script>\n</figure>')

    decl = next((a for a in slides[-1][3] or [] if a[1].endswith(name.split(".")[-1])), None)
    snippet = 'transition: { animations: [ { elem: "%s", name: geomlib.A.%s%s } ] }' % (
        decl[0], name, (", args: " + decl[2]) if decl and decl[2] else "") if decl else ""

    parts = ['<section class="ctor-card" id="%s">' % name.replace(".", "-").lower(),
             "<h3>A.%s</h3>" % name,
             '<p class="ctor-sig"><b>Applies to</b> — <code>%s</code></p>' % inline(target),
             '<p class="ctor-sig"><b>Arguments</b> — <code>%s</code></p>' % inline(args),
             '<p class="ctor-sig"><b>Default rate</b> — <code>%s</code></p>' % inline(dur),
             '<p class="ctor-desc">%s</p>' % inline(desc)]
    if snippet:
        parts.append("<pre><code>%s</code></pre>" % html.escape(snippet, quote=False))
    parts.append(fig)
    parts.append('<p class="ctor-note">%s</p>' % inline(note))
    parts.append('<div class="ctor-actions">'
                 '<button type="button" class="ctor-src" aria-haspopup="dialog">'
                 'Source</button></div>')
    parts.append("</section>")
    return "\n".join(parts)


index = ", ".join('<a href="#%s"><code>A.%s</code></a>'
                  % (e[0].replace(".", "-").lower(), e[0]) for e in ANIMS)

body = """Animations run on the transition between one slide and the next. Each is named
`A.{Type}.{name}` and attached to an element in the slide it arrives on.

Every figure below is a two-slide deck. Step it with the controls under the
canvas, or with the arrow keys once the canvas has focus, and press **r** to
run it again.

```javascript
slides: [
    { text: "Two points.", visible: ["A", "B"] },
    { text: "Join AB.",    visible: ["A", "B", "AB"],
      transition: { animations: [ { elem: "AB", name: geomlib.A.Line.straightEdgeConnect } ] } },
]
```

An element a later slide introduces must be listed in `initiallyHidden`, or it
is on screen before the slide that draws it. `mode` on the transition sequences
several animations: `"parallel"` runs them together, `"cascade"` one after the
next.

<nav class="ctor-index">
<div class="ctor-index-group"><b>Animations</b> — %s</div>
</nav>

<div class="ctor-grid wide">
%s
</div>

## Library documentation

- [**animations-reference.md**](https://github.com/brownnrl/euclid/blob/main/doc/animations-reference.md)
  — the full table, including the reserved names not yet implemented, and the
  `animationConfig` tuning fields.
- [**creating-animations.md**](https://github.com/brownnrl/euclid/blob/main/doc/creating-animations.md)
  — adding a transition of your own.
- [**Constructions**](/geomlib/constructions/) — the elements these animations
  are attached to.
""" % (index, "\n".join(card(e) for e in ANIMS))

page = """_model: other_work
---
title: Slide transitions
---
order: 5
---
body:

%s""" % body
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w").write(page)
print("wrote %s: %d animations" % (OUT, len(ANIMS)))
