# Repo documentation

Reference for the Lektor rebuild of Dr. David E. Joyce's *Euclid's Elements*.

| File | What you'll find |
|---|---|
| [repo-layout.md](repo-layout.md) | Folder structure, what lives where, and what each script does |
| [content-model.md](content-model.md) | URL hierarchy, Lektor models and templates, and the **bundle pattern** for grouped source pages |
| [conventions.md](conventions.md) | Markdown patterns — figures, marginal `[!just]` refs, citation shortcodes, editorial footnotes, KaTeX — plus URL and CSS conventions |
| [process.md](process.md) | **How a slideshow deck gets built**: the planning table, the authoring rules, and the verification checklist |
| [deck-tracker.md](deck-tracker.md) | Per-proposition deck status and notes, plus what is deferred and why |

## Where to start

- **Building a deck** → [process.md](process.md), then the relevant row of
  [deck-tracker.md](deck-tracker.md) for how similar propositions were handled.
- **Editing page content** → [conventions.md](conventions.md).
- **Finding your way around** → [repo-layout.md](repo-layout.md), then
  [content-model.md](content-model.md).
- **Running or publishing the site** → the root [README](../README.md).

## Status

All 13 books are converted, and **every Book I proposition (I.1–I.48) has a
slideshow deck**, each visually confirmed. Books II–XIII have converted prose
and figures but no decks yet. The site is published from the `gh-pages` branch
of `euclids-elements.org` — see the root README's *Publishing* section.

## Checks

`scripts/check-decks.js` evaluates every page's inline geomlib script against
the real bundle and fails on any diagnostic. It gates both
`scripts/deploy-preview.sh` and `scripts/publish.sh`, so a broken figure cannot
reach a preview or the live site:

```sh
NODE_PATH=../euclid/node_modules node scripts/check-decks.js
```

## Regenerating the content audit

The prose conversion was checked page-by-page against Joyce's original HTML.
Those reports are **derived data and are not committed** — regenerate them into
`doc/journal/` (gitignored) when you need them:

```sh
python3 scripts/audit-content.py          # -> doc/journal/content-audit.md
python3 scripts/audit-review.py           # interactive review, appends a log
```

The last full run flagged 70 pages; all were reviewed, and the four genuine
citation errors it found were fixed in the content.
