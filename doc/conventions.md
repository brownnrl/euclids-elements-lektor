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

### Marginal justifications (`[!just …]`)

The little right-floated reference column next to each proof step. Use the `[!just …]` directive — the `lektor-eucrefs` plugin (see [Euclid citation shortcodes](#euclid-citation-shortcodes) below) resolves the bare tokens to `<a href>` links and emits the wrapping `<div class="just">`.

```markdown
Describe the circle *BCD* with center *A* and radius *AB.* [!just I.Post.3, I.Post.1]

Now, since the point *A* is the center of the circle *CDB,* therefore *AC* equals *AB.* [!just I.Def.15]
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
