# Proposition slideshow process

How a proposition page gets its slideshow: the planning table, the
authoring rules accumulated over propI.1–I.5, and the verification
checklist. Point a fresh session here before starting a new
proposition. (The older [journal/process.md](journal/process.md) is
the Phase-3 HTML-conversion process — different work.)

Illustration and education are the primary goals. The slides should
glean intent from Joyce's writing and convey the construction — kept
as simple as the proof allows.

## Workflow

1. Read the proposition's proof text and existing figure
   (`content/elements/books/bookI/propositions/propIN/contents.lr`).
2. Split the proof into slides — typically one clause or sentence per
   slide, following the proof's own rhythm. The author may supply the
   breakdown; otherwise draft it from the text.
3. Fill in the planning table (format below) and review it with the
   author **before implementing**. Note in the surrounding narrative
   which diagrams get constructions, and flag anything in the text
   that calls for work outside this process.
4. Implement: figure additions, `slides:` array, prose `{NAME}` refs,
   aliases, `window.eucrefs`.
5. Verify (checklist below), then commit.
6. Only if the **Not yet implemented** column has entries: geomlib
   issue → feature branch → PR → test the deck against the dev bundle
   (`EUCLIDS_GEOMLIB_LOCAL=1`) → release → bump the
   `geomlib_default` pin in `templates/layout.html`.

## The planning table

| # | Slide text | Shown / hidden | Highlighted | Animation (mode) | Justs | Not yet implemented |
|---|---|---|---|---|---|---|

- **Slide text** — the caption, with `{NAME}` tokens. Editorial
  asides (e.g. "[the construction of I.2 is shown in full]") go in
  square brackets.
- **Shown / hidden** — the `visible` set, written as deltas
  ("+ BD, D"; "(inherit)"; "transitory X dropped from #N on").
  `visible` inherits from the most recent slide that declared it;
  `highlighted` clears every slide and auto-unions into visible.
- **Highlighted** — the gold callouts for that slide.
- **Animation (mode)** — `A.*` entries in order, with the transition
  mode when it isn't the default cascade.
- **Justs** — marginal justification refs (`I.Post.3`, `C.N.1`, …)
  plus the closing `Q.E.F.` / `Q.E.D.`.
- **Not yet implemented** — anything the current geomlib vocabulary
  can't do. **Last column, ideally empty.** A non-empty cell means a
  geomlib release precedes the deck.

## Authoring rules

### Constructions and the fatigue rule

Show a construction in full when it is the proposition's own work or
when the technique is new to the reader. Once a technique has been
demonstrated once or twice removed from its originating proposition,
stop showing it — assume it. Example: extending a line by a given
length got the full treatment in I.2 (with I.1 embedded) and the full
chain again in I.3; from I.5 on, a cut-off is a single transitory
circle or a bare point-appear with the marginal ref carrying the
justification. A later proposition may deliberately revive the full
construction for demonstrative purposes — that is an authoring choice
to flag in the table's narrative, not the default.

Only the **proposition canvas** gets slides and animations. Guide
canvases get `{NAME}` hover refs (and invisible highlight targets as
needed) but no slideshow.

### Invisible highlight targets (the Zeno pattern)

Prose names segments, angles, and triangles that aren't standalone
drawn elements. Author them as zero-color elements — `;0;0;0` for
lines, `;0;0;0;0` for circles/sectors/polygons. They draw nothing
normally and render in the gold highlight stroke when a slide set or
a `{NAME}` hover lights them. Two hard rules:

- Any zero-color element a **caption** references must be in that
  slide's `visible` set — hover emphasis bails on `visible = false`.
  (`highlighted` entries are auto-unioned; caption-only mentions are
  not.)
- Transitory construction scaffolding (compass circles, produced
  rays, intermediate points) is zero-color too: it renders gold only
  while its animation runs, fades with the post-animation emphasis
  taper, and is dropped from the next slide's visible set.

### Angle markers

A small sector at the vertex: build a quarter-radius point with a
midpoint chain (`mXY;point;midpoint;X,Y` then `qX;point;midpoint;X,mXY`)
and `angX;sector;sector;X,qX,Z;0;0;0;0`. The sweep direction is fixed
(inherited from the Java applet), so **arm order picks interior vs
reflex** — verify the sign of `Center.angle(A, B, P)` for every
marker with a node script before the visual pass (negative = interior;
positive = swap the radial arm). See the `checkI4` pattern in the
session journal: build the slate headlessly with ts-node in the
geomlib repo and print the signs.

Markers animate with `A.Sector.sweep` on the slide where the angle
first matters, then persist invisibly (zero-color) for later
highlight-only mentions. Angles with the same rays share one marker
(e.g. angle AFC = angle BFC when A, B, F are collinear).

### Names, aliases, collisions

- Aliases map Joyce's letter permutations and angle names onto
  canonical elements: `"CDB": "BCD"`, `"FAG": "angA"`, …
- When an angle name collides with a triangle name (angle ABC vs
  triangle ABC), the element name belongs to the triangle, and the
  prose/caption token uses the **display override** (geomlib 0.7.1+):
  `{ABC|angBint}` renders "ABC" but binds the hover highlight to the
  angle marker. Works in slide captions (geomlib tokenizer) and proof
  prose (eucrefs plugin) alike.
- Internal helpers that share prose names get suffixes (`DABh`,
  `CGHh`) so the prose name resolves to the visible element.

### Justifications

Each page defines `window.eucrefs` (symbolic ref → URL) and passes
`resolveJustification: function(ref) { return (window.eucrefs &&
window.eucrefs[ref]) || null; }`. An unmapped ref renders as plain
text — that is how `Q.E.F.` / `Q.E.D.` goes on the closing slide.

### Animation choices

- Lines: `A.Line.straightEdgeConnect` (joins) /
  `straightEdgeExtend` (produces). Circles: `A.Circle.compass`.
  Points: `A.Point.appear`. Polygons: `A.Polygon.outline` /
  `outlineAndFill` / `superpose` (ephemeral gold ghost; args
  `{ onto }`). Angles: `A.Sector.sweep`. Catalog:
  geomlib's `doc/animations-reference.md`.
- Cascade (default) follows the prose's verb order; `parallel` for
  symmetric twin operations ("the angle BAC equal to the angle EDF").
- Standard rates unless the deck drags; tune per-slate via
  `animationConfig` only after a visual pass.

## Verification checklist

1. Extract each inline `<script>` and `node --check` it.
2. `lektor clean --yes && lektor build` — the artifact cache does not
   track the dev-bundle env toggle, so builds after toggling require
   a clean.
3. **One serve instance only.** Two serves race the shared build
   directory and silently overwrite each other's artifacts (stale
   instances have burned us twice). `ps aux | grep lektor` first.
4. `EUCLIDS_GEOMLIB_LOCAL=1` on both build and serve when the deck
   needs unreleased geomlib (the toggle swaps unpkg for
   `assets/geomlib-dev.js` → the sibling repo's `dist/bundle.js`).
   Without unreleased needs, serve plain against the pinned version.
5. Walk every slide: animations land, transitory pieces vanish on the
   next slide, caption hovers light the right elements, justification
   links resolve.
6. Static figure + exit-presentation: matches Joyce's layout, free
   points drag, the whole construction tracks.

## Worked example — proposition I.5

The deck below was planned with the author before implementation.
Narrative: the proposition canvas gets simple-vocabulary animations
only. The produces (I.Post.2 primitives) and joins (I.Post.1) animate
as single strokes. The I.3 cut-off gets **one transitory circle** —
Joyce's I.3 guide notes that when the line to cut off already has an
end at the given point, a single circle is the whole construction;
the I.2/I.1 machinery behind the general case is assumed per the
fatigue rule (shown in full one proposition removed). No draggability
cost: E and G are already derived points in this figure.

Out-of-scope flags noted at planning time: F stays a draggable
"arbitrary point" (the deck doesn't pin it); the guide's Pappus proof
(a triangle superposed on its own mirror image) would need a
reflection variant of `A.Polygon.superpose` — recorded as a future
idea, not built.

One consequence of keeping F draggable: **draggable elements are
auto-unioned into every slide's visible set**, so F's handle shows
from slide 1 and slide 4's "appear" is a pulse on an already-visible
point. Accepted — the alternative is de-sliding F, which trades away
the "arbitrary point" interactivity. The same applies to any
proposition whose construction points are sliders.

| # | Slide text (gist) | Shown / hidden | Highlighted | Animation (mode) | Justs | Not impl. |
|---|---|---|---|---|---|---|
| 1 | Let {ABC} be an isosceles triangle having the side {AB} equal to the side {AC} | ABC only | AB, AC | — | I.Def.20 | — |
| 2 | and let {BD} and {CE} be produced further in a straight line with {AB} and {AC} | + BD, D, CE, E | — | BD, CE straightEdgeExtend (cascade) | I.Post.2 | — |
| 3 | I say the angle {ABC} equals {ACB}, and {CBD} equals {BCE} | + angBint, angCint, angBext, angCext | — | 4 sector sweeps (parallel) | — | — |
| 4 | Take an arbitrary point {F} on {BD} | + F | — | F appear | — | — |
| 5 | Cut off {AG} from {AE} the greater equal to {AF} the less | + G, AG, AE, AF, AFcirc (transitory; dropped from #6) | — | AFcirc compass → G appear (cascade) | I.3 | — |
| 6 | and join the straight lines {FC} and {GB} | + FC, BG | — | FC, BG straightEdgeConnect (cascade) | I.Post.1 | — |
| 7 | Since {AF} equals {AG}, and {AB} equals {AC} | (inherit) | AF, AG, AB, AC | — | — | — |
| 8 | therefore the two sides {FA} and {AC} equal {GA} and {AB}… a common angle, the angle {FAG} | + angA | AF, AC, AG, AB | angA sweep | — | — |
| 9 | Therefore the base {FC} equals the base {GB}, the triangle {AFC} equals the triangle {AGB} | + AFC, AGB | FC, BG, AFC, AGB | — | I.4 | — |
| 10 | and the remaining angles equal… the angle {ACF} equals {ABG}, and the angle AFC equals AGB | + angACF, angABG, angF, angG | — | 4 sweeps (parallel) | — | — |
| 11 | Since the whole {AF} equals the whole {AG}, and in these {AB} equals {AC}, the remainder {BF} equals the remainder {CG} | + BF, CG | AF, AG, AB, AC, BF, CG | — | C.N.3 | — |
| 12 | But {FC} was also proved equal to {GB}, therefore the two sides {BF} and {FC} equal {CG} and {GB} | (inherit) | FC, BG, BF, CG | — | — | — |
| 13 | and the angle BFC equals the angle CGB, while the base {BC} is common | + BC | angF, angG, BC | — (swept at #10) | — | — |
| 14 | Therefore the triangle {BFC} also equals the triangle {CGB}, and the remaining angles equal… | + BFC, CGB | BFC, CGB | — | I.4 | — |
| 15 | Therefore the angle {FBC} equals {GCB}, and the angle {BCF} equals {CBG} | + angBCF, angCBG | angBext, angCext | angBCF, angCBG sweeps (parallel) | — | — |
| 16 | Accordingly, since the whole angle {ABG} equals {ACF}, and in these {CBG} equals {BCF}, the remaining angle {ABC} equals the remaining {ACB}, at the base | (inherit) | angABG, angACF, angCBG, angBCF, angBint, angCint | — | C.N.3 | — |
| 17 | But the angle {FBC} was also proved equal to {GCB}, and they are under the base | (inherit) | angBext, angCext | — | — | — |
| 18 | Therefore in isosceles triangles the angles at the base equal one another… | (inherit) | ABC, angBint, angCint, angBext, angCext | — | Q.E.D. | — |
