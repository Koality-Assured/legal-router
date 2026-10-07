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

## Primary-law corpus

Official federal, state, and District of Columbia locators live in the `ai-router` checkout at `references/us-law/`. When the legal-router repository sits next to that checkout, the corpus path from the legal-router repository root is `../ai-router/references/us-law/AGENTS.md`. That path is not relative to this file. Do not copy those pages into this repo.

`legal-research-operator` uses that corpus for locators. Citation verification still marks a pinpoint unverified until an official page is fetched in the session. GovInfo is the working United States Code source while `uscode.house.gov` serves a maintenance page.
