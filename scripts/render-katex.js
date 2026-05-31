#!/usr/bin/env node
// Read TeX from stdin, write rendered HTML to stdout.
//
// Usage:
//   echo '\frac{a}{b}' | node scripts/render-katex.js          # inline mode
//   echo '\frac{a}{b}' | node scripts/render-katex.js --display # block mode
//
// Designed to be spawned once per math block by the Lektor plugin.
// For very many blocks per build we could batch via a long-running
// process; this is the simple per-call form.

const katex = require("katex");

const displayMode = process.argv.includes("--display");

let buf = "";
process.stdin.on("data", chunk => (buf += chunk));
process.stdin.on("end", () => {
    try {
        const html = katex.renderToString(buf, {
            displayMode,
            throwOnError: false,
            // Don't pollute output with strict-mode warnings.
            strict: false,
        });
        process.stdout.write(html);
    } catch (e) {
        process.stderr.write("KaTeX error: " + e.message + "\n");
        process.stdout.write(
            '<span class="katex-error" style="color:#cc0000">' +
                String(buf).replace(/[<>&]/g, c => ({"<":"&lt;",">":"&gt;","&":"&amp;"}[c])) +
                "</span>"
        );
        process.exit(0);
    }
});
