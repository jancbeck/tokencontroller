#!/bin/sh
# Serves the built docs at http://localhost:8898, laid out as on docs.tokencontroller.com.
cd "$(dirname "$0")" || exit 1
exec python3 -m http.server 8898 --directory site
