// Euclid's Elements Lektor — JS-driven bottom navigation footer.
// Adapted from D. Joyce's original loadFooter() in header-footer.js
// (euclids-elements.org/js/). URL forms updated for this rebuild's
// /elements/books/<book>/<section>/<leaf>/ tree, and bundle-page
// labels collapsed to one entry each (defI11 = "I.Def.11-12" etc.,
// cn1 = "Common Notions").

var booktable = [
    ["bookI",    "Book I"],
    ["bookII",   "Book II"],
    ["bookIII",  "Book III"],
    ["bookIV",   "Book IV"],
    ["bookV",    "Book V"],
    ["bookVI",   "Book VI"],
    ["bookVII",  "Book VII"],
    ["bookVIII", "Book VIII"],
    ["bookIX",   "Book IX"],
    ["bookX",    "Book X"],
    ["bookXI",   "Book XI"],
    ["bookXII",  "Book XII"],
    ["bookXIII", "Book XIII"]
];

// Per-book ordered nav list. Each entry: [path-relative-to-book, label].
// Bundled definitions/common-notions are represented by a single entry
// pointing at the first member of the bundle (the URL serves the combined
// view anyway, since bundle members all re-render the group). Only Book I
// is fleshed out so far; the rest are empty placeholders.
var proptable = [
    [ // Book I
        ["definitions/defI1/",   "I.Def.1"],
        ["definitions/defI2/",   "I.Def.2"],
        ["definitions/defI3/",   "I.Def.3"],
        ["definitions/defI4/",   "I.Def.4"],
        ["definitions/defI5/",   "I.Def.5"],
        ["definitions/defI6/",   "I.Def.6"],
        ["definitions/defI7/",   "I.Def.7"],
        ["definitions/defI8/",   "I.Def.8"],
        ["definitions/defI9/",   "I.Def.9"],
        ["definitions/defI10/",  "I.Def.10"],
        ["definitions/defI11/",  "I.Def.11-12"],
        ["definitions/defI13/",  "I.Def.13-14"],
        ["definitions/defI15/",  "I.Def.15-18"],
        ["definitions/defI19/",  "I.Def.19"],
        ["definitions/defI20/",  "I.Def.20-21"],
        ["definitions/defI22/",  "I.Def.22"],
        ["definitions/defI23/",  "I.Def.23"],
        ["commonnotions/cn1/",   "Common Notions"],
        ["postulates/post1/",    "I.Post.1"],
        ["postulates/post2/",    "I.Post.2"],
        ["postulates/post3/",    "I.Post.3"],
        ["postulates/post4/",    "I.Post.4"],
        ["postulates/post5/",    "I.Post.5"],
        ["propositions/propI1/",  "I.1"],
        ["propositions/propI2/",  "I.2"],
        ["propositions/propI3/",  "I.3"],
        ["propositions/propI4/",  "I.4"],
        ["propositions/propI5/",  "I.5"],
        ["propositions/propI6/",  "I.6"],
        ["propositions/propI7/",  "I.7"],
        ["propositions/propI8/",  "I.8"],
        ["propositions/propI9/",  "I.9"],
        ["propositions/propI10/", "I.10"],
        ["propositions/propI11/", "I.11"],
        ["propositions/propI12/", "I.12"],
        ["propositions/propI13/", "I.13"],
        ["propositions/propI14/", "I.14"],
        ["propositions/propI15/", "I.15"],
        ["propositions/propI16/", "I.16"],
        ["propositions/propI17/", "I.17"],
        ["propositions/propI18/", "I.18"],
        ["propositions/propI19/", "I.19"],
        ["propositions/propI20/", "I.20"],
        ["propositions/propI21/", "I.21"],
        ["propositions/propI22/", "I.22"],
        ["propositions/propI23/", "I.23"],
        ["propositions/propI24/", "I.24"],
        ["propositions/propI25/", "I.25"],
        ["propositions/propI26/", "I.26"],
        ["propositions/propI27/", "I.27"],
        ["propositions/propI28/", "I.28"],
        ["propositions/propI29/", "I.29"],
        ["propositions/propI30/", "I.30"],
        ["propositions/propI31/", "I.31"],
        ["propositions/propI32/", "I.32"],
        ["propositions/propI33/", "I.33"],
        ["propositions/propI34/", "I.34"],
        ["propositions/propI35/", "I.35"],
        ["propositions/propI36/", "I.36"],
        ["propositions/propI37/", "I.37"],
        ["propositions/propI38/", "I.38"],
        ["propositions/propI39/", "I.39"],
        ["propositions/propI40/", "I.40"],
        ["propositions/propI41/", "I.41"],
        ["propositions/propI42/", "I.42"],
        ["propositions/propI43/", "I.43"],
        ["propositions/propI44/", "I.44"],
        ["propositions/propI45/", "I.45"],
        ["propositions/propI46/", "I.46"],
        ["propositions/propI47/", "I.47"],
        ["propositions/propI48/", "I.48"]
    ],
    [ // Book II
        ["definitions/defII1/",   "II.Def.1-2"],
        ["propositions/propII1/", "II.1"],
        ["propositions/propII2/", "II.2"],
        ["propositions/propII3/", "II.3"],
        ["propositions/propII4/", "II.4"],
        ["propositions/propII5/", "II.5"],
        ["propositions/propII6/", "II.6"],
        ["propositions/propII7/", "II.7"],
        ["propositions/propII8/", "II.8"],
        ["propositions/propII9/", "II.9"],
        ["propositions/propII10/", "II.10"],
        ["propositions/propII11/", "II.11"],
        ["propositions/propII12/", "II.12"],
        ["propositions/propII13/", "II.13"],
        ["propositions/propII14/", "II.14"]
    ],
    [ // Book III
        ["definitions/defIII1/",  "III.Def.1"],
        ["definitions/defIII2/",  "III.Def.2-3"],
        ["definitions/defIII4/",  "III.Def.4-5"],
        ["definitions/defIII6/",  "III.Def.6-9"],
        ["definitions/defIII10/", "III.Def.10"],
        ["definitions/defIII11/", "III.Def.11"],
        ["propositions/propIII1/",  "III.1"],
        ["propositions/propIII2/",  "III.2"],
        ["propositions/propIII3/",  "III.3"],
        ["propositions/propIII4/",  "III.4"],
        ["propositions/propIII5/",  "III.5"],
        ["propositions/propIII6/",  "III.6"],
        ["propositions/propIII7/",  "III.7"],
        ["propositions/propIII8/",  "III.8"],
        ["propositions/propIII9/",  "III.9"],
        ["propositions/propIII10/", "III.10"],
        ["propositions/propIII11/", "III.11"],
        ["propositions/propIII12/", "III.12"],
        ["propositions/propIII13/", "III.13"],
        ["propositions/propIII14/", "III.14"],
        ["propositions/propIII15/", "III.15"],
        ["propositions/propIII16/", "III.16"],
        ["propositions/propIII17/", "III.17"],
        ["propositions/propIII18/", "III.18"],
        ["propositions/propIII19/", "III.19"],
        ["propositions/propIII20/", "III.20"],
        ["propositions/propIII21/", "III.21"],
        ["propositions/propIII22/", "III.22"],
        ["propositions/propIII23/", "III.23"],
        ["propositions/propIII24/", "III.24"],
        ["propositions/propIII25/", "III.25"],
        ["propositions/propIII26/", "III.26"],
        ["propositions/propIII27/", "III.27"],
        ["propositions/propIII28/", "III.28"],
        ["propositions/propIII29/", "III.29"],
        ["propositions/propIII30/", "III.30"],
        ["propositions/propIII31/", "III.31"],
        ["propositions/propIII32/", "III.32"],
        ["propositions/propIII33/", "III.33"],
        ["propositions/propIII34/", "III.34"],
        ["propositions/propIII35/", "III.35"],
        ["propositions/propIII36/", "III.36"],
        ["propositions/propIII37/", "III.37"]
    ],
    [ // Book IV
        ["definitions/defIV1/",   "IV.Def.1-7"],
        ["propositions/propIV1/", "IV.1"],
        ["propositions/propIV2/", "IV.2"],
        ["propositions/propIV3/", "IV.3"],
        ["propositions/propIV4/", "IV.4"],
        ["propositions/propIV5/", "IV.5"],
        ["propositions/propIV6/", "IV.6"],
        ["propositions/propIV7/", "IV.7"],
        ["propositions/propIV8/", "IV.8"],
        ["propositions/propIV9/", "IV.9"],
        ["propositions/propIV10/", "IV.10"],
        ["propositions/propIV11/", "IV.11"],
        ["propositions/propIV12/", "IV.12"],
        ["propositions/propIV13/", "IV.13"],
        ["propositions/propIV14/", "IV.14"],
        ["propositions/propIV15/", "IV.15"],
        ["propositions/propIV16/", "IV.16"]
    ],
    [ // Book V
        ["definitions/defV1/",  "V.Def.1-2"],
        ["definitions/defV3/",  "V.Def.3"],
        ["definitions/defV4/",  "V.Def.4"],
        ["definitions/defV5/",  "V.Def.5-6"],
        ["definitions/defV7/",  "V.Def.7"],
        ["definitions/defV8/",  "V.Def.8-10"],
        ["definitions/defV11/", "V.Def.11-13"],
        ["definitions/defV14/", "V.Def.14-16"],
        ["definitions/defV17/", "V.Def.17-18"],
        ["propositions/propV1/",  "V.1"],
        ["propositions/propV2/",  "V.2"],
        ["propositions/propV3/",  "V.3"],
        ["propositions/propV4/",  "V.4"],
        ["propositions/propV5/",  "V.5"],
        ["propositions/propV6/",  "V.6"],
        ["propositions/propV7/",  "V.7"],
        ["propositions/propV8/",  "V.8"],
        ["propositions/propV9/",  "V.9"],
        ["propositions/propV10/", "V.10"],
        ["propositions/propV11/", "V.11"],
        ["propositions/propV12/", "V.12"],
        ["propositions/propV13/", "V.13"],
        ["propositions/propV14/", "V.14"],
        ["propositions/propV15/", "V.15"],
        ["propositions/propV16/", "V.16"],
        ["propositions/propV17/", "V.17"],
        ["propositions/propV18/", "V.18"],
        ["propositions/propV19/", "V.19"],
        ["propositions/propV20/", "V.20"],
        ["propositions/propV21/", "V.21"],
        ["propositions/propV22/", "V.22"],
        ["propositions/propV23/", "V.23"],
        ["propositions/propV24/", "V.24"],
        ["propositions/propV25/", "V.25"]
    ],
    [ // Book VI
        ["definitions/defVI1/", "VI.Def.1"],
        ["definitions/defVI2/", "VI.Def.2"],
        ["definitions/defVI3/", "VI.Def.3"],
        ["definitions/defVI4/", "VI.Def.4"],
        ["propositions/propVI1/",  "VI.1"],
        ["propositions/propVI2/",  "VI.2"],
        ["propositions/propVI3/",  "VI.3"],
        ["propositions/propVI4/",  "VI.4"],
        ["propositions/propVI5/",  "VI.5"],
        ["propositions/propVI6/",  "VI.6"],
        ["propositions/propVI7/",  "VI.7"],
        ["propositions/propVI8/",  "VI.8"],
        ["propositions/propVI9/",  "VI.9"],
        ["propositions/propVI10/", "VI.10"],
        ["propositions/propVI11/", "VI.11"],
        ["propositions/propVI12/", "VI.12"],
        ["propositions/propVI13/", "VI.13"],
        ["propositions/propVI14/", "VI.14"],
        ["propositions/propVI15/", "VI.15"],
        ["propositions/propVI16/", "VI.16"],
        ["propositions/propVI17/", "VI.17"],
        ["propositions/propVI18/", "VI.18"],
        ["propositions/propVI19/", "VI.19"],
        ["propositions/propVI20/", "VI.20"],
        ["propositions/propVI21/", "VI.21"],
        ["propositions/propVI22/", "VI.22"],
        ["propositions/propVI23/", "VI.23"],
        ["propositions/propVI24/", "VI.24"],
        ["propositions/propVI25/", "VI.25"],
        ["propositions/propVI26/", "VI.26"],
        ["propositions/propVI27/", "VI.27"],
        ["propositions/propVI28/", "VI.28"],
        ["propositions/propVI29/", "VI.29"],
        ["propositions/propVI30/", "VI.30"],
        ["propositions/propVI31/", "VI.31"],
        ["propositions/propVI32/", "VI.32"],
        ["propositions/propVI33/", "VI.33"]
    ],
    [ // Book VII
        ["definitions/defVII1/",  "VII.Def.1-2"],
        ["definitions/defVII3/",  "VII.Def.3-5"],
        ["definitions/defVII6/",  "VII.Def.6-10"],
        ["definitions/defVII11/", "VII.Def.11-14"],
        ["definitions/defVII15/", "VII.Def.15-19"],
        ["definitions/defVII20/", "VII.Def.20"],
        ["definitions/defVII21/", "VII.Def.21"],
        ["definitions/defVII22/", "VII.Def.22"],
        ["propositions/propVII1/",  "VII.1"],
        ["propositions/propVII2/",  "VII.2"],
        ["propositions/propVII3/",  "VII.3"],
        ["propositions/propVII4/",  "VII.4"],
        ["propositions/propVII5/",  "VII.5"],
        ["propositions/propVII6/",  "VII.6"],
        ["propositions/propVII7/",  "VII.7"],
        ["propositions/propVII8/",  "VII.8"],
        ["propositions/propVII9/",  "VII.9"],
        ["propositions/propVII10/", "VII.10"],
        ["propositions/propVII11/", "VII.11"],
        ["propositions/propVII12/", "VII.12"],
        ["propositions/propVII13/", "VII.13"],
        ["propositions/propVII14/", "VII.14"],
        ["propositions/propVII15/", "VII.15"],
        ["propositions/propVII16/", "VII.16"],
        ["propositions/propVII17/", "VII.17"],
        ["propositions/propVII18/", "VII.18"],
        ["propositions/propVII19/", "VII.19"],
        ["propositions/propVII20/", "VII.20"],
        ["propositions/propVII21/", "VII.21"],
        ["propositions/propVII22/", "VII.22"],
        ["propositions/propVII23/", "VII.23"],
        ["propositions/propVII24/", "VII.24"],
        ["propositions/propVII25/", "VII.25"],
        ["propositions/propVII26/", "VII.26"],
        ["propositions/propVII27/", "VII.27"],
        ["propositions/propVII28/", "VII.28"],
        ["propositions/propVII29/", "VII.29"],
        ["propositions/propVII30/", "VII.30"],
        ["propositions/propVII31/", "VII.31"],
        ["propositions/propVII32/", "VII.32"],
        ["propositions/propVII33/", "VII.33"],
        ["propositions/propVII34/", "VII.34"],
        ["propositions/propVII35/", "VII.35"],
        ["propositions/propVII36/", "VII.36"],
        ["propositions/propVII37/", "VII.37"],
        ["propositions/propVII38/", "VII.38"],
        ["propositions/propVII39/", "VII.39"]
    ],
    [ // Book VIII
        ["propositions/propVIII1/",  "VIII.1"],
        ["propositions/propVIII2/",  "VIII.2"],
        ["propositions/propVIII3/",  "VIII.3"],
        ["propositions/propVIII4/",  "VIII.4"],
        ["propositions/propVIII5/",  "VIII.5"],
        ["propositions/propVIII6/",  "VIII.6"],
        ["propositions/propVIII7/",  "VIII.7"],
        ["propositions/propVIII8/",  "VIII.8"],
        ["propositions/propVIII9/",  "VIII.9"],
        ["propositions/propVIII10/", "VIII.10"],
        ["propositions/propVIII11/", "VIII.11"],
        ["propositions/propVIII12/", "VIII.12"],
        ["propositions/propVIII13/", "VIII.13"],
        ["propositions/propVIII14/", "VIII.14"],
        ["propositions/propVIII15/", "VIII.15"],
        ["propositions/propVIII16/", "VIII.16"],
        ["propositions/propVIII17/", "VIII.17"],
        ["propositions/propVIII18/", "VIII.18"],
        ["propositions/propVIII19/", "VIII.19"],
        ["propositions/propVIII20/", "VIII.20"],
        ["propositions/propVIII21/", "VIII.21"],
        ["propositions/propVIII22/", "VIII.22"],
        ["propositions/propVIII23/", "VIII.23"],
        ["propositions/propVIII24/", "VIII.24"],
        ["propositions/propVIII25/", "VIII.25"],
        ["propositions/propVIII26/", "VIII.26"],
        ["propositions/propVIII27/", "VIII.27"]
    ],
    [ // Book IX
        ["propositions/propIX1/",  "IX.1"],
        ["propositions/propIX2/",  "IX.2"],
        ["propositions/propIX3/",  "IX.3"],
        ["propositions/propIX4/",  "IX.4"],
        ["propositions/propIX5/",  "IX.5"],
        ["propositions/propIX6/",  "IX.6"],
        ["propositions/propIX7/",  "IX.7"],
        ["propositions/propIX8/",  "IX.8"],
        ["propositions/propIX9/",  "IX.9"],
        ["propositions/propIX10/", "IX.10"],
        ["propositions/propIX11/", "IX.11"],
        ["propositions/propIX12/", "IX.12"],
        ["propositions/propIX13/", "IX.13"],
        ["propositions/propIX14/", "IX.14"],
        ["propositions/propIX15/", "IX.15"],
        ["propositions/propIX16/", "IX.16"],
        ["propositions/propIX17/", "IX.17"],
        ["propositions/propIX18/", "IX.18"],
        ["propositions/propIX19/", "IX.19"],
        ["propositions/propIX20/", "IX.20"],
        ["propositions/propIX21/", "IX.21"],
        ["propositions/propIX22/", "IX.22"],
        ["propositions/propIX23/", "IX.23"],
        ["propositions/propIX24/", "IX.24"],
        ["propositions/propIX25/", "IX.25"],
        ["propositions/propIX26/", "IX.26"],
        ["propositions/propIX27/", "IX.27"],
        ["propositions/propIX28/", "IX.28"],
        ["propositions/propIX29/", "IX.29"],
        ["propositions/propIX30/", "IX.30"],
        ["propositions/propIX31/", "IX.31"],
        ["propositions/propIX32/", "IX.32"],
        ["propositions/propIX33/", "IX.33"],
        ["propositions/propIX34/", "IX.34"],
        ["propositions/propIX35/", "IX.35"],
        ["propositions/propIX36/", "IX.36"]
    ],
    [], // Book X (placeholder)
    [ // Book XI
        ["definitions/defXI1/",  "XI.Def.1-2"],
        ["definitions/defXI3/",  "XI.Def.3-5"],
        ["definitions/defXI6/",  "XI.Def.6-8"],
        ["definitions/defXI9/",  "XI.Def.9-10"],
        ["definitions/defXI11/", "XI.Def.11"],
        ["definitions/defXI12/", "XI.Def.12-13"],
        ["definitions/defXI14/", "XI.Def.14-17"],
        ["definitions/defXI18/", "XI.Def.18-20"],
        ["definitions/defXI21/", "XI.Def.21-23"],
        ["definitions/defXI24/", "XI.Def.24"],
        ["definitions/defXI25/", "XI.Def.25-28"],
        ["propositions/propXI1/",  "XI.1"],
        ["propositions/propXI2/",  "XI.2"],
        ["propositions/propXI3/",  "XI.3"],
        ["propositions/propXI4/",  "XI.4"],
        ["propositions/propXI5/",  "XI.5"],
        ["propositions/propXI6/",  "XI.6"],
        ["propositions/propXI7/",  "XI.7"],
        ["propositions/propXI8/",  "XI.8"],
        ["propositions/propXI9/",  "XI.9"],
        ["propositions/propXI10/", "XI.10"],
        ["propositions/propXI11/", "XI.11"],
        ["propositions/propXI12/", "XI.12"],
        ["propositions/propXI13/", "XI.13"],
        ["propositions/propXI14/", "XI.14"],
        ["propositions/propXI15/", "XI.15"],
        ["propositions/propXI16/", "XI.16"],
        ["propositions/propXI17/", "XI.17"],
        ["propositions/propXI18/", "XI.18"],
        ["propositions/propXI19/", "XI.19"],
        ["propositions/propXI20/", "XI.20"],
        ["propositions/propXI21/", "XI.21"],
        ["propositions/propXI22/", "XI.22"],
        ["propositions/propXI23/", "XI.23"],
        ["propositions/propXI24/", "XI.24"],
        ["propositions/propXI25/", "XI.25"],
        ["propositions/propXI26/", "XI.26"],
        ["propositions/propXI27/", "XI.27"],
        ["propositions/propXI28/", "XI.28"],
        ["propositions/propXI29/", "XI.29"],
        ["propositions/propXI30/", "XI.30"],
        ["propositions/propXI31/", "XI.31"],
        ["propositions/propXI32/", "XI.32"],
        ["propositions/propXI33/", "XI.33"],
        ["propositions/propXI34/", "XI.34"],
        ["propositions/propXI35/", "XI.35"],
        ["propositions/propXI36/", "XI.36"],
        ["propositions/propXI37/", "XI.37"],
        ["propositions/propXI38/", "XI.38"],
        ["propositions/propXI39/", "XI.39"]
    ],
    [ // Book XII
        ["propositions/propXII1/",  "XII.1"],
        ["propositions/propXII2/",  "XII.2"],
        ["propositions/propXII3/",  "XII.3"],
        ["propositions/propXII4/",  "XII.4"],
        ["propositions/propXII5/",  "XII.5"],
        ["propositions/propXII6/",  "XII.6"],
        ["propositions/propXII7/",  "XII.7"],
        ["propositions/propXII8/",  "XII.8"],
        ["propositions/propXII9/",  "XII.9"],
        ["propositions/propXII10/", "XII.10"],
        ["propositions/propXII11/", "XII.11"],
        ["propositions/propXII12/", "XII.12"],
        ["propositions/propXII13/", "XII.13"],
        ["propositions/propXII14/", "XII.14"],
        ["propositions/propXII15/", "XII.15"],
        ["propositions/propXII16/", "XII.16"],
        ["propositions/propXII17/", "XII.17"],
        ["propositions/propXII18/", "XII.18"]
    ],
    [ // Book XIII
        ["propositions/propXIII1/",  "XIII.1"],
        ["propositions/propXIII2/",  "XIII.2"],
        ["propositions/propXIII3/",  "XIII.3"],
        ["propositions/propXIII4/",  "XIII.4"],
        ["propositions/propXIII5/",  "XIII.5"],
        ["propositions/propXIII6/",  "XIII.6"],
        ["propositions/propXIII7/",  "XIII.7"],
        ["propositions/propXIII8/",  "XIII.8"],
        ["propositions/propXIII9/",  "XIII.9"],
        ["propositions/propXIII10/", "XIII.10"],
        ["propositions/propXIII11/", "XIII.11"],
        ["propositions/propXIII12/", "XIII.12"],
        ["propositions/propXIII13/", "XIII.13"],
        ["propositions/propXIII14/", "XIII.14"],
        ["propositions/propXIII15/", "XIII.15"],
        ["propositions/propXIII16/", "XIII.16"],
        ["propositions/propXIII17/", "XIII.17"],
        ["propositions/propXIII18/", "XIII.18"]
    ]
];

function bookUrl(book) {
    return "/elements/books/" + booktable[book][0] + "/";
}

function propUrl(book, prop) {
    return bookUrl(book) + proptable[book][prop][0];
}

function getbook() {
    var m = window.location.pathname.match(/^\/elements\/books\/([^\/]+)\//);
    if (!m) return -1;
    for (var i = 0; i < booktable.length; i++) {
        if (booktable[i][0] === m[1]) return i;
    }
    return -1;
}

function getprop(book) {
    if (book === -1) return -1;
    var prefix = "/elements/books/" + booktable[book][0] + "/";
    var rest = window.location.pathname.substring(prefix.length);
    for (var i = 0; i < proptable[book].length; i++) {
        if (proptable[book][i][0] === rest) return i;
    }
    return -1;
}

function getBookLink(book) {
    if (book < 0 || book >= booktable.length) return '<a href="/">Introduction</a>';
    return '<a href="' + bookUrl(book) + '">' + booktable[book][1] + '</a>';
}

function getFirstPageLink(book) {
    if (!proptable[book].length) return "";
    return 'First page: <a href="' + propUrl(book, 0) + '">' + proptable[book][0][1] + '</a>';
}

function getNextProp(book, prop) {
    if (book === -1) return "";
    if (prop === -1 && proptable[book].length) {
        return 'Next: <a href="' + propUrl(book, 0) + '">' + proptable[book][0][1] + '</a>';
    }
    if (prop < proptable[book].length - 1) {
        return 'Next: <a href="' + propUrl(book, prop + 1) + '">' + proptable[book][prop + 1][1] + '</a>';
    }
    // Walk forward to the next non-empty book
    for (var b = book + 1; b < booktable.length; b++) {
        if (proptable[b].length) {
            return 'Next: <a href="' + propUrl(b, 0) + '">' + proptable[b][0][1] + '</a>';
        }
    }
    return "";
}

function getPreviousProp(book, prop) {
    if (book === -1) return "";
    if (prop === -1 && book === 0) return "";
    if (prop === -1) {
        // Previous book's first item
        for (var b = book - 1; b >= 0; b--) {
            if (proptable[b].length) {
                return 'Previous: <a href="' + propUrl(b, 0) + '">' + proptable[b][0][1] + '</a>';
            }
        }
        return "";
    }
    if (prop !== 0) {
        return 'Previous: <a href="' + propUrl(book, prop - 1) + '">' + proptable[book][prop - 1][1] + '</a>';
    }
    // Walk backward to the previous non-empty book's last entry
    for (var b = book - 1; b >= 0; b--) {
        if (proptable[b].length) {
            var last = proptable[b].length - 1;
            return 'Previous: <a href="' + propUrl(b, last) + '">' + proptable[b][last][1] + '</a>';
        }
    }
    return "";
}

function getPropForm(book) {
    var s = '<form name="PropForm" style="display:inline">';
    s += '<select name="select1" size="1" onchange="if (options[selectedIndex].value){ location = options[selectedIndex].value }">';
    s += '<option value="">Select from ' + booktable[book][1] + '</option>';
    s += '<option value="' + bookUrl(book) + '">' + booktable[book][1] + ' intro</option>';
    for (var i = 0; i < proptable[book].length; i++) {
        s += '<option value="' + propUrl(book, i) + '">' + proptable[book][i][1] + '</option>';
    }
    s += '</select></form>';
    return s;
}

function getBookForm() {
    var s = '<form name="BookForm" style="display:inline">';
    s += '<select name="select2" size="1" onchange="if (options[selectedIndex].value){ location = options[selectedIndex].value }">';
    s += '<option value="">Select book</option>';
    for (var i = 0; i < booktable.length; i++) {
        s += '<option value="' + bookUrl(i) + '">' + booktable[i][1] + '</option>';
    }
    s += '</select></form>';
    return s;
}

function getTopicForm() {
    var s = '<form name="TopicForm" style="display:inline">';
    s += '<select name="select3" size="1" onchange="if (options[selectedIndex].value){ location = options[selectedIndex].value }">';
    s += '<option value="">Select topic</option>';
    s += '<option value="/">Introduction</option>';
    s += '<option value="/elements/">Table of Contents</option>';
    s += '</select></form>';
    return s;
}

function loadFooter(copyrightDates) {
    var book = getbook();
    var prop = getprop(book);
    var t = '<hr class="footer-sep">';
    t += '<table class="footer-nav"><tbody>';
    if (book === -1) {
        // Top-level page (Intro, master TOC, etc.) — just the two general dropdowns
        t += '<tr><td>' + getTopicForm() + '</td><td>&nbsp;</td>';
        t += '<td>' + getBookForm() + '</td></tr>';
    } else if (prop === -1) {
        // Book intro page
        t += '<tr><td>' + getFirstPageLink(book) + '</td>';
        t += '<td>' + getPropForm(book) + '</td></tr>';
        t += '<tr><td>Next: ' + getBookLink(book + 1) + '</td>';
        t += '<td>' + getBookForm() + '</td></tr>';
        t += '<tr><td>Previous: ' + getBookLink(book - 1) + '</td>';
        t += '<td>' + getTopicForm() + '</td></tr>';
    } else {
        // Leaf page (def / post / cn / prop)
        t += '<tr><td>' + getNextProp(book, prop) + '</td>';
        t += '<td>' + getPropForm(book) + '</td></tr>';
        t += '<tr><td>' + getPreviousProp(book, prop) + '</td>';
        t += '<td>' + getBookForm() + '</td></tr>';
        t += '<tr><td>' + getBookLink(book) + '</td>';
        t += '<td>' + getTopicForm() + '</td></tr>';
    }
    t += '</tbody></table>';
    t += '<hr class="footer-sep">';
    t += '<p class="footer-credit"><a href="/">Home</a>';
    t += '<br>©' + copyrightDates;
    t += '<br>David E. Joyce (Professor Emeritus, <a href="https://www.clarku.edu/">Clark University</a>)';
    t += '<br><a href="https://www.euclids-elements.org/copyright.html">Copyright Notice</a>';
    t += '<br><a href="https://github.com/brownnrl/euclids-elements-lektor">Source</a></p>';
    var el = document.getElementById("footer");
    if (el) el.innerHTML = t;
}
