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
| Book I | 48 | 6 (I.1–I.6) + I.9 🚧 | markers on 0.8.0 (see open Qs) |
| Books II–XIII | 417 | 0 | — |
| **Total** | **465** | **6** | — |

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
| I.6 | Converse of I.5 (equal angles ⇒ equal sides) | T | 🚧 | 9 | Sector.sweep, Point.appear, Line.straightEdgeConnect, Polygon.outline | ⚠ | Reductio; containment+gold emphasis (no superpose). Markers old-pattern → #91 rework. Slide 3–4 case-variants + D-slide-back deferred to [euclid#94](https://github.com/brownnrl/euclid/issues/94) + [#95](https://github.com/brownnrl/euclid/issues/95). Pending visual pass |
| I.7 | Uniqueness of triangle on a base | T | ⬜ | | | ⚠? | Reductio with angle inequalities |
| I.8 | SSS congruence | T | ⬜ | | | ⚠? | Superposition (`Polygon.superpose` fits); concludes contained angles equal |
| I.9 | Bisect an angle | C | 🚧 | 11 | Sector.sweep, Point.appear, Circle.compass, Line.straightEdgeConnect, Polygon.outline | ⚠ | 0.8.0 angleMarker. 3 markers at A (whole ∠BAC + halves ∠DAF/∠EAF) — built flat, overlap until 0.8.1 auto-nesting. Equilateral triangle shown in full — two compass circles (+ the slide-4 cut-off circle = Joyce's three circles), deliberately revived to connect to the Guide's construction-steps canvas. Pending visual pass |
| I.10 | Bisect a segment | C | ⬜ | | | — | Pure construction; cites I.9/I.1 |
| I.11 | Erect a perpendicular at a point on a line | C | ⬜ | | | ~ | One right-angle marker at most |
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

## 0.8.0 angle-marker migration (#91 shipped 2026-06-13)

geomlib 0.8.0 shipped `E.Sector.angleMarker` (vertex + two arm points,
auto-interior, fixed radius, palette fill — no midpoint-chain helpers,
no sign-check). Pin bumped to **0.8.0** in `templates/layout.html`.
Markers migrated: **I.4 ✅, I.5 ✅ (flat — see open Q1), I.6 ✅.**

## Open questions / deferred

| # | Item | State | Trigger to resolve |
|---|---|---|---|
| Q1 | **I.5 same-vertex marker overlap** — 4 markers at B and 4 at C overlap at the default radius (migrated "flat" per author's call). | Migrated, overlapping. | geomlib **0.8.1** auto radius-stepping (deferred there). Then drop any hand-radii. |
| Q2 | **Markers render in the initial/static figure** — 0.8.0 markers are normal colored elements (always drawn; no `visible=false` via params). The initial/printed figure should match the source diagram (Euclid draws no angle arcs); the modern marker view is wanted only during the slide walk + on highlight. | Requested. | Library session to add a general **initial-visibility parameter** for markers (annotated in coord doc — API shape is their call, not ours). Then author markers initially hidden, revealed via slide `visible` sets / highlight. |
| Q3 | **I.6 slides 3–4** — the trichotomy two case-variants ("one of them is greater") and the cut-off point **D sliding back between A and B** are stubbed (single figure + `A.Point.appear`). | v1 simple version shipped. | geomlib **#94** (`A.Polygon.translateAside`, case-variant display) + **#95** (`A.Point.slide`, point glide). Handed back to the library session. |
| Q4 | **process.md angle-marker section** still describes the retired midpoint-chain + sign-check pattern. | Stale. | Rewrite for the `angleMarker` construction (TODO this batch). |
| Q5 | **Visual pass not yet run** — blocked on the shared `lektor serve` (PID 18738; library session says not theirs). Nothing committed; pin bump + all marker migrations are unverified. | Blocked. | Confirm/kill PID 18738 → single clean `lektor serve` → walk I.1–I.6. |
