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
    [], [], [], [], [], [], [], [], [], [] // Books IV-XIII (placeholders)
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
