# Content audit — our Lektor pages vs Joyce's original HTML

Audit run over 537 pages.

- ✅ Clean (≥ 92% text similarity + no link diffs): **428**
- ⚠️  Flagged for review: **109**
- ❌ Could not fetch Joyce source: **0**

## How to read this report

- Text similarity is a token-based ratio (after stripping markdown / HTML markup, eucref shortcodes, and Joyce's header/footer chrome). 100% means every word matches in order; lower means there are insertions, deletions, or rewordings.
- Link diffs report (display text, target) tuples present on Joyce's page but missing from ours, or vice versa. Joyce's `propI5.html` is normalised to `i.5.` for comparison against our `@I.5` shortcode rendering.
- Already-catalogued intentional fixes (see [`doc/journal/mismatch-review.md`](mismatch-review.md)) will appear as link-diff entries here; cross-check before re-fixing.

## ⚠️ Pages flagged for review

### `content/elements/prematter/copyright/contents.lr` (vs `copyright.html`)

- Text similarity: **15.1%**
- Joyce link count: 1, ours: 8
- Missing in our version: 1
    - `http://aleph0.clarku.edu/~djoyce/java/elements/elements.html` → `elements`
- Added in our version: 8
    - `/elements/` → `/elements/`
    - `/other-works/compass-geometry/` → `/other-works/compass-geometry/`
    - `/other-works/desargues-theorem/` → `/other-works/desargues-theorem/`
    - `/other-works/euler-line/` → `/other-works/euler-line/`
    - `/other-works/round-triangles/` → `/other-works/round-triangles/`
    - `/other-works/six-circles-eight-points/` → `/other-works/six-circles-eight-points/`
    - `github.com/brownnrl/euclid` → `euclid`
    - `theoriginalatclarkuniversity` → `elements`
- Text differences (first 5 passages):

  - Joyce: copyright information 1996, 1997, 2002, 2013 documents
    Ours:  content of this site the textual narrative, diagrams, proposition layout, page structure,
  - Joyce: files covered this copyright notice covers all of euclid s
    Ours:  accompanying images in the following directories are david e. joyce , used by his permission: /elements/ — euclid's
  - Joyce: documents,
    Ours:  books i–xiii /other-works/compass-geometry/ — compass geometry tutorial /other-works/round-triangles/ , /other-works/six-circles-eight-points/ , /other-works/desargues-theorem/ — spherical / inversive…
  - Joyce: files served by
    Ours:  2020 for his online elements edition at clark university. nelson brown received permission in may 2026 to republish
  - Joyce: web servers in
    Ours:  content and port
  - …and 6 more passages

### `content/elements/books/bookIX/propositions/propIX35/contents.lr` (vs `bookIX/propIX35.html`)

- Text similarity: **60.9%**
- Joyce link count: 5, ours: 5
- Text differences (first 5 passages):

  - Joyce: (missing)
    Ours:  this proposition says if a sequence of numbers a 1 , a 2 , a 3 , ..., a n , a n 1 is in continued proportion a 1 : a 2 a 2 : a 3 ... a n : a n 1 then ( a 2 – a 1 ) : a 1 ( a n 1 – a 1 ) : ( a 1 a 2 ..…

### `content/elements/books/bookX/propositions/propX54/contents.lr` (vs `bookX/propX54.html`)

- Text similarity: **62.9%**
- Joyce link count: 25, ours: 25
- Added in our version: 1
    - `x.91` → `x.91`
- Text differences (first 5 passages):

  - Joyce: (missing)
    Ours:  let there be two squares ab and bc, and let them be placed so that db is in a straight line with be. then fb is also in a straight line with bg. complete the parallelogram ac. i say that ac is a squar…
  - Joyce: there be two squares ab and bc , and let them be placed so that db is in a straight line with be . then fb is also in a straight line with bg . complete the parallelogram ac . i say that ac is a squar…
    Ours:  (missing)
  - Joyce: ad .
    Ours:  ad.
  - Joyce: e ,
    Ours:  e,
  - Joyce: ae ,
    Ours:  ae,
  - …and 55 more passages

### `content/elements/books/bookX/propositions/propX20/contents.lr` (vs `bookX/propX20.html`)

- Text similarity: **64.4%**
- Joyce link count: 5, ours: 5
- Text differences (first 5 passages):

  - Joyce: ab ,
    Ours:  ab,
  - Joyce: ba .
    Ours:  ba.
  - Joyce: ab .
    Ours:  ab.
  - Joyce: ac .
    Ours:  ac.
  - Joyce: bc .
    Ours:  bc.
  - …and 5 more passages

### `content/elements/books/bookX/propositions/propX14/contents.lr` (vs `bookX/propX14.html`)

- Text similarity: **65.6%**
- Joyce link count: 13, ours: 13
- Text differences (first 5 passages):

  - Joyce: (missing)
    Ours:  let ab and c be the given two unequal straight lines, and let ab be the greater of them. it is required to find by what square the square on ab is greater than the square on c. describe the semicircle…
  - Joyce: let ab
    Ours:  if four straight lines are proportional,
  - Joyce: c be the given two unequal straight lines, and let ab be the greater of them. it is required to find by what square
    Ours:  (missing)
  - Joyce: ab
    Ours:  the first
  - Joyce: c . describe
    Ours:  (missing)
  - …and 36 more passages

### `content/elements/books/bookV/definitions/defV5_6/contents.lr` (vs `bookV/defV5.html`)

- Text similarity: **65.9%**
- Joyce link count: 9, ours: 7
- Missing in our version: 2
    - `guide` → `v.14#guide, v.def.3#guide`
    - `x.def.1` → `x.def..i`
- Added in our version: 1
    - `x.def.i.1` → `x.def.i.1`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: (missing)
    Ours:  mx, then ny mz. it is very convenient to use the shorter notation if nw mx, then ny mz. note that whenever the symbol if n bc m cd, then n abc m acd. note that in order to check this condition, it is …
  - Joyce: v.11
    Ours:  (missing)
  - Joyce: do
    Ours:  "do
  - Joyce: exist?
    Ours:  exist?"
  - …and 13 more passages

### `content/elements/prematter/Euclid/contents.lr` (vs `Euclid.html`)

- Text similarity: **69.3%**
- Joyce link count: 1, ours: 2
- Added in our version: 1
    - `perseusproject` → `/`
- Text differences (first 5 passages):

  - Joyce: euclid s
    Ours:  euclid's
  - Joyce: (missing)
    Ours:  all those who have written histories bring to this point their account of the development of this science. not long after these men came euclid, who brought together the elements, systematizing many o…
  - Joyce: euclid s
    Ours:  euclid's
  - Joyce: euclid s
    Ours:  euclid's
  - Joyce: euclid s
    Ours:  euclid's
  - …and 4 more passages

### `content/elements/prematter/web/contents.lr` (vs `web.html`)

- Text similarity: **69.7%**
- Joyce link count: 5, ours: 9
- Missing in our version: 4
    - `http://aleph0.clarku.edu/~djoyce/java/elements/elements.html` → `elements`
    - `http://farside.ph.utexas.edu/euclid/elements.pdf` → `elements.pdf`
    - `http://www.claymath.org/euclids-elements-constantinople-888-ad` → `euclids-elements-constantinople-888-ad`
    - `http://www.math.ubc.ca/people/faculty/cass/euclid/byrne.html` → `byrne`
- Added in our version: 8
    - `greenlionpress` → ``
    - `http://aleph0.clarku.edu/~djoyce/java/elements/toc.html` → `toc`
    - `http://www.euclides.org/` → `/`
    - `https://farside.ph.utexas.edu/books/euclid/elements.pdf` → `elements.pdf`
    - `https://www.c82.net/euclid/` → `/euclid/`
    - `https://www.euclids-elements.org/` → `/`
    - `perseusproject` → `/`
    - `waybackmachine` → `byrne`
- Text differences (first 5 passages):

  - Joyce: euclid s
    Ours:  euclid's
  - Joyce: (missing)
    Ours:  https://www.euclids-elements.org/ . it has been updated from dr. david e. joyce's original site at clark university, which resides at
  - Joyce: djoyce/java/elements/elements.html
    Ours:  djoyce/java/elements/toc.html
  - Joyce: heath s
    Ours:  heath's
  - Joyce: euclid s
    Ours:  euclid's
  - …and 14 more passages

### `content/elements/books/bookX/propositions/propX6/contents.lr` (vs `bookX/propX6.html`)

- Text similarity: **69.7%**
- Joyce link count: 11, ours: 11
- Missing in our version: 1
    - `x.def.1` → `x.def..i`
- Added in our version: 1
    - `x.def.i.1` → `x.def.i.1`
- Text differences (first 5 passages):

  - Joyce: e .
    Ours:  e.
  - Joyce: d ,
    Ours:  d,
  - Joyce: e .
    Ours:  e.
  - Joyce: d ,
    Ours:  d,
  - Joyce: d ,
    Ours:  d,
  - …and 21 more passages

### `content/elements/books/bookIX/propositions/propIX20/contents.lr` (vs `bookIX/propIX20.html`)

- Text similarity: **69.9%**
- Joyce link count: 3, ours: 3
- Text differences (first 5 passages):

  - Joyce: (missing)
    Ours:  this proposition states that there are more than any finite number of prime numbers, that is to say, there are infinitely many primes. outline of the proof suppose that there are n primes, a 1 , a 2 ,…

### `content/elements/books/bookX/propositions/propX23/contents.lr` (vs `bookX/propX23.html`)

- Text similarity: **71.2%**
- Joyce link count: 12, ours: 12
- Missing in our version: 1
    - `x.def.3` → `x.def..i#1`
- Added in our version: 1
    - `x.def.i.3` → `x.def.i.3`
- Text differences (first 5 passages):

  - Joyce: is medial. from this it is clear that an area commensurable with a medial area
    Ours:  (missing)
  - Joyce: a .
    Ours:  a.
  - Joyce: cd .
    Ours:  cd.
  - Joyce: a ,
    Ours:  a,
  - Joyce: cd .
    Ours:  cd.
  - …and 13 more passages

### `content/elements/books/bookVI/propositions/propVI15/contents.lr` (vs `bookVI/propVI15.html`)

- Text similarity: **71.6%**
- Joyce link count: 8, ours: 5
- Missing in our version: 1
    - `v.9` → `v.9`
- Text differences (first 5 passages):

  - Joyce: next, let the sides of the triangles abc and ade be reciprocally proportional, that is to say, let ae be to ab as ca is to ad. i say that the triangle abc equals the triangle ade. if bd is again joine…
    Ours:  (missing)
  - Joyce: vi.19
    Ours:  (missing)

### `content/elements/books/bookX/propositions/propX22/contents.lr` (vs `bookX/propX22.html`)

- Text similarity: **72.5%**
- Joyce link count: 11, ours: 11
- Text differences (first 5 passages):

  - Joyce: (missing)
    Ours:  if there are two straight lines, then the first is to the second as the square on the first is to the rectangle contained by the two straight lines. let fe and eg be two straight lines. i say that fe …
  - Joyce: fe and eg be two straight lines. i say that fe is to eg as the square on fe is to the rectangle fe by eg . describe the square df on fe , and complete gd . since then fe is to eg as fd is to dg , and …
    Ours:  (missing)
  - Joyce: bc ,
    Ours:  bc,
  - Joyce: cb .
    Ours:  cb.
  - Joyce: gf .
    Ours:  gf.
  - …and 30 more passages

### `content/elements/books/bookX/propositions/propX4/contents.lr` (vs `bookX/propX4.html`)

- Text similarity: **74.3%**
- Joyce link count: 6, ours: 6
- Text differences (first 5 passages):

  - Joyce: a , b ,
    Ours:  a, b,
  - Joyce: a , b ,
    Ours:  a, b,
  - Joyce: c .
    Ours:  c.
  - Joyce: b .
    Ours:  b.
  - Joyce: c ,
    Ours:  c,
  - …and 38 more passages

### `content/elements/books/bookVI/propositions/propVI14/contents.lr` (vs `bookVI/propVI14.html`)

- Text similarity: **76.2%**
- Joyce link count: 11, ours: 8
- Missing in our version: 1
    - `v.9` → `v.9`
- Text differences (first 5 passages):

  - Joyce: next, let db be to be as bg is to bf. i say that the parallelogram ab equals the parallelogram bc. since db is to be as bg is to bf, while db is to be as the parallelogram ab is to the parallelogram f…
    Ours:  (missing)
  - Joyce: vi.16
    Ours:  (missing)
  - Joyce: vi.30
    Ours:  (missing)
  - Joyce: x.22
    Ours:  (missing)

### `content/elements/books/bookVI/propositions/propVI16/contents.lr` (vs `bookVI/propVI16.html`)

- Text similarity: **76.2%**
- Joyce link count: 8, ours: 6
- Text differences (first 5 passages):

  - Joyce: next, let the rectangle ab by f be equal to the rectangle cd by e. i say that the four straight lines are proportional, so that ab is to cd as e is to f. with the same construction, since the rectangl…
    Ours:  (missing)
  - Joyce: vi.14
    Ours:  (missing)

### `content/elements/books/bookVI/propositions/propVI3/contents.lr` (vs `bookVI/propVI3.html`)

- Text similarity: **77.1%**
- Joyce link count: 12, ours: 7
- Missing in our version: 3
    - `i.5` → `i.5`
    - `v.11` → `v.11`
    - `v.9` → `v.9`
- Text differences (first 5 passages):

  - Joyce: next, let db be to dc as ab is to ac. join ad. i say that the straight line ad bisects the angle bac. with the same construction, since db is to dc as ab is to ac, and also db is to dc as ab is to ae,…
    Ours:  (missing)
  - Joyce: vi.2
    Ours:  (missing)

### `content/elements/books/bookX/propositions/propX9/contents.lr` (vs `bookX/propX9.html`)

- Text similarity: **79.3%**
- Joyce link count: 9, ours: 9
- Missing in our version: 1
    - `viii.26` → `viii.26`
- Added in our version: 1
    - `viii.26(andconverse)` → `viii.26 (and converse)`
- Text differences (first 5 passages):

  - Joyce: and it is clear from what has been proved that straight lines commensurable in length are always commensurable in square also, but those commensurable in square are not always also commensurable in le…
    Ours:  (missing)
  - Joyce: b ,
    Ours:  b,
  - Joyce: d .
    Ours:  d.
  - Joyce: d ,
    Ours:  d,
  - Joyce: b ,
    Ours:  b,
  - …and 28 more passages

### `content/elements/books/bookVI/propositions/propVI2/contents.lr` (vs `bookVI/propVI2.html`)

- Text similarity: **80.0%**
- Joyce link count: 13, ours: 9
- Text differences (first 5 passages):

  - Joyce: next, let the sides ab and ac of the triangle abc be cut proportionally, so that bd is to ad as ce is to ae. join de. i say that de is parallel to bc. with the same construction, since bd is to ad as …
    Ours:  (missing)
  - Joyce: vi.1
    Ours:  (missing)
  - Joyce: v.7
    Ours:  (missing)
  - Joyce: v.9
    Ours:  (missing)
  - Joyce: i.37
    Ours:  (missing)
  - …and 1 more passages

### `content/elements/books/bookX/propositions/propX17/contents.lr` (vs `bookX/propX17.html`)

- Text similarity: **80.3%**
- Joyce link count: 13, ours: 13
- Text differences (first 5 passages):

  - Joyce: (missing)
    Ours:  if to any straight line there is applied a parallelogram but falling short by a square, then the applied parallelogram equals the rectangle contained by the segments of the straight line resulting fro…
  - Joyce: apply to the straight line ab the parallelogram ad but falling short by the square db . i say that ad equals the rectangle ac by cb . this is indeed at once clear, for, since db is a square, dc equals…
    Ours:  lemma
  - Joyce: a ,
    Ours:  a,
  - Joyce: dc ,
    Ours:  dc,
  - Joyce: dc .
    Ours:  dc.
  - …and 48 more passages

### `content/elements/books/bookVI/propositions/propVI7/contents.lr` (vs `bookVI/propVI7.html`)

- Text similarity: **80.9%**
- Joyce link count: 12, ours: 9
- Missing in our version: 1
    - `i.17` → `i.17`
- Text differences (first 5 passages):

  - Joyce: next let each of the angles at c and f be supposed not less than a right angle. i say again that, in this case too, the triangle abc is equiangular with the triangle def. with the same construction, w…
    Ours:  (missing)

### `content/elements/books/bookIV/propositions/propIV15/contents.lr` (vs `bookIV/propIV15.html`)

- Text similarity: **82.3%**
- Joyce link count: 9, ours: 9
- Text differences (first 5 passages):

  - Joyce: from this it is clear that he side of the hexagon equals the radius of the circle. and, in like manner as in the case of the pentagon, if through the points of division on the circle we draw tangents …
    Ours:  (missing)
  - Joyce: guide
    Ours:  (missing)
  - Joyce: xiii.9
    Ours:  (missing)
  - Joyce: (missing)
    Ours:  from this it is clear that the side of the hexagon equals the radius of the circle. and, in like manner as in the case of the pentagon, if through the points of division on the circle we draw tangents…

### `content/elements/books/bookX/propositions/propX3/contents.lr` (vs `bookX/propX3.html`)

- Text similarity: **82.9%**
- Joyce link count: 2, ours: 2
- Text differences (first 5 passages):

  - Joyce: from this it is clear that, if a magnitude measures two magnitudes, then it also measures their greatest common measure .
    Ours:  (missing)
  - Joyce: cd .
    Ours:  cd.
  - Joyce: cd .
    Ours:  cd.
  - Joyce: ab .
    Ours:  ab.
  - Joyce: cd .
    Ours:  cd.
  - …and 26 more passages

### `content/elements/books/bookV/definitions/defV7/contents.lr` (vs `bookV/defV7.html`)

- Text similarity: **83.0%**
- Joyce link count: 5, ours: 4
- Missing in our version: 1
    - `guide` → `cn#guide`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: (missing)
    Ours:  mx, then ny mz. definition 7 now says w : x
  - Joyce: (see the guide for the common notions.)
    Ours:  (missing)
  - Joyce: (missing)
    Ours:  w : x, and w : x y : z, then u : v y : z. if u : v w : x, and w : x y : z, then u : v y : z. if u : v w : x, and w : x y : z, then u : v y : z. euclid only has the first property, which is is proposit…
  - Joyce: v.9
    Ours:  (missing)
  - …and 17 more passages

### `content/elements/books/bookV/definitions/defV14_16/contents.lr` (vs `bookV/defV14.html`)

- Text similarity: **83.5%**
- Joyce link count: 7, ours: 6
- Missing in our version: 1
    - `corollary` → `v.19#cor`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: ( u v ): v.
    Ours:  (u v):v.
  - Joyce: ( u v ): v
    Ours:  (u v):v
  - Joyce: ( u v ): v
    Ours:  (u v):v
  - Joyce: ( u v ): u.
    Ours:  (u v):u.
  - …and 16 more passages

### `content/elements/books/bookV/definitions/defV8_10/contents.lr` (vs `bookV/defV8.html`)

- Text similarity: **83.8%**
- Joyce link count: 3, ours: 3
- Text differences (first 5 passages):

  - Joyce: (missing)
    Ours:  when four magnitudes are continuously proportional, the first is said to have to the fourth the triplicate ratio of that which it has to the second, and so on continually, whatever be the proportion.
  - Joyce: when four magnitudes are continuously proportional, the first is said to have to the fourth the triplicate ratio of that which it has to the second, and so on continually, whatever be the proportion. …
    Ours:  (missing)
  - Joyce: viii ,
    Ours:  viii,
  - Joyce: viii.1
    Ours:  (missing)
  - Joyce: sequences .
    Ours:  sequences.
  - …and 1 more passages

### `content/elements/books/bookIX/propositions/propIX11/contents.lr` (vs `bookIX/propIX11.html`)

- Text similarity: **85.6%**
- Joyce link count: 1, ours: 1
- Text differences (first 5 passages):

  - Joyce: and it is clear that, whatever place the measuring number has, reckoned from the unit, the same place also has the number according to which it measures, reckoned from the number measured, in the dire…
    Ours:  (missing)
  - Joyce: guide
    Ours:  (missing)
  - Joyce: n - k
    Ours:  n-k
  - Joyce: (missing)
    Ours:  and it is clear that, whatever place the measuring number has, reckoned from the unit, the same place also has the number according to which it measures, reckoned from the number measured, in the dire…

### `content/elements/books/bookIV/propositions/propIV16/contents.lr` (vs `bookIV/propIV16.html`)

- Text similarity: **85.6%**
- Joyce link count: 9, ours: 7
- Text differences (first 5 passages):

  - Joyce: and, in like manner as in the case of the pentagon, if through the points of division on the circle we draw tangents to the circle, there will be circumscribed about the circle a fifteen-angled figure…
    Ours:  (missing)
  - Joyce: inscribe a side ac of an equilateral triangle and a side ab of an equilateral pentagon in in the circle abcd. therefore, of the equal segments of which there are fifteen in the circle abcd, there will…
    Ours:  (missing)
  - Joyce: guide
    Ours:  (missing)
  - Joyce: –1/5
    Ours:  – 1/5
  - Joyce: i.1
    Ours:  (missing)
  - …and 11 more passages

### `content/elements/prematter/trip/contents.lr` (vs `trip.html`)

- Text similarity: **87.2%**
- Joyce link count: 128, ours: 128
- Missing in our version: 3
    - `def.v.5andv.6` → `v.def.5`
    - `def.xi.25through28` → `xi.def.25`
    - `x.def.1` → `x.def..i`
- Added in our version: 3
    - `v.def.5` → `v.def.5`
    - `x.def.i.1` → `x.def.i.1`
    - `xi.def.25` → `xi.def.25`
- Text differences (first 5 passages):

  - Joyce: def. i.23
    Ours:  -
  - Joyce: post. i.5
    Ours:  -
  - Joyce: (missing)
    Ours:  -
  - Joyce: notions ,
    Ours:  notions,
  - Joyce: prop. i.1
    Ours:  -
  - …and 129 more passages

### `content/elements/books/bookXI/definitions/defXI1_2/contents.lr` (vs `bookXI/defXI1.html`)

- Text similarity: **87.6%**
- Joyce link count: 21, ours: 21
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: i.def.2
    Ours:  (missing)
  - Joyce: i.def.3
    Ours:  (missing)
  - Joyce: i.def.5
    Ours:  (missing)
  - Joyce: i.def.6
    Ours:  (missing)
  - …and 22 more passages

### `content/elements/books/bookIV/propositions/propIV5/contents.lr` (vs `bookIV/propIV5.html`)

- Text similarity: **87.9%**
- Joyce link count: 10, ours: 10
- Text differences (first 5 passages):

  - Joyce: and it is clear that when the center of the circle falls within the triangle, the angle bac, being in a segment greater than the semicircle, is less than a right angle, when the center falls on the st…
    Ours:  (missing)
  - Joyce: guide
    Ours:  (missing)
  - Joyce: iii.20
    Ours:  (missing)
  - Joyce: ac /(2 r )
    Ours:  ac/(2r)
  - Joyce: iv.10
    Ours:  (missing)
  - …and 2 more passages

### `content/elements/books/bookI/propositions/propI15/contents.lr` (vs `bookI/propI15.html`)

- Text similarity: **88.5%**
- Joyce link count: 7, ours: 8
- Missing in our version: 1
    - `iv.15clarkuniversity` → `iv.15`
- Added in our version: 2
    - `corollary` → `/elements/books/booki/propositions/i.15/#cor`
    - `iv.15` → `iv.15`
- Text differences (first 5 passages):

  - Joyce: (missing)
    Ours:  corollary. if two straight lines cut one another, then they will make the angles at the point of section equal to four right angles.
  - Joyce: guide
    Ours:  (missing)
  - Joyce: proclus s
    Ours:  proclus's
  - Joyce: ii.10
    Ours:  (missing)
  - Joyce: iv.15 clark university
    Ours:  , and a few propositions in book xi. if two straight lines cut one another, then they make the angles at the point of section equal to four right angles. from this it is manifest that, if two straight…

### `content/elements/books/bookX/propositions/propX24/contents.lr` (vs `bookX/propX24.html`)

- Text similarity: **88.8%**
- Joyce link count: 4, ours: 4
- Text differences (first 5 passages):

  - Joyce: ab .
    Ours:  ab.
  - Joyce: bc ,
    Ours:  bc,
  - Joyce: bd ,
    Ours:  bd,
  - Joyce: bc ,
    Ours:  bc,
  - Joyce: ac .
    Ours:  ac.
  - …and 15 more passages

### `content/elements/books/bookX/propositions/propX33/contents.lr` (vs `bookX/propX33.html`)

- Text similarity: **88.8%**
- Joyce link count: 16, ours: 16
- Text differences (first 5 passages):

  - Joyce: to find two straight lines incommensurable in square which make the sum of the squares on them rational but the rectangle contained by them medial.
    Ours:  (missing)
  - Joyce: ba ,
    Ours:  ba,
  - Joyce: ca ,
    Ours:  ca,
  - Joyce: ad ,
    Ours:  ad,
  - Joyce: ac ,
    Ours:  ac,
  - …and 38 more passages

### `content/elements/books/bookX/propositions/propX25/contents.lr` (vs `bookX/propX25.html`)

- Text similarity: **88.9%**
- Joyce link count: 10, ours: 10
- Text differences (first 5 passages):

  - Joyce: bc .
    Ours:  bc.
  - Joyce: fg .
    Ours:  fg.
  - Joyce: ad ,
    Ours:  ad,
  - Joyce: ac ,
    Ours:  ac,
  - Joyce: be ,
    Ours:  be,
  - …and 32 more passages

### `content/elements/books/bookV/propositions/propV19/contents.lr` (vs `bookV/propV19.html`)

- Text similarity: **89.2%**
- Joyce link count: 8, ours: 8
- Text differences (first 5 passages):

  - Joyce: from this it is manifest that, if magnitudes are proportional taken jointly, then they are also proportional in conversion. v.def.16
    Ours:  (missing)
  - Joyce: guide
    Ours:  (missing)
  - Joyce: ( u v )
    Ours:  (u v)
  - Joyce: ( x y )
    Ours:  (x y)
  - Joyce: theon s
    Ours:  theon's
  - …and 7 more passages

### `content/elements/books/bookX/propositions/propX12/contents.lr` (vs `bookX/propX12.html`)

- Text similarity: **89.3%**
- Joyce link count: 7, ours: 7
- Text differences (first 5 passages):

  - Joyce: c .
    Ours:  c.
  - Joyce: b .
    Ours:  b.
  - Joyce: c ,
    Ours:  c,
  - Joyce: e .
    Ours:  e.
  - Joyce: b ,
    Ours:  b,
  - …and 18 more passages

### `content/elements/books/bookX/propositions/propX60/contents.lr` (vs `bookX/propX60.html`)

- Text similarity: **89.3%**
- Joyce link count: 20, ours: 20
- Text differences (first 5 passages):

  - Joyce: the square on the binomial straight line applied to a rational straight line produces as breadth the first binomial.
    Ours:  (missing)
  - Joyce: c ,
    Ours:  c,
  - Joyce: cb .
    Ours:  cb.
  - Joyce: d .
    Ours:  d.
  - Joyce: c ,
    Ours:  c,
  - …and 45 more passages

### `content/elements/books/bookVI/propositions/propVI19/contents.lr` (vs `bookVI/propVI19.html`)

- Text similarity: **89.4%**
- Joyce link count: 12, ours: 12
- Text differences (first 5 passages):

  - Joyce: from this it is clear that if three straight lines are proportional, then the first is to the third as the figure described on the first is to that which is similar and similarly described on the seco…
    Ours:  (missing)
  - Joyce: guide
    Ours:  (missing)
  - Joyce: vi.22
    Ours:  (missing)
  - Joyce: vi.31
    Ours:  (missing)
  - Joyce: x.6
    Ours:  (missing)
  - …and 1 more passages

### `content/elements/books/bookI/definitions/defI6/contents.lr` (vs `bookI/defI6.html`)

- Text similarity: **89.5%**
- Joyce link count: 3, ours: 3
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: i.def.3
    Ours:  (missing)
  - Joyce: i.def.3
    Ours:  (missing)
  - Joyce: xi.def.2
    Ours:  (missing)
  - Joyce: that
    Ours:  "that
  - …and 12 more passages

### `content/elements/books/bookX/propositions/propX114/contents.lr` (vs `bookX/propX114.html`)

- Text similarity: **89.5%**
- Joyce link count: 6, ours: 6
- Text differences (first 5 passages):

  - Joyce: and it is clear by this that it is possible for a rational area to be contained by irrational straight lines
    Ours:  (missing)
  - Joyce: cd ,
    Ours:  cd,
  - Joyce: cd ,
    Ours:  cd,
  - Joyce: g .
    Ours:  g.
  - Joyce: h ,
    Ours:  h,
  - …and 14 more passages

### `content/elements/books/bookI/commonnotions/cn1_5/contents.lr` (vs `bookI/cn.html`)

- Text similarity: **89.5%**
- Joyce link count: 14, ours: 14
- Text differences (first 5 passages):

  - Joyce: 1. things which equal the same thing also equal one another. 2. if equals are added to equals, then the wholes are equal. 3. if equals are subtracted from equals, then the remainders are equal. 4. thi…
    Ours:  (missing)
  - Joyce: i.4
    Ours:  (missing)
  - Joyce: greater than.
    Ours:  "greater than."
  - Joyce: (missing)
    Ours:  property used in --- --- ---
  - Joyce: i.19
    Ours:  (missing)
  - …and 23 more passages

### `content/elements/books/bookX/propositions/propX41/contents.lr` (vs `bookX/propX41.html`)

- Text similarity: **89.7%**
- Joyce link count: 12, ours: 12
- Text differences (first 5 passages):

  - Joyce: de .
    Ours:  de.
  - Joyce: bc ,
    Ours:  bc,
  - Joyce: bc .
    Ours:  bc.
  - Joyce: ac .
    Ours:  ac.
  - Joyce: df ,
    Ours:  df,
  - …and 27 more passages

### `content/elements/books/bookX/propositions/propX55/contents.lr` (vs `bookX/propX55.html`)

- Text similarity: **89.7%**
- Joyce link count: 15, ours: 15
- Text differences (first 5 passages):

  - Joyce: ad .
    Ours:  ad.
  - Joyce: e ,
    Ours:  e,
  - Joyce: ae ,
    Ours:  ae,
  - Joyce: ab .
    Ours:  ab.
  - Joyce: f ,
    Ours:  f,
  - …and 38 more passages

### `content/elements/books/bookX/propositions/propX36/contents.lr` (vs `bookX/propX36.html`)

- Text similarity: **90.0%**
- Joyce link count: 7, ours: 7
- Text differences (first 5 passages):

  - Joyce: bc ,
    Ours:  bc,
  - Joyce: bc ,
    Ours:  bc,
  - Joyce: bc .
    Ours:  bc.
  - Joyce: bc ,
    Ours:  bc,
  - Joyce: bc ,
    Ours:  bc,
  - …and 15 more passages

### `content/elements/books/bookX/propositions/propX28/contents.lr` (vs `bookX/propX28.html`)

- Text similarity: **90.2%**
- Joyce link count: 10, ours: 10
- Text differences (first 5 passages):

  - Joyce: a , b ,
    Ours:  a, b,
  - Joyce: b .
    Ours:  b.
  - Joyce: e .
    Ours:  e.
  - Joyce: b ,
    Ours:  b,
  - Joyce: d ,
    Ours:  d,
  - …and 17 more passages

### `content/elements/books/bookX/propositions/propX94/contents.lr` (vs `bookX/propX94.html`)

- Text similarity: **90.2%**
- Joyce link count: 13, ours: 13
- Text differences (first 5 passages):

  - Joyce: ad .
    Ours:  ad.
  - Joyce: ad ,
    Ours:  ad,
  - Joyce: ag .
    Ours:  ag.
  - Joyce: ag ,
    Ours:  ag,
  - Joyce: e ,
    Ours:  e,
  - …and 37 more passages

### `content/elements/books/bookX/propositions/propX91/contents.lr` (vs `bookX/propX91.html`)

- Text similarity: **90.3%**
- Joyce link count: 18, ours: 18
- Missing in our version: 1
    - `x.def.iii.2` → `x.def..iii#1`
- Added in our version: 1
    - `x.def.iii.1` → `x.def.iii.1`
- Text differences (first 5 passages):

  - Joyce: ad .
    Ours:  ad.
  - Joyce: ag .
    Ours:  ag.
  - Joyce: e ,
    Ours:  e,
  - Joyce: fg .
    Ours:  fg.
  - Joyce: fg .
    Ours:  fg.
  - …and 40 more passages

### `content/elements/books/bookX/propositions/propX93/contents.lr` (vs `bookX/propX93.html`)

- Text similarity: **90.4%**
- Joyce link count: 23, ours: 23
- Text differences (first 5 passages):

  - Joyce: ad .
    Ours:  ad.
  - Joyce: ad .
    Ours:  ad.
  - Joyce: ag .
    Ours:  ag.
  - Joyce: ag ,
    Ours:  ag,
  - Joyce: e ,
    Ours:  e,
  - …and 49 more passages

### `content/elements/books/bookX/propositions/propX29/contents.lr` (vs `bookX/propX29.html`)

- Text similarity: **90.6%**
- Joyce link count: 18, ours: 18
- Text differences (first 5 passages):

  - Joyce: to find two square numbers such that their sum is not square. to find two rational straight lines commensurable in square only such that the square on the greater is greater than the square on the les…
    Ours:  (missing)
  - Joyce: bc ,
    Ours:  bc,
  - Joyce: d .
    Ours:  d.
  - Joyce: bd .
    Ours:  bd.
  - Joyce: bc ,
    Ours:  bc,
  - …and 77 more passages

### `content/elements/books/bookVI/propositions/propVI8/contents.lr` (vs `bookVI/propVI8.html`)

- Text similarity: **90.6%**
- Joyce link count: 13, ours: 13
- Text differences (first 5 passages):

  - Joyce: from this it is clear that, if in a right-angled triangle a perpendicular is drawn from the right angle to the base, then the straight line so drawn is a mean proportional between the segments of the …
    Ours:  (missing)
  - Joyce: guide
    Ours:  (missing)
  - Joyce: vi.4
    Ours:  (missing)
  - Joyce: vi.21
    Ours:  (missing)
  - Joyce: i.47
    Ours:  (missing)
  - …and 7 more passages

### `content/elements/books/bookX/propositions/propX98/contents.lr` (vs `bookX/propX98.html`)

- Text similarity: **90.6%**
- Joyce link count: 15, ours: 15
- Text differences (first 5 passages):

  - Joyce: ab .
    Ours:  ab.
  - Joyce: ch ,
    Ours:  ch,
  - Joyce: ag ,
    Ours:  ag,
  - Joyce: kl ,
    Ours:  kl,
  - Joyce: gb ,
    Ours:  gb,
  - …and 33 more passages

### `content/elements/books/bookX/propositions/propX44/contents.lr` (vs `bookX/propX44.html`)

- Text similarity: **90.9%**
- Joyce link count: 12, ours: 12
- Text differences (first 5 passages):

  - Joyce: c ,
    Ours:  c,
  - Joyce: (missing)
    Ours:  x.41.lemma
  - Joyce: d ,
    Ours:  d,
  - Joyce: db ,
    Ours:  db,
  - Joyce: cb .
    Ours:  cb.
  - …and 35 more passages

### `content/elements/books/bookX/propositions/propX92/contents.lr` (vs `bookX/propX92.html`)

- Text similarity: **90.9%**
- Joyce link count: 16, ours: 16
- Text differences (first 5 passages):

  - Joyce: ad .
    Ours:  ad.
  - Joyce: ad .
    Ours:  ad.
  - Joyce: ag .
    Ours:  ag.
  - Joyce: ag ,
    Ours:  ag,
  - Joyce: e ,
    Ours:  e,
  - …and 39 more passages

### `content/elements/books/bookXI/propositions/propXI33/contents.lr` (vs `bookXI/propXI33.html`)

- Text similarity: **91.0%**
- Joyce link count: 12, ours: 12
- Text differences (first 5 passages):

  - Joyce: if four straight lines are continuously proportional, then the first is to the fourth as a parallelepipedal solid on the first is to the similar and similarly situated parallelepipedal solid on the se…
    Ours:  (missing)
  - Joyce: guide
    Ours:  corollary if four straight lines are continuously proportional, then the first is to the fourth as a parallelepipedal solid on the first is to the similar and similarly situated parallelepipedal solid…
  - Joyce: xi.37
    Ours:  (missing)
  - Joyce: xii.8
    Ours:  (missing)

### `content/elements/books/bookVII/propositions/propVII32/contents.lr` (vs `bookVII/propVII32.html`)

- Text similarity: **91.0%**
- Joyce link count: 1, ours: 1
- Text differences (first 5 passages):

  - Joyce: guide after the previous proposition, this one really doesn t need to be stated at all.
    Ours:  (missing)

### `content/elements/books/bookX/propositions/propX1/contents.lr` (vs `bookX/propX1.html`)

- Text similarity: **91.2%**
- Joyce link count: 9, ours: 9
- Text differences (first 5 passages):

  - Joyce: (missing)
    Ours:  and the theorem can similarly be proven even if the parts subtracted are halves.
  - Joyce: c .
    Ours:  c. cf. v.def.4
  - Joyce: ab .
    Ours:  ab.
  - Joyce: df , fg ,
    Ours:  df, fg,
  - Joyce: c .
    Ours:  c.
  - …and 26 more passages

### `content/elements/books/bookX/propositions/propX97/contents.lr` (vs `bookX/propX97.html`)

- Text similarity: **91.2%**
- Joyce link count: 15, ours: 15
- Missing in our version: 1
    - `x.def.iii.2` → `x.def..iii#1`
- Added in our version: 1
    - `x.def.iii.1` → `x.def.iii.1`
- Text differences (first 5 passages):

  - Joyce: ab .
    Ours:  ab.
  - Joyce: ch ,
    Ours:  ch,
  - Joyce: ag ,
    Ours:  ag,
  - Joyce: kl ,
    Ours:  kl,
  - Joyce: bg .
    Ours:  bg.
  - …and 35 more passages

### `content/elements/books/bookX/propositions/propX99/contents.lr` (vs `bookX/propX99.html`)

- Text similarity: **91.2%**
- Joyce link count: 18, ours: 18
- Text differences (first 5 passages):

  - Joyce: ab ,
    Ours:  ab,
  - Joyce: ch ,
    Ours:  ch,
  - Joyce: ag ,
    Ours:  ag,
  - Joyce: kl ,
    Ours:  kl,
  - Joyce: bg ,
    Ours:  bg,
  - …and 37 more passages

### `content/elements/books/bookX/propositions/propX35/contents.lr` (vs `bookX/propX35.html`)

- Text similarity: **91.3%**
- Joyce link count: 12, ours: 12
- Text differences (first 5 passages):

  - Joyce: ab .
    Ours:  ab.
  - Joyce: ab ,
    Ours:  ab,
  - Joyce: (missing)
    Ours:  x.31 ad fin.
  - Joyce: fb ,
    Ours:  fb,
  - Joyce: db .
    Ours:  db.
  - …and 19 more passages

### `content/elements/books/bookX/propositions/propX59/contents.lr` (vs `bookX/propX59.html`)

- Text similarity: **91.3%**
- Joyce link count: 7, ours: 7
- Text differences (first 5 passages):

  - Joyce: ad ,
    Ours:  ad,
  - Joyce: e ,
    Ours:  e,
  - Joyce: ac ,
    Ours:  ac,
  - Joyce: no .
    Ours:  no.
  - Joyce: ab ,
    Ours:  ab,
  - …and 15 more passages

### `content/elements/books/bookX/propositions/propX13/contents.lr` (vs `bookX/propX13.html`)

- Text similarity: **91.4%**
- Joyce link count: 2, ours: 2
- Text differences (first 5 passages):

  - Joyce: a ,
    Ours:  a,
  - Joyce: c .
    Ours:  c.
  - Joyce: b ,
    Ours:  b,
  - Joyce: c .
    Ours:  c.
  - Joyce: c ,
    Ours:  c,
  - …and 5 more passages

### `content/elements/books/bookX/propositions/propX26/contents.lr` (vs `bookX/propX26.html`)

- Text similarity: **91.5%**
- Joyce link count: 10, ours: 10
- Text differences (first 5 passages):

  - Joyce: db .
    Ours:  db.
  - Joyce: ef .
    Ours:  ef.
  - Joyce: ac .
    Ours:  ac.
  - Joyce: kh .
    Ours:  kh.
  - Joyce: fg ,
    Ours:  fg,
  - …and 23 more passages

### `content/elements/books/bookX/propositions/propX100/contents.lr` (vs `bookX/propX100.html`)

- Text similarity: **91.6%**
- Joyce link count: 15, ours: 15
- Text differences (first 5 passages):

  - Joyce: ab .
    Ours:  ab.
  - Joyce: ch ,
    Ours:  ch,
  - Joyce: ag ,
    Ours:  ag,
  - Joyce: kl ,
    Ours:  kl,
  - Joyce: bg ,
    Ours:  bg,
  - …and 36 more passages

### `content/elements/books/bookX/propositions/propX57/contents.lr` (vs `bookX/propX57.html`)

- Text similarity: **91.6%**
- Joyce link count: 9, ours: 9
- Text differences (first 5 passages):

  - Joyce: e ,
    Ours:  e,
  - Joyce: ae ,
    Ours:  ae,
  - Joyce: ab .
    Ours:  ab.
  - Joyce: f ,
    Ours:  f,
  - Joyce: ge ,
    Ours:  ge,
  - …and 20 more passages

### `content/elements/books/bookX/propositions/propX34/contents.lr` (vs `bookX/propX34.html`)

- Text similarity: **91.7%**
- Joyce link count: 9, ours: 9
- Text differences (first 5 passages):

  - Joyce: bc ,
    Ours:  bc,
  - Joyce: ab .
    Ours:  ab. x.31 ad fin.
  - Joyce: ab .
    Ours:  ab.
  - Joyce: fb .
    Ours:  fb.
  - Joyce: fb .
    Ours:  fb.
  - …and 13 more passages

### `content/elements/books/bookX/propositions/propX38/contents.lr` (vs `bookX/propX38.html`)

- Text similarity: **91.7%**
- Joyce link count: 16, ours: 16
- Text differences (first 5 passages):

  - Joyce: de ,
    Ours:  de,
  - Joyce: ac ,
    Ours:  ac,
  - Joyce: bc ,
    Ours:  bc,
  - Joyce: eh ,
    Ours:  eh,
  - Joyce: bc ,
    Ours:  bc,
  - …and 23 more passages

### `content/elements/books/bookX/propositions/propX47/contents.lr` (vs `bookX/propX47.html`)

- Text similarity: **91.7%**
- Joyce link count: 6, ours: 6
- Text differences (first 5 passages):

  - Joyce: c ,
    Ours:  c,
  - Joyce: d ,
    Ours:  d,
  - Joyce: bd ,
    Ours:  bd,
  - Joyce: ef ,
    Ours:  ef,
  - Joyce: cb ,
    Ours:  cb,
  - …and 17 more passages

### `content/elements/books/bookX/propositions/propX102/contents.lr` (vs `bookX/propX102.html`)

- Text similarity: **92.0%**
- Joyce link count: 12, ours: 12
- Text differences (first 5 passages):

  - Joyce: ab .
    Ours:  ab.
  - Joyce: gb .
    Ours:  gb.
  - Joyce: bg .
    Ours:  bg.
  - Joyce: gb .
    Ours:  gb.
  - Joyce: cd .
    Ours:  cd.
  - …and 29 more passages

### `content/elements/books/bookIII/propositions/propIII1/contents.lr` (vs `bookIII/propIII1.html`)

- Text similarity: **92.0%**
- Joyce link count: 12, ours: 13
- Added in our version: 1
    - `corollary` → `/elements/books/bookiii/propositions/iii.1/#cor`
- Text differences (first 5 passages):

  - Joyce: from this it is clear that
    Ours:  corollary.
  - Joyce: guide
    Ours:  (missing)
  - Joyce: i.def.15
    Ours:  (missing)
  - Joyce: that s
    Ours:  that's
  - Joyce: isn t
    Ours:  isn't
  - …and 8 more passages

### `content/elements/books/bookX/propositions/propX113/contents.lr` (vs `bookX/propX113.html`)

- Text similarity: **92.4%**
- Joyce link count: 18, ours: 18
- Missing in our version: 1
    - `x.def.3` → `x.def..i#1`
- Added in our version: 1
    - `x.def.i.3` → `x.def.i.3`
- Text differences (first 5 passages):

  - Joyce: a ,
    Ours:  a,
  - Joyce: bd .
    Ours:  bd.
  - Joyce: bd .
    Ours:  bd.
  - Joyce: a .
    Ours:  a.
  - Joyce: bc ,
    Ours:  bc,
  - …and 38 more passages

### `content/elements/books/bookX/propositions/propX108/contents.lr` (vs `bookX/propX108.html`)

- Text similarity: **92.8%**
- Joyce link count: 8, ours: 8
- Missing in our version: 1
    - `x.def.iii.2` → `x.def..iii#1`
- Added in our version: 1
    - `x.def.iii.1` → `x.def.iii.1`
- Text differences (first 5 passages):

  - Joyce: (missing)
    Ours:  from a rational area
  - Joyce: subtracted from a rational area, then
    Ours:  subtracted,
  - Joyce: bc .
    Ours:  bc.
  - Joyce: fg ,
    Ours:  fg,
  - Joyce: bc ,
    Ours:  bc,
  - …and 13 more passages

### `content/elements/books/bookV/definitions/defV11_13/contents.lr` (vs `bookV/defV11.html`)

- Text similarity: **93.8%**
- Joyce link count: 5, ours: 4
- Missing in our version: 1
    - `corollary` → `v.7#cor`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: they re
    Ours:  they're
  - Joyce: they re
    Ours:  they're
  - Joyce: v.16
    Ours:  (missing)
  - Joyce: v.def.5
    Ours:  (missing)
  - …and 6 more passages

### `content/elements/books/bookX/propositions/propX105/contents.lr` (vs `bookX/propX105.html`)

- Text similarity: **95.0%**
- Joyce link count: 13, ours: 13
- Missing in our version: 1
    - `x23,cor` → `x.23#cor`
- Added in our version: 1
    - `x.23.cor` → `x.23.cor`
- Text differences (first 5 passages):

  - Joyce: ab .
    Ours:  ab.
  - Joyce: fd ,
    Ours:  fd,
  - Joyce: fd .
    Ours:  fd.
  - Joyce: fd .
    Ours:  fd.
  - Joyce: df ,
    Ours:  df,
  - …and 6 more passages

### `content/elements/books/bookX/propositions/propX85/contents.lr` (vs `bookX/propX85.html`)

- Text similarity: **95.2%**
- Joyce link count: 7, ours: 7
- Missing in our version: 1
    - `x.def.iii.2` → `x.def..iii#1`
- Added in our version: 1
    - `x.def.iii.1` → `x.def.iii.1`
- Text differences (first 5 passages):

  - Joyce: a .
    Ours:  a.
  - Joyce: ef ,
    Ours:  ef,
  - Joyce: gc .
    Ours:  gc.
  - Joyce: gc .
    Ours:  gc.
  - Joyce: gc .
    Ours:  gc.
  - …and 8 more passages

### `content/elements/books/bookI/definitions/defI13_14/contents.lr` (vs `bookI/defI13.html`)

- Text similarity: **96.8%**
- Joyce link count: 10, ours: 11
- Added in our version: 1
    - `i.def.18` → `i.def.18`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: extremity
    Ours:  "extremity"
  - Joyce: contained by.
    Ours:  "contained by."
  - Joyce: elements :
    Ours:  elements:
  - Joyce: i.def.15
    Ours:  (missing)
  - …and 17 more passages

### `content/elements/books/bookXII/propositions/propXII17/contents.lr` (vs `bookXII/propXII17.html`)

- Text similarity: **96.9%**
- Joyce link count: 27, ours: 27
- Missing in our version: 2
    - `vi.18.cor` → `vi.8#cor`
    - `xii.18.cor` → `xii.8#cor`
- Added in our version: 2
    - `vi.8.cor` → `vi.8.cor`
    - `xii.8.cor` → `xii.8.cor`
- Text differences (first 5 passages):

  - Joyce: but if in another sphere a polyhedral solid is inscribed similar to the solid in the sphere bcde, then the polyhedral solid in the sphere bcde has to the polyhedral solid in the other sphere the ratio…
    Ours:  (missing)
  - Joyce: (missing)
    Ours:  corollary but if in another sphere a polyhedral solid is inscribed similar to the solid in the sphere bcde, then the polyhedral solid in the sphere bcde has to the polyhedral solid in the other sphere…
  - Joyce: guide
    Ours:  (missing)
  - Joyce: it s
    Ours:  it's
  - Joyce: xii.18
    Ours:  (missing)

### `content/elements/books/bookIII/propositions/propIII16/contents.lr` (vs `bookIII/propIII16.html`)

- Text similarity: **97.0%**
- Joyce link count: 13, ours: 14
- Added in our version: 1
    - `corollary` → `/elements/books/bookiii/propositions/iii.16/#cor`
- Text differences (first 5 passages):

  - Joyce: (missing)
    Ours:  corollary.
  - Joyce: clear
    Ours:  manifest
  - Joyce: (missing)
    Ours:  above
  - Joyce: guide
    Ours:  (missing)
  - Joyce: i.def.8
    Ours:  (missing)
  - …and 11 more passages

### `content/elements/books/bookVII/definitions/defVII20/contents.lr` (vs `bookVII/defVII20.html`)

- Text similarity: **97.1%**
- Joyce link count: 10, ours: 10
- Missing in our version: 1
    - `v.def.9-10` → `v.def.8`
- Added in our version: 1
    - `v.def.9` → `v.def.9`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: v.def.5
    Ours:  (missing)
  - Joyce: vii.def.3
    Ours:  (missing)
  - Joyce: d .
    Ours:  d.
  - Joyce: ratio doesn t
    Ours:  "ratio" doesn't
  - …and 8 more passages

### `content/elements/books/bookIX/propositions/propIX36/contents.lr` (vs `bookIX/propIX36.html`)

- Text similarity: **97.4%**
- Joyce link count: 16, ours: 17
- Added in our version: 1
    - `thegreatinternetmersenneprimesearch` → `/`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: p -1
    Ours:  p-1
  - Joyce: s 2 p -1
    Ours:  s2 p-1
  - Joyce: p -1
    Ours:  p-1
  - Joyce: euclid s
    Ours:  euclid's
  - …and 26 more passages

### `content/elements/prematter/aboutText/contents.lr` (vs `aboutText.html`)

- Text similarity: **97.8%**
- Joyce link count: 1, ours: 2
- Added in our version: 1
    - `perseusproject` → `/`
- Text differences (first 5 passages):

  - Joyce: euclid s
    Ours:  euclid's
  - Joyce: euclid s
    Ours:  euclid's
  - Joyce: euclid s
    Ours:  euclid's
  - Joyce: ais.
    Ours:  ccedil;ais.

### `content/elements/books/bookV/definitions/defV3/contents.lr` (vs `bookV/defV3.html`)

- Text similarity: **97.9%**
- Joyce link count: 17, ours: 15
- Missing in our version: 2
    - `guide` → `cn#guide, v.def.5#guide`
    - `vi.33` → `vii.33`
- Added in our version: 1
    - `vii.33` → `vii.33`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: euclid s
    Ours:  euclid's
  - Joyce: isn t
    Ours:  isn't
  - Joyce: aren t
    Ours:  aren't
  - Joyce: that s
    Ours:  that's
  - …and 27 more passages

### `content/elements/books/bookI/postulates/post5/contents.lr` (vs `bookI/post5.html`)

- Text similarity: **98.1%**
- Joyce link count: 4, ours: 5
- Added in our version: 1
    - `i.27` → `i.27`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: that
    Ours:  "that
  - Joyce: (missing)
    Ours:  "
  - Joyce: parallel postulate
    Ours:  "parallel postulate"
  - Joyce: wasn t
    Ours:  wasn't
  - …and 1 more passages

### `content/elements/books/bookVI/propositions/propVI13/contents.lr` (vs `bookVI/propVI13.html`)

- Text similarity: **98.1%**
- Joyce link count: 8, ours: 8
- Missing in our version: 1
    - `ii.4` → `ii.14`
- Added in our version: 1
    - `ii.14` → `ii.14`
- Text differences (first 5 passages):

  - Joyce: (missing)
    Ours:  vi.8,cor
  - Joyce: guide
    Ours:  (missing)
  - Joyce: ii.4
    Ours:  (missing)
  - Joyce: vi.17
    Ours:  (missing)
  - Joyce: b .
    Ours:  b.
  - …and 3 more passages

### `content/elements/books/bookVI/propositions/propVI31/contents.lr` (vs `bookVI/propVI31.html`)

- Text similarity: **98.1%**
- Joyce link count: 9, ours: 7
- Missing in our version: 2
    - `bookv` → `bookv`
    - `bookxi` → `bookxii`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: i.47
    Ours:  (missing)
  - Joyce: hippocrates
    Ours:  hippocrates'
  - Joyce: euclid s
    Ours:  euclid's
  - Joyce: crescent )
    Ours:  crescent)
  - …and 7 more passages

### `content/elements/books/bookXI/definitions/defXI6_8/contents.lr` (vs `bookXI/defXI6.html`)

- Text similarity: **98.3%**
- Joyce link count: 3, ours: 3
- Missing in our version: 1
    - `i.23` → `i.def.23`
- Added in our version: 1
    - `i.def.23` → `i.def.23`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: i.23
    Ours:  (missing)
  - Joyce: xi.14
    Ours:  (missing)
  - Joyce: xi.3
    Ours:  (missing)
  - Joyce: don t
    Ours:  don't

### `content/elements/books/bookIX/propositions/propIX23/contents.lr` (vs `bookIX/propIX23.html`)

- Text similarity: **98.5%**
- Joyce link count: 7, ours: 7
- Missing in our version: 1
    - `(vii.def.7)` → `vii.def.6`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: vii.def.7
    Ours:  (missing)
  - Joyce: ix.29
    Ours:  (missing)
  - Joyce: ix.30
    Ours:  (missing)

### `content/elements/books/bookII/propositions/propII4/contents.lr` (vs `bookII/propII4.html`)

- Text similarity: **98.5%**
- Joyce link count: 14, ours: 14
- Missing in our version: 1
    - `ix15` → `ix.15`
- Added in our version: 1
    - `ix.15` → `ix.15`
- Text differences (first 5 passages):

  - Joyce: then
    Ours:  (missing)
  - Joyce: the sum of
    Ours:  (missing)
  - Joyce: guide
    Ours:  (missing)
  - Joyce: 2 yz.
    Ours:  2yz.
  - Joyce: ii.12
    Ours:  (missing)
  - …and 3 more passages

### `content/elements/books/bookIX/propositions/propIX15/contents.lr` (vs `bookIX/propIX15.html`)

- Text similarity: **98.5%**
- Joyce link count: 16, ours: 16
- Missing in our version: 1
    - `cor` → `viii.2#cor`
- Added in our version: 1
    - `viii.2.cor` → `viii.2.cor`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: viii.2
    Ours:  (missing)
  - Joyce: vii.28
    Ours:  (missing)
  - Joyce: vii.24
    Ours:  (missing)
  - Joyce: vii.25
    Ours:  (missing)
  - …and 6 more passages

### `content/elements/books/bookIX/propositions/propIX12/contents.lr` (vs `bookIX/propIX12.html`)

- Text similarity: **98.6%**
- Joyce link count: 19, ours: 19
- Missing in our version: 1
    - `cor` → `ix.11#cor`
- Added in our version: 1
    - `ix.11.cor` → `ix.11.cor`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: k -1
    Ours:  k-1
  - Joyce: vii.29
    Ours:  (missing)
  - Joyce: ( a
    Ours:  (a
  - Joyce: / p )
    Ours:  /p)
  - …and 4 more passages

### `content/elements/books/bookIII/propositions/propIII26/contents.lr` (vs `bookIII/propIII26.html`)

- Text similarity: **98.8%**
- Joyce link count: 7, ours: 7
- Missing in our version: 1
    - `iv,15` → `iv.15`
- Added in our version: 1
    - `iv.15` → `iv.15`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: iii.28
    Ours:  (missing)
  - Joyce: iv.11
    Ours:  (missing)
  - Joyce: iv,15
    Ours:  (missing)
  - Joyce: xiii.10
    Ours:  (missing)

### `content/elements/books/bookVIII/propositions/propVIII5/contents.lr` (vs `bookVIII/propVIII5.html`)

- Text similarity: **98.9%**
- Joyce link count: 11, ours: 12
- Missing in our version: 1
    - `v.9-10` → `v.def.8`
- Added in our version: 2
    - `v.def.10` → `v.def.10`
    - `v.def.9` → `v.def.9`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: vi.23
    Ours:  (missing)
  - Joyce: v.9-10
    Ours:  and
  - Joyce: c ,
    Ours:  c,
  - Joyce: vi.11
    Ours:  (missing)
  - …and 6 more passages

### `content/elements/books/bookXI/propositions/propXI3/contents.lr` (vs `bookXI/propXI3.html`)

- Text similarity: **99.0%**
- Joyce link count: 3, ours: 3
- Missing in our version: 1
    - `postulatei` → `i.post.1`
- Added in our version: 1
    - `i.post.1` → `i.i.post..1`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: postulate i
    Ours:  (missing)
  - Joyce: dlquoclearly
    Ours:  "clearly
  - Joyce: absurd.
    Ours:  absurd."
  - Joyce: xi.5
    Ours:  (missing)
  - …and 1 more passages

### `content/elements/books/bookVI/propositions/propVI23/contents.lr` (vs `bookVI/propVI23.html`)

- Text similarity: **99.0%**
- Joyce link count: 14, ours: 13
- Missing in our version: 1
    - `bookxi` → `bookxi`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: compounding
    Ours:  "compounding
  - Joyce: ratios.
    Ours:  ratios."
  - Joyce: quadrature,
    Ours:  "quadrature,"
  - Joyce: i.35
    Ours:  (missing)
  - …and 6 more passages

### `content/elements/books/bookXII/propositions/propXII3/contents.lr` (vs `bookXII/propXII3.html`)

- Text similarity: **99.2%**
- Joyce link count: 14, ours: 15
- Added in our version: 1
    - `xii.4` → `xii.4`
- Text differences (first 5 passages):

  - Joyce: fg .
    Ours:  fg.
  - Joyce: guide
    Ours:  (missing)
  - Joyce: xii.5
    Ours:  (missing)
  - Joyce: xi.32
    Ours:  (missing)
  - Joyce: xi.28
    Ours:  (missing)
  - …and 5 more passages

### `content/elements/books/bookV/definitions/defV17_18/contents.lr` (vs `bookV/defV17.html`)

- Text similarity: **99.2%**
- Joyce link count: 3, ours: 3
- Missing in our version: 1
    - `vi.33` → `vii.33`
- Added in our version: 1
    - `vii.33` → `vii.33`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: v.22
    Ours:  (missing)
  - Joyce: vi.33
    Ours:  (missing)
  - Joyce: v.23
    Ours:  (missing)

### `content/elements/books/bookIII/propositions/propIII28/contents.lr` (vs `bookIII/propIII28.html`)

- Text similarity: **99.3%**
- Joyce link count: 5, ours: 5
- Missing in our version: 1
    - `xiii.18` → `xiii.8`
- Added in our version: 1
    - `xiii.8` → `xiii.8`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: iii.30
    Ours:  (missing)
  - Joyce: xiii.18
    Ours:  (missing)

### `content/elements/books/bookVII/propositions/propVII31/contents.lr` (vs `bookVII/propVII31.html`)

- Text similarity: **99.3%**
- Joyce link count: 4, ours: 5
- Missing in our version: 1
    - `vii.def.11,13` → `vii.def.11`
- Added in our version: 1
    - `vii.def.11` → `vii.def.11`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: ix.13
    Ours:  (missing)
  - Joyce: ix.20
    Ours:  (missing)

### `content/elements/books/bookXI/propositions/propXI23/contents.lr` (vs `bookXI/propXI23.html`)

- Text similarity: **99.4%**
- Joyce link count: 26, ours: 26
- Added in our version: 1
    - `lemmabelow` → `#lemma`
- Text differences (first 5 passages):

  - Joyce: (missing)
    Ours:  xi.12 lemma below
  - Joyce: (missing)
    Ours:  lemma
  - Joyce: guide
    Ours:  (missing)
  - Joyce: xi.20
    Ours:  (missing)
  - Joyce: xi.21
    Ours:  (missing)
  - …and 4 more passages

### `content/elements/prematter/subjindex/contents.lr` (vs `subjindex.html`)

- Text similarity: **99.4%**
- Joyce link count: 889, ours: 890
- Missing in our version: 5
    - `numbers&symbols` → `#sym`
    - `x.def.1` → `x.def..i`
    - `x.def.2` → `x.def..i`
    - `x.def.3` → `x.def..i`
    - `x.def.4` → `x.def..i`
- Added in our version: 5
    - `numbers&amp;symbols` → `#sym`
    - `x.def.i.1` → `/elements/books/bookx/i.def.nitions/x.def..i.1/`
    - `x.def.i.2` → `/elements/books/bookx/i.def.nitions/x.def..i.2/`
    - `x.def.i.3` → `/elements/books/bookx/i.def.nitions/x.def..i.3/`
    - `x.def.i.4` → `/elements/books/bookx/i.def.nitions/x.def..i.4/`
- Text differences (first 5 passages):

  - Joyce: heron s
    Ours:  heron's
  - Joyce: carpenter s
    Ours:  carpenter's
  - Joyce: x.def.1
    Ours:  x.def.i.1
  - Joyce: x.def.2
    Ours:  x.def.i.2
  - Joyce: pacioli s
    Ours:  pacioli's
  - …and 17 more passages

### `content/elements/books/bookIX/propositions/propIX22/contents.lr` (vs `bookIX/propIX22.html`)

- Text similarity: **99.5%**
- Joyce link count: 4, ours: 3
- Missing in our version: 1
    - `guide` → `vii.def.6#guide`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: vii.def.7
    Ours:  (missing)

### `content/elements/books/bookXIII/propositions/propXIII6/contents.lr` (vs `bookXIII/propXIII6.html`)

- Text similarity: **99.6%**
- Joyce link count: 8, ours: 9
- Added in our version: 1
    - `x.def.i.4` → `x.def.i.4`
- Text differences (first 5 passages):

  - Joyce: x.def.4
    Ours:  (missing)
  - Joyce: guide
    Ours:  (missing)
  - Joyce: xiii.17
    Ours:  (missing)

### `content/elements/books/bookIV/propositions/propIV9/contents.lr` (vs `bookIV/propIV9.html`)

- Text similarity: **99.6%**
- Joyce link count: 2, ours: 3
- Added in our version: 1
    - `iv.6` → `iv.6`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: iv.6
    Ours:  (missing)

### `content/elements/books/bookXIII/propositions/propXIII5/contents.lr` (vs `bookXIII/propXIII5.html`)

- Text similarity: **99.7%**
- Joyce link count: 6, ours: 6
- Missing in our version: 1
    - `i.def.3` → `devvi3`
- Added in our version: 1
    - `vi.def.3` → `vi.def.3`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: xiii.17
    Ours:  (missing)

### `content/elements/books/bookVI/propositions/propVI5/contents.lr` (vs `bookVI/propVI5.html`)

- Text similarity: **99.7%**
- Joyce link count: 10, ours: 9
- Missing in our version: 1
    - `vi.def.1.thispropositionisusedintheproofofpropositionxii.12` → `vi.def.1`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: vi.def.1
    Ours:  (missing)
  - Joyce: xii.12
    Ours:  (missing)

### `content/elements/books/bookXI/propositions/propXI34/contents.lr` (vs `bookXI/propXI34.html`)

- Text similarity: **99.7%**
- Joyce link count: 21, ours: 21
- Missing in our version: 1
    - `x.11` → `xi.11`
- Added in our version: 1
    - `xi.11` → `xi.11`
- Text differences (first 5 passages):

  - Joyce: (missing)
    Ours:  above
  - Joyce: (missing)
    Ours:  above
  - Joyce: guide
    Ours:  (missing)
  - Joyce: xi.32
    Ours:  (missing)
  - Joyce: euclid s
    Ours:  euclid's
  - …and 1 more passages

### `content/elements/books/bookXIII/propositions/propXIII8/contents.lr` (vs `bookXIII/propXIII8.html`)

- Text similarity: **99.8%**
- Joyce link count: 11, ours: 11
- Missing in our version: 1
    - `vi.14` → `v.14`
- Added in our version: 1
    - `v.14` → `v.14`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)
  - Joyce: xiii.11
    Ours:  (missing)

### `content/elements/books/bookIV/propositions/propIV8/contents.lr` (vs `bookIV/propIV8.html`)

- Text similarity: **99.8%**
- Joyce link count: 3, ours: 4
- Added in our version: 1
    - `iii.16` → `iii.16`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)

### `content/elements/books/bookIX/propositions/propIX10/contents.lr` (vs `bookIX/propIX10.html`)

- Text similarity: **99.9%**
- Joyce link count: 5, ours: 5
- Missing in our version: 1
    - `viii.26` → `viii.26`
- Added in our version: 1
    - `viii.26converse` → `viii.26 converse`
- Text differences (first 5 passages):

  - Joyce: guide
    Ours:  (missing)

## ✅ Clean pages

- `content/elements/books/bookI/definitions/defI1/contents.lr` (96%)
- `content/elements/books/bookI/definitions/defI10/contents.lr` (99%)
- `content/elements/books/bookI/definitions/defI11_12/contents.lr` (98%)
- `content/elements/books/bookI/definitions/defI15_18/contents.lr` (96%)
- `content/elements/books/bookI/definitions/defI19/contents.lr` (96%)
- `content/elements/books/bookI/definitions/defI2/contents.lr` (97%)
- `content/elements/books/bookI/definitions/defI20_21/contents.lr` (99%)
- `content/elements/books/bookI/definitions/defI22/contents.lr` (99%)
- `content/elements/books/bookI/definitions/defI23/contents.lr` (99%)
- `content/elements/books/bookI/definitions/defI3/contents.lr` (95%)
- `content/elements/books/bookI/definitions/defI4/contents.lr` (97%)
- `content/elements/books/bookI/definitions/defI5/contents.lr` (99%)
- `content/elements/books/bookI/definitions/defI7/contents.lr` (98%)
- `content/elements/books/bookI/definitions/defI8/contents.lr` (99%)
- `content/elements/books/bookI/definitions/defI9/contents.lr` (99%)
- `content/elements/books/bookI/postulates/post1/contents.lr` (98%)
- `content/elements/books/bookI/postulates/post2/contents.lr` (98%)
- `content/elements/books/bookI/postulates/post3/contents.lr` (98%)
- `content/elements/books/bookI/postulates/post4/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI1/contents.lr` (98%)
- `content/elements/books/bookI/propositions/propI10/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI11/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI12/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI13/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI14/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI16/contents.lr` (96%)
- `content/elements/books/bookI/propositions/propI17/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI18/contents.lr` (96%)
- `content/elements/books/bookI/propositions/propI19/contents.lr` (98%)
- `content/elements/books/bookI/propositions/propI2/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI20/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI21/contents.lr` (100%)
- `content/elements/books/bookI/propositions/propI22/contents.lr` (98%)
- `content/elements/books/bookI/propositions/propI23/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI24/contents.lr` (100%)
- `content/elements/books/bookI/propositions/propI25/contents.lr` (100%)
- `content/elements/books/bookI/propositions/propI26/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI27/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI28/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI29/contents.lr` (97%)
- `content/elements/books/bookI/propositions/propI3/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI30/contents.lr` (96%)
- `content/elements/books/bookI/propositions/propI31/contents.lr` (100%)
- `content/elements/books/bookI/propositions/propI32/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI33/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI34/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI35/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI36/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI37/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI38/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI39/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI4/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI40/contents.lr` (98%)
- `content/elements/books/bookI/propositions/propI41/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI42/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI43/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI44/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI45/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI46/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI47/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI48/contents.lr` (100%)
- `content/elements/books/bookI/propositions/propI5/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI6/contents.lr` (96%)
- `content/elements/books/bookI/propositions/propI7/contents.lr` (97%)
- `content/elements/books/bookI/propositions/propI8/contents.lr` (99%)
- `content/elements/books/bookI/propositions/propI9/contents.lr` (98%)
- `content/elements/books/bookII/definitions/defII1_2/contents.lr` (96%)
- `content/elements/books/bookII/propositions/propII1/contents.lr` (98%)
- `content/elements/books/bookII/propositions/propII10/contents.lr` (99%)
- `content/elements/books/bookII/propositions/propII11/contents.lr` (99%)
- `content/elements/books/bookII/propositions/propII12/contents.lr` (99%)
- `content/elements/books/bookII/propositions/propII13/contents.lr` (100%)
- `content/elements/books/bookII/propositions/propII14/contents.lr` (98%)
- `content/elements/books/bookII/propositions/propII2/contents.lr` (99%)
- `content/elements/books/bookII/propositions/propII3/contents.lr` (98%)
- `content/elements/books/bookII/propositions/propII5/contents.lr` (98%)
- `content/elements/books/bookII/propositions/propII6/contents.lr` (97%)
- `content/elements/books/bookII/propositions/propII7/contents.lr` (99%)
- `content/elements/books/bookII/propositions/propII8/contents.lr` (99%)
- `content/elements/books/bookII/propositions/propII9/contents.lr` (98%)
- `content/elements/books/bookIII/definitions/defIII1/contents.lr` (98%)
- `content/elements/books/bookIII/definitions/defIII10/contents.lr` (98%)
- `content/elements/books/bookIII/definitions/defIII11/contents.lr` (97%)
- `content/elements/books/bookIII/definitions/defIII2_3/contents.lr` (99%)
- `content/elements/books/bookIII/definitions/defIII4_5/contents.lr` (98%)
- `content/elements/books/bookIII/definitions/defIII6_9/contents.lr` (99%)
- `content/elements/books/bookIII/propositions/propIII10/contents.lr` (99%)
- `content/elements/books/bookIII/propositions/propIII11/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII12/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII13/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII14/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII15/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII17/contents.lr` (99%)
- `content/elements/books/bookIII/propositions/propIII18/contents.lr` (99%)
- `content/elements/books/bookIII/propositions/propIII19/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII2/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII20/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII21/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII22/contents.lr` (99%)
- `content/elements/books/bookIII/propositions/propIII23/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII24/contents.lr` (99%)
- `content/elements/books/bookIII/propositions/propIII25/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII27/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII29/contents.lr` (99%)
- `content/elements/books/bookIII/propositions/propIII3/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII30/contents.lr` (99%)
- `content/elements/books/bookIII/propositions/propIII31/contents.lr` (99%)
- `content/elements/books/bookIII/propositions/propIII32/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII33/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII34/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII35/contents.lr` (99%)
- `content/elements/books/bookIII/propositions/propIII36/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII37/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII4/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII5/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII6/contents.lr` (98%)
- `content/elements/books/bookIII/propositions/propIII7/contents.lr` (99%)
- `content/elements/books/bookIII/propositions/propIII8/contents.lr` (100%)
- `content/elements/books/bookIII/propositions/propIII9/contents.lr` (99%)
- `content/elements/books/bookIV/definitions/defIV1_7/contents.lr` (99%)
- `content/elements/books/bookIV/propositions/propIV1/contents.lr` (98%)
- `content/elements/books/bookIV/propositions/propIV10/contents.lr` (99%)
- `content/elements/books/bookIV/propositions/propIV11/contents.lr` (98%)
- `content/elements/books/bookIV/propositions/propIV12/contents.lr` (99%)
- `content/elements/books/bookIV/propositions/propIV13/contents.lr` (99%)
- `content/elements/books/bookIV/propositions/propIV14/contents.lr` (98%)
- `content/elements/books/bookIV/propositions/propIV2/contents.lr` (96%)
- `content/elements/books/bookIV/propositions/propIV3/contents.lr` (98%)
- `content/elements/books/bookIV/propositions/propIV4/contents.lr` (95%)
- `content/elements/books/bookIV/propositions/propIV6/contents.lr` (100%)
- `content/elements/books/bookIV/propositions/propIV7/contents.lr` (99%)
- `content/elements/books/bookIX/propositions/propIX1/contents.lr` (98%)
- `content/elements/books/bookIX/propositions/propIX13/contents.lr` (99%)
- `content/elements/books/bookIX/propositions/propIX14/contents.lr` (99%)
- `content/elements/books/bookIX/propositions/propIX16/contents.lr` (99%)
- `content/elements/books/bookIX/propositions/propIX17/contents.lr` (99%)
- `content/elements/books/bookIX/propositions/propIX18/contents.lr` (99%)
- `content/elements/books/bookIX/propositions/propIX19/contents.lr` (97%)
- `content/elements/books/bookIX/propositions/propIX2/contents.lr` (98%)
- `content/elements/books/bookIX/propositions/propIX21/contents.lr` (99%)
- `content/elements/books/bookIX/propositions/propIX24/contents.lr` (99%)
- `content/elements/books/bookIX/propositions/propIX25/contents.lr` (100%)
- `content/elements/books/bookIX/propositions/propIX26/contents.lr` (99%)
- `content/elements/books/bookIX/propositions/propIX27/contents.lr` (99%)
- `content/elements/books/bookIX/propositions/propIX28/contents.lr` (99%)
- `content/elements/books/bookIX/propositions/propIX29/contents.lr` (100%)
- `content/elements/books/bookIX/propositions/propIX3/contents.lr` (99%)
- `content/elements/books/bookIX/propositions/propIX30/contents.lr` (100%)
- `content/elements/books/bookIX/propositions/propIX31/contents.lr` (96%)
- `content/elements/books/bookIX/propositions/propIX32/contents.lr` (99%)
- `content/elements/books/bookIX/propositions/propIX33/contents.lr` (99%)
- `content/elements/books/bookIX/propositions/propIX34/contents.lr` (98%)
- `content/elements/books/bookIX/propositions/propIX4/contents.lr` (98%)
- `content/elements/books/bookIX/propositions/propIX5/contents.lr` (100%)
- `content/elements/books/bookIX/propositions/propIX6/contents.lr` (99%)
- `content/elements/books/bookIX/propositions/propIX7/contents.lr` (98%)
- `content/elements/books/bookIX/propositions/propIX8/contents.lr` (100%)
- `content/elements/books/bookIX/propositions/propIX9/contents.lr` (100%)
- `content/elements/books/bookV/definitions/defV1_2/contents.lr` (100%)
- `content/elements/books/bookV/definitions/defV4/contents.lr` (98%)
- `content/elements/books/bookV/propositions/propV1/contents.lr` (99%)
- `content/elements/books/bookV/propositions/propV10/contents.lr` (96%)
- `content/elements/books/bookV/propositions/propV11/contents.lr` (97%)
- `content/elements/books/bookV/propositions/propV12/contents.lr` (98%)
- `content/elements/books/bookV/propositions/propV13/contents.lr` (99%)
- `content/elements/books/bookV/propositions/propV14/contents.lr` (94%)
- `content/elements/books/bookV/propositions/propV15/contents.lr` (100%)
- `content/elements/books/bookV/propositions/propV16/contents.lr` (97%)
- `content/elements/books/bookV/propositions/propV17/contents.lr` (98%)
- `content/elements/books/bookV/propositions/propV18/contents.lr` (93%)
- `content/elements/books/bookV/propositions/propV2/contents.lr` (99%)
- `content/elements/books/bookV/propositions/propV20/contents.lr` (98%)
- `content/elements/books/bookV/propositions/propV21/contents.lr` (98%)
- `content/elements/books/bookV/propositions/propV22/contents.lr` (99%)
- `content/elements/books/bookV/propositions/propV23/contents.lr` (98%)
- `content/elements/books/bookV/propositions/propV24/contents.lr` (94%)
- `content/elements/books/bookV/propositions/propV25/contents.lr` (94%)
- `content/elements/books/bookV/propositions/propV3/contents.lr` (99%)
- `content/elements/books/bookV/propositions/propV4/contents.lr` (93%)
- `content/elements/books/bookV/propositions/propV5/contents.lr` (98%)
- `content/elements/books/bookV/propositions/propV6/contents.lr` (98%)
- `content/elements/books/bookV/propositions/propV7/contents.lr` (93%)
- `content/elements/books/bookV/propositions/propV8/contents.lr` (95%)
- `content/elements/books/bookV/propositions/propV9/contents.lr` (98%)
- `content/elements/books/bookVI/definitions/defVI1/contents.lr` (97%)
- `content/elements/books/bookVI/definitions/defVI2/contents.lr` (95%)
- `content/elements/books/bookVI/definitions/defVI3/contents.lr` (98%)
- `content/elements/books/bookVI/definitions/defVI4/contents.lr` (98%)
- `content/elements/books/bookVI/propositions/propVI1/contents.lr` (95%)
- `content/elements/books/bookVI/propositions/propVI10/contents.lr` (99%)
- `content/elements/books/bookVI/propositions/propVI11/contents.lr` (99%)
- `content/elements/books/bookVI/propositions/propVI12/contents.lr` (98%)
- `content/elements/books/bookVI/propositions/propVI17/contents.lr` (100%)
- `content/elements/books/bookVI/propositions/propVI18/contents.lr` (99%)
- `content/elements/books/bookVI/propositions/propVI20/contents.lr` (95%)
- `content/elements/books/bookVI/propositions/propVI21/contents.lr` (98%)
- `content/elements/books/bookVI/propositions/propVI22/contents.lr` (100%)
- `content/elements/books/bookVI/propositions/propVI24/contents.lr` (99%)
- `content/elements/books/bookVI/propositions/propVI25/contents.lr` (100%)
- `content/elements/books/bookVI/propositions/propVI26/contents.lr` (100%)
- `content/elements/books/bookVI/propositions/propVI27/contents.lr` (100%)
- `content/elements/books/bookVI/propositions/propVI28/contents.lr` (100%)
- `content/elements/books/bookVI/propositions/propVI29/contents.lr` (99%)
- `content/elements/books/bookVI/propositions/propVI30/contents.lr` (98%)
- `content/elements/books/bookVI/propositions/propVI32/contents.lr` (100%)
- `content/elements/books/bookVI/propositions/propVI33/contents.lr` (99%)
- `content/elements/books/bookVI/propositions/propVI4/contents.lr` (99%)
- `content/elements/books/bookVI/propositions/propVI6/contents.lr` (99%)
- `content/elements/books/bookVI/propositions/propVI9/contents.lr` (96%)
- `content/elements/books/bookVII/definitions/defVII11_14/contents.lr` (95%)
- `content/elements/books/bookVII/definitions/defVII15_19/contents.lr` (94%)
- `content/elements/books/bookVII/definitions/defVII1_2/contents.lr` (97%)
- `content/elements/books/bookVII/definitions/defVII21/contents.lr` (99%)
- `content/elements/books/bookVII/definitions/defVII22/contents.lr` (99%)
- `content/elements/books/bookVII/definitions/defVII3_5/contents.lr` (93%)
- `content/elements/books/bookVII/definitions/defVII6_10/contents.lr` (95%)
- `content/elements/books/bookVII/propositions/propVII1/contents.lr` (97%)
- `content/elements/books/bookVII/propositions/propVII10/contents.lr` (96%)
- `content/elements/books/bookVII/propositions/propVII11/contents.lr` (99%)
- `content/elements/books/bookVII/propositions/propVII12/contents.lr` (99%)
- `content/elements/books/bookVII/propositions/propVII13/contents.lr` (99%)
- `content/elements/books/bookVII/propositions/propVII14/contents.lr` (99%)
- `content/elements/books/bookVII/propositions/propVII15/contents.lr` (97%)
- `content/elements/books/bookVII/propositions/propVII16/contents.lr` (96%)
- `content/elements/books/bookVII/propositions/propVII17/contents.lr` (100%)
- `content/elements/books/bookVII/propositions/propVII18/contents.lr` (99%)
- `content/elements/books/bookVII/propositions/propVII19/contents.lr` (99%)
- `content/elements/books/bookVII/propositions/propVII2/contents.lr` (95%)
- `content/elements/books/bookVII/propositions/propVII20/contents.lr` (98%)
- `content/elements/books/bookVII/propositions/propVII21/contents.lr` (100%)
- `content/elements/books/bookVII/propositions/propVII22/contents.lr` (99%)
- `content/elements/books/bookVII/propositions/propVII23/contents.lr` (100%)
- `content/elements/books/bookVII/propositions/propVII24/contents.lr` (99%)
- `content/elements/books/bookVII/propositions/propVII25/contents.lr` (97%)
- `content/elements/books/bookVII/propositions/propVII26/contents.lr` (99%)
- `content/elements/books/bookVII/propositions/propVII27/contents.lr` (99%)
- `content/elements/books/bookVII/propositions/propVII28/contents.lr` (100%)
- `content/elements/books/bookVII/propositions/propVII29/contents.lr` (99%)
- `content/elements/books/bookVII/propositions/propVII3/contents.lr` (96%)
- `content/elements/books/bookVII/propositions/propVII30/contents.lr` (98%)
- `content/elements/books/bookVII/propositions/propVII33/contents.lr` (97%)
- `content/elements/books/bookVII/propositions/propVII34/contents.lr` (99%)
- `content/elements/books/bookVII/propositions/propVII35/contents.lr` (99%)
- `content/elements/books/bookVII/propositions/propVII36/contents.lr` (99%)
- `content/elements/books/bookVII/propositions/propVII37/contents.lr` (98%)
- `content/elements/books/bookVII/propositions/propVII38/contents.lr` (99%)
- `content/elements/books/bookVII/propositions/propVII39/contents.lr` (100%)
- `content/elements/books/bookVII/propositions/propVII4/contents.lr` (95%)
- `content/elements/books/bookVII/propositions/propVII5/contents.lr` (95%)
- `content/elements/books/bookVII/propositions/propVII6/contents.lr` (97%)
- `content/elements/books/bookVII/propositions/propVII7/contents.lr` (100%)
- `content/elements/books/bookVII/propositions/propVII8/contents.lr` (100%)
- `content/elements/books/bookVII/propositions/propVII9/contents.lr` (98%)
- `content/elements/books/bookVIII/propositions/propVIII1/contents.lr` (99%)
- `content/elements/books/bookVIII/propositions/propVIII10/contents.lr` (99%)
- `content/elements/books/bookVIII/propositions/propVIII11/contents.lr` (99%)
- `content/elements/books/bookVIII/propositions/propVIII12/contents.lr` (100%)
- `content/elements/books/bookVIII/propositions/propVIII13/contents.lr` (100%)
- `content/elements/books/bookVIII/propositions/propVIII14/contents.lr` (98%)
- `content/elements/books/bookVIII/propositions/propVIII15/contents.lr` (100%)
- `content/elements/books/bookVIII/propositions/propVIII16/contents.lr` (99%)
- `content/elements/books/bookVIII/propositions/propVIII17/contents.lr` (95%)
- `content/elements/books/bookVIII/propositions/propVIII18/contents.lr` (100%)
- `content/elements/books/bookVIII/propositions/propVIII19/contents.lr` (100%)
- `content/elements/books/bookVIII/propositions/propVIII2/contents.lr` (93%)
- `content/elements/books/bookVIII/propositions/propVIII20/contents.lr` (98%)
- `content/elements/books/bookVIII/propositions/propVIII21/contents.lr` (100%)
- `content/elements/books/bookVIII/propositions/propVIII22/contents.lr` (99%)
- `content/elements/books/bookVIII/propositions/propVIII23/contents.lr` (99%)
- `content/elements/books/bookVIII/propositions/propVIII24/contents.lr` (100%)
- `content/elements/books/bookVIII/propositions/propVIII25/contents.lr` (100%)
- `content/elements/books/bookVIII/propositions/propVIII26/contents.lr` (99%)
- `content/elements/books/bookVIII/propositions/propVIII27/contents.lr` (100%)
- `content/elements/books/bookVIII/propositions/propVIII3/contents.lr` (99%)
- `content/elements/books/bookVIII/propositions/propVIII4/contents.lr` (98%)
- `content/elements/books/bookVIII/propositions/propVIII6/contents.lr` (99%)
- `content/elements/books/bookVIII/propositions/propVIII7/contents.lr` (99%)
- `content/elements/books/bookVIII/propositions/propVIII8/contents.lr` (99%)
- `content/elements/books/bookVIII/propositions/propVIII9/contents.lr` (99%)
- `content/elements/books/bookX/definitions/defX.I/contents.lr` (97%)
- `content/elements/books/bookX/definitions/defX.II/contents.lr` (97%)
- `content/elements/books/bookX/definitions/defX.III/contents.lr` (97%)
- `content/elements/books/bookX/propositions/propX10/contents.lr` (95%)
- `content/elements/books/bookX/propositions/propX101/contents.lr` (93%)
- `content/elements/books/bookX/propositions/propX103/contents.lr` (93%)
- `content/elements/books/bookX/propositions/propX104/contents.lr` (94%)
- `content/elements/books/bookX/propositions/propX106/contents.lr` (96%)
- `content/elements/books/bookX/propositions/propX107/contents.lr` (97%)
- `content/elements/books/bookX/propositions/propX109/contents.lr` (95%)
- `content/elements/books/bookX/propositions/propX11/contents.lr` (92%)
- `content/elements/books/bookX/propositions/propX110/contents.lr` (93%)
- `content/elements/books/bookX/propositions/propX111/contents.lr` (93%)
- `content/elements/books/bookX/propositions/propX112/contents.lr` (94%)
- `content/elements/books/bookX/propositions/propX115/contents.lr` (97%)
- `content/elements/books/bookX/propositions/propX15/contents.lr` (92%)
- `content/elements/books/bookX/propositions/propX16/contents.lr` (93%)
- `content/elements/books/bookX/propositions/propX18/contents.lr` (95%)
- `content/elements/books/bookX/propositions/propX19/contents.lr` (94%)
- `content/elements/books/bookX/propositions/propX2/contents.lr` (99%)
- `content/elements/books/bookX/propositions/propX21/contents.lr` (92%)
- `content/elements/books/bookX/propositions/propX27/contents.lr` (93%)
- `content/elements/books/bookX/propositions/propX30/contents.lr` (95%)
- `content/elements/books/bookX/propositions/propX31/contents.lr` (93%)
- `content/elements/books/bookX/propositions/propX32/contents.lr` (94%)
- `content/elements/books/bookX/propositions/propX37/contents.lr` (94%)
- `content/elements/books/bookX/propositions/propX39/contents.lr` (95%)
- `content/elements/books/bookX/propositions/propX40/contents.lr` (97%)
- `content/elements/books/bookX/propositions/propX42/contents.lr` (96%)
- `content/elements/books/bookX/propositions/propX43/contents.lr` (97%)
- `content/elements/books/bookX/propositions/propX45/contents.lr` (97%)
- `content/elements/books/bookX/propositions/propX46/contents.lr` (98%)
- `content/elements/books/bookX/propositions/propX48/contents.lr` (95%)
- `content/elements/books/bookX/propositions/propX49/contents.lr` (94%)
- `content/elements/books/bookX/propositions/propX5/contents.lr` (94%)
- `content/elements/books/bookX/propositions/propX50/contents.lr` (95%)
- `content/elements/books/bookX/propositions/propX51/contents.lr` (94%)
- `content/elements/books/bookX/propositions/propX52/contents.lr` (95%)
- `content/elements/books/bookX/propositions/propX53/contents.lr` (95%)
- `content/elements/books/bookX/propositions/propX56/contents.lr` (94%)
- `content/elements/books/bookX/propositions/propX58/contents.lr` (92%)
- `content/elements/books/bookX/propositions/propX61/contents.lr` (93%)
- `content/elements/books/bookX/propositions/propX62/contents.lr` (93%)
- `content/elements/books/bookX/propositions/propX63/contents.lr` (95%)
- `content/elements/books/bookX/propositions/propX64/contents.lr` (94%)
- `content/elements/books/bookX/propositions/propX65/contents.lr` (95%)
- `content/elements/books/bookX/propositions/propX66/contents.lr` (96%)
- `content/elements/books/bookX/propositions/propX67/contents.lr` (94%)
- `content/elements/books/bookX/propositions/propX68/contents.lr` (94%)
- `content/elements/books/bookX/propositions/propX69/contents.lr` (97%)
- `content/elements/books/bookX/propositions/propX7/contents.lr` (98%)
- `content/elements/books/bookX/propositions/propX70/contents.lr` (96%)
- `content/elements/books/bookX/propositions/propX71/contents.lr` (96%)
- `content/elements/books/bookX/propositions/propX72/contents.lr` (93%)
- `content/elements/books/bookX/propositions/propX73/contents.lr` (94%)
- `content/elements/books/bookX/propositions/propX74/contents.lr` (97%)
- `content/elements/books/bookX/propositions/propX75/contents.lr` (93%)
- `content/elements/books/bookX/propositions/propX76/contents.lr` (98%)
- `content/elements/books/bookX/propositions/propX77/contents.lr` (97%)
- `content/elements/books/bookX/propositions/propX78/contents.lr` (93%)
- `content/elements/books/bookX/propositions/propX79/contents.lr` (98%)
- `content/elements/books/bookX/propositions/propX8/contents.lr` (99%)
- `content/elements/books/bookX/propositions/propX80/contents.lr` (98%)
- `content/elements/books/bookX/propositions/propX81/contents.lr` (92%)
- `content/elements/books/bookX/propositions/propX82/contents.lr` (98%)
- `content/elements/books/bookX/propositions/propX83/contents.lr` (98%)
- `content/elements/books/bookX/propositions/propX84/contents.lr` (94%)
- `content/elements/books/bookX/propositions/propX86/contents.lr` (94%)
- `content/elements/books/bookX/propositions/propX87/contents.lr` (95%)
- `content/elements/books/bookX/propositions/propX88/contents.lr` (95%)
- `content/elements/books/bookX/propositions/propX89/contents.lr` (95%)
- `content/elements/books/bookX/propositions/propX90/contents.lr` (95%)
- `content/elements/books/bookX/propositions/propX95/contents.lr` (95%)
- `content/elements/books/bookX/propositions/propX96/contents.lr` (94%)
- `content/elements/books/bookXI/definitions/defXI11/contents.lr` (99%)
- `content/elements/books/bookXI/definitions/defXI12_13/contents.lr` (95%)
- `content/elements/books/bookXI/definitions/defXI14_17/contents.lr` (98%)
- `content/elements/books/bookXI/definitions/defXI18_20/contents.lr` (96%)
- `content/elements/books/bookXI/definitions/defXI21_23/contents.lr` (96%)
- `content/elements/books/bookXI/definitions/defXI24/contents.lr` (100%)
- `content/elements/books/bookXI/definitions/defXI25_28/contents.lr` (95%)
- `content/elements/books/bookXI/definitions/defXI3_5/contents.lr` (99%)
- `content/elements/books/bookXI/definitions/defXI9_10/contents.lr` (94%)
- `content/elements/books/bookXI/propositions/propXI1/contents.lr` (98%)
- `content/elements/books/bookXI/propositions/propXI10/contents.lr` (99%)
- `content/elements/books/bookXI/propositions/propXI11/contents.lr` (95%)
- `content/elements/books/bookXI/propositions/propXI12/contents.lr` (100%)
- `content/elements/books/bookXI/propositions/propXI13/contents.lr` (99%)
- `content/elements/books/bookXI/propositions/propXI14/contents.lr` (98%)
- `content/elements/books/bookXI/propositions/propXI15/contents.lr` (100%)
- `content/elements/books/bookXI/propositions/propXI16/contents.lr` (100%)
- `content/elements/books/bookXI/propositions/propXI17/contents.lr` (100%)
- `content/elements/books/bookXI/propositions/propXI18/contents.lr` (100%)
- `content/elements/books/bookXI/propositions/propXI19/contents.lr` (100%)
- `content/elements/books/bookXI/propositions/propXI2/contents.lr` (99%)
- `content/elements/books/bookXI/propositions/propXI20/contents.lr` (99%)
- `content/elements/books/bookXI/propositions/propXI21/contents.lr` (99%)
- `content/elements/books/bookXI/propositions/propXI22/contents.lr` (100%)
- `content/elements/books/bookXI/propositions/propXI24/contents.lr` (99%)
- `content/elements/books/bookXI/propositions/propXI25/contents.lr` (95%)
- `content/elements/books/bookXI/propositions/propXI26/contents.lr` (100%)
- `content/elements/books/bookXI/propositions/propXI27/contents.lr` (100%)
- `content/elements/books/bookXI/propositions/propXI28/contents.lr` (99%)
- `content/elements/books/bookXI/propositions/propXI29/contents.lr` (100%)
- `content/elements/books/bookXI/propositions/propXI30/contents.lr` (100%)
- `content/elements/books/bookXI/propositions/propXI31/contents.lr` (100%)
- `content/elements/books/bookXI/propositions/propXI32/contents.lr` (98%)
- `content/elements/books/bookXI/propositions/propXI35/contents.lr` (94%)
- `content/elements/books/bookXI/propositions/propXI36/contents.lr` (100%)
- `content/elements/books/bookXI/propositions/propXI37/contents.lr` (100%)
- `content/elements/books/bookXI/propositions/propXI38/contents.lr` (100%)
- `content/elements/books/bookXI/propositions/propXI39/contents.lr` (99%)
- `content/elements/books/bookXI/propositions/propXI4/contents.lr` (100%)
- `content/elements/books/bookXI/propositions/propXI5/contents.lr` (100%)
- `content/elements/books/bookXI/propositions/propXI6/contents.lr` (99%)
- `content/elements/books/bookXI/propositions/propXI7/contents.lr` (99%)
- `content/elements/books/bookXI/propositions/propXI8/contents.lr` (100%)
- `content/elements/books/bookXI/propositions/propXI9/contents.lr` (100%)
- `content/elements/books/bookXII/propositions/propXII1/contents.lr` (100%)
- `content/elements/books/bookXII/propositions/propXII10/contents.lr` (100%)
- `content/elements/books/bookXII/propositions/propXII11/contents.lr` (100%)
- `content/elements/books/bookXII/propositions/propXII12/contents.lr` (100%)
- `content/elements/books/bookXII/propositions/propXII13/contents.lr` (99%)
- `content/elements/books/bookXII/propositions/propXII14/contents.lr` (100%)
- `content/elements/books/bookXII/propositions/propXII15/contents.lr` (100%)
- `content/elements/books/bookXII/propositions/propXII16/contents.lr` (100%)
- `content/elements/books/bookXII/propositions/propXII18/contents.lr` (99%)
- `content/elements/books/bookXII/propositions/propXII2/contents.lr` (98%)
- `content/elements/books/bookXII/propositions/propXII4/contents.lr` (100%)
- `content/elements/books/bookXII/propositions/propXII5/contents.lr` (100%)
- `content/elements/books/bookXII/propositions/propXII6/contents.lr` (100%)
- `content/elements/books/bookXII/propositions/propXII7/contents.lr` (95%)
- `content/elements/books/bookXII/propositions/propXII8/contents.lr` (96%)
- `content/elements/books/bookXII/propositions/propXII9/contents.lr` (100%)
- `content/elements/books/bookXIII/propositions/propXIII1/contents.lr` (99%)
- `content/elements/books/bookXIII/propositions/propXIII10/contents.lr` (99%)
- `content/elements/books/bookXIII/propositions/propXIII11/contents.lr` (100%)
- `content/elements/books/bookXIII/propositions/propXIII12/contents.lr` (100%)
- `content/elements/books/bookXIII/propositions/propXIII13/contents.lr` (99%)
- `content/elements/books/bookXIII/propositions/propXIII14/contents.lr` (99%)
- `content/elements/books/bookXIII/propositions/propXIII15/contents.lr` (100%)
- `content/elements/books/bookXIII/propositions/propXIII16/contents.lr` (96%)
- `content/elements/books/bookXIII/propositions/propXIII17/contents.lr` (98%)
- `content/elements/books/bookXIII/propositions/propXIII18/contents.lr` (98%)
- `content/elements/books/bookXIII/propositions/propXIII2/contents.lr` (100%)
- `content/elements/books/bookXIII/propositions/propXIII3/contents.lr` (100%)
- `content/elements/books/bookXIII/propositions/propXIII4/contents.lr` (100%)
- `content/elements/books/bookXIII/propositions/propXIII7/contents.lr` (100%)
- `content/elements/books/bookXIII/propositions/propXIII9/contents.lr` (100%)

