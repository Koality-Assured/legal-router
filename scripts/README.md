# Scripts

> [!IMPORTANT]
> **Human-Facing Documentation Only**: This README is maintained strictly for human developers and repository visitors. Autonomous AI agents MUST NOT ingest or utilize `README.md` files for operational instructions or context. All agent directives and navigation reside strictly in [`AGENTS.md`](./AGENTS.md) and [`routing/`](../routing/).

Tagged Python utilities organized by purpose subfolders. Index: [`script-index.md`](./script-index.md) (generated). Shared library modules live in [`_lib/`](./_lib/) and are not indexed.

| Subfolder | Role |
| --- | --- |
| [`_lib/`](./_lib/) | Shared helpers (`md.py`, `paths.py`) — not indexed |
| [`ai-tooling/`](./ai-tooling/) | Agent and skill catalog validation scripts |
| [`benchmarks/`](./benchmarks/) | Benchmarking and cost methodology tooling |
| [`change-history/`](./change-history/) | Provenance log append scripts |
| [`cli/`](./cli/) | Harness CLI operations and cleanup tools |
| [`cost-layers/`](./cost-layers/) | Combined qmd and Headroom validation scripts |
| [`docs/`](./docs/) | Repository and documentation structure validators |
| [`github/`](./github/) | GitHub workflow and PR utilities |
| [`legal/`](./legal/) | Domain legal tooling: citation verification, contract differ, SPDX scanner |
| [`qmd/`](./qmd/) | QMD collection management and index refresh tools |
| [`repos/`](./repos/) | Repository synchronization and management |
| [`research/`](./research/) | Research automation utilities |
| [`routing/`](./routing/) | Routing index generation and worktree spawning |
| [`sync/`](./sync/) | Core harness synchronization utilities |
| [`tests/`](./tests/) | Test suite runners and regression tests |

Invoke as `python scripts/<purpose>/<name>.py`. Regenerate the index after add/remove/rename: `python scripts/routing/generate_script_index.py`.
