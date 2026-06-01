# Process — how to continue

A playbook for converting the remaining 12 books (II–XIII) and for picking up the work from a fresh session.

## Where we are

Book I is complete: 23 definitions, 5 postulates, 5 common notions, 48 propositions, book intro Guide. All rendered through markdown with the bundle pattern handling the few grouped sources.

Books II–XIII have placeholder slots in the footer-nav `proptable` but no content yet. The conversion is roughly mechanical from here: source HTML for each book is at `/data-mirrored/projects/geometry/euclids-elements.org/elements/book{N}/`.

## High-level workflow per book

1. **Scaffold the content tree.** Mirror Book I's shape under `content/elements/books/book{N}/`. For each book:
   - `bookN/contents.lr` (book model + intro Guide markdown)
   - `bookN/definitions/contents.lr` (section_index with `child_model: definition`)
   - `bookN/postulates/contents.lr` if the book has any (it usually doesn't past Book I)
   - `bookN/commonnotions/contents.lr` likewise (typically Book I only)
   - `bookN/propositions/contents.lr` (section_index with `child_model: proposition`)
   - Per-leaf folders with `contents.lr` containing frontmatter (title, short_label, order, statement, red_highlight) and empty `proof:` / `body:`.
2. **Identify bundles.** Scan the source HTML in `euclids-elements.org/elements/book{N}/` for pages that contain multiple `<div class="theorem">` blocks — those are bundles. Set up hidden `<bundle-slug>/` folders with `_model: definition_group` (or analogous for whatever leaf type) and `group:` references on the bundled leaves. See [content-model.md](../content-model.md#the-bundle-pattern).
3. **Identify red-highlighted entries.** Scan the book's TOC HTML (`bookN.html` source) for `<font color=bb0033>` opens/closes. The earlier-used parser is at `/tmp/fix-red-highlight.py` — adapt it by changing the file paths and re-run. Toggle `red_highlight: yes` on matching leaves.
4. **Convert content via parallel agents.** See agent-brief template below. Batch ~10–12 leaves per agent, run several in background.
5. **Build + spot-check.** `lektor build --output-path build/` from the activated venv. Open the rendered HTML for a few leaves, verify figures float correctly, links resolve, Q.E.D./Q.E.F. markers appear.
6. **Copy fallback gifs.** Every `<canvas>` figure has a `<noscript><img src="propN{X}.gif"/></noscript>` fallback for users with JS disabled. The agents preserve those `<img src="...">` references but don't copy the actual files. Run the bulk-copy script:
   ```sh
   python3 scripts/copy-gif-fallbacks.py
   ```
   The script walks every leaf's `contents.lr`, finds all `<img src="*.gif">` references, and copies the file from any of the Joyce mirror paths into the leaf's content folder so Lektor ships it as a page attachment. Sources searched, in priority order:
   - `/data-mirrored/projects/geometry/euclids-elements.org/elements/bookN/` (the official mirror; sparse for books past I)
   - `/data-mirrored/projects/geometry/djoyce/converted/elements/bookN/`
   - `/data-mirrored/projects/geometry/djoyce/converted/java/elements/bookN/` (older JS-applet version; usually has the gif even when the modern mirror doesn't — see propII8)
   - `/data-mirrored/projects/geometry/djoyce/mirror/aleph0.clarku.edu/~djoyce/elements/bookN/` and the matching java path
7. **Normalize + convert citations.** Run the two scripts in sequence — both default to dry-run so you can eyeball every proposed edit before applying. Idempotent: re-running on already-normalized content is a no-op.
   ```sh
   # Pass 1 — rewrite Joyce's variant display text to canonical eucref form.
   #   Post.4 → I.Post.4         Def.I.5 → I.Def.5         Def.5 → I.Def.5
   #   I.5.   → I.5  (trailing)  C.N     → C.N.            Post.I.N → I.Post.N
   #   Postulate N → I.Post.N    Proposition I.N → I.N     Prop.I.N → I.N
   python3 scripts/normalize-citations.py            # dry-run
   python3 scripts/normalize-citations.py --write    # apply

   # Pass 2 — convert now-canonical markdown links into eucref shortcodes.
   #   [I.5](url) → @I.5  (when url matches canonical Lektor leaf)
   #   <div class="just"><a>X</a>, <a>Y</a><br><a>Z</a></div> → [!just X, Y; Z]
   python3 scripts/convert-to-eucref.py              # dry-run
   python3 scripts/convert-to-eucref.py --write      # apply
   ```
   The scripts print a "Left as-is for hand-review" tally of cases where the display text matches the eucref grammar but the URL points at a non-canonical leaf — these are real source bugs (Joyce's hand-typed URL is wrong relative to his intended display). Look at each and decide: usually convert to `@TOKEN` form (the canonical URL is what was meant, even if Joyce's URL pointed at a bundle root or the wrong number); occasionally keep the markdown link if there's an intentional anchor (`#guide`, `#cor`) or the citation links into something the resolver can't express (an anchor-suffixed link, a cross-work reference to Apollonius later, etc.).
8. **Polish.** The agents will preserve some source quirks verbatim (typos in hrefs, mis-positioned figures). Iterate on user feedback or proactively check the patterns documented in [Common edge cases](#common-edge-cases).
9. **Extend `proptable[i]`** in `assets/js/footer-nav.js` with the book's nav order so Next/Previous works end-to-end.
10. **Update Book I intro Guide cross-references** where they pointed at "Book IV" / "Book XI" placeholder URLs — they should now resolve to live pages.

## Build / verify cycle

```sh
source ~/venvs/lektor/bin/activate
lektor build --output-path build/
```

Spot-checks (use `grep` against `build/` rather than `lektor serve` — the former is faster and surfaces actual rendered HTML):

```sh
# Did the page build?
ls build/elements/books/bookN/propositions/propN5/

# Theorem box + proof + Guide present?
grep -E "<h1>|<h2 id=\"guide\">|<div class=\"qed\">" build/elements/books/bookN/propositions/propN5/index.html

# Any unresolved markdown link syntax?
grep -E '\[[^]]+\]\([^)]*\)' build/elements/books/bookN/propositions/propN5/index.html
# (zero hits = clean; non-zero = markdown links bypassed by HTML block, fix to <a href>)
```

## Agent brief template

Each conversion agent gets a self-contained brief. The Book I template was:

> Convert N Euclid's Elements Book X propositions from HTML to markdown for a Lektor static site rebuild.
>
> Your assigned range: **propX{N}, propX{N+1}, …**.
>
> For each:
> - Read source: `/data-mirrored/projects/geometry/euclids-elements.org/elements/bookX/propX{N}.html`
> - Read current target: `/data-mirrored/projects/geometry/euclids-elements-lektor/content/elements/books/bookX/propositions/propX{N}/contents.lr`
> - Write updated target with `proof:` and `body:` markdown fields populated.

Then in the brief:

- **What to extract** — content between `<a name=guide><h2>Guide</h2></a>` and `<div id="footer">` for body; content between `<div class="statement">…</div>` and the closing `</div>` of the theorem div for proof.
- **What to drop** — `<div class="theorem">`, `<h1>`, `<div class="statement">`, `<h2>Guide</h2>`, layout `<table>`/`<tr>`/`<td>` wrappers around figures, `<p>` tags, header/footer JS.
- **What to preserve as inline HTML** — `<div class="qed">Q.E.F./Q.E.D.</div>`, `<br clear="all">`, `<figure class="diagram"[ rdiagram]>` wrapping canvas+noscript+script.
- **Marginal justifications** — convert source `<div class="just"><a href="…">I.3</a>, <a href="…">I.46</a><br><a href="…">I.31</a></div>` to the directive form `[!just I.3, I.46; I.31]`. The `lektor-eucrefs` plugin resolves the tokens to URLs at build time. Place the directive at the end of the sentence it justifies (it gets hoisted to before the `<p>` automatically). See [conventions.md → Marginal justifications](../conventions.md#marginal-justifications-just-) and [Euclid citation shortcodes](../conventions.md#euclid-citation-shortcodes).
- **Markdown rules** — `<i>` → `*`, `<b>` → `**`, `<h4>` → `####`, `<a href>` → `[text](url)` *only in prose* (or `@I.5` / `@I.Def.10` / `@I.Post.3` / `@C.N.1` for Elements citations — see plugin), `<p>` → blank line, `<center>` → `<center>` (keep, with `<i>` inside not `*`), `<ul>` indenter → `> …` blockquote.
- **Entity table** — `&ldquo; &rdquo; &rsquo; &lsquo; &ndash; &mdash; &deg; &nbsp; &pi;` → literal Unicode.
- **URL conversion table** — see [conventions.md](../conventions.md#url-conventions).
- **Figure rules** — left float vs right float based on source `<div class="ldiagram">` vs `<div class="rdiagram">` vs `<td>` position. Strip wrappers, keep canvas/noscript/script verbatim, fix stale `title:` in geomlib.init.
- **Worked example** — paste propI1's converted `.lr` so the agent has a template.

Then a closing instruction: "Report a short summary listing each file written and noting any oddities."

Adapt this brief per book (change book identifier, URL templates, worked example reference).

## Common edge cases

These come up most books. Watch for them and proactively check after each agent batch.

### Figure positioning

If a body subsection has `#### heading` then long text then `<figure rdiagram>`, the figure floats RIGHT but starts after the text block — so it bleeds into the NEXT section. Fix: move the figure to right after the `#### heading`.

```diff
 #### Construction steps

-Para 1.
-Para 2.
-<figure class="diagram rdiagram">…</figure>
+<figure class="diagram rdiagram">…</figure>
+
+Para 1.
+Para 2.

 #### Next section
```

Patterns in Book I that needed this fix: propI9, propI10, propI11, propI46, propI47. Likely similar in other books — search by `awk '/^body:/{b=1;next} b' propX*/contents.lr | grep -E "^####|^<figure"` and inspect the order.

### Bundled source pages

Some `<book>.html` source files describe multiple definitions (Book I's defI11.html bundles 11+12, defI15.html bundles 15-18, etc.). Identify them by counting `<div class="theorem">` blocks in the source. Use the bundle pattern (see [content-model.md](../content-model.md#the-bundle-pattern)).

### `<ul>` used as indenter, not list

When source has `<ul>...prose...</ul>` with no `<li>` children, it's an indented-quote — render as markdown blockquote (`> …`), not as `- bullet`. Book I had two cases: propI7 and propI17.

### `<center>` displayed formulas

Preserve `<center>…</center>` in markdown source with HTML italics inside. Mistune passes raw HTML through but does NOT process markdown inside it, so `*x*` will render as literal asterisks.

### Source typos to expect

Joyce's HTML has a fair number of small bugs that agents reliably flag:

- Link text says "I.19" but `href` is `propI45.html` (or vice versa). Convention: follow the visible text; the user reads the citation.
- Stray `</tr>` or `</td>` inside cells. Silently drop.
- Filename typos like `propIII.16.html` (extra dot). Map to the canonical slug.
- Unnumbered `<a href="cn.html">C.N.</a>` (no specific notion called out). Default to `cn1`.
- Missing visible link text (`<a href="propI27.html"></a>`). Supply the citation as visible text.

### Page-attached images

Two distinct cases here, both solved by copying the source `.gif` into the leaf's content folder so it ships as a Lektor page attachment:

1. **Visible non-canvas images** in the Guide body (e.g., Joyce's pre-rendered math diagram for the law of sines, or the *xian tu* raster). The agent preserves the `<img>` tag pointing at the bare filename; we copy the file by hand or as part of step 6 above. Book I needed `propI19b.gif` (law of sines) and `propI47a.gif` (*xian tu*); Book II needed `propII5b/c.gif` and `propII6b.gif`.
2. **Canvas `<noscript>` fallbacks** — every interactive canvas has a `<noscript><img src="propN{X}.gif"/></noscript>` for users without JS. There are ~100 of these across Book I + II; the bulk-copy is **step 6 in [High-level workflow per book](#high-level-workflow-per-book)** via `scripts/copy-gif-fallbacks.py`. Skipping that step means JS-disabled visitors see broken-image icons where canvases would be.

### Anchor links in `statement` field

The `statement` field is rendered both on the leaf page AND inside the section_index `<dd>`. Bare `#anchor` links resolve relative to the *current* page. On the section_index that's wrong. Use absolute paths for anchor links in statements:

```html
<a href="/elements/books/bookI/propositions/propI15/#cor">Corollary.</a>
```

## Parallel-agent etiquette

- **One book at a time** — don't fan out across books; they share so few patterns it's not worth the coordination.
- **~10–12 leaves per agent** — fewer than that and the brief overhead dominates; more and the context gets unwieldy.
- **Run in background** — `run_in_background: true` so multiple agents can work in parallel. You'll get completion notifications.
- **Agents do NOT share context.** Each `Agent(...)` call is a fresh process. They can't see this conversation, can't see sibling agents' work, and don't load any per-repo defaults. Every brief has to either inline the rules or tell the agent which file to Read.
- **Brief is self-contained.** Re-state the worked example, URL tables, figure rules, etc. The brief template above already does this for the bulk of the conversion rules.
- **Point each agent at `doc/conventions.md` for the slow-moving rules.** The brief should include a line like:
  > Before starting, Read `/data-mirrored/projects/geometry/euclids-elements-lektor/doc/conventions.md` end-to-end. It documents the canvas background convention (tan vs white), figure float direction (diagram vs rdiagram), marginal-justification HTML, axiom blockquotes, and other rules the agents can't infer from the source HTML alone.

  Agents reliably read it when instructed.
- **Trust but verify** — agents reliably preserve source quirks (typos, broken hrefs). Skim their oddity reports and spot-check the obvious patterns above.

### Conventions agents have missed in the past

These are the per-leaf details parallel agents have tended to drop. If you skip the "Read `conventions.md`" step, double-check each:

- **Canvas background (`background:` in `geomlib.init`)** — proof canvases use `"35,19,100"` (tan, matches theorem box); Guide canvases use `"0,0,100"` (white, matches page). Joyce's source HTML usually has the right value, but Book II's `<table>`-wrapped Guide canvases inherited the tan value from the surrounding proof figure layout. The fix is a one-line sed across the leaf:
  ```bash
  sed -i '/canvasid: "canvas_1"/,/^        title:/ s/background: "35,19,100"/background: "0,0,100"/' contents.lr
  ```
  Same pattern for `canvas_2`, etc.

- **Figure position within a subsection** — the figure goes RIGHT AFTER `#### Heading`, before the prose, so floats anchor to the top of their section. Agents often place it after the text (matching source order), which causes float-bleed into the next section.

- **`<ul>` indenter vs list** — Joyce uses `<ul>…prose…</ul>` (no `<li>`) as a CSS indenter. Convert to markdown blockquote (`> …`), not bullet list (`- …`).

- **Anchor links in `statement` field** — must be absolute URLs, not bare `#anchor`. The statement is rendered both on the leaf page and in the section_index `<dd>`; a relative `#anchor` resolves wrong from the section_index.

- **Source-HTML font tags leaking into frontmatter** — when scaffolding from a TOC, stray `<font color=…>` opens/closes around red-flagged entries can leak into the adjacent statement field. Strip with:
  ```bash
  sed -i -E 's| *<font color=[a-z0-9]+> *$||; s| *</font color> *$||' contents.lr
  ```
  Set `red_highlight: yes` on the leaves that were inside the font wrap.

## Commit cadence

Roughly per logical milestone. Recent commit shape:

```
6026e38 templates: red highlight on the title's <dt>, not the <dd> statement
8964f1c commonnotions: bundle as group with shared guide; axiom blue + centered tables
81a7b28 propositions: convert propI2-48 to markdown
0ac582f props: figure positioning fixes; center inline formulas; corollary link; page-attached gifs
14161eb footer: port Joyce's JS-driven bottom nav; stacked h1 walks up to book
d4b92d6 license: add LICENSE + COPYRIGHT.md, paths adapted for Lektor layout
```

Subjects are terse (semicolons separate sub-topics if needed). No Co-Authored-By trailer (user preference). Group by concern: model changes, content conversion, CSS polish, structural refactors.

## Picking up from a fresh session

If you're a new Claude Code session walking in:

1. Read `doc/README.md`, `doc/repo-layout.md`, `doc/content-model.md`, `doc/conventions.md`, `doc/journal/journal.md`. They were written for this exact handoff.
2. `git log --oneline -20` to orient on recent work.
3. `git status` — was anything left mid-stream?
4. Activate the venv: `source ~/venvs/lektor/bin/activate`.
5. `lektor build --output-path build/` to confirm the project still builds.
6. The user will direct: usually "convert book N" or "polish issue X". For (1) follow the workflow above; for (2) skim the journal for similar fixes.

If user mentions a book by name and there's no content yet, scaffold per the workflow. If they mention a polish issue (figure position, broken link, missing centering), check the common-edge-cases section.

## Open work, not yet started

### Content

- Books II–XIII content (likely Books IV, VI, XI, XIII in highest user-interest order based on references in Book I).
- Book intro Guides for II–XIII reference live pages that don't exist yet — links currently 404.
- Master TOC at `/elements/` may need polishing once more books exist.
- Prematter pages (`/elements/prematter/`) are sparse.

### Refactors / design

- **Split the JS footer three ways.** Currently `assets/js/footer-nav.js`'s `loadFooter()` renders the whole footer block — Next/Previous links + three `<select>` dropdowns + credit block — all in JS. Tracking on [issue #2](https://github.com/brownnrl/euclids-elements-lektor/issues/2). The intended split:
  - **Next / Previous → static** (Jinja-rendered from `this.parent.children.filter(F._model == this._model).order_by('order')`). These are deterministic from the current page's `order` field; no need for a client-side scan.
  - **Three dropdowns → stay in JS** (`assets/js/footer-nav.js`, slimmed to `loadNavDropdowns()`). They list all books / all topics / all entries in the current book and need the `onchange` handler to navigate.
  - **Credit block → static** (`<footer class="site-footer">` back in `templates/layout.html`). Home / ©dates / David E. Joyce / Copyright Notice / Source. The static version existed before commit `14161eb` — use that diff as the template. Copyright date string lives in `layout.html` (Jinja constant) or `.lektorproject` — avoid per-page customization.

  Net effect: with JS disabled the user still gets working Next/Previous and the full credit attribution. With JS enabled, the dropdowns appear too. Issue #2 has the full implementation sketch.

- **Geomlib version pin**: currently `0.3.0` in `templates/layout.html` — bump in lockstep with `brownnrl/euclid` releases.
