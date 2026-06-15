# Slideshow deck tracker

Per-proposition status of the **slideshow deck** layer — the
`slides[]` / `transition` / `{NAME}` authoring that turns a converted
proposition page into a step-through proof. This is distinct from the
prose conversion (all 465 props are converted; that history lives in
[journal/journal.md](journal/journal.md)). A deck is built per the
[process.md](process.md) workflow.

Update the summary and the relevant row at the end of each deck.

## Status key

| Mark | Meaning |
|------|---------|
| ✅ | Done — `slides[]` authored, verified against the checklist, committed |
| 🚧 | In progress |
| ⬜ | Not started — prose + static figure exist, no deck yet |
| 🔒 | Blocked — needs an unreleased geomlib capability (named in Notes) |

## Angle-markers column (the #91 coupling)

The library session is reworking angle markers in
[euclid#91](https://github.com/brownnrl/euclid/issues/91) — a dedicated
angle-marker construction that will **retire** the midpoint-chain +
arm-order-sign-check pattern in [process.md](process.md). Any deck
authored with markers against the current pattern becomes rework when
#91 lands. This column tracks the exposure:

| Mark | Meaning |
|------|---------|
| — | No angle markers. #91-safe. |
| ⚠ | Has (or will have) angle markers — **re-author when #91 ships.** |
| ~ | Light — at most a single marker (e.g. one right angle). Minor rework. |
| ? | Estimate for an unstarted prop; confirm at planning time. |

## Summary

| Scope | Props | Decks done | Need #91 rework |
|---|---|---|---|
| Book I | 48 | 10 (I.1–I.7, I.9–I.11) | markers on 0.11.0 (see open Qs) |
| Books II–XIII | 417 | 0 | — |
| **Total** | **465** | **10** | — |

---

## Book I

Decks are authored in order. Kind: **C** = construction ("To …"),
**T** = theorem. The angle column for ⬜ rows is a planning estimate.

| # | Gist | Kind | Status | Slides | Animations | Angle (#91) | Notes |
|---|---|---|---|---|---|---|---|
| I.1 | Equilateral triangle on a segment | C | ✅ | 13 | Line.straightEdgeConnect, Circle.compass, Point.appear, Polygon.outlineAndFill | — | First deck; demo-mirrored from geomlib `view/test/slideshow/propI1.html` |
| I.2 | Place a line equal to a given line at a point | C | ✅ | 12 | + Line.straightEdgeExtend | — | Full I.1-embedded construction |
| I.3 | Cut off a line equal to the less | C | ✅ | 10 | Circle.compass, both straightEdge, Point.appear | — | Full cut-off chain shown here |
| I.4 | SAS congruence | T | ✅ | 22 | Polygon.superpose, Sector.sweep | ⚠ | First superposition; angA–angF markers |
| I.5 | Isosceles base angles (pons asinorum) | T | ✅ | 18 | Circle.compass, straightEdge×2, Point.appear, Sector.sweep | ⚠ | `deferDraggables:["F"]`; worked example in process.md; many `ang*` markers |
| I.6 | Converse of I.5 (equal angles ⇒ equal sides) | T | ✅ | 9 | Sector.sweep, Point.appear, Line.straightEdgeConnect, Polygon.outline, Group.cloneAside | ⚠ | Reductio; containment+gold emphasis (no superpose). Apex A on BC's perp bisector (∠B=∠C invariant); slide-3 trichotomy ghosts via one `cloneAside` autoPlace+variants (#99, 0.10.0); D rests ~75% toward A, slides to midpoint slide 4. Markers → #91 rework |
| I.7 | Uniqueness of triangle on a base | T | ✅ | 10 | Line.straightEdgeConnect, Point.appear, Sector.sweep | ⚠ | First single-negation reductio (no cloneAside). D is a `circleSlider` on a hidden circle centred A through C → AD=AC genuine, so the ∠ACD=∠ADC step is honest (free D made them 95° vs 71°); D snaps ~8px off Euclid's gif point. 4 angle markers, nested at C (∠DCB⊂∠ACD) and D (∠ADC⊂∠CDB) via #103. Contradiction = ∠CDB(142°) ≫ ∠DCB(30°) vs claimed ∠CDB=∠DCB. Markers → #91 rework. Pending visual pass |
| I.8 | SSS congruence | T | ⬜ | | | ⚠? | Superposition (`Polygon.superpose` fits); concludes contained angles equal |
| I.9 | Bisect an angle | C | ✅ | 11 | Sector.sweep, Point.appear, Circle.compass, Line.straightEdgeConnect, Polygon.outline | ⚠ | 0.8.0 angleMarker. 3 markers at A (whole ∠BAC + halves ∠DAF/∠EAF) — built flat, overlap until 0.8.1 auto-nesting. Equilateral triangle shown in full — two compass circles (+ the slide-4 cut-off circle = Joyce's three circles), deliberately revived to connect to the Guide's construction-steps canvas. Committed 15a083c |
| I.10 | Bisect a segment | C | 🚧 | 8 + 9 | canvas_0: Polygon.outline, Point.appear, Sector.sweep, Line.straightEdgeConnect · canvas_1: Circle.compass, Point.appear, Line.straightEdgeConnect, Sector.sweep | ⚠ | **TWO independent slideshows** (author's choice): proposition proof (canvas_0) + Guide construction-steps (canvas_1, Joyce's double-equilateral-triangle narrative). Same two-circle build on both — canvas_0 shows the circles transitorily on the build slide then hides them (back to Joyce's triangle + CD); canvas_1 keeps the circles. 3 markers at C flat. Guide prose hover-refs canvas_1. Pending visual pass |
| I.11 | Erect a perpendicular at a point on a line | C | 🚧 | 9 + 3 | canvas_0: Circle.compass, Point.appear, Polygon.outlineAndFill, Line.straightEdgeConnect, Sector.sweep · canvas_1: Circle.compass, Point.appear, Line.straightEdgeConnect | ~ | TWO slideshows (proposition + Joyce's guide 3-circle construction, verbatim). Transitory construction circles; two adjacent right-angle markers at C (auto-nest #103). Pending visual pass |
| I.12 | Drop a perpendicular from a point off a line | C | ⬜ | | | ~ | One right-angle marker at most |
| I.13 | Angles on a line sum to two right angles | T | ⬜ | | | ⚠? | |
| I.14 | Converse of I.13 (lines straight) | T | ⬜ | | | ⚠? | |
| I.15 | Vertical angles are equal | T | ⬜ | | | ⚠? | |
| I.16 | Exterior angle > either remote interior | T | ⬜ | | | ⚠? | |
| I.17 | Any two angles sum < two right angles | T | ⬜ | | | ⚠? | |
| I.18 | Greater side ⇒ greater opposite angle | T | ⬜ | | | ⚠? | |
| I.19 | Greater angle ⇒ greater opposite side | T | ⬜ | | | ⚠? | |
| I.20 | Triangle inequality | T | ⬜ | | | — | |
| I.21 | Inner cevians: shorter sum, greater angle | T | ⬜ | | | ⚠? | |
| I.22 | Triangle from three given lines | C | ⬜ | | | — | Compass-heavy construction |
| I.23 | Copy an angle onto a line | C | ⬜ | | | ⚠? | Subject is an angle → #91 |
| I.24 | Greater contained angle ⇒ greater base | T | ⬜ | | | ⚠? | |
| I.25 | Greater base ⇒ greater contained angle | T | ⬜ | | | ⚠? | |
| I.26 | ASA / AAS congruence | T | ⬜ | | | ⚠? | |
| I.27 | Equal alternate angles ⇒ parallel | T | ⬜ | | | ⚠? | |
| I.28 | Equal corresponding / co-interior ⇒ parallel | T | ⬜ | | | ⚠? | |
| I.29 | Parallels ⇒ equal alternate / corresponding angles | T | ⬜ | | | ⚠? | |
| I.30 | Transitivity of parallelism | T | ⬜ | | | — | |
| I.31 | Draw a parallel through a point | C | ⬜ | | | ~ | Uses I.23 angle copy; marker incidental |
| I.32 | Exterior angle = sum of remotes; angles sum 2R | T | ⬜ | | | ⚠? | |
| I.33 | Equal+parallel ends joined ⇒ equal+parallel | T | ⬜ | | | — | |
| I.34 | Parallelogram opposite sides/angles; diameter bisects | T | ⬜ | | | ⚠? | |
| I.35 | Parallelograms, same base & parallels, equal | T | ⬜ | | | — | Area/superposition flavored |
| I.36 | Parallelograms on equal bases & parallels equal | T | ⬜ | | | — | |
| I.37 | Triangles on same base & parallels equal | T | ⬜ | | | — | |
| I.38 | Triangles on equal bases & parallels equal | T | ⬜ | | | — | |
| I.39 | Equal triangles, same base/side ⇒ same parallels | T | ⬜ | | | — | |
| I.40 | Equal triangles, equal bases/side ⇒ same parallels | T | ⬜ | | | — | |
| I.41 | Parallelogram double the triangle (same base/parallels) | T | ⬜ | | | — | |
| I.42 | Parallelogram equal to a triangle in a given angle | C | ⬜ | | | ⚠? | Given angle → likely a marker |
| I.43 | Complements about the diameter equal | T | ⬜ | | | — | |
| I.44 | Apply a parallelogram equal to a triangle | C | ⬜ | | | ⚠? | |
| I.45 | Parallelogram equal to a rectilinear figure | C | ⬜ | | | ⚠? | |
| I.46 | Square on a given line | C | ⬜ | | | ~ | Right angles by construction |
| I.47 | Pythagorean theorem | T | ⬜ | | | ⚠? | Right-angle + square areas |
| I.48 | Converse of Pythagoras | T | ⬜ | | | ⚠? | |

---

## Books II–XIII

No decks yet. Add a per-book section here as the work reaches each
book, mirroring the Book I table. Prose conversion for all of these is
already complete (see [journal/journal.md](journal/journal.md)).

## Deck polish to-dos (from the visual walk)

- **I.4 — vertex label `C` drops out.** `C` is a derived point
  (`point;last`), so unlike the free/slider vertices (A, B, D, E, F) it
  is not auto-unioned into every slide; its label disappears whenever a
  slide's `visible` set omits it (gone on slide 1, faint by slide 14).
  Fix: add `"C"` to the slides' `visible` sets so the label stays across
  all 22 slides. (Pre-existing; not caused by the 0.8.0 migration.)
- **I.11 — "AC" has no hover-ref.** ✅ Done — added zero-color
  `AC;line;connect;A,C;0;0;0` target and tokenized `{AC}` in the caption +
  prose.

## geomlib migration (markers + animations)

Pinned at **0.11.0** (#107 maximize/presentation recenter + reset-on-exit;
#108 `geomlib:highlight` bidirectional event — see `elem-ref-highlight.js`).
Angle markers (`E.Sector.angleMarker`) are hidden in the static figure by
default and revealed during the walk / on hover (#100); markers migrated
across **I.4, I.5, I.6, I.9, I.10**. I.6's trichotomy + D-slide use
`A.Group.cloneAside` (#98/#99 `autoPlace`+`variants`) + `A.Point.slide`
(#95). Captions must match the source text verbatim (proof text for the
proposition; Joyce's guide prose for a guide slideshow) — `[brackets]`
for any editorial aside.

## Open questions / deferred

| # | Item | State |
|---|---|---|
| Q1 | **Same-vertex marker overlap** — I.5 (4@B/4@C), I.9 (3@A), I.10 (3@C), authored flat. | **Resolved — 0.9.1 pinned** (#103 auto radius-stepping); markers auto-nest into concentric rings. No deck changes. |
| Q2 | **Cascade pre-render** — elements in a cascade drew fully from t=0 ("appear too soon"): I.2 DAB, I.6, I.9, I.10 (Bcirc fill, the triangle, point C). | **Resolved — 0.9.1 pinned** (#104). Workarounds dropped: I.10 guide slide-2 back to cascade, proposition circles back to filled. Captions are exact source text. |
| Q3 | Markers in the static figure (must match Euclid's no-arcs diagram). | **Resolved 0.9.0** (#100: hidden by default, `initiallyHidden`, hover reveals a hidden element). |
| Q4 | I.6 slides 3–4 trichotomy case-variants. | **Done — 0.10.0** (#99 `cloneAside` `autoPlace` + atomic `variants`): the figure centres and both ghost copies place to the sides (top/bottom fallback, both-or-neither). Apex A constrained to BC's perpendicular bisector so ∠ABC = ∠ACB is invariant; D rests ~75% toward A (Euclid's static placement); slide-4 slides it to the midpoint of AB (`Point.slide` to 0.5) after the cases — the main slider never moves during slide 3 (variants restore it). |

## 0.9.1 cleanup (done)

Interim cascade-pre-render workarounds dropped: I.10 guide slide-2
circles back to cascade; I.10 proposition circles back to filled. I.9 /
I.5 same-vertex markers left flat — #103 auto-nests them. Remaining
library dependency: **#99** (cloneAside auto-placement + recenter) for
I.6's trichotomy ghosts — in progress.
