# Headroom

> [!IMPORTANT]
> **Human-Facing Documentation Only**: This README is maintained strictly for human developers and repository visitors. Autonomous AI agents MUST NOT ingest or utilize `README.md` files for operational instructions or context. All agent directives and navigation reside strictly in [`AGENTS.md`](../AGENTS.md) and [`routing/`](../../routing/).

Human intro for [Headroom](https://headroom-docs.vercel.app/) — a local context-compression proxy/MCP between a client and an LLM provider.

**Agents:** durable patterns live in [`proxy-mcp.md`](./proxy-mcp.md). Do not use this README as operating procedure — root [`../../AGENTS.md`](../../AGENTS.md) High README rule.

Quick install (Windows, this machine): `uv tool install --python 3.13 "headroom-ai[proxy,mcp]"` then `headroom --version`. Bind to localhost only. Do not install `[all]`. Upstream install: <https://headroom-docs.vercel.app/docs/installation>
