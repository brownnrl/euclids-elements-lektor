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
| Book I | 48 | 5 | 2 (I.4, I.5) |
| Books II–XIII | 417 | 0 | — |
| **Total** | **465** | **5** | **2** |

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
| I.6 | Converse of I.5 (equal angles ⇒ equal sides) | T | ⬜ | | | ⚠? | Reductio leaning on base angles; angle-dense |
| I.7 | Uniqueness of triangle on a base | T | ⬜ | | | ⚠? | Reductio with angle inequalities |
| I.8 | SSS congruence | T | ⬜ | | | ⚠? | Superposition (`Polygon.superpose` fits); concludes contained angles equal |
| I.9 | Bisect an angle | C | ⬜ | | | ⚠? | Subject is an angle; wants clean half-angle marking → #91 |
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

## When #91 lands

1. process.md's angle-marker section gets rewritten for the new
   construction.
2. Re-author the ⚠ decks (currently **I.4, I.5**) to drop the
   midpoint-chain markers for the new angle-marker primitive.
3. Flip ⚠? estimates to real values as each angle-heavy deck is built.
