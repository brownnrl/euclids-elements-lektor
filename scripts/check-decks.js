#!/usr/bin/env node
// Prototype of the lektor-side deck checker.
//
// Runs each proposition page's inline <script> in a vm sandbox with the REAL
// geomlib bundle loaded, so aliases, param parsing and #154's init-time deck
// validation all apply exactly as they do in a browser. No regex guessing:
// decks compose `visible` sets from shared vars via .concat(), which a static
// scan cannot follow.

const fs = require("fs");
const path = require("path");
const vm = require("vm");
const { createCanvas } = require("canvas");

const EUCLID = process.env.EUCLID_REPO || path.resolve(__dirname, "../../euclid");
const LEKTOR = path.resolve(__dirname, "..");
const BOOKS = path.join(LEKTOR, "content/elements/books");

const bundle = fs.readFileSync(path.join(EUCLID, "dist/bundle.js"), "utf-8");

function makeSandbox() {
    const canvases = {};
    const doc = {
        getElementById(id) {
            if (!canvases[id]) {
                const c = createCanvas(400, 300);
                // init() reads CSS/attr sizing and installs listeners; give it
                // just enough surface to get through without a real DOM.
                c.style = {};
                c.clientWidth = 400;
                c.clientHeight = 300;
                c.getAttribute = () => null;
                c.setAttribute = () => {};
                c.addEventListener = () => {};
                c.removeEventListener = () => {};
                c.dispatchEvent = () => true;
                c.parentElement = null;   // -> createControls bails, no DOM needed
                c.id = id;
                canvases[id] = c;
            }
            return canvases[id];
        },
        createElement: () => ({ style: {}, setAttribute() {}, appendChild() {},
                                addEventListener() {}, getContext: () => null }),
        head: { appendChild() {} },
        documentElement: { appendChild() {} },
        addEventListener() {},
    };
    const sandbox = {
        console: { log() {}, warn() {}, error() {}, info() {} },  // silence the mirror
        document: doc,
        navigator: { userAgent: "node" },
        setTimeout, clearTimeout, Math, Date, JSON, Object, Array, String, Number,
        RegExp, Error, TypeError, Map, Set, WeakMap, isNaN, parseFloat, parseInt,
    };
    sandbox.window = sandbox;
    sandbox.globalThis = sandbox;
    sandbox.matchMedia = () => ({ matches: false });
    sandbox.requestAnimationFrame = () => 0;
    sandbox.cancelAnimationFrame = () => {};
    vm.createContext(sandbox);
    vm.runInContext(bundle, sandbox, { filename: "geomlib-bundle.js" });
    return sandbox;
}

// Pull every inline <script> body out of a contents.lr.
function scriptsOf(text) {
    const out = [];
    const re = /<script[^>]*>([\s\S]*?)<\/script>/gi;
    let m;
    while ((m = re.exec(text)) !== null) {
        if (m[1].includes("geomlib.init")) out.push(m[1]);
    }
    return out;
}

// Every page in the content tree that carries a geomlib figure — all 13
// books, definitions/postulates/common-notions/propositions alike, plus
// prematter and other-works. The prototype only walked bookI/propositions,
// which is why propIV3 went unseen since conversion.
function findPages(dir, out) {
    for (const name of fs.readdirSync(dir)) {
        const full = path.join(dir, name);
        const st = fs.statSync(full);
        if (st.isDirectory()) findPages(full, out);
        else if (name === "contents.lr") {
            const text = fs.readFileSync(full, "utf-8");
            if (text.includes("geomlib.init")) out.push(full);
        }
    }
    return out;
}
const files = findPages(path.join(LEKTOR, "content"), []).sort();

let totalDecks = 0, totalCanvases = 0, pagesWithIssues = 0, totalIssues = 0;
let totalSuppressed = 0;
let refPages = 0, refFigures = 0;

// ---------------------------------------------------------------------------
// Reference pages vs decks.
//
// This checker exists to guard the PROOF decks: a slide naming an element
// that doesn't exist is a broken walk-through, and that's what the #154
// diagnostics detect. The /geomlib/ pages are a different kind of page —
// a live reference for the library, one small figure per construction, no
// slides. There, deck-shaped diagnostics are noise: a figure deliberately
// carrying invisible helper points or a construction demonstrated in
// isolation is the POINT of the page, not a defect.
//
// So reference pages are still built — a figure that throws, or a
// construction that doesn't exist, is a real failure and still blocks a
// publish — but their deck diagnostics are not treated as issues.
// ---------------------------------------------------------------------------
function isReferencePage(dir) {
    return dir === "geomlib" || dir.startsWith("geomlib/") || dir.startsWith("geomlib" + path.sep);
}

// ---------------------------------------------------------------------------
// Known false positives: none.
//
// I.23's keepCircles names were suppressed here while euclid#159 was open —
// #154 validated at figure-build time, so names a macro animation creates at
// RUN time looked unresolvable. Fixed library-side in 0.15.0: an animation now
// declares the names it will create, and compassTransfer declares its
// keepCircles. The suppression is gone; a real typo in that deck is still
// caught.
// ---------------------------------------------------------------------------
function isKnownFalsePositive(dir, entry) {
    return false;
}

const rows = [];

for (const lr of files) {
    const dir = path.relative(path.join(LEKTOR, "content"), path.dirname(lr));
    totalDecks++;
    const text = fs.readFileSync(lr, "utf-8");
    const sandbox = makeSandbox();
    const failures = [];

    for (const body of scriptsOf(text)) {
        try {
            vm.runInContext(body, sandbox, { filename: dir, timeout: 10000 });
        } catch (err) {
            failures.push({ kind: "script-threw", message: String(err).slice(0, 160) });
        }
    }

    let diags = { count: 0, slates: [] };
    try { diags = sandbox.geomlib.diagnostics(); } catch (_) {}
    totalCanvases += (sandbox.geomlib.slates || []).length;

    const issues = [];
    let suppressed = 0;
    const reference = isReferencePage(dir);
    if (reference) {
        refPages++;
        refFigures += (sandbox.geomlib.slates || []).length;
    } else {
        for (const s of diags.slates || []) {
            for (const e of s.entries) {
                if (isKnownFalsePositive(dir, e)) { suppressed++; continue; }
                issues.push(`${s.canvasid || "?"} [${e.severity}] ${e.code}: ${e.message}`);
            }
        }
    }
    totalSuppressed += suppressed;
    for (const f of failures) issues.push(`${f.kind}: ${f.message}`);

    if (issues.length) {
        pagesWithIssues++;
        totalIssues += issues.length;
        rows.push({ dir, issues });
    }
}

console.log(`pages scanned      : ${totalDecks}`);
console.log(`canvases built     : ${totalCanvases}`);
console.log(`reference pages    : ${refPages} (${refFigures} figures — built, deck diagnostics not applied)`);
console.log(`decks with issues  : ${pagesWithIssues}`);
console.log(`total issues       : ${totalIssues}`);
console.log("");
for (const r of rows) {
    console.log(`=== ${r.dir}  (${r.issues.length})`);
    for (const i of r.issues.slice(0, 12)) console.log(`    ${i}`);
    if (r.issues.length > 12) console.log(`    ... and ${r.issues.length - 12} more`);
}

if (totalSuppressed) {
    console.log(`suppressed         : ${totalSuppressed} known false positive(s) — see isKnownFalsePositive()`);
}
process.exit(totalIssues > 0 ? 1 : 0);
