#!/usr/bin/env node
// Guard the geomlib version against drift.
//
// The layout owns the version: `geomlib_default` in templates/layout.html
// feeds both the <script src> every page loads and the <meta> tag the
// constructions page's "Source" overlay hands to CodePen. Bump it in one
// place and the whole site follows.
//
// Prose is the exception. A CDN snippet inside a markdown body can't be
// templated — Lektor doesn't run Jinja in content — so it gets written by
// hand and then quietly rots. The landing page's "use it on your own page"
// snippet sat at 0.3.0, twelve minor versions behind, pointing at unpkg,
// which had stopped serving this package at all. Nothing failed; it was
// simply wrong for anyone who copied it.
//
// So: every hardcoded geomlib version outside the layout must match the
// layout's, and must name the CDN the site actually uses.

const fs = require("fs");
const path = require("path");

const LEKTOR = path.resolve(__dirname, "..");
const LAYOUT = path.join(LEKTOR, "templates/layout.html");
const CDN_HOST = "cdn.jsdelivr.net";

const layout = fs.readFileSync(LAYOUT, "utf-8");
const m = layout.match(/geomlib_default\s*=\s*"([^"]+)"/);
if (!m) {
    console.error("!! could not find geomlib_default in templates/layout.html");
    process.exit(2);
}
const EXPECTED = m[1];

// Everything a reader could copy from, minus the layout that defines it.
const ROOTS = ["content", "doc", "assets", "scripts", "README.md"];
const SKIP = new Set(["node_modules", ".git", "build", "temp", "__pycache__"]);

function walk(p, out) {
    let st;
    try { st = fs.statSync(p); } catch (_) { return out; }
    if (st.isDirectory()) {
        if (SKIP.has(path.basename(p))) return out;
        for (const n of fs.readdirSync(p)) walk(path.join(p, n), out);
    } else if (/\.(lr|md|html|js|css|json|sh)$/.test(p)) {
        out.push(p);
    }
    return out;
}

const files = ROOTS.flatMap((r) => walk(path.join(LEKTOR, r), []));
const issues = [];

for (const f of files) {
    if (path.resolve(f) === LAYOUT) continue;
    const text = fs.readFileSync(f, "utf-8");
    const rel = path.relative(LEKTOR, f);
    const re = /@brownnrl\/geomlib@([0-9][^/"'\s)]*)/g;
    let hit;
    while ((hit = re.exec(text)) !== null) {
        const line = text.slice(0, hit.index).split("\n").length;
        if (hit[1] !== EXPECTED) {
            issues.push(`${rel}:${line}  pinned ${hit[1]}, layout says ${EXPECTED}`);
        }
        // Same line, separate concern: unpkg began failing for this package
        // specifically (see the note in templates/layout.html).
        const around = text.slice(Math.max(0, hit.index - 60), hit.index);
        if (/https?:\/\//.test(around) && !around.includes(CDN_HOST)) {
            issues.push(`${rel}:${line}  CDN is not ${CDN_HOST}`);
        }
    }
}

console.log(`geomlib version    : ${EXPECTED} (templates/layout.html)`);
console.log(`files scanned      : ${files.length}`);
console.log(`version issues     : ${issues.length}`);
for (const i of issues) console.log(`    ${i}`);
process.exit(issues.length ? 1 : 0);
