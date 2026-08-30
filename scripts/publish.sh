#!/usr/bin/env bash
# Publish the Lektor site to the LIVE site at www.euclids-elements.org.
#
# GitHub Pages serves brownnrl/euclids-elements.org. Lektor's ghpages publisher
# pushes the build to the `gh-pages` branch and writes CNAME from the ?cname=
# param on the target in euclids-elements.lektorproject.
#
# This wrapper exists so a publish can never skip validation: it runs the deck
# checker first and refuses to deploy if any figure is broken. Use it instead of
# `lektor deploy production`.
#
# Usage:
#   ./scripts/publish.sh              # check, build, confirm, deploy
#   ./scripts/publish.sh --dry-run    # check + build only; report, deploy nothing
#
# Env:
#   EUCLIDS_GEOMLIB_REPO  path to the euclid checkout (for node-canvas)
#                         default: ../euclid
#   LEKTOR_BIN            default: ~/venvs/lektor/bin/lektor
set -euo pipefail

cd "$(dirname "$0")/.."
LEKTOR="${LEKTOR_BIN:-$HOME/venvs/lektor/bin/lektor}"
EUCLID="${EUCLIDS_GEOMLIB_REPO:-$(cd .. && pwd)/euclid}"
DRY_RUN=""
[ "${1:-}" = "--dry-run" ] && DRY_RUN=1

echo "==> Checking deck consistency"
# Evaluates every page's inline geomlib script against the real bundle.
# A broken figure must never reach the live site.
if ! NODE_PATH="${EUCLID}/node_modules" node scripts/check-decks.js; then
    echo "!! deck check FAILED — refusing to publish. Fix the diagnostics above." >&2
    exit 1
fi

echo "==> Checking geomlib version consistency"
# A hand-written CDN snippet in prose can't be templated, so it rots
# silently. Nothing breaks the build; it just misleads anyone who copies it.
if ! node scripts/check-versions.js; then
    echo "!! version check FAILED — refusing to publish. Fix the pins above." >&2
    exit 1
fi

echo "==> Building"
rm -rf build
"$LEKTOR" build --output-path build

# CNAME is written by the publisher, not the build — confirm the pieces that
# ARE the build's responsibility actually made it.
echo "==> Verifying build output"
missing=0
for f in index.html LICENSE COPYRIGHT.md elements/index.html geomlib/index.html; do
    if [ ! -f "build/$f" ]; then echo "    ! missing build/$f" >&2; missing=1; fi
done
[ "$missing" -eq 0 ] || { echo "!! build is incomplete — refusing to publish." >&2; exit 1; }
pages=$(find build -name 'index.html' | wc -l)
echo "    $(find build -type f | wc -l) files, ${pages} pages"

if [ -n "$DRY_RUN" ]; then
    echo "==> --dry-run: nothing deployed."
    exit 0
fi

cat <<WARN

  This publishes to the LIVE site: https://www.euclids-elements.org/
  Lektor force-updates the gh-pages branch of brownnrl/euclids-elements.org.
  The URL scheme differs from the current hand-authored site, so existing
  deep links will not resolve.

WARN
read -r -p "  Type 'publish' to continue: " reply
[ "$reply" = "publish" ] || { echo "aborted."; exit 1; }

echo "==> Deploying to production"
"$LEKTOR" deploy production

echo "==> Done. Pages will rebuild; check https://www.euclids-elements.org/"
