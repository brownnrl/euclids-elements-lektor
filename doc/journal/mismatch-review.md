# Mismatch review — Books III–XIII

For each display/href mismatch in [journal.md](journal.md)'s catalog, this document checks Joyce's source on Clark (`http://aleph0.clarku.edu/~djoyce/elements/`) and recommends whether to keep or fix.

## The bundle-navigation pattern

Joyce uses one source HTML file per "definition bundle" — so `defV1.html` contains the text for both V.Def.1 and V.Def.2, `defVII6.html` contains 6 through 10, etc. When Joyce cites a specific def within a bundle, his hand-typed HTML looks like `<a href="defV1.html">V.Def.2</a>` — the href is the bundle's source file, the display label tells you which member. This is **not a mismatch** — both are correct, just an artifact of bundle URLs being shared by all members.

Confirmed bundles:

| Source file | Members |
|---|---|
| `bookV/defV1.html` | V.Def.1, V.Def.2 |
| `bookV/defV5.html` | V.Def.5, V.Def.6 |
| `bookV/defV8.html` | V.Def.8, V.Def.9, V.Def.10 |
| `bookV/defV11.html` | V.Def.11, V.Def.12, V.Def.13 |
| `bookV/defV14.html` | V.Def.14–16 |
| `bookV/defV17.html` | V.Def.17, V.Def.18 |
| `bookVII/defVII1.html` | VII.Def.1, VII.Def.2 |
| `bookVII/defVII3.html` | VII.Def.3–5 |
| `bookVII/defVII6.html` | VII.Def.6–10 |
| `bookVII/defVII11.html` | VII.Def.11–14 |
| `bookVII/defVII15.html` | VII.Def.15–19 |
| `bookXI/defXI1.html` | XI.Def.1, XI.Def.2 |
| `bookXI/defXI3.html` | XI.Def.3–5 |
| `bookXI/defXI6.html` | XI.Def.6–8 |
| `bookXI/defXI9.html` | XI.Def.9, XI.Def.10 |
| `bookXI/defXI12.html` | XI.Def.12, XI.Def.13 |
| `bookXI/defXI14.html` | XI.Def.14–17 |
| `bookXI/defXI18.html` | XI.Def.18–20 |
| `bookXI/defXI21.html` | XI.Def.21–23 |
| `bookXI/defXI25.html` | XI.Def.25–28 |
| `bookX/defX.I.html` | X.Def.I.1–4 |
| `bookX/defX.II.html` | X.Def.II.1–6 |
| `bookX/defX.III.html` | X.Def.III.1–6 |

Our eucref plugin resolves the *display* token, so `@V.Def.9` → `/elements/books/bookV/definitions/defV9/` (the leaf URL), which re-renders the bundle-group page anyway. So display-driven resolution is correct in all these cases.

## Classification key

- 🟢 **Bundle nav** — not a real mismatch; display and href both correct, just bundle URL convention.
- 🟡 **Joyce typo, agent right** — display or href is wrong; agent followed the correct side.
- 🔴 **Joyce typo, agent wrong** — agent followed the wrong side; fix needed.
- 🟠 **Both ambiguous / context unclear** — manual review needed.

## Per-book review

### Book V — [bookV.html](http://aleph0.clarku.edu/~djoyce/elements/bookV/bookV.html)

| Location | Display \| href | Context snippet | Class | Current | Recommendation |
|---|---|---|---|---|---|
| [propV1](http://aleph0.clarku.edu/~djoyce/elements/bookV/propV1.html), V.2, V.3 | `V.Def.2` \| `defV1.html` | "Let any number of magnitudes *AB* and *CD* each be the same multiple of magnitudes *E* and *F* respectively." (def 2 = same multiple) | 🟢 | `@V.Def.2` | Keep |
| [propV8](http://aleph0.clarku.edu/~djoyce/elements/bookV/propV8.html), V.14, V.16, V.19 | `V.Def.12` \| `defV11.html` | various — def 12 is "ratio is the size of a relation" | 🟢 | `@V.Def.12` | Keep |
| [propV11](http://aleph0.clarku.edu/~djoyce/elements/bookV/propV11.html) | `Guide to definition V.Def.6` \| `defV5.html#guide` | non-citation link | 🟢 | hand-rolled link | Keep |
| [defV3](http://aleph0.clarku.edu/~djoyce/elements/bookV/defV3.html) | `VI.33` \| `../bookVII/propVII33.html` | "in Book VII ratios of three or more terms are used in proposition VI.33" | 🟡 | `@VII.33` (agent followed href) | **Keep** — context says "Book VII", so href is correct; "VI.33" is the typo |
| [defV17](http://aleph0.clarku.edu/~djoyce/elements/bookV/defV17.html) | `VI.33` \| `../bookVII/propVII33.html` | "In Book VII ratios of three terms are used in proposition VI.33" | 🟡 | `@VII.33` (agent followed href) | **Keep** — same as defV3 |

### Book VI — [bookVI.html](http://aleph0.clarku.edu/~djoyce/elements/bookVI/bookVI.html)

| Location | Display \| href | Context snippet | Class | Current | Recommendation |
|---|---|---|---|---|---|
| [propVI4](http://aleph0.clarku.edu/~djoyce/elements/bookVI/propVI4.html) | `I.Post.5` \| `../bookI/post1.html` | "sum of the angles *ABC* and *DEC* is less than two right angles, therefore *BA* and *ED*, when produced, will meet" — parallel postulate | 🟡 | `@I.Post.5` | **Keep** — context = parallel postulate (Post.5); display correct |
| [propVI13](http://aleph0.clarku.edu/~djoyce/elements/bookVI/propVI13.html) | `I.11` \| `../bookII/propII1.html` | "Place them in a straight line, and describe the semicircle... Draw *BD* from the point *B* at right angles" — I.11 constructs perpendicular | 🟡 | `@I.11` | **Keep** — context = perpendicular construction (I.11); display correct |
| [propVI13](http://aleph0.clarku.edu/~djoyce/elements/bookVI/propVI13.html) | `II.4` \| `../bookII/propII14.html` | "This construction of the mean proportional was used before in II.4 to find a square equal to a given rectangle" — II.14 (not II.4) constructs a square equal to a rectangle | 🔴 | `@II.4` (agent followed display) | **FIX** — context says "find a square equal to a given rectangle" = II.14. Change `@II.4` → `@II.14` in `body:` |
| [propVI19](http://aleph0.clarku.edu/~djoyce/elements/bookVI/propVI19.html) | `V.Def.9` \| `../bookV/defV8.html` | "BC is to EF as EF is to BG... a ratio duplicate" — def 9 = duplicate ratio | 🟢 | `@V.Def.9` | Keep |

### Book VII — [bookVII.html](http://aleph0.clarku.edu/~djoyce/elements/bookVII/bookVII.html)

| Location | Display \| href | Context snippet | Class | Current | Recommendation |
|---|---|---|---|---|---|
| [propVII7](http://aleph0.clarku.edu/~djoyce/elements/bookVII/propVII7.html) | `VII.Def.13` \| `defVII11.html` | bundle defVII11 covers 11–14 | 🟢 | `@VII.Def.13` | Keep |
| [propVII7](http://aleph0.clarku.edu/~djoyce/elements/bookVII/propVII7.html) | `VII.Def.15` \| `defVII15.html` | bundle root | 🟢 | `@VII.Def.15` | Keep |
| [propVII29](http://aleph0.clarku.edu/~djoyce/elements/bookVII/propVII29.html), VII.31 | `VII.Def.13` etc. \| `defVII11.html` | bundle nav | 🟢 | as emitted | Keep |
| [propVII11](http://aleph0.clarku.edu/~djoyce/elements/bookVII/propVII11.html), VII.12, VII.22 | bundle hrefs | bundle nav | 🟢 | as emitted | Keep |

### Book VIII — [bookVIII.html](http://aleph0.clarku.edu/~djoyce/elements/bookVIII/bookVIII.html)

| Location | Display \| href | Context snippet | Class | Current | Recommendation |
|---|---|---|---|---|---|
| [propVIII8](http://aleph0.clarku.edu/~djoyce/elements/bookVIII/propVIII8.html) | `V.Def.9` \| `defV8.html` | bundle (defs 8–10) | 🟢 | `@V.Def.9` | Keep |
| [propVIII11](http://aleph0.clarku.edu/~djoyce/elements/bookVIII/propVIII11.html) | `V.Def.9` \| `defV8.html` | "A, E, B in proportion... duplicate ratio" — def 9 | 🟢 | `@V.Def.9` | Keep |
| [propVIII12](http://aleph0.clarku.edu/~djoyce/elements/bookVIII/propVIII12.html) | `V.Def.10` \| `defV8.html` | "A, H, K, B four numbers in proportion... triplicate ratio" — def 10 | 🟢 | `@V.Def.10` | Keep |

### Book IX — [bookIX.html](http://aleph0.clarku.edu/~djoyce/elements/bookIX/bookIX.html)

| Location | Display \| href | Context snippet | Class | Current | Recommendation |
|---|---|---|---|---|---|
| [propIX7](http://aleph0.clarku.edu/~djoyce/elements/bookIX/propIX7.html) | `VII.Def.13` \| `defVII11.html` | "A composite, measured by D" — Def.13 = composite | 🟢 | `@VII.Def.13` | Keep |
| [propIX7](http://aleph0.clarku.edu/~djoyce/elements/bookIX/propIX7.html) | `VII.Def.15` \| `defVII15.html` | "E multiplied by D makes A" — Def.15 = multiplication | 🟢 | `@VII.Def.15` | Keep |
| [propIX25](http://aleph0.clarku.edu/~djoyce/elements/bookIX/propIX25.html)–27, 32–34 | `VII.Def.7/8/9` \| `defVII6.html` | bundle (defs 6–10) | 🟢 | as emitted | Keep |

### Book X — [bookX.html](http://aleph0.clarku.edu/~djoyce/elements/bookX/bookX.html)

| Location | Display \| href | Context snippet | Class | Current | Recommendation |
|---|---|---|---|---|---|
| [propX10](http://aleph0.clarku.edu/~djoyce/elements/bookX/propX10.html) | `V.Def.9` \| `defV8.html` | "Take a mean proportional E between A and D" — duplicate ratio | 🟢 | `@V.Def.9` | Keep |
| [propX76](http://aleph0.clarku.edu/~djoyce/elements/bookX/propX76.html) | `X.16` \| `propX15.html` | "sum of squares incommensurable with twice the rectangle" — X.16 = incommensurable case | 🟡 | `@X.16` | **Keep** — context = incommensurable (X.16); display correct |
| [propX85](http://aleph0.clarku.edu/~djoyce/elements/bookX/propX85.html) | `X.Def.III.2` \| `defX.III.html#1` | "Therefore *BC* is a first apotome" — Def.III.1 = first apotome | 🟡 | `@X.Def.III.1` (agent followed href) | **Keep** — context = first apotome (III.1); href correct |
| [propX97](http://aleph0.clarku.edu/~djoyce/elements/bookX/propX97.html) | `X.Def.III.2` \| `defX.III.html#1` | "*CF* is a first apotome" | 🔴 | `@X.Def.III.2` (agent followed display) | **FIX** — context says "first apotome" = III.1. Change `@X.Def.III.2` → `@X.Def.III.1` |
| [propX108](http://aleph0.clarku.edu/~djoyce/elements/bookX/propX108.html) | `X.Def.III.2` \| `defX.III.html#1` | "*KH* is a first apotome" | 🔴 | `@X.Def.III.2` (agent followed display) | **FIX** — same as X.97, change to `@X.Def.III.1` |
| [propX54](http://aleph0.clarku.edu/~djoyce/elements/bookX/propX54.html) Guide | `X.11` \| `propX91.html` | "The lemma is used in this proposition, X.60, and X.11" — but X.54's lemma is actually used in X.71 and X.91 | 🔴 | `@X.11` (agent followed display) | **FIX** — context lists three uses; X.91 is documented user of X.54's lemma. Change `@X.11` → `@X.91` |

### Book XI — [bookXI.html](http://aleph0.clarku.edu/~djoyce/elements/bookXI/bookXI.html)

| Location | Display \| href | Context snippet | Class | Current | Recommendation |
|---|---|---|---|---|---|
| [propXI18](http://aleph0.clarku.edu/~djoyce/elements/bookXI/propXI18.html) | `XI.Def.3` and `XI.Def.4` \| `defXI3.html` | bundle (defs 3–5) | 🟢 | as emitted | Keep — both bundle nav |
| [propXI34](http://aleph0.clarku.edu/~djoyce/elements/bookXI/propXI34.html) | `X.11` \| `propXI11.html` | "Draw perpendiculars from the points to the planes" — XI.11 constructs perpendicular to a plane | 🟡 | `@XI.11` (agent followed href) | **Keep** — context = perpendicular-to-plane (XI.11); display missing the "I" |

### Book XII — [bookXII.html](http://aleph0.clarku.edu/~djoyce/elements/bookXII/bookXII.html)

| Location | Display \| href | Context snippet | Class | Current | Recommendation |
|---|---|---|---|---|---|
| [propXII3](http://aleph0.clarku.edu/~djoyce/elements/bookXII/propXII3.html) | `XI.Def.10` \| `defXI9.html` | bundle (defs 9–10), "pyramid equals and similar" — Def.10 = similar solid figures | 🟢 | `@XI.Def.10` | Keep |
| [propXII17](http://aleph0.clarku.edu/~djoyce/elements/bookXII/propXII17.html) | `VI.18,Cor` \| `propVI8.html#cor` | "BD is to DZ as the rectangle DB by BZ is to the rectangle DZ by ZB" — ratio of rectangles by common altitude is VI.1 (or VI.1.Cor); VI.18 has no corollary | 🟠 | `@VI.8.Cor` (agent followed href) | **Manual review** — context fits VI.1 or VI.1.Cor better than VI.8.Cor; Joyce's source is ambiguous |
| [propXII17](http://aleph0.clarku.edu/~djoyce/elements/bookXII/propXII17.html) | `XII.18,Cor.` \| `propXII8.html#cor` | "similar pyramids are to one another in the triplicate ratio of their corresponding sides" — XII.8.Cor exactly | 🟡 | `@XII.8.Cor` (agent followed href) | **Keep** — context = XII.8 corollary; display "XII.18" is Joyce typo |
| [propXII17](http://aleph0.clarku.edu/~djoyce/elements/bookXII/propXII17.html) | `XI.Def.4` \| `defXI3.html` | bundle | 🟢 | `@XI.Def.4` | Keep |

### Book XIII — [bookXIII.html](http://aleph0.clarku.edu/~djoyce/elements/bookXIII/bookXIII.html)

| Location | Display \| href | Context snippet | Class | Current | Recommendation |
|---|---|---|---|---|---|
| [propXIII5](http://aleph0.clarku.edu/~djoyce/elements/bookXIII/propXIII5.html) | `I.Def.3` \| `bookVI/devVI3.html` | "*AB* is cut in extreme and mean ratio at *C*" — VI.Def.3 = extreme and mean ratio | 🟡 | `@VI.Def.3` (agent inferred from context) | **Keep** — both display and href are typos; agent's inferred VI.Def.3 is correct |
| [propXIII8](http://aleph0.clarku.edu/~djoyce/elements/bookXIII/propXIII8.html) | `VI.14` \| `../bookV/propV14.html` | "BE is greater than EH, therefore EH is also greater than HB" — V.14: same-ratio inequality preservation | 🟡 | `@V.14` (agent followed href) | **Keep** — context = ratio-implies-inequality (V.14); display "VI.14" is Joyce typo |
| [propXIII14](http://aleph0.clarku.edu/~djoyce/elements/bookXIII/propXIII14.html), 15, 16, 17 | `XI.Def.{25/26/27/28}` \| `defXI25.html` | bundle (defs 25–28) | 🟢 | as emitted | Keep |
| [propXIII18](http://aleph0.clarku.edu/~djoyce/elements/bookXIII/propXIII18.html) | `VI.20,Cor.` \| `propVI10.html#cor` | "three straight lines are proportional, the first is to the third as the square on the first is to the square on the second" — VI.20.Cor.2 (similar polygons in duplicate ratio); VI.10 has no corollary | 🟡 | `@VI.20.Cor` (agent followed display) | **Keep** — context fits VI.20 corollary; href is Joyce typo |

## Summary

**Total mismatches reviewed: 28**

- 🟢 Bundle nav (no fix): 18
- 🟡 Joyce typo, agent picked correct side (no fix): 7
- 🔴 Joyce typo, agent picked wrong side (**fix needed**): 3
- 🟠 Ambiguous (manual review): 1

### Fixes to apply

1. **[propVI13](../../content/elements/books/bookVI/propositions/propVI13/contents.lr) body** — change `@II.4` → `@II.14` in the sentence "This construction of the mean proportional was used before in II.4 to find a square equal to a given rectangle"
2. **[propX97](../../content/elements/books/bookX/propositions/propX97/contents.lr)** — change `[!just X.Def.III.2]` → `[!just X.Def.III.1]` on the "*CF* is a first apotome" sentence
3. **[propX108](../../content/elements/books/bookX/propositions/propX108/contents.lr)** — change `[!just X.Def.III.2]` → `[!just X.Def.III.1]` on the "*KH* is a first apotome" sentence
4. **[propX54](../../content/elements/books/bookX/propositions/propX54/contents.lr) body** — change `@X.11` → `@X.91` in the "The lemma is used in this proposition, X.60, and X.11" Guide sentence

### Manual review

1. **[propXII17](../../content/elements/books/bookX/propositions/propXII17/contents.lr) `@VI.8.Cor`** — context discusses rectangle-to-rectangle ratios via common altitude. Joyce's display "VI.18,Cor" labels it as VI.18 (which has no corollary), href points at VI.8.Cor. VI.1's corollary may be what was meant. Pull the proof step in question and verify against Heath's edition.
