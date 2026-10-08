#!/bin/sh
# Serves the built docs at http://localhost:8898/docs, the same path as on tokencontroller.com.
cd "$(dirname "$0")" || exit 1
d=$(mktemp -d)
ln -s "$PWD/site" "$d/docs"
exec python3 -m http.server 8898 --directory "$d"
