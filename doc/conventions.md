# Conventions

Patterns the templates and content rely on. If you violate one, the build still passes — but the render breaks subtly.

## Markdown body patterns

### Figures (geomlib canvases)

Float left (default) — wrap in `<figure class="diagram">`:

```markdown
<figure class="diagram">
<canvas id="canvas_0" width="340" height="260" tabindex="0"></canvas>
<noscript><img alt="I.1 diagram" src="propI1.gif"/></noscript>
<script type="text/javascript">
geomlib.init({
    canvasid: "canvas_0",
    background: "0,0,100",
    title: "I.1",
    elements: [ ... ],
});
</script>
</figure>
```

Float right (text wraps left) — add `rdiagram`:

```markdown
<figure class="diagram rdiagram"> ... </figure>
```

**Place the figure at the TOP of the subsection it belongs to** (immediately after the `#### Heading`). If you put it after the prose, it floats down into the next section because there's no flow content left in its own section to wrap around.

#### Canvas background

The `background:` parameter passed to `geomlib.init(...)` paints the canvas's own backdrop. Match it to the surrounding page region:

| Region | `background:` value | What it looks like |
|---|---|---|
| Proof (inside the beige theorem box) | `"35,19,100"` | Cream / pale tan — blends with the `.theorem` box |
| Guide (below the theorem box, on the white page) | `"0,0,100"` | White — blends with the page background |

If you use the tan value on a Guide-area canvas, the canvas shows up as a tan rectangle on the white page (visible mismatch). If you use the white value on a proof-area canvas, the canvas shows up as a white rectangle on the beige theorem box (also visible mismatch).

The first canvas on a page (`canvas_0`) almost always lives in the proof. Secondary canvases (`canvas_1`, `canvas_2`, …) almost always live in the Guide. Joyce's source HTML usually uses the right value, but bookII's `<table>` layouts often inherited `35,19,100` for guide-area canvases — those need to be flipped to `0,0,100` during conversion.

On mobile (`max-width: 480px`) figures stop floating and stack centered. The `canvas` itself has `max-width: 100%; height: auto;` so it shrinks on narrow viewports — geomlib 0.2.0+ remaps Pointer Events through CSS scaling, so hit-testing is preserved.

### Element references (`{AB}`) — the interactive layer

Wrapping an element's letters in braces turns them into a live reference: hover
or tap it and the matching element lights up on the figure, and (geomlib 0.11+)
every *other* reference to the same element lights up with it.

```markdown
Describe the circle {BCD} with center {A} and radius {AB}. [!just I.Post.3, I.Post.1]
```

`lektor-eucrefs` renders that as:

```html
<span class="elem-ref" data-elem="BCD">BCD</span>
```

and `assets/js/elem-ref-highlight.js` binds the hover/touch handlers.

**`*AB*` vs `{AB}`.** Joyce's source italicises element letters, and that is
what the converted prose starts as. Italics are inert — no highlight, no
binding. Converting `*AB*` → `{AB}` is the normal way to bring a page into the
interactive layer, and it is explicitly allowed on proof and guide prose:
tokenizing words that are **already there** is fine, adding words is not (see
[process.md](process.md#dont-add-words-to-the-guide-or-proof-prose)). Leave
`*AB*` where the element does not exist on the page's figure.

#### Display override — `{DISPLAY|element}`

When the prose spells an element differently from how the figure declares it,
show one and bind to the other:

```markdown
the angle {ABC|CBA}          # reads "ABC", lights the element declared CBA
the angle {CEF|angCEF}       # reads "CEF", lights the angle marker
```

This is what makes name collisions liveable: a triangle usually owns the plain
name (`ABC`), so its angle marker is declared `angABC` and the prose reaches it
with `{ABC|angABC}`. Same for a reversed spelling — `{DBC|BCD}` — although a
reversal is usually better handled once, as an `aliases` entry on the figure,
than repeated at every mention.

> **Both halves are constrained identifiers** — letter-led, then letters,
> digits, `'` or `-`. **No spaces and no underscores in either half.** So a
> multi-word display (`{the side from D to A|sideDA}`) does **not** work in
> prose; it is a geomlib *caption* feature, not a lektor one. Phrase around it:
> `the {side|sideDA} from D to A`.

#### Which canvas does a reference bind to?

The browser resolves each span in this order:

1. An explicit `data-canvas` / `data-canvases` attribute, if present.
2. The nearest enclosing `div.theorem` section.
3. **The nearest canvas *preceding* the span** — latest-preceding first, since a
   reference is normally talking about the figure just above it.
4. Failing that, a canvas *following* it — for prose that names an element
   before its figure appears.

On a single-canvas page this is automatic: tokenize freely. On a multi-canvas
page, **order the prose so each reference's nearest preceding canvas is the one
it means** — a guide reference placed after `canvas_1` binds to `canvas_1`, one
between the canvases binds to `canvas_0`.

#### Naming the canvas explicitly — `{AB:1}`

Add a canvas **index** to pin which figure a reference lights, for the cases
where the fallback above is not what the prose means:

```markdown
{AB:1}                   → data-canvas="canvas_1"
{ABC:0,1}                → data-canvases="canvas_0,canvas_1"   (light both)
{ABC|angABC:1}           → display override AND selector
```

The multi form is the cross-canvas highlight (geomlib 0.13+): one reference
lights the same element on several figures at once — how I.26's two case
figures light together.

> **It is an index, not the id.** `{AB:canvas_1}` does **not** work: Mistune
> splits inline text at `_`, so that token reaches the renderer as two pieces
> (`{AB:canvas` + `_1}`) and never matches. The rejoined output still *looks*
> intact on the page, which makes this easy to misdiagnose — if a selector is
> rendering literally, check for an underscore first.

The equivalent raw HTML still works, and is what older pages use:

```html
<span class="elem-ref" data-elem="AB" data-canvas="canvas_1">AB</span>
<span class="elem-ref" data-elem="ABC" data-canvases="canvas_0,canvas_1">ABC</span>
```

#### Caveat: slide sets are not prose

`aliases` resolve for these prose references, but **not** inside a slide's
`visible` / `highlighted` arrays, where only the declared name matches. See
[process.md](process.md#slide-sets-take-canonical-names-only--aliases-are-inert-there).

### Marginal justifications (`[!just …]`)

The little right-floated reference column next to each proof step. Use the `[!just …]` directive — the `lektor-eucrefs` plugin (see [Euclid citation shortcodes](#euclid-citation-shortcodes) below) resolves the bare tokens to `<a href>` links and emits the wrapping `<div class="just">`.

```markdown
Describe the circle {BCD} with center {A} and radius {AB}. [!just I.Post.3, I.Post.1]

Now, since the point {A} is the center of the circle {CDB}, therefore {AC} equals {AB}. [!just I.Def.15]
```

Inside the directive:
- `,` keeps refs on the same logical line (rendered with literal `", "` between links).
- `;` breaks to a new line (rendered as `<br>`).

The directive may appear **anywhere** in a paragraph — at the start, at the end of the sentence it justifies, or on its own line as a standalone block. In all three forms the plugin hoists the rendered `<div class="just">` to **before** the surrounding `<p>` so the float-right CSS lines it up alongside the paragraph it accompanies.

```markdown
[!just I.Post.3, I.Post.1]                       # block, before the paragraph

Describe the circle BCD... [!just I.Post.3]      # inline at end

[!just I.Post.3] Describe the circle BCD...      # inline at start
```

All three render identically. Pick whichever reads cleanest in source — for short single-ref justifications, end-of-sentence reads most naturally; for stacked multi-line refs, the block form keeps the sentence uncluttered.

The CSS rule is `float: right; clear: right;` — each `.just` div clears prior right floats so they stack vertically against the right edge instead of left of each other.

### Euclid citation shortcodes

The `lektor-eucrefs` plugin (`packages/lektor-eucrefs/`) recognizes two markdown additions for citations into Euclid's Elements:

| Source | Renders to |
|---|---|
| `@I.5` | `<a href="/elements/books/bookI/propositions/propI5/">I.5</a>` |
| `@I.Def.10` | `<a href="/elements/books/bookI/definitions/defI10/">I.Def.10</a>` |
| `@I.Post.3` | `<a href="/elements/books/bookI/postulates/post3/">I.Post.3</a>` |
| `@C.N.1` | `<a href="/elements/books/bookI/commonnotions/cn1/">C.N.1</a>` |
| `@II.4`, `@XIII.18` | other-book propositions |
| `@XI.Def.2` | other-book definitions |
| `[!just I.3, I.46; I.31]` | `<div class="just"><a/>, <a/><br><a/></div>` |

Token grammar: Roman numeral book (`I` through `XIII`), then optional `Def.` or `Post.`, then a number. Common notions are spelled `C.N.{N}` (Book I implied — no other book has common notions). Anything that doesn't fit becomes `<a href="#unresolved-…">` so the issue surfaces visibly in the rendered page.

**Hand-rolled `<div class="just">` HTML still works** if you need a one-off that the resolver can't express (e.g. a cross-work citation into Apollonius later, or an anchor like `propI15/#cor`). The plugin only fires on the bracket-bang directive, not on raw HTML.

### End-of-proof marker

```markdown
<div class="qed">Q.E.F.</div>
<br clear="all">
```

`Q.E.F.` for constructions (also flagged `red_highlight: yes`); `Q.E.D.` otherwise. The trailing `<br clear="all">` is preserved when present in source and helps clear residual floats inside the theorem box.

### Editorial footnotes (source corrections)

When Dr. Joyce's source text contains an error (verified against the
`djoyce/` mirror as original, not a conversion artifact), **correct it inline**
and record the emendation in a numbered footnote at the end of the page,
flagged with a superscript marker. Never change the text silently — the
footnote is the audit trail. Note wording is a dated, initialed changelog
entry: `Typo correction from "<old>" to "<new>." —<initials>, <YYYY-MM-DD>`.
First used on I.22 (`propI22/contents.lr`).

Marker at the corrected text (in the `proof` or `guide` field, right after the
word/punctuation):

```html
<sup class="fn-ref" id="fnref-1"><a href="#fn-1">1</a></sup>
```

Footnotes section, appended at the **end of the `guide:` field** (it renders
after the guide prose and before the `referenced_by` table — i.e. the end of
the page; anchors resolve across the proof/guide fields since they share one
HTML document):

```html
<hr class="footnotes-sep">
<section class="footnotes" id="footnotes">
<ol>
<li id="fn-1">Typo correction from &ldquo;…&rdquo; to &ldquo;… .&rdquo; &mdash;NB, 2026-06-17 <a href="#fnref-1" class="fn-back" aria-label="Back to text">&#8617;</a></li>
</ol>
</section>
```

Numbering is per page (`fnref-1`/`fn-1`, `fnref-2`/`fn-2`, …). CSS lives in
`assets/css/style.css` (`sup.fn-ref`, `hr.footnotes-sep`, `section.footnotes`,
`li:target` flash). **Slideshow caveat:** a slide caption is plain text drawn
on canvas and can't carry a DOM anchor — in a caption use a bare superscript
character (e.g. `¹`) with no link; the prose body carries the linked marker.

### Math (KaTeX)

Math is **pre-rendered at build time** by the `lektor-katex` plugin
(`packages/lektor-katex/lektor_katex.py`), which shells out to Node + KaTeX
via `scripts/render-katex.js` and substitutes the rendered HTML into the page.
KaTeX's CSS + fonts are vendored under `assets/css/katex/` (matched to KaTeX
**0.17.0**); there is **no client-side KaTeX JS** — nothing renders in the
browser, so there are no `$…$`-style delimiters to scan for.

Two authoring forms — both raw HTML, so Mistune passes the TeX through
verbatim (the plugin's regexes are anchored, so each must sit on its own and
match the class string exactly):

```markdown
<div class="math display">…TeX…</div>      ← displayed (centred block)
<span class="math">…TeX…</span>            ← inline
```

Write the body as ordinary LaTeX; wrap any prose words in `\text{…}` so they
stay upright and keep their spaces:

```markdown
<div class="math display">\text{If } x < y \text{ and } y = z \text{, then } x < z\text{.}</div>
```

A render failure emits a visible red `<span class="katex-error">` rather than
breaking the build, so a typo is easy to spot on the page.

**Editorial rule.** Re-typesetting Joyce's `<i>x</i> < <i>y</i>`-style HTML
math (or `<center>`-wrapped formulas) into KaTeX is purely a *typesetting*
change: never reword, drop, or add meaning. The prose ("If … and … then …")
and the relations must read identically — only the rendering gets cleaner.
Legacy `<center>`+`<i>` formulas still in the content get migrated to this
form as you touch a page.

### Axiom blocks

Formal axiom statements (introduced in the cn1_5 guide and likely elsewhere later) render blue:

```markdown
<blockquote class="axiom">
<p>Reflexivity: For each <i>x,</i> <i>x</i> = <i>x.</i></p>
<p>Symmetry: If <i>x</i> = <i>y,</i> then <i>y</i> = <i>x.</i></p>
</blockquote>
```

Derived properties (not formal axioms) stay as plain markdown blockquotes (`> …`). The CSS selector is `blockquote.axiom { color: #0000ff }` — plain `<blockquote>` inherits default text color.

### Page-attached images (non-canvas `.gif`s)

Place the file inside the leaf's content folder next to `contents.lr`:

```
content/.../propositions/propI19/contents.lr
content/.../propositions/propI19/propI19b.gif
```

Reference it with a relative path:

```markdown
<center><img alt="law of sines" src="propI19b.gif"></center>
```

Lektor's asset pipeline ships attachments alongside `index.html` in the build output, so the relative `src` resolves cleanly.

### `<center>` for displayed prose vs. `text-align: center` for everything else

Displayed math: use the KaTeX `<div class="math display">` block (see [Math (KaTeX)](#math-katex)) — **not** `<center>`.

Displayed non-math prose or a centred image (e.g. the `propI19b.gif` law-of-sines panel above): `<center>` (HTML — markdown can't express centering).

Page-level centering (h1/h2 titles, statement boxes): CSS only — never write `<center>` for these, the templates handle it.

## URL conventions

The original source used `.html` filenames, all relative to the book root. The Lektor URL forms:

| Source href | Markdown link target |
|---|---|
| `defI{N}.html` | `../../definitions/defI{N}/` |
| `post{N}.html` | `../../postulates/post{N}/` |
| `cn{N}.html` or `cn.html` | `../../commonnotions/cn{N}/` (default `cn1` for unnumbered) |
| `propI{N}.html` | `../propI{N}/` (within propositions/) or `../../propositions/propI{N}/` (cross-section) |
| `../bookN/defN{X}.html` | `/elements/books/bookN/definitions/defN{X}/` |
| `../bookN/postN{X}.html` | `/elements/books/bookN/postulates/postN{X}/` |
| `../bookN/propN{X}.html` | `/elements/books/bookN/propositions/propN{X}/` |
| `../bookN/bookN.html` | `/elements/books/bookN/` |
| `cn.html#…` or `propIN.html#anchor` | drop the `.html`, keep `/#anchor` |

**Cross-book and cross-section: prefer absolute paths starting `/elements/books/...`.** Within the same section, relative `../<sibling>/` is fine.

**One special case for in-page anchors that are also referenced from section indexes**: use the full absolute URL of the leaf, not a `#anchor` alone. The `statement` field is rendered both on the leaf page and in the section_index `<dd>`; a bare `#cor` would resolve to the section_index page (which has no such anchor). See `propI15/contents.lr` for the worked example: `<a href="/elements/books/bookI/propositions/propI15/#cor">Corollary.</a>`.

## HTML entity → Unicode

Convert in markdown source:

```
&ldquo; → "
&rdquo; → "
&rsquo; → '
&lsquo; → '
&ndash; → –
&mdash; → —
&#150;  → –
&#151;  → —
&deg;   → °
&nbsp;  → (regular space)
&pi;    → π
```

Greek letter and numeric entities — use the literal Unicode character.

## Footer nav (`assets/js/footer-nav.js`)

`booktable` lists 13 books with directory slugs. `proptable[0]` enumerates Book I's nav order:

```
defI1, defI2, …, defI10,
defI11 (label "I.Def.11-12"), defI13 ("I.Def.13-14"),
defI15 ("I.Def.15-18"), defI19,
defI20 ("I.Def.20-21"), defI22, defI23,
cn1 ("Common Notions"),
post1 … post5,
propI1 … propI48
```

**Bundle entries collapse to ONE proptable row each**, pointing at the first member URL. Next/Previous skips over bundled siblings because they share content with their group leader.

When adding Books II–XIII, extend the same `proptable[i]` shape for each. Until then, those slots stay as empty `[]` arrays and Next/Previous walks past them at book boundaries.

## CSS rules worth knowing

| Rule | Why |
|---|---|
| `div.theorem { display: flow-root }` | Contains floated figures/justifications inside the beige box — original site had the same bug (canvases hanging out the bottom) and we fix it cleanly |
| `figure.diagram canvas { max-width: 100% }` | Canvases shrink on narrow viewports; geomlib 0.2.0+ remaps coords through CSS scale |
| `@media (max-width: 480px)` for figures | Below this, float collapses to centered block. Above, even narrow desktop widths keep text wrapping |
| `div.just { float: right; clear: right }` | Marginal annotations stack vertically against the right edge |
| `blockquote.axiom { color: #0000ff }` | Joyce's formal-axiom highlight |
| `table { margin: 0.8em auto }` | Markdown tables center on the page |
| `.red-highlight { color: #bb0033 }` (no anchor override) | Theorem entries get red; nested `<a>` tags keep default blue link color (matches how the source `<font color=bb0033>` behaved under browser link styling) |
| `h2 a / h3 a / h4 a` stay blue without underline regardless of visited | Section headings are navigation, not prose links |
