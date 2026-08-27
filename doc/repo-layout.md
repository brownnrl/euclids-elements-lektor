# Repo layout

```
euclids-elements-lektor/
├── euclids-elements.lektorproject  # project metadata (Lektor entrypoint)
├── requirements.txt                # Python deps (pinned Lektor version)
├── README.md                       # quick start
├── LICENSE                         # MIT (Lektor plumbing only)
├── COPYRIGHT.md                    # Joyce content licensing
│
├── models/                         # field definitions per content type
│   ├── page.ini                    # generic fallback
│   ├── toc.ini                     # master /elements/ table of contents
│   ├── book.ini                    # book intro (Book I, II, …)
│   ├── section_index.ini           # definitions / postulates / commonnotions / propositions
│   ├── definition.ini              # leaf: a single definition
│   ├── postulate.ini               # leaf: a single postulate
│   ├── commonnotion.ini            # leaf: a single common notion
│   ├── proposition.ini             # leaf: a single proposition (has `proof` + `body`)
│   ├── definition_group.ini        # hidden shared-guide page for bundled defs (15-18 etc.)
│   ├── commonnotion_group.ini      # hidden shared-guide page for the 5 CNs
│   ├── prematter.ini               # leaf: intro / aboutText / Euclid / Web etc.
│   └── prematter_index.ini         # the /elements/prematter/ folder index
│
├── templates/                      # Jinja per model
│   ├── layout.html                 # base — stacked header, breadcrumb, JS footer slot
│   ├── _imagemap.html              # 13-region clickable pentagon (non-leaf pages)
│   ├── leaf.html                   # legacy raw-body fallback (still used by some leaves)
│   ├── page.html                   # generic
│   ├── toc.html                    # master TOC
│   ├── book.html                   # book intro (auto-lists section_index entries)
│   ├── section_index.html          # section listing (dl/dt/dd of leaf members)
│   ├── definition.html             # walks bundle siblings, builds theorem box + Guide
│   ├── definition_group.html       # minimal landing for hidden group URL
│   ├── commonnotion.html           # combined single theorem box (all 5 numbered) + Guide
│   ├── commonnotion_group.html     # minimal landing for hidden CN group URL
│   ├── postulate.html              # theorem box + Guide
│   ├── proposition.html            # theorem box (statement + proof inside) + Guide
│   ├── prematter.html              # prematter leaf
│   └── prematter_index.html        # prematter index
│
├── assets/                         # served verbatim at the site root
│   ├── css/style.css               # one stylesheet for the whole site
│   ├── js/footer-nav.js            # JS-driven bottom navigation (Joyce-style)
│   ├── js/elem-ref-highlight.js    # lights prose {NAME} refs from geomlib's highlight event
│   ├── favicon.svg / .ico / *.png  # site icon (Proposition I.1)
│   ├── LICENSE, COPYRIGHT.md       # symlinks to the repo copies — they must be IN
│   │                               #   the build to be published (see publish.sh)
│   └── geomlib-dev.js              # symlink to ../euclid/dist/bundle.js (local-dev toggle)

├── packages/                       # local Lektor plugins
│   ├── lektor-eucrefs/             # @I.5 / [!just …] citation shortcodes + referenced_by
│   └── lektor-katex/               # build-time KaTeX rendering (no client JS)

├── flowblocks/                     # Lektor flow blocks used by the models
│
├── content/                        # Lektor content tree (the source of truth)
│   └── elements/
│       ├── contents.lr             # master /elements/ TOC
│       ├── prematter/              # intro essays
│       └── books/
│           ├── bookI/
│           │   ├── contents.lr     # Book I intro + Guide
│           │   ├── definitions/    # section_index + defI1…defI23 + group folders
│           │   │   ├── defI11_12/  # hidden bundle group (defs 11–12)
│           │   │   ├── defI13_14/  # hidden bundle group (defs 13–14)
│           │   │   ├── defI15_18/  # hidden bundle group (defs 15–18)
│           │   │   ├── defI20_21/  # hidden bundle group (defs 20–21)
│           │   │   └── defIN/contents.lr
│           │   ├── postulates/     # section_index + post1…post5
│           │   ├── commonnotions/  # section_index + cn1…cn5 + cn1_5/ (hidden group)
│           │   └── propositions/   # section_index + propI1…propI48
│           └── bookII/ … bookXIII/ # converted prose + figures; no decks yet
│       └── other-works/            # Compass Geometry, Round Triangles, Six Circles,
│                                   #   Desargues, Euler line, and geomlib's own site
│
├── scripts/
│   ├── check-decks.js              # evaluates every page's geomlib script against the real
│   │                               #   bundle; gates both deploy scripts. Needs node-canvas
│   │                               #   from ../euclid
│   ├── publish.sh                  # check + build + confirm + deploy to the LIVE site
│   ├── deploy-preview.sh           # check + build + force-push to a lektor/<branch> preview
│   ├── audit-content.py            # regenerate the prose audit vs Joyce's HTML (output
│   │                               #   goes to the gitignored doc/journal/)
│   ├── audit-review.py             # interactive review over that audit
│   ├── normalize-citations.py      # Joyce's variant citation spellings → canonical
│   ├── convert-to-eucref.py        # [text](url) links → @TOKEN shortcodes
│   ├── copy-gif-fallbacks.py       # walk content, copy <noscript> .gif assets
│   └── render-katex.js             # build-time math helper (used by lektor-katex)
│
├── build/                          # `lektor build` output (gitignored)
└── doc/                            # this directory
```

## Notes on the tree

- **`models/` and `templates/` are paired**: every model needs a same-name template, so adding a new content type means adding both files.
- **Group folders (`defI15_18/`, `cn1_5/`) are siblings of the bundled leaves, not children.** They use a separate model (`definition_group` / `commonnotion_group`) so the section index filter (`F._model == this.child_model`) naturally excludes them. They also carry `_hidden: yes` so cross-record queries exclude them too.
- **`.lr` field separator is `---` on its own line.** A blank line after a system field like `_hidden: yes` does NOT separate — you'll get a multi-line field value. Always put `---` between system fields.
- **The build directory is ephemeral.** The published site is a *copy* of it on the `gh-pages` branch of `euclids-elements.org`, which GitHub Pages serves; the local `build/` is just for spot-checks. Cloudflare Workers serves the `lektor/<branch>` previews.
- **Anything the live site must carry has to be in the build.** The publisher does `git add -f --all` on the build directory, which is why `LICENSE` and `COPYRIGHT.md` are symlinked into `assets/`.
