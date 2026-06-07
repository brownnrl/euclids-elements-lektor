# Link-normalisation patterns observed in the audit

Generated alongside [`content-audit.md`](content-audit.md). Each row is a Joyce-display-label ↔ ours-display-label
pair that was flagged as a link diff somewhere in the audit. Sorted by frequency.

- `(missing)` in the right column means Joyce's display label has no equivalent display in our version — usually a canonicalisation: Joyce wrote `Post.4`, our normalized version shows `I.Post.4`.
- `(added)` in the left column means we surfaced a display label Joyce never wrote.
- The `audit-content.py` normaliser already accepts a baked-in set of canonicalisations (`Post.N` → `I.Post.N`, `Def.N` → `I.Def.N`, etc.). Patterns that show up here are the ones the normaliser doesn't yet recognise.

| Count | Joyce display | Ours display | Pages |
|---|---|---|---|
| 4 | `x.def.iii.2` | `(missing)` | `propX108`, `propX85`, `propX91`, …(+1) |
| 4 | `x.def.1` | `(missing)` | `defV5_6`, `propX6`, `trip`, …(+1) |
| 4 | `(added)` | `x.def.iii.1` | `propX108`, `propX85`, `propX91`, …(+1) |
| 4 | `(added)` | `x.def.i.1` | `defV5_6`, `propX6`, `trip`, …(+1) |
| 3 | `x.def.3` | `(missing)` | `propX113`, `propX23`, `subjindex` |
| 3 | `guide` | `(missing)` | `propIX22`, `defV3`, `defV7` |
| 3 | `(added)` | `x.def.i.3` | `propX113`, `propX23`, `subjindex` |
| 3 | `(added)` | `perseusproject` | `aboutText`, `Euclid`, `web` |
| 3 | `(added)` | `corollary` | `propI15`, `propIII1`, `propIII16` |
| 2 | `viii.26` | `(missing)` | `propIX10`, `propX9` |
| 2 | `vi.33` | `(missing)` | `defV17_18`, `defV3` |
| 2 | `v.9` | `(missing)` | `propVI14`, `propVI3` |
| 2 | `http://aleph0.clarku.edu/~djoyce/java/elements/elements.html` | `(missing)` | `web`, `copyright` |
| 2 | `corollary` | `(missing)` | `defV11_13`, `defV14_16` |
| 2 | `cor` | `(missing)` | `propIX12`, `propIX15` |
| 2 | `bookxi` | `(missing)` | `propVI23`, `propVI31` |
| 2 | `(added)` | `x.def.i.4` | `propXIII6`, `subjindex` |
| 2 | `(added)` | `vii.33` | `defV17_18`, `defV3` |
| 2 | `(added)` | `v.def.9` | `defVII20`, `propVIII5` |
| 2 | `(added)` | `iv.15` | `propI15`, `propIII26` |
| 1 | `xiii.18` | `(missing)` | `propIII28` |
| 1 | `xii.18.cor` | `(missing)` | `propXII17` |
| 1 | `x23,cor` | `(missing)` | `propX105` |
| 1 | `x.def.4` | `(missing)` | `subjindex` |
| 1 | `x.def.2` | `(missing)` | `subjindex` |
| 1 | `x.11` | `(missing)` | `propXI34` |
| 1 | `vii.def.11,13` | `(missing)` | `propVII31` |
| 1 | `vi.def.1.thispropositionisusedintheproofofpropositionxii.12` | `(missing)` | `propVI5` |
| 1 | `vi.18.cor` | `(missing)` | `propXII17` |
| 1 | `vi.14` | `(missing)` | `propXIII8` |
| 1 | `v.def.9-10` | `(missing)` | `defVII20` |
| 1 | `v.9-10` | `(missing)` | `propVIII5` |
| 1 | `v.11` | `(missing)` | `propVI3` |
| 1 | `postulatei` | `(missing)` | `propXI3` |
| 1 | `numbers&symbols` | `(missing)` | `subjindex` |
| 1 | `ix15` | `(missing)` | `propII4` |
| 1 | `iv.15clarkuniversity` | `(missing)` | `propI15` |
| 1 | `iv,15` | `(missing)` | `propIII26` |
| 1 | `ii.4` | `(missing)` | `propVI13` |
| 1 | `i.def.3` | `(missing)` | `propXIII5` |
| 1 | `i.5` | `(missing)` | `propVI3` |
| 1 | `i.23` | `(missing)` | `defXI6_8` |
| 1 | `i.17` | `(missing)` | `propVI7` |
| 1 | `http://www.math.ubc.ca/people/faculty/cass/euclid/byrne.html` | `(missing)` | `web` |
| 1 | `http://www.claymath.org/euclids-elements-constantinople-888-ad` | `(missing)` | `web` |
| 1 | `http://farside.ph.utexas.edu/euclid/elements.pdf` | `(missing)` | `web` |
| 1 | `def.xi.25through28` | `(missing)` | `trip` |
| 1 | `def.v.5andv.6` | `(missing)` | `trip` |
| 1 | `bookv` | `(missing)` | `propVI31` |
| 1 | `(vii.def.7)` | `(missing)` | `propIX23` |
| 1 | `(added)` | `xiii.8` | `propIII28` |
| 1 | `(added)` | `xii.8.cor` | `propXII17` |
| 1 | `(added)` | `xii.4` | `propXII3` |
| 1 | `(added)` | `xi.def.25` | `trip` |
| 1 | `(added)` | `xi.11` | `propXI34` |
| 1 | `(added)` | `x.def.i.2` | `subjindex` |
| 1 | `(added)` | `x.91` | `propX54` |
| 1 | `(added)` | `x.23.cor` | `propX105` |
| 1 | `(added)` | `waybackmachine` | `web` |
| 1 | `(added)` | `viii.26converse` | `propIX10` |
| 1 | `(added)` | `viii.26(andconverse)` | `propX9` |
| 1 | `(added)` | `viii.2.cor` | `propIX15` |
| 1 | `(added)` | `vii.def.11` | `propVII31` |
| 1 | `(added)` | `vi.def.3` | `propXIII5` |
| 1 | `(added)` | `vi.8.cor` | `propXII17` |
| 1 | `(added)` | `v.def.5` | `trip` |
| 1 | `(added)` | `v.def.10` | `propVIII5` |
| 1 | `(added)` | `v.14` | `propXIII8` |
| 1 | `(added)` | `theoriginalatclarkuniversity` | `copyright` |
| 1 | `(added)` | `thegreatinternetmersenneprimesearch` | `propIX36` |
| 1 | `(added)` | `numbers&amp;symbols` | `subjindex` |
| 1 | `(added)` | `lemmabelow` | `propXI23` |
| 1 | `(added)` | `ix.15` | `propII4` |
| 1 | `(added)` | `ix.11.cor` | `propIX12` |
| 1 | `(added)` | `iv.6` | `propIV9` |
| 1 | `(added)` | `iii.16` | `propIV8` |
| 1 | `(added)` | `ii.14` | `propVI13` |
| 1 | `(added)` | `i.post.1` | `propXI3` |
| 1 | `(added)` | `i.def.23` | `defXI6_8` |
| 1 | `(added)` | `i.def.18` | `defI13_14` |
| 1 | `(added)` | `i.27` | `post5` |
| 1 | `(added)` | `https://www.euclids-elements.org/` | `web` |
| 1 | `(added)` | `https://www.c82.net/euclid/` | `web` |
| 1 | `(added)` | `https://farside.ph.utexas.edu/books/euclid/elements.pdf` | `web` |
| 1 | `(added)` | `http://www.euclides.org/` | `web` |
| 1 | `(added)` | `http://aleph0.clarku.edu/~djoyce/java/elements/toc.html` | `web` |
| 1 | `(added)` | `greenlionpress` | `web` |
| 1 | `(added)` | `github.com/brownnrl/euclid` | `copyright` |
| 1 | `(added)` | `/other-works/six-circles-eight-points/` | `copyright` |
| 1 | `(added)` | `/other-works/round-triangles/` | `copyright` |
| 1 | `(added)` | `/other-works/euler-line/` | `copyright` |
| 1 | `(added)` | `/other-works/desargues-theorem/` | `copyright` |
| 1 | `(added)` | `/other-works/compass-geometry/` | `copyright` |
| 1 | `(added)` | `/elements/` | `copyright` |
