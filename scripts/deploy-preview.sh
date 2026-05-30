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
