# Journal — work to date

Reverse-chronological (most recent first). Each entry is a logical milestone, not a 1:1 with commits.

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
