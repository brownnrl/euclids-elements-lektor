# euclids-elements-lektor

[Lektor](https://www.getlektor.com/)-based static-site-generator rebuild
of [euclids-elements.org](https://www.euclids-elements.org/) (the online
edition of Dr. David E. Joyce's *Euclid's Elements*).

This is **Phase 2** of the
[mobile/presentation roadmap](https://github.com/brownnrl/euclids-elements.org/issues/17),
tracked at [euclids-elements.org#13](https://github.com/brownnrl/euclids-elements.org/issues/13).
Per-milestone work lives in this repo's own issue tracker.

## Status

**Milestone 1 — scaffold.** A working Lektor project that reproduces
two Book I pages (the intro stub and Proposition I.1, plus a stub for
Proposition I.4) in the existing site's visual identity, and a
deploy-preview script that pushes the built output to a branch on
`euclids-elements.org` so Cloudflare Workers Builds auto-deploys it
to a phone-reachable preview URL.

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
├── models/                         Lektor content models (.ini files)
│   ├── page.ini                    Generic fallback
│   ├── book.ini                    Book intro pages (e.g. Book I TOC)
│   └── proposition.ini             Individual proposition pages
├── templates/                      Jinja2 templates
│   ├── layout.html                 Base: <head>, header div, footer div, geomlib script
│   ├── page.html
│   ├── book.html
│   └── proposition.html
├── assets/                         Verbatim-copied static files (css, js)
│   ├── css/style.css               From euclids-elements.org/css/style.css
│   └── js/header-footer.js         From euclids-elements.org/js/header-footer.js
├── content/                        Lektor content tree (one folder per URL)
│   ├── contents.lr                 Site root
│   └── bookI/
│       ├── contents.lr             Book I intro (book model)
│       ├── propI1/contents.lr      Proposition I.1 (proposition model)
│       └── propI4/contents.lr      Proposition I.4 stub
└── scripts/
    └── deploy-preview.sh           Build + push to euclids-elements.org/lektor/<branch>
```

## Roadmap

Milestones tracked as GitHub issues in this repo. The big arc:

- **M1** (this commit) — scaffold + 2 pages + deploy loop
- **M2** — full Book I conversion (intro page, all 48 propositions,
  definitions, postulates, common notions)
- **M3+** — Books II through XIII, the compass / round / eulerline tutorials
- **Refactor** — promote `proposition.model`'s raw-HTML `body` field
  into structured fields (statement / diagrams / proof / guide) so
  Phase 4a (cross-highlighting prose↔canvas) and Phase 4b
  (animated step-throughs) can compose against the data model

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
