# Token Controller

Cost accounting and management control for AI agents.

The docs at [docs.tokencontroller.com](https://docs.tokencontroller.com) say exactly how Token Controller works. They are written first, and the code is built to match them.

## Layout

| Folder | What it holds | License |
|---|---|---|
| `apps/docs/` | The docs: page sources, the glossary, the build script and the built site | |
| `apps/server/` | The service at app.tokencontroller.com, in Rust: sign-in, API, telemetry ingest, background jobs, MCP server. It also serves the web app | AGPL-3.0 |
| `apps/web/` | The web app, built into the service's Docker image | AGPL-3.0 |
| `apps/cli/` | The `tc` command, in Rust | MIT |
| `crates/` | Rust libraries the service and the CLI share, such as `core` (money and rules) | AGPL-3.0 or MIT, per crate |
| `packages/` | Everything published to a registry, one folder each: `claude-code-mod` first, then one mod per agent harness that allows mods, `sdk` and `github-action` | MIT |

Rust code is one Cargo workspace (`Cargo.toml` at the root). TypeScript code is one pnpm workspace (`pnpm-workspace.yaml` at the root). The `Dockerfile` for the service image sits at the root too. Only `apps/docs/` exists so far; the rest arrives with the code.

## Docs

- `apps/docs/pages/`: one HTML file per page body. `apps/docs/pages.txt` lists every page with its title, group and description.
- `apps/docs/glossary.md`: what every term means. The glossary page is built from it, and the rest of the docs use only these words.
- `apps/docs/site/`: the built site. `apps/docs/site/index.html` holds the shared head and sidebar.

Run `sh apps/docs/build.sh` after any change, and `sh apps/docs/serve.sh` to preview at http://localhost:8898. Cloudflare deploys `apps/docs/` to docs.tokencontroller.com on every push to main (`apps/docs/wrangler.jsonc`).
