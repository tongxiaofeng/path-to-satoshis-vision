#!/bin/bash
# Sync chapters to mdBook source and build the site.
# Run this after updating any chapter markdown files.
# Output goes to docs/ for GitHub Pages.

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BOOK_SRC="$PROJECT_ROOT/book/src"
CHAPTERS_DIR="$PROJECT_ROOT/chapters"

echo "==> Syncing chapters to book/src/"
for f in "$CHAPTERS_DIR"/*.md; do
    cp "$f" "$BOOK_SRC/$(basename "$f")"
done
echo "    Copied $(ls "$CHAPTERS_DIR"/*.md | wc -l | tr -d ' ') chapter files"

echo "==> Building mdBook site"
cd "$PROJECT_ROOT/book"
mdbook build

echo "==> Done. Site output in docs/"
echo "    $(find "$PROJECT_ROOT/docs" -name '*.html' | wc -l | tr -d ' ') HTML files generated"
