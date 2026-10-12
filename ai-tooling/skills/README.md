# Skills

> [!IMPORTANT]
> **Human-Facing Documentation Only**: This README is maintained strictly for human developers and repository visitors. Autonomous AI agents MUST NOT ingest or utilize `README.md` files for operational instructions or context. All agent directives and navigation reside strictly in [`AGENTS.md`](./AGENTS.md) and [`routing/`](../../routing/).

Human overview: router skills live organized into domain families under `<family>/<name>/SKILL.md`.

**Agents do not use this README as a catalog.** They load [`../../routing/skill-dispatch.md`](../../routing/skill-dispatch.md) (regenerate with `python scripts/routing/generate_skill_dispatch.py`) and spawn `owner_agent`. Template: [`../../ai-tooling/skills/skill-conventions.md`](skill-conventions.md). Validate: `python scripts/ai-tooling/validate_skill.py --all`.

Human index (not agent SoT):

| Skill | Owner | Isolation |
| --- | --- | --- |
| [`agent-builder/`](./meta/agent-builder/) | harness-operator | mutate |
| [`antagonistic-review/`](./meta/antagonistic-review/) | detailed-activity | read-only |
| [`anti-slop/`](./reporting/anti-slop/) | document-operator | mutate |
| [`architecture-diagram/`](./reporting/architecture-diagram/) | document-operator | mutate |
| [`ast-grep/`](./cost-layers/ast-grep/) | harness-operator | read-only |
| [`citation-verification/`](./legal/citation-verification/) | legal-research-operator | read-only |
| [`code-review-report/`](./reporting/code-review-report/) | document-operator | mutate |
| [`contract-clause-review/`](./legal/contract-clause-review/) | contract-lifecycle-operator | mutate |
| [`contract-redline-diff/`](./legal/contract-redline-diff/) | contract-lifecycle-operator | mutate |
| [`corpus-draft/`](./reporting/corpus-draft/) | document-operator | mutate |
| [`cost-layer-dry-run/`](./cost-layers/cost-layer-dry-run/) | harness-operator | mutate |
| [`deal-risk-memo/`](./legal/deal-risk-memo/) | contract-lifecycle-operator | mutate |
| [`deep-research/`](./meta/deep-research/) | research-operator | mutate |
| [`doc-builder/`](./meta/doc-builder/) | document-operator | mutate |
| [`executive-report/`](./reporting/executive-report/) | document-operator | mutate |
| [`git-basics/`](./git/git-basics/) | git-fast-operator | mutate |
| [`github-paths/`](./git/github-paths/) | github-ops | read-only |
| [`github-workflow/`](./git/github-workflow/) | github-ops | mutate |
| [`guidance-draft/`](./reporting/guidance-draft/) | document-operator | mutate |
| [`headroom/`](./cost-layers/headroom/) | harness-operator | read-only |
| [`harness-review/`](./harness-review/) | harness-operator | mutate |
| [`humanizer/`](./reporting/humanizer/) | document-operator | mutate |
| [`isolate-work/`](./meta/isolate-work/) | router | mutate |
| [`jurisdiction-hierarchy-map/`](./legal/jurisdiction-hierarchy-map/) | legal-research-operator | read-only |
| [`markdownlint/`](./meta/markdownlint/) | document-operator | mutate |
| [`readme-maintain/`](./meta/readme-maintain/) | document-operator | mutate |
| [`memory-adjust/`](./memory/memory-adjust/) | harness-operator | mutate |
| [`memory-cleanup/`](./memory/memory-cleanup/) | harness-operator | mutate |
| [`memory-create/`](./memory/memory-create/) | harness-operator | mutate |
| [`mermaid-diagram/`](./reporting/mermaid-diagram/) | document-operator | mutate |
| [`model-memory-operate/`](./model-memory-operate/) | harness-operator | mutate |
| [`open-source-license-scan/`](./legal/open-source-license-scan/) | ip-licensing-curator | read-only |
| [`patent-claim-crosswalk/`](./legal/patent-claim-crosswalk/) | ip-licensing-curator | mutate |
| [`privacy-policy-benchmark/`](./legal/privacy-policy-benchmark/) | statutory-compliance-analyst | mutate |
| [`proposal-report/`](./reporting/proposal-report/) | document-operator | mutate |
| [`qmd-efficiency/`](./meta/qmd-efficiency/) | harness-operator | mutate |
| [`qmd-usage/`](./meta/qmd-usage/) | harness-operator | read-only |
| [`reference-maintain/`](./meta/reference-maintain/) | document-operator | mutate |
| [`regulatory-crosswalk-audit/`](./legal/regulatory-crosswalk-audit/) | statutory-compliance-analyst | mutate |
| [`scratch-cleanup/`](./meta/scratch-cleanup/) | harness-operator | mutate |
| [`script-builder/`](./meta/script-builder/) | harness-operator | mutate |
| [`skill-builder/`](./meta/skill-builder/) | harness-operator | mutate |
| [`skill-dry-run/`](./meta/skill-dry-run/) | harness-operator | read-only |
| [`router-structure/`](./meta/router-structure/) | document-operator | read-only |
| [`local-webfetch/`](./research/local-webfetch/) | research-operator | read-only |
| [`agent-cost-estimator/`](./benchmarks/agent-cost-estimator/) | benchmark-agent | mutate |
| [`agent-fleet-benchmark/`](./benchmarks/agent-fleet-benchmark/) | benchmark-agent | mutate |
| [`retrieval-benchmark/`](./benchmarks/retrieval-benchmark/) | benchmark-agent | mutate |
| [`tool-efficiency-benchmark/`](./benchmarks/tool-efficiency-benchmark/) | benchmark-agent | mutate |
| [`task-eval-benchmark/`](./benchmarks/task-eval-benchmark/) | benchmark-agent | mutate |
