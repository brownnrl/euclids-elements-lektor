# Proposition slideshow process

How a proposition page gets its slideshow: the planning table, the
authoring rules accumulated over propI.1–I.5, and the verification
checklist. Point a fresh session here before starting a new
proposition.

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
4. Implement: figure additions, `slides:` array, prose **and guide**
   `{NAME}` refs (each bound to the canvas it refers to in context —
   see [Guide / prose refs](#guide--prose-refs-bind-to-the-canvas-in-context)),
   aliases, `window.eucrefs`.
5. Verify (checklist below), then commit.
6. Only if the **Not yet implemented** column has entries: geomlib
   issue → feature branch → PR → test the deck against the dev bundle
   (`EUCLIDS_GEOMLIB_LOCAL=1`) → release → bump the
   `geomlib_default` pin in `templates/layout.html`. That one line feeds
   every page's `<script src>` and the `<meta name="geomlib-version">`
   the constructions page's Source overlay hands to CodePen, so it is
   the only pin to change. Hardcoded versions in *prose* (the CDN
   snippet on `/geomlib/`) can't be templated — Lektor doesn't run Jinja
   in content bodies — so `scripts/check-versions.js` fails the publish
   if one drifts from the layout, or names a CDN other than jsDelivr.

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
needed) but no slideshow — **except** when a guide canvas is *itself a
proof* (Joyce sometimes works a full argument in the guide, e.g. I.20's
Heron minimum-distance construction). Such a canvas may carry its own
`slides:` array, just like a proposition canvas; its captions follow the
guide prose verbatim and its `resolveJustification`/`window.eucrefs`
citations are merged into the page lookup with `Object.assign` (the
shared `window.eucrefs` is keyed once across all canvases on the page).

### Guide / prose refs bind to the canvas in context

Every `{NAME}` in the guide (and in any prose) must refer to **the canvas
it is talking about in context** — this includes guide prose that
discusses the *proposition* diagram, not just a guide canvas. The browser
binds a ref to a canvas by DOM order: the **nearest preceding canvas
wins** (then any following canvas), per `assets/js/elem-ref-highlight.js`.
So:

- **Single-canvas page** (just `canvas_0`): every guide ref resolves to
  `canvas_0` automatically — tokenize the guide's letters freely.
- **Multi-canvas page** (proposition `canvas_0` + a guide-construction
  `canvas_1`): a ref placed *after* `canvas_1` binds to `canvas_1`; one
  *between* the canvases binds to `canvas_0`. Order the prose so each
  ref's nearest preceding canvas is the one it means.
- When the wording can't be reordered, name the canvas in the ref itself:
  `{AB:canvas_0}`, or `{AB:canvas_0,canvas_1}` for several, combining with
  the display override as `{DISPLAY|element:canvas_1}`. This works in markdown
  prose — `lektor-eucrefs` registers its own inline rule ahead of emphasis and
  adds `{` to Mistune's `text` stop set, which is what the underscore split
  used to break (lektor#19).
- **Inside raw HTML** — a `<center>`, a `<table>`, any block-level HTML —
  Mistune does not process inline markdown at all, so `{AB}` stays literal
  there. Use the span form instead:
  `<span class="elem-ref" data-elem="AB" data-canvas="canvas_0">AB</span>`.

Every element a guide ref names must exist on its target canvas; add an
invisible highlight target there if the prose names something the diagram
doesn't draw.

### Don't add words to the guide or proof prose

The proof and guide text is Dr. Joyce's edition, republished faithfully —
treat it as read-only. **Don't insert explanatory sentences** (lead-ins
like "The walk below carries out…", "step through to see…", summaries of
what a figure shows). Adding prose is editorializing, even when it feels
helpful.

What *is* allowed on the prose: tokenizing words that are already there
(wrapping existing letters in `{NAME}` refs), and the editorial-footnote
convention for correcting a source typo (see `conventions.md`). Adding new
words is not.

All framing, narration, and "here's what to notice" belongs in the
**slideshow captions** (`slides[].text`), which are ours to write — not in
the guide.

### Captions carry Joyce's sentence, not a paraphrase of it

"Ours to write" governs **which** sentences a slide carries and how the walk
is paced. It does not license rewording the sentence itself. A caption is his
prose for that step, tokenized — the same rule as the proof body, arrived at
from the other direction.

**Consolidating citations is fine. Changing words is not.** Those are separate
freedoms and it is easy to take the second while reaching for the first.

Caught on II.4 slide 3. Joyce's step reads:

> Describe the square *ADEB* on *AB.* Join *BD.* Draw *CF* through *C* parallel
> to either *AD* or *EB,* and draw *HK* through *G* parallel to either *AB* or
> *DE.* [!just I.46; I.31]

and the caption had been written as:

> Describe the square {ADEB} on {AB}, join {BD}, and draw the two parallels —
> {CF} through {C}, and {HK} through {G}.

It reads well and it is shorter, which is exactly why it slipped through. But
"the two parallels" throws away *which lines they are parallel to*, and that is
the content — the next slide's argument turns on `CF ∥ AD`. What the caption may
do is take his two marginal refs and pair them as claims:

```js
justifications: [
    { claim: "the square on AB", ref: "I.46" },
    { claim: "parallels through C and G", ref: "I.31" },
]
```

That is summation of the references, which the `claim` convention exists for.
The sentence stays his:

```js
{ text: "Describe the square {ADEB} on {AB}. Join {BD}. Draw {CF} through {C} "
      + "parallel to either {AD} or {EB}, and draw {HK} through {G} parallel "
      + "to either {AB} or {DE}." }
```

Where a caption legitimately is ours: the opening "Let … be …" and "I say that
…" beats, a closing summary slide, and editorial asides in square brackets.
Anywhere the slide is walking a step of the proof, the step's own words are the
caption.

**Split rather than compress.** If a step's sentences won't sit comfortably on
one slide, the answer is more slides carrying his wording — never fewer slides
carrying a summary of it. A deck that runs long because it keeps the text
intact is doing its job; a shorter one that paraphrases is not.

This does not reopen the citation split that `claim` closed. Two different
reasons to split, and only one of them was retired:

| Reason to split | Verdict |
|---|---|
| To keep each statement beside its own citation | **Retired** — `claim` pairs them on one slide |
| Because one slide cannot carry the step's own words | **Correct** — take the split |

**The guide is looser.** Its commentary is Joyce talking *about* the text
rather than proving anything, and much of it is informal. Tokenizing is still
the only change to make to guide prose, but a guide-canvas caption need not
track his sentences as tightly as a proposition caption does. The strict rule
is for the proof walk, where the words are the mathematics. (Same spirit as "only build figures Joyce's page had": the
republished page stays his; our layer is the interactive slideshow on top.)

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

### An omitted `faceColor` is NOT transparent

For a 2-D element (any polygon), leaving the `faceColor` field off gives it
**`lighten(bgcolor)` — a near-white OPAQUE face**, not transparency
(`index.ts`, `defaultFaceColor`). Only an explicit `;0` (or `none`) makes a
polygon a true outline.

This matters because of the layering rule: **a highlighted element is promoted
within its draw pass (#140)**. So a polygon you believed was an empty outline
will, the moment it is highlighted or hovered, cover every coloured region
underneath it.

```
"B2;polygon;square;B,A;0;0;black"      // near-white FACE — will hide fills
"B2;polygon;square;B,A;0;0;black;0"    // a real outline
```

Caught on I.47: the orange `GBfill` appeared while its animation ran (an
animating element is promoted too) and then vanished the instant it settled,
because the highlighted square `B2` was promoted over it. The same latent bug
was then found in **I.41, I.43 and I.44** — in each case a big containing
polygon described in its own comment as "left unfilled so its own regions fill
it", which was in fact painting a white face over exactly those regions
whenever it was highlighted. On I.41 and I.47 that would have whited out the
closing slides, the payoff of both decks.

**Rule:** any polygon meant as an outline or an invisible highlight target
needs an explicit `;0` face. Grep for `polygon` declarations with fewer than
eight `;`-separated fields.

### Slide sets take CANONICAL names only — aliases are inert there

`aliases` resolve for prose `{NAME}` refs, but **not** inside a slide's
`visible` or `highlighted` arrays. Both code paths test the element's own
name — `SlateControls.ts` (`state.highlighted.has(e.name)`) and
`SlateAnimator.ts` (`targetHighlighted.has(e.name)`) — so an alias in a
slide set matches nothing and is **silently ignored**: no error, no
warning, the element simply never lights.

So write the **declared** name in `visible` / `highlighted` / `elem:`,
and keep the alias for the prose:

```js
aliases: { "FC": "CF" },
// caption may say {FC}; the slide set must say "CF"
highlighted: ["AL","AD","CF"],
```

When the prose spells it one way and the element is declared another,
the caption can still read Joyce's spelling via the display override —
`{FC|CF}` — while the slide set uses `CF`.

Caught on I.47, where slide 4 highlighted `"FC"` and the line stayed
black while AL and AD lit gold. An audit then found **33 inert names
across 17 deck-canvases**, including decks predating the area block.

### Points the proof introduces mid-walk (`deferDraggables`)

Visibility has two defaults pulling in opposite directions, and both bite:

- **Draggables are auto-unioned into every slide.** `free` and
  `*Slider` points ignore the `visible` sets and stand on the canvas from
  slide 1 — including points the proof does not introduce until later. A
  reader on slide 1 sees lettered points the caption never mentions.
  **Fix: list them in `deferDraggables`**, which drops them out of the
  auto-union so they follow `visible` like any other element. (Caught on
  I.44's `E` and I.45's `K`/`F`, which only arrive with the I.42
  construction; also I.5's `F`, I.20's `P`, I.27's `G`, I.39's `E`,
  I.40's `F`.)
- **Derived points are NOT auto-unioned.** `vertex` / `last` /
  `intersection` / `cutoff` / `midpoint` points follow the `visible`
  sets, so a slide that omits one loses its dot *and its label*. **Fix:
  list them explicitly in every slide they belong to** (C in I.4/I.8/I.26,
  D in I.27, G/H in I.28).

The rule of thumb: **a slide should show exactly what its caption has
introduced.** Sub-points of a composite given are fine — the arms
`D1`/`D2`/`D3` of a given angle `{D}` belong on slide 1 because `{D}`
itself is a given — but a lettered point the prose has not reached yet
does not.

Note `deferDraggables` affects only the slideshow's auto-union; the
resting figure still shows the point, so Joyce's static diagram is
unchanged.

### Angle markers

A small sector at the vertex marking the interior angle. Use the
`angleMarker` construction (geomlib 0.8.0+):
`angX;sector;angleMarker;Vertex,Arm1,Arm2` — vertex first, then any two
points on the arms. It computes its own fixed radius (≈22px, clamped to
a fraction of the shorter arm) and **auto-orients to the interior arc**,
so arm order no longer matters and there is no midpoint-chain radius
helper and no `Center.angle` sign-check (both retired with the old
`sector;sector;...;0;0;0;0` pattern). An optional 4th integer overrides
the radius (`...;Vertex,Arm1,Arm2,38`); the rare reflex (>180°) case is
`angleMarkerReflex`. Angles with the same rays share one marker (e.g.
angle AFC = angle BFC when A, B, F are collinear).

Markers are normal colored elements now (translucent palette fill,
distinct edge cycled per marker). Reveal them with `A.Sector.sweep` (the
whole wedge flashes on its transition) on the slide where the angle
first matters, and keep them in the `visible` set of every slide they
should appear on.

Two caveats while the library catches up (tracked in
[deck-tracker.md](deck-tracker.md) open questions):

- **Same-vertex overlap.** Multiple markers at one vertex render at the
  same radius and overlap until geomlib 0.8.1 adds auto radius-stepping;
  until then hand-separate with the radius-override integer.
- **Initial visibility.** Markers currently always render, including in
  the initial / static figure (no `visible=false` via params yet). The
  initial figure should match the source diagram — Euclid draws no angle
  arcs — so an initial-visibility parameter has been requested of the
  library session. Once it lands, author markers initially hidden and
  let the slides reveal them; the modern marker view stays a
  slide-walk / highlight affordance.

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

**`claim` — use it from Book II on** (geomlib 0.14.0+, euclid#146). A
justification may state *what* the step asserts, not just which proposition
licenses it. It renders ahead of the citation as `claim — ref`:

```js
justifications: [
    { claim: "angle EGB = angle AGH",       ref: "I.15" },
    { claim: "angle AGH + angle BGH = 2rt", ref: "I.13" },
    { claim: "subtract angle BGH",          ref: "C.N.3" },
]
```

Two things follow from having it:

- **Stop splitting a slide just to keep each statement beside its citation.**
  That is why I.28's three reasoning steps became per-statement sub-slides —
  a chip could name the proposition but not the claim, so the only way to pair
  them was one step per slide. A split is now a *pacing* choice: take it when
  the steps genuinely deserve separate beats, not to work around the chip.
- **Layout follows the data.** If any justification on a slide carries a claim,
  that slide's entries stack one per line; with no claims anywhere the panel
  stays the inline `·`-joined row. So adopting it on one slide does not disturb
  the rest of a deck, and Book I decks are untouched.

`claim` is **plain text — no `{NAME}` tokens**, so it cannot light elements.
Keep it short and let the caption carry the prose; the chip is a summary, not a
second narration.

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
6. Hover the **guide** `{NAME}` refs: each lights the canvas it refers to
   in context (on multi-canvas pages, confirm a ref means `canvas_0` vs
   `canvas_1` correctly).
7. Static figure + exit-presentation: matches Joyce's layout, free
   points drag, the whole construction tracks.
8. **Run the deck checker.** `node scripts/check-decks.js` (needs
   `node-canvas` from the euclid checkout — `NODE_PATH=../euclid/node_modules`,
   or set `EUCLIDS_GEOMLIB_REPO`). It evaluates **every** page's inline
   geomlib script against the real bundle — 524 pages, 634 canvases — and
   fails on any diagnostic: a figure that throws, a slide name that resolves
   to nothing, an animation target that matches nothing. Exit 1 means fix it.
   `scripts/deploy-preview.sh` runs it before building, so a bad deck cannot
   reach a preview.

   This **replaces** the manual greps that used to be steps 8–10 here (alias
   names in slide sets, points shown before their caption introduces them,
   bounds sanity). The checker catches those cases directly, and it
   *evaluates* rather than greps — 14 Book I decks build `visible` sets from
   shared `var`s via `.concat()`, which no static scan can follow. It is what
   caught propIV3, whose figure had not rendered since conversion because two
   element lines were transposed.

   Known false positives are suppressed by name in `isKnownFalsePositive()`,
   each with a comment and a ticket. Today that is I.23's `keepCircles` names
   (euclid#159) — created by a macro animation at run time, so they do not
   resolve at init even though the deck is correct. **Never silence a
   diagnostic by deleting the name** until you have checked whether something
   creates it later.

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
