---
doc_kind: requirement
canonical_id: legal-overlay
purpose: [requirement]
rank: medium
topics: [legal, overlay]
rag_keywords: [legal, domain-overlay, spoke]
---

# legal domain overlay

This spoke is a `legal` harness scaffolded from `ai-harness-core`. Feed legal corpus here. Keep generic machinery in the core.

Do not copy this overlay, instance `projects/`, `research/`, or `ai-tooling/memory/` back to the generic core.

Pull core updates: `python scripts/sync/pull_harness_core.py --dry-run --json`.

Propose generic core changes: `python scripts/sync/propose_core_update.py --dry-run --json`.
