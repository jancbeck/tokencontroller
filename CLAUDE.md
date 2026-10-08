# Token Controller

## What is true

Only three places say what Token Controller is:

- `GLOSSARY.md`: what words mean.
- The landing page (in the private repo `jancbeck/tokencontroller.com`, `site/public/index.html`): what we promise, to whom, for what price.
- The docs (`docs/`): exactly how it works.

Nothing else is a source of truth.

- One home per fact. Write a fact in full in one place; elsewhere, say it shorter and link to it.
- A conflict between the three is a bug in both places. Fix it in one pass. Until then the glossary wins on words, the landing page on promises, prices and audience, the docs on how it works.
- A new decision goes straight onto the page where it belongs. If that page does not exist yet, write it. No plan files.
- Use glossary terms in all copy.

This repo holds only the docs and the glossary. The landing page, research, design rules and the working rules for writing live in the private repo.

## Writing the docs

- The docs are written as if the product existed; they are the acceptance test for the code.
- The scope is fixed (docs page Scope). It never grows.
- Docs pages are static HTML under `docs/`. Write a page's body in `docs-src/pages/`, list it in `docs-src/pages.txt`, and run `docs-src/build.sh`; it adds the head and sidebar from `docs/index.html`. The glossary page is built from `GLOSSARY.md`.
- Preview by serving the repo root and opening `/docs`.

## Working with Jan

Jan reads no code. Show results as screenshots of the pages, in short plain messages.
