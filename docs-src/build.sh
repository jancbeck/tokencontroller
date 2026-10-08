#!/bin/sh
# Rebuilds every docs page from pages/*.html with the head and sidebar of
# public/docs/index.html. Edit the sidebar there, then run this script.
cd "$(dirname "$0")" || exit 1
python3 glossary.py
while IFS='|' read -r slug title group desc body; do
  python3 gen.py "$slug" "$title" "$group" "$desc" "$body" >/dev/null
done < pages.txt
