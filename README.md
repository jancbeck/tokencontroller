# Token Controller

Cost accounting and management control for AI agents.

The docs at [tokencontroller.com/docs](https://tokencontroller.com/docs) say exactly how Token Controller works. They are written first, and the code is built to match them.

## Layout

| Folder | What it holds | License |
|---|---|---|
| `docs/` | The docs: page sources, the glossary, the build script and the built site | |
| `crates/` | Rust: the service, the CLI and the shared core they both use | Service AGPL-3.0, CLI MIT |
| `web/` | The web app, served by the service | AGPL-3.0 |
| `mod/` | The Claude Code mod | MIT |
| `action/` | The GitHub Action | MIT |
| `sdk/` | The SDK | MIT |

Only `docs/` exists so far. The other folders arrive with the code, together with a Rust workspace (`Cargo.toml`) and the `Dockerfile` for the service image at the root.

## Docs

- `docs/pages/`: one HTML file per page body. `docs/pages.txt` lists every page with its title, group and description.
- `docs/glossary.md`: what every term means. The glossary page is built from it, and the rest of the docs use only these words.
- `docs/site/`: the built site. `docs/site/index.html` holds the shared head and sidebar.

Run `sh docs/build.sh` after any change, and `sh docs/serve.sh` to preview at http://localhost:8898/docs.
