---
doc_kind: requirement
canonical_id: legal-overlay
purpose: [requirement]
rank: high
topics: [legal, overlay]
rag_keywords: [legal, domain-overlay, spoke, advisory, attorney]
---

# legal domain overlay

This spoke is a `legal` harness scaffolded from `ai-harness-core`. Domain specialists live here. Keep generic machinery in the core.

Do not copy this overlay, instance `projects/`, `research/`, or `ai-tooling/memory/` back to the generic core.

Pull core updates: `python scripts/sync/pull_harness_core.py --dry-run --json`.

Propose generic core changes: `python scripts/sync/propose_core_update.py --dry-run --json`.

## MUST

- Every memo, redline, crosswalk, and scan is `ADVISORY WORK PRODUCT - REQUIRES LICENSED ATTORNEY REVIEW`.
- A licensed attorney reviews before client communication or filing. This spoke does not practice law.
- Citation verification flags planted hallucinations and marks unverified live cites; it does not claim zero hallucination.
- No WorldCC / IACCM member scrape. No Bluebook table redistribution. No client secrets in git.

## Domain pack

| Kind | Ids |
| --- | --- |
| Agents | `contract-lifecycle-operator`, `statutory-compliance-analyst`, `ip-licensing-curator`, `legal-research-operator` |
| Skills | `contract-clause-review`, `regulatory-crosswalk-audit`, `open-source-license-scan`, `citation-verification` |
| Scripts | `scripts/legal/verify_citations.py`, `scripts/legal/contract_differ.py`, `scripts/legal/spdx_license_checker.py` |

Recipes: [`supporting/legal/`](../../supporting/legal/).
