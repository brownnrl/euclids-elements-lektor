# Journal — work to date

Reverse-chronological (most recent first). Each entry is a logical milestone, not a 1:1 with commits.

## Books III–XIII — bulk markdown conversion

Books III–XIII converted in one extended session via per-book parallel agent fan-out:

| Book | Defs | Props | Agents | Notes |
|---|---|---|---|---|
| III | 11 (3 bundles) | 37 | 4 | First book to use the eucref + `[!just]` shortcode workflow end-to-end |
| IV | 7 (1 bundle) | 16 | 3 | All 7 defs share one Guide |
| V | 18 (6 bundles, 3 solos) | 25 | 4 | Theory of proportions; few figures |
| VI | 4 | 33 | 3 | Similar figures; many corollary refs |
| VII | 22 (5 bundles, 3 solos) | 39 | 4 | Number theory; **propVII32 source missing** from main mirror, hand-sourced from `/converted/java/` |
| VIII | 0 | 27 | 2 | Continued proportions |
| IX | 0 | 36 | 3 | Number theory; IX.20 infinitude of primes |
| X | 16 (3 bundles) | 115 | 10 | Three def-subsections (I/II/III) merged to global 1-16; eucref grammar extended for `X.Def.I.N` |
| XI | 28 (9 bundles, 2 solos) | 39 | 5 | Solid geometry |
| XII | 0 | 18 | 2 | Method of exhaustion; XII.2/4 have internal Lemmas |
| XIII | 0 | 18 | 2 | Platonic solids; XIII.13–17 are the actual constructions |

Wave pacing was 3 books at a time (decided after Book IV) to keep the trust-but-verify loop tight.

### Plugin grammar additions

- `@X.Def.{I|II|III}.N` — Book X subsection notation (resolves to global `defX{N}` paths via `_X_DEF_OFFSET`)
- `@X.Y.Cor` — corollary anchor (resolves to `…/propXY/#cor`)

Anchor-suffixed references the grammar still can't express (and that landed as hand-rolled `<div class="just">` HTML during conversion): `#lemma`, `#lemma1`, `#lemma2`, `#note`, `#cor` when display text isn't an Elements citation (e.g. `III.16,Cor` with comma — kept as hand-rolled to preserve the comma).

### Scaffolder + workflow improvements

- Generalised `/tmp/scaffold-book.py` auto-detects quoted vs unquoted `<a href>` (Book VII is unquoted), derives bundles from href reuse, handles both `bb0033` and `a00044` red-flag colors.
- Book X needed a separate `/tmp/scaffold-bookX.py` because its three definition subsections each restart numbering at 1.
- `scripts/copy-gif-fallbacks.py` extended with all 9 new book paths plus `/converted/java/` mirrors.

### Mismatch catalog (for follow-up)

Agents flagged these in their reports. None broke the build; all are candidates for hand-review.

#### Display/href mismatches in Joyce's source

Where the visible link text disagrees with the URL it points at. Default policy was "follow visible text" (what the reader sees), but a few cases followed href instead. Worth confirming each is rendered to the correct target.

- **Book V**:
  - propV1/V.2/V.3: `<a href="defV1.html">V.Def.2</a>` — href→def 1, label→def 2. Agent followed display.
  - propV8/V.14/V.16/V.19: cite `V.Def.12` linking to `defV11.html` (the bundle root). Both resolve via bundle URL — likely fine.
  - propV11: `<a href="defV5.html#guide">Guide to definition V.Def.6</a>` — display says V.Def.6, href is defV5 anchor. Hand-rolled link.
  - defV3 / defV17: cite `VI.33` with href `propVII33.html` — agent followed href (emitted `@VII.33`). **Inconsistency** — worth checking which Joyce intended.
- **Book VI**:
  - propVI4: `I.Post.5` linked to `post1.html` — agent followed display.
  - propVI13: `I.11` linked to `propII1.html`; `II.4` linked to `propII14.html` — both agent followed display.
  - propVI19: `V.Def.9` linked to `defV8.html` — agent followed display.
- **Book VII**:
  - propVII7: `VII.Def.13` linked to `defVII11.html`; `VII.Def.15` linked to `defVII15.html` — agent followed display.
  - propVII29 / VII.31: defXI11 referenced as `VII.Def.13`/`VII.Def.11,13` — agent followed display.
  - propVII11/12/22/22: similar bundle-href patterns.
- **Book VIII**:
  - propVIII8 / VIII.11 / VIII.12: cite `V.Def.9` / `V.Def.10` linking to `defV8.html` — agent followed display.
- **Book IX**:
  - All `defVII6.html` URLs in IX.25-27, IX.32-34: href stale but labels (`VII.Def.7`, etc.) correct — agent followed display.
  - propIX7: `VII.Def.13` linked to `defVII11.html`; `VII.Def.15` linked to `defVII15.html` — agent followed display.
- **Book X**:
  - propX10: `V.Def.9` linked to `defV8.html` — agent followed display.
  - propX76: `X.16` linked to `propX15.html` — agent followed display.
  - propX85 / X.97 / X.108: `X.Def.III.2` linked to `defX.III.html#1` (anchor 1, label 2) — agent followed display except X.85 where it followed href. **Inconsistency**.
  - propX54 Guide: `X.11` linked to `propX91.html` — agent followed display. Worth confirming Joyce meant X.11.
- **Book XI**:
  - propXI18: `XI.Def.4` linked to `defXI3.html` (bundle root) — agent followed display.
  - propXI34: `X.11` linked to `propXI11.html` (literal `X` vs `XI`) — agent resolved to `@XI.11`.
- **Book XII**:
  - propXII3: `XI.Def.10` linked to `defXI9.html` — agent followed display.
  - propXII17: `VI.18,Cor` linked to `propVI8.html#cor`; `XII.18,Cor.` linked to `propXII8.html#cor` — agent canonicalized to `VI.8.Cor` and `XII.8.Cor` (matching href, not display). **Inconsistency**.
  - propXII17: `XI.Def.4` linked to `defXI3.html` — agent followed display.
- **Book XIII**:
  - propXIII5: `I.Def.3` linked to `bookVI/devVI3.html` (typo + wrong book) — agent emitted `VI.Def.3` from context.
  - propXIII8: `VI.14` linked to `propV14.html` — agent followed **href** here (`V.14`). **Inconsistency**.
  - propXIII14/15/16/17: cite `XI.Def.{25|26|27|28}` linking to `defXI25.html` (bundle root) — agent followed display.
  - propXIII18: `VI.20,Cor.` linked to `propVI10.html#cor` — agent followed display.

#### Statement-field scaffolder leaks

The TOC parser stops at `<p><dt>`, `</dl>`, `<font`, `<center>`, `<p><b><a>`, but Joyce sometimes uses `<p><a>` (no `<b>`) for embedded corollary teasers. These leaked into the `statement:` frontmatter. Hand-stripped during the session; worth checking if any remain:

- propIV5, propIV15, propIV16: stripped trailing `</font color>` + `<p><b><a>Corollary.</a></b>` teaser
- propV19: stripped trailing `<p><a href="propV19.html#cor">Corollary.</a>` teaser
- defXI20: Joyce TOC typo "the straight in which" (missing "line") — fixed in scaffold
- propXI12: Joyce TOC typo "to a give plane" (missing "n") — fixed
- propVII15: scaffold reads "unit number" but source body uses "unit" — left as scaffolded
- propVII18: scaffold reads "two number" (missing "s") — left as scaffolded

#### Compound theorem blocks (Lemma / Corollary / Note as siblings)

Joyce wraps lemmas, corollaries, and other auxiliary blocks in their own `<div class="theorem">` after the main proposition. Convention is `<h3 id="cor">Corollary</h3>` inside the same proof field. Some agents used `<h1 id="...">` instead, matching propXIII18's pattern. Consistency check:

- Inside-proof `<h3 id="cor">` pattern: propIII1, propIII16, propIV5, propIV15, propIV16, propV7, propV19, propVI8, propVII2, propVII11, propVIII2, propIX11, propXI33, propXI35, propXII7, propXII8, propXII17, propXIII9, propXIII16, propXIII17, propX3, propX4, propX6, propX23, propX114
- Compound-theorem `<h1 id="...">` pattern: propXIII13 (lemma), propXIII18 (remark + lemma), propX14, propX17, propX19, propX22 (lemma+prop), propX29 (lemma1+lemma2+prop), propX33 (lemma+prop), propX41 (prop+lemma), propX54, propX60 (lemma+prop), propX111 (remark), propXII2, propXII4 (lemma)
- Hand-rolled `<a name="lemma">` anchors: propXI23, propX48 (cites propX28#lemma1 — anchor doesn't exist in propX28 source, pre-existing dangling reference)

Worth picking one pattern and converging.

#### Anchor-suffixed citations rendered as hand-rolled justs

The plugin grammar covers `@X.Y.Cor` but not `@X.Y.Lemma` / `@X.Y.Note` / freeform glue. These were rendered as raw HTML `<div class="just">`:

- Lemma anchors: propX22, propX29, propX33, propX41 (cited from propX44), propX48 (broken — see above), propX54 (cited from propX60), propX91 (cites propX54), propXII5 (cites propXII2), propXII18 (cites propXII2)
- Note anchors: propX23 (cited from propX27)
- Freeform "Above" markers: propX9 (×2), propXI31, propXI34 — hand-rolled `<div class="just">Above</div>`
- "cf. X.Y" prefix: propX1 (`cf. V.Def.4`), propX74 (`cf. II.7`) — hand-rolled
- Glue words dropped in `[!just]`: VIII.21/26/27 (`or` between refs), VII.34 (parens around `(V.11)`), V.23 (parens around `(V.16)`), IX.31 (parens), IX.36 (parens)

If a `@X.Y.Lemma` grammar lands later, sweep these to convert.

#### Joyce source typos preserved verbatim

Agents preserved these as faithful to Joyce. Hand-review candidates if you want a corrected edition:

- propV1 source `<h1>Proposition 2</h1>` (h1 dropped on conversion, frontmatter correct)
- propV21 source `<h1>Proposition 20</h1>` (h1 dropped)
- propVI15 source `<h1>Proposition 5</h1>` (h1 dropped)
- propXI24 source `<h1>Definition 24</h1>` (should be "Proposition 24", h1 dropped)
- propIV15 corollary "he side" (missing "t") — fixed inline
- propIV16: duplicate proof paragraph in source (Joyce copy-paste) — agent de-duped
- propXI11: verbatim duplicate paragraph + two `[!just XI.8]` divs — agent de-duped
- propXI23 Lemma: "*LO*" where logically "*AC*" — preserved
- propXI34: "solid *CY*" where "*CV*" intended — preserved
- propXI35: "angle *DPE*" where "*DFE*" intended — preserved
- propXI39: "prism *GMKLMN*" where "*GHKLMN*" intended — preserved
- propVIII19: "a *D* is to *G*" (missing "as") — preserved
- propVIII4 / VIII.6 / VIII.13: `0` for variable *O* in places — preserved
- propIX13: "is no measured" for "not measured" — preserved
- propIX19: corrupt Greek text — preserved (Joyce's own note)
- propIX35: "comprehisible" — preserved
- propX87: "the ratio which 3 square number has" (missing "a") — preserved
- propX88: "*DE* nor *EF*" (first *DE* should be *DF*) — preserved
- propX98: incomplete sentence "*AG* and *GB*" → only "*AG*" in source — preserved
- propX103: stray "*B*" mid-sentence — agent removed
- propX111 / X.114: Joyce's old global `X.Def.3` numbering vs new subsection `X.Def.I.3` — agent canonicalized to subsection form
- propXIII11 Guide: says XIII.11 is used in dodecahedron but it's actually used in icosahedron — preserved
- propXIII17: "*A* a through *F*" extra "a" — preserved

#### Missing or stale source assets

- **propVII32**: source HTML missing from `/converted/elements/bookVII/` entirely. Sourced from `/converted/java/elements/bookVII/propVII32.html` and hand-converted.
- Several propositions have noscript `<img src="propXN.gif"/>` pointing at a different prop's gif (Joyce reused diagrams). Agents normalized noscript src to per-prop filenames during conversion; the per-prop file may or may not exist in the mirror. Affected propositions (where `propX{N}.gif` likely doesn't exist as a standalone file): propVIII15 (src→propVIII12.gif), propIX17 (src→propIX11.gif), propIX22 (src→propIX21.gif), propIX28 (src→propIX6.gif), propIX29 (src→propIX6.gif), propX18 (src→propX17.gif), propX21 (src→propX20.gif), propX67-70 (src→propX66.gif), propX72 (src→propX71.gif), propX74/76/77 (src→propX73.gif), propX78 (src→propX75.gif), propX80/82/83 (src→propX79.gif), propX84 (src→propX81.gif), propX90 (src→propX87.gif), propX55-59 (src→propX54.gif), propX61-65 (src→propX60.gif), propX93-96 (src→propX92.gif), propX98-102 (src→propX97.gif), propX104 (src→propX103.gif), propX107 (canvas title `X.104` typo, agent fixed), propX115 (canvas title `X.114` typo, agent fixed).
- **propVIII15 missing gif file** in djoyce mirror — JS-disabled visitors would 404 on the fallback. Same risk on the others above. Bulk audit: check `find content/elements/books -name 'prop*.gif' | wc -l` vs noscript references.

#### Other notes worth a look

- defVII3 has `<font color="0000ff">` blue letter `u` matching a blue unit line in the canvas. Agent rendered as inline `<span style="color:#0000ff">*u*</span>`. Worth a proper CSS class.
- propIV15 corollary has `<font color=a00044>` mid-paragraph (questionable construction red highlight). Agent dropped initially; I restored as inline `<font color="a00044">` block. Should be a CSS class (`.questionable` or similar).
- propX29 statement frontmatter was modified by the agent to use absolute URL (`/elements/books/.../#lemma1`) instead of bare `propX29.html#lemma1` — needed for the section-index render to resolve. Same fix may be needed on other statement-with-anchor fields.
- propX72 has an unnumbered companion theorem inline (binomial-vs-medial). Agent kept as addendum; could be promoted to its own page.

## Book I — Markdown conversion complete

### Polish across propositions (after agent batch conversion)

- propI9 / propI10 / propI11 / propI46 / propI47: figures in subsections were placed AFTER the prose, so they floated down into the wrong section. Fix is mechanical — move the `<figure>` to right after the `#### heading` so the float starts at the top of the section it belongs to.
- propI7 / propI17: source `<ul>` blocks used as plain indenters (no `<li>` semantics) had been converted to markdown `- bullet` items. Switched to markdown blockquotes (`> …`), which is what the source actually wanted.
- propI7 / propI18: source `<center>` formulas were dropped to plain paragraphs. Re-wrapped in `<center>` HTML (with `<i>` italics, not `*` — markdown bypassed inside HTML).
- propI19: law-of-sines image wasn't carried over. Copied `propI19b.gif` into the page's content folder as a Lektor attachment.
- propI47: ditto for the *xian tu* image (`propI47a.gif`).
- propI15: in-statement `Corollary.` link pointed at `propI15.html#cor`. Replaced with absolute `/elements/books/bookI/propositions/propI15/#cor` (because `statement` is also rendered on the section index page, where a bare `#cor` resolves to the wrong place).
- propI18 / propI19 / propI27 source typos preserved or noted (e.g. `propI45.html` href with `I.19` label text — agent followed the visible label).
- Book I intro Guide: added the ~12 missing inline links (`Def.I.4`, `Def.I.5`, `Def.I.10`, `Def.I.22`, `Post.I.3`, `Post.I.4`, `III.16`, `I.Def.8`, `I.Def.9`, `Prop.I.5`, `I.4`, etc.) and ported the **Dependencies within Book I** table at the end of the Guide.

### Footer nav: ported Joyce's JS-driven bottom navigation

Originally we shipped a Jinja-rendered static next/prev widget. Switched to a port of Joyce's `loadFooter()` from `header-footer.js`:

- `assets/js/footer-nav.js` carries `booktable` (13 books) + `proptable[0]` (Book I's 71 nav entries — bundles collapsed to one entry each: `I.Def.11-12`, `I.Def.15-18`, `Common Notions`, etc.).
- Footer placeholder in layout: `<div id="footer"></div>` + `<script>loadFooter("1996, 1997, 2025");</script>`.
- Three `<select>` dropdowns (current-book contents, all books, topics) plus Next/Previous/Book-link rows.
- Books II–XIII have empty `proptable` rows; Next from propI48 walks past them as more books get filled in.
- Stacked-h1 header now walks `this.parent.parent` to show **Book I** instead of section name **Propositions**.

### Propositions (47 of 48) converted to markdown via parallel agents

Spawned 4 background `general-purpose` agents, each handling 11–12 propositions: propI2-13, propI14-25, propI26-37, propI38-48. Each agent got the same brief (see `process.md`), produced `proof:` + `body:` fields per leaf, and reported notable oddities (source typos, bundled sources, unusual layouts).

propI1 was converted by hand first as a worked example referenced in the agent briefs.

Model + template work that preceded the agents:
- Added `proof` field to `proposition.ini` (markdown), changed `body` to markdown.
- Rewrote `proposition.html` to extend `layout.html` directly; theorem box contains title → statement → proof; Guide section renders below.
- `short_label` field was missing from the proposition model — added it (had been silently dropped from `.lr` frontmatter).

### Common Notions: combined-view bundle

The 5 common notions share one source page (`cn.html`) with all 5 statements numbered inside one theorem box. Implemented as:

- New `commonnotion_group` model (parallel to `definition_group`).
- Hidden `cn1_5/` folder holding the shared markdown guide.
- Each cn1–cn5 carries `group: cn1_5` and empty body.
- `commonnotion.html` renders a single combined theorem box with all 5 statements numbered (matching original layout), then the shared guide.
- Blue-highlighted axiom blocks (Reflexivity/Symmetry/Transitivity, Substitution/Associativity/Commutativity, Cancellation, both trichotomy axioms) use `<blockquote class="axiom">` — CSS gives them `color: #0000ff`. Derived properties stay as plain markdown blockquotes.

### Postulates: convert post2–post5

post1 was the worked example for the markdown pattern. post2-5 done via a single agent. Two source typos cleaned (`propIII.16` → `propIII16` in post4; duplicated `propI29` href in post5 corrected to `propI30`).

### Definitions: bundle pattern

Initial pass left bundled definitions (defs 15-18, 11-12, 13-14, 20-21) with either duplicated bodies or empty placeholders. Designed the bundle pattern (see [content-model.md](../content-model.md#the-bundle-pattern)) and migrated all four groups into hidden `definition_group` pages with shared markdown bodies. Each member's URL re-renders the bundle (all member theorem boxes stacked + shared Guide).

Solo definitions (defI1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 19, 22, 23) converted to markdown individually; defI10–14 / 15–19 / 20–23 done by parallel agents.

### Definition model + template

- Added `group` field to `definition.ini`.
- Refactored `definition.html` to construct the theorem box from fields (rather than expecting raw HTML in body).
- Body field type: `html` → `markdown`.
- Section index template: drop `short_label` prefix from each `<dt>`; show plain `Definition N` label.

### Bottom nav iteration

Several iterations before the JS port:
- Initial Jinja next/prev within section, link back to parent book.
- Then noticed `short_label` was being dropped silently (model didn't declare it).
- Then user requested switching to the JS-driven port to match the original.

### Section index cleanup

- Dropped `short_label` from section_index `<dt>` (was showing "I.Def.1 Definition 1" — now just "Definition 1").
- Bundle group folders excluded from listing via `F._model == this.child_model` filter.

### CSS polish accumulated along the way

| Iteration | What |
|---|---|
| theorem float containment | `display: flow-root` on `.theorem` so canvases stop hanging out the bottom |
| `.just` annotations | added `clear: right` so multiple justifications stack vertically against right edge |
| figure float layout | `figure.diagram` (left) + `figure.diagram.rdiagram` (right); replaces legacy `<div class="ldiagram">` |
| mobile figure breakpoint | dropped from 768px → 480px so narrow-desktop widths keep text-wrapping |
| canvas max-width | `max-width: 100%; height: auto` on canvas — safe since geomlib 0.2.0+ |
| markdown tables | `margin: 0.8em auto` so reference tables center |
| axiom blockquote | `blockquote.axiom { color: #0000ff }` |
| heading anchors | h2/h3/h4 `<a>` stay blue, no underline regardless of visited |
| red highlight | applies to `<dt>` and `<dd>` of section_index entries; nested `<a>` stays default link color |

## Book I — scaffolding milestone

Before the Markdown conversion:

- Scaffolded all 81 Book I records from `bookI.html` via a one-off parser.
- Built the URL hierarchy `/elements/books/bookI/<section>/<leaf>/` (originally was flatter).
- Initial static stacked header (drops the Joyce `loadHeader()` JS approach in favor of Jinja-rendered headers — three shapes depending on page depth).
- `_imagemap.html` partial for the 13-region clickable pentagon on non-leaf pages.
- Master `/elements/` TOC with explicit Prematter-then-Books ordering.
- Section index, book index templates.
- Initial book.html guide listing with `<dl>/<dt>/<dd>` entries matching Joyce's pattern.
- Red highlight detection: a Python parser (`/tmp/fix-red-highlight.py`) walks bookI.html tracking `<font color=bb0033>` opens/closes by position to identify which entries should be flagged red. Result: Postulates 1–3 and 5; Propositions 1, 2, 3, 9–12, 22, 23, 31, 42, 44–46.
- License and copyright: `LICENSE` (MIT for plumbing) + `COPYRIGHT.md` (Joyce content) at top level.

## Project metadata

- `euclids-elements.lektorproject`, `requirements.txt`, `README.md`, `scripts/deploy-preview.sh`.
- Cloudflare Workers Static Assets target: `lektor-<branch>` branches on the `euclids-elements.org` repo serve at `lektor-<branch>-euclids-elements-org.brownnrl.workers.dev`.
