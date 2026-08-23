#!/usr/bin/env bash
# Build the Lektor site and force-push the output to a `lektor/<branch>`
# branch on `euclids-elements.org`. Cloudflare Workers Builds auto-deploys
# every branch push, so the preview lands at:
#
#   https://lektor-<branch>-euclids-elements-org.brownnrl.workers.dev/
#
# Usage:
#   ./scripts/deploy-preview.sh                # uses current git branch
#   ./scripts/deploy-preview.sh some-name      # uses provided name
#
# Env:
#   EUCLIDS_REPO   path to the euclids-elements.org checkout
#                  (default: ../euclids-elements.org)
#   LEKTOR_BIN     path to the lektor executable
#                  (default: ~/venvs/lektor/bin/lektor)
set -euo pipefail

LEKTOR_REPO="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${EUCLIDS_REPO:-${LEKTOR_REPO}/../euclids-elements.org}"
LEKTOR="${LEKTOR_BIN:-${HOME}/venvs/lektor/bin/lektor}"

if [[ ! -d "$DEST/.git" ]]; then
    echo "ERROR: \$EUCLIDS_REPO ($DEST) does not look like a git checkout."
    echo "Point EUCLIDS_REPO at your euclids-elements.org checkout."
    exit 1
fi

cd "$LEKTOR_REPO"
SOURCE_BRANCH="${1:-$(git rev-parse --abbrev-ref HEAD)}"
SOURCE_COMMIT="$(git rev-parse --short HEAD)"
SOURCE_DIRTY=""
if ! git diff --quiet || ! git diff --cached --quiet; then
    SOURCE_DIRTY=" (dirty)"
fi
PREVIEW_BRANCH="lektor/${SOURCE_BRANCH}"

echo "==> Checking deck consistency"
# Evaluates every page's inline geomlib script against the real bundle and
# fails on any diagnostic (unresolvable slide names, animation targets that
# match nothing, figures that throw). This is what caught propIV3, whose
# figure had not rendered since conversion. Needs node-canvas from the euclid
# checkout; skipped with a warning if that is not available, so the deploy
# still works on a machine without it.
if NODE_PATH="${EUCLIDS_GEOMLIB_REPO:-$(cd "$(dirname "$0")/../../euclid" && pwd)}/node_modules" \
       node "$(dirname "$0")/check-decks.js"; then
    :
else
    status=$?
    if [ "$status" -eq 1 ]; then
        echo "!! deck check failed — fix the diagnostics above, or re-run with SKIP_DECK_CHECK=1" >&2
        [ "${SKIP_DECK_CHECK:-}" = "1" ] || exit 1
        echo "!! SKIP_DECK_CHECK=1 set — continuing anyway" >&2
    else
        echo "!! deck check could not run (exit $status) — continuing" >&2
    fi
fi

echo "==> Building Lektor site"
rm -rf build
"$LEKTOR" build --output-path build

echo "==> Force-checkout ${PREVIEW_BRANCH} in ${DEST}"
cd "$DEST"
git fetch origin --quiet || true
# Use an orphan-style update: wipe the tree, drop in the build output.
# Keeps the preview branch independent of the consumer site's main.
git checkout --orphan _lektor_temp 2>/dev/null || git checkout -B _lektor_temp
git rm -rf --quiet . 2>/dev/null || true

cp -a "$LEKTOR_REPO/build/." ./

# Carry over the Cloudflare Workers infrastructure (worker entrypoint
# + wrangler config + assetsignore) from main so CF Builds has an
# entry-point. The orphan-style replacement above wipes everything,
# including these files, even though they're not part of the Lektor
# build output. Without them CF Builds errors with "Missing
# entry-point to Worker script or to assets directory".
echo "==> Copying Cloudflare config from main"
for cf_file in wrangler.jsonc _worker.js .assetsignore; do
    if git show "origin/main:${cf_file}" > "${cf_file}" 2>/dev/null; then
        echo "    + ${cf_file} (from origin/main)"
    elif git show "main:${cf_file}" > "${cf_file}" 2>/dev/null; then
        echo "    + ${cf_file} (from main)"
    else
        rm -f "${cf_file}"
        echo "    ! ${cf_file} missing on main — preview deploy will likely fail"
    fi
done

git add -A
COMMIT_MSG="lektor build from ${SOURCE_BRANCH}@${SOURCE_COMMIT}${SOURCE_DIRTY}"
git commit -m "$COMMIT_MSG" --quiet

# Replace the preview branch atomically.
git branch -D "$PREVIEW_BRANCH" 2>/dev/null || true
git branch -m "$PREVIEW_BRANCH"
git push -f origin "$PREVIEW_BRANCH"

echo ""
echo "Pushed ${PREVIEW_BRANCH}."
echo "Preview URL (CF builds in ~30s):"
echo "  https://lektor-${SOURCE_BRANCH//\//-}-euclids-elements-org.brownnrl.workers.dev/"
echo "Example page:"
echo "  https://lektor-${SOURCE_BRANCH//\//-}-euclids-elements-org.brownnrl.workers.dev/bookI/propI1/"
