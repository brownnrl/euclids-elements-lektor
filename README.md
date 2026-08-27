# euclids-elements-lektor

[Lektor](https://www.getlektor.com/)-based static-site-generator rebuild
of [euclids-elements.org](https://www.euclids-elements.org/) (the online
edition of Dr. David E. Joyce's *Euclid's Elements*).

This is **Phase 2** of the
[mobile/presentation roadmap](https://github.com/brownnrl/euclids-elements.org/issues/17),
tracked at [euclids-elements.org#13](https://github.com/brownnrl/euclids-elements.org/issues/13).
Per-milestone work lives in this repo's own issue tracker. Phase 2 is
near completion; the next phase (cross-highlighting prose↔canvas,
animated proof step-throughs) needs the structured-field refactor of
`proposition.model` called out in the roadmap below.

## Status

**Content conversion complete.** All 13 books of the *Elements* —
definitions, postulates, common notions, and the full corpus of
~465 propositions — are rendered as markdown content with
`geomlib.init({...})` canvases. Prematter pages are converted
(Introduction, Quick Trip, Euclid, About the Text, References on the
Web, Subject Index, Copyright). Joyce's republished tutorials
(Compass Geometry's 7-part series, Round Triangles, Six Circles &
Eight Points, Desargues' Theorem, the Euler Line) live under
`/other-works/`, and the library's own site (landing + Using
diagrams + Joyce's 1996 *Geometry Applet* archive + the original
construction-methods tables) lives under `/geomlib/`. Mobile layouts
collapse the master TOC and Subject Index across breakpoints and
stack the footer-nav row on phones.

Authoring reference lives under [`doc/`](doc/) — see
[`doc/README.md`](doc/README.md) for the map.

## Setup

### Lektor in a venv

Lektor is a Python package; install into a venv to keep system Python
clean:

```sh
# global venv (recommended — reusable across Lektor projects)
mkdir -p ~/venvs && python3 -m venv ~/venvs/lektor
source ~/venvs/lektor/bin/activate
pip install -r requirements.txt
lektor --version  # should print 3.3.13 or newer
```

Or per-project (uses `.venv/`, which is `.gitignore`d):

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Local development

```sh
source ~/venvs/lektor/bin/activate
lektor serve              # http://127.0.0.1:5000/ with live reload
```

Or one-shot build + a plain HTTP server:

```sh
lektor build --output-path build
cd build && python3 -m http.server 8001 --bind 0.0.0.0
# Visit http://localhost:8001/ or http://<your-LAN-ip>:8001/ on a phone
```

## Publishing to the live site

`www.euclids-elements.org` is served by **GitHub Pages** from the
`brownnrl/euclids-elements.org` repo. Publish with:

```sh
./scripts/publish.sh --dry-run    # check + build, deploy nothing
./scripts/publish.sh              # check, build, confirm, deploy
```

The wrapper exists so a publish cannot skip validation — it runs
[`scripts/check-decks.js`](scripts/check-decks.js) over every page and refuses
to deploy if any figure is broken, then verifies the build actually produced
its key files before asking for confirmation.

It calls Lektor's `ghpages` publisher via the `[servers.production]` target in
`euclids-elements.lektorproject`, which pushes the build to `gh-pages` and
writes **`CNAME`** from the target's `?cname=` parameter — Pages reads that to
bind the custom domain, so it has to be in the published tree.

`LICENSE` and `COPYRIGHT.md` reach the build through `assets/` (symlinks to
this repo's copies). The publisher does `git add -f --all` on the build
directory, so **anything not in the build is not published** — that is the
mechanism to use for any file the live site must carry.

> **Note on URLs.** The Lektor tree uses directory URLs
> (`/elements/books/bookI/propositions/propI47/`) where the older hand-authored
> site used flat files (`/elements/bookI/propI47.html`). The scheme change is
> deliberate; deep links into the old scheme do not resolve.

## Deploying a preview to euclids-elements.org

The site at `euclids-elements.org` already has Cloudflare Workers
Builds connected — every branch push gets a preview URL at
`<branch-slug>-euclids-elements-org.brownnrl.workers.dev`. This repo's
[`scripts/deploy-preview.sh`](scripts/deploy-preview.sh) leverages that:

1. Runs `lektor build`
2. Force-pushes the build output to a `lektor/<branch>` branch on
   `euclids-elements.org`
3. CF picks up the push, builds, deploys
4. Preview URL: `https://lektor-<branch>-euclids-elements-org.brownnrl.workers.dev/`

Usage:

```sh
./scripts/deploy-preview.sh                # uses current git branch
./scripts/deploy-preview.sh my-experiment  # custom branch name
```

The script assumes the `euclids-elements.org` checkout sits at
`../euclids-elements.org` (override with `EUCLIDS_REPO=...`).

## Repo layout

```
.
├── euclids-elements.lektorproject  Project metadata
├── requirements.txt                Lektor pin
├── packages/
│   ├── lektor-eucrefs/             @I.5 / [!just …] inline + block citations
│   └── lektor-katex/               Build-time KaTeX rendering
├── models/                         Lektor content models (.ini files)
│   ├── book.ini, section_index.ini, toc.ini
│   ├── definition.ini + definition_group.ini   (bundle pattern, shared Guide)
│   ├── postulate.ini, commonnotion.ini, commonnotion_group.ini
│   ├── proposition.ini             Statement + proof + body markdown fields
│   ├── prematter.ini, prematter_index.ini
│   ├── other_work.ini              Compass series, round, sixeight, euler, geomlib
│   └── page.ini                    Generic markdown fallback
├── templates/                      Jinja2 templates, one per model
├── assets/                         Static CSS + JS
│   ├── css/style.css               Mobile-aware (column collapse, footer stack)
│   ├── js/footer-nav.js            JS-driven booktable + proptable nav
│   └── css/katex/                  KaTeX font + stylesheet
├── content/                        Lektor content tree (one folder per URL)
│   ├── contents.lr                 Introduction
│   ├── elements/                   Master TOC + prematter + bookI…bookXIII
│   ├── other-works/                Compass Geometry, round, sixeight, desargues, euler
│   └── geomlib/                    Landing + Using + Joyce archive + reference tables
├── scripts/
│   ├── deploy-preview.sh           Build + push to euclids-elements.org/lektor/<branch>
│   ├── copy-gif-fallbacks.py       Walk content + copy <noscript> .gif assets
│   ├── normalize-citations.py      Joyce variant spellings → canonical (idempotent)
│   ├── convert-to-eucref.py        [text](url) markdown links → @TOKEN shortcodes
│   └── render-katex.js             Build-time math rendering helper
└── doc/
    ├── conventions.md              Canvas backgrounds, figure floats, eucref grammar
    ├── content-model.md            Bundle pattern, frontmatter shapes
    └── deck-tracker.md             Per-proposition deck status and notes
```

## Roadmap

Milestones tracked as GitHub issues in this repo. The big arc:

- **M1** ✅ — scaffold + 2 pages + deploy loop
- **M2** ✅ — full Book I conversion (intro, 48 propositions,
  definitions, postulates, common notions)
- **M3** ✅ — Books II through XIII, the compass / round / euler
  tutorials, geomlib's own site (landing + Using + Joyce archive)
- **M4 — structured-field refactor** (next) — promote
  `proposition.model`'s markdown `body` into structured fields
  (statement / diagrams / proof / guide) so Phase 4a
  (cross-highlighting prose↔canvas) and Phase 4b (animated
  step-throughs) can compose against the data model.

## Licensing

- Content under `content/` is &copy; David E. Joyce, republished by
  permission. The hand-authored source HTML lives at
  [brownnrl/euclids-elements.org](https://github.com/brownnrl/euclids-elements.org)
  with the same posture; this repo carries the structured-data
  rewrite of the same material.
- Templates, scripts, and Lektor models authored for this repo are
  MIT-licensed.
- `geomlib` (loaded from unpkg at build time) is MIT;
  [brownnrl/euclid](https://github.com/brownnrl/euclid).
