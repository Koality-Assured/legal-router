# AI Tooling

> [!IMPORTANT]
> **Human-Facing Documentation Only**: This README is maintained strictly for human developers and repository visitors. Autonomous AI agents MUST NOT ingest or utilize `README.md` files for operational instructions or context. All agent directives and navigation reside strictly in [`AGENTS.md`](./AGENTS.md) and [`routing/`](../routing/).

Enablement layer for agents: memory checkpoints (`memory/user/`, `memory/agent/`, `memory/model/`), skills, standalone agent definitions, and A2A contracts.

The parent **router** classifies work, isolates mutating checkouts, and spawns domain specialists listed in [`agents/README.md`](./agents/README.md). Skills catalog: [`skills/README.md`](./skills/README.md). Generated dispatch table: [`../routing/skill-dispatch.md`](../routing/skill-dispatch.md).
