# Standalone agents

Human overview: specialist definitions live in `<id>/AGENT.md`. Optional host stubs under `.cursor/agents/` only point here.

**Agents do not use this README as a catalog.** Catalogs are `AGENT.md` (Schema V2) + [`../../routing/skill-dispatch.md`](../../routing/skill-dispatch.md) / [`../../routing/area-map.md`](../../routing/area-map.md). Tiers: [`model-tiers.md`](./model-tiers.md).

Human index (not agent SoT):

### Broad-sweeping operators

| Operator | Role / Scope | Tier |
| --- | --- | --- |
| [`harness-operator/`](./harness-operator/) | Harness lifecycle, control plane, cost layers, skill/agent builder, repository maintenance | standard |
| [`document-operator/`](./document-operator/) | Technical writing, diagrams, reports, Confluence/Slack/Google collab, anti-slop | standard |
| [`research-operator/`](./research-operator/) | Deep technical research, BenchLM, AI vendor tracking, community intelligence, web crawl | high |

### Legal domain specialists

| Specialist | Role | Tier |
| --- | --- | --- |
| [`contract-lifecycle-operator/`](./contract-lifecycle-operator/) | Commercial contract clause extraction, redlines, liability caps, and SLA audits | high |
| [`ip-licensing-curator/`](./ip-licensing-curator/) | SPDX and CycloneDX SBOM license identification, copyleft heuristic flags | standard |
| [`legal-research-operator/`](./legal-research-operator/) | Statutory retrieval, precedent citation verification, and advisory memo drafting | high |
| [`statutory-compliance-analyst/`](./statutory-compliance-analyst/) | Regulatory crosswalks and gap analysis (EU AI Act, GDPR, HIPAA, FTC, SEC) | high |

### Coordinator & true specialists

| Specialist | Role | Tier |
| --- | --- | --- |
| [`router/`](./router/) | Parent coordinator: classify, isolate, spawn | standard |
| [`detailed-activity/`](./detailed-activity/) | Dedicated adversarial / antagonistic review and challenge audits | high |
| [`benchmark-agent/`](./benchmark-agent/) | Empirical benchmarking: cost estimation, fleet dry runs, retrieval, tool efficiency | standard |
| [`github-ops/`](./github-ops/) | GitHub PR workflow, branch discipline, issue management | standard |
| [`git-fast-operator/`](./git-fast-operator/) | Simple git fetch/status/log/diff/sync | fast |

### Legacy & component specialists (Consolidated into Operators)

| Agent | Consolidated into | Tier |
| --- | --- | --- |
| [`documentation-ops/`](./documentation-ops/) | `document-operator` | standard |
| [`router-maintenance/`](./router-maintenance/) | `harness-operator` | standard |
| [`qmd-ops/`](./qmd-ops/) | `harness-operator` | standard |
| [`ai-tooling-ops/`](./ai-tooling-ops/) | `harness-operator` | standard |
| [`memory-operator/`](./memory-operator/) | `harness-operator` | standard |
| [`script-ops/`](./script-ops/) | `harness-operator` | standard |
| [`artifact-agent/`](./artifact-agent/) | `document-operator` | standard |
| [`reference-ops/`](./reference-ops/) | `document-operator` | standard |

A2A specifications & schemas: canonical in `AGENT.md` (Schema V2); see also [`../a2a/agent-cards/README.md`](../a2a/agent-cards/README.md).
