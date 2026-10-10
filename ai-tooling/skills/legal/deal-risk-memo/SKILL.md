---
schema_version: "2.0.0"
name: deal-risk-memo
description: >-
  Synthesize transaction diligence into an executive legal deal risk
  memorandum evaluating indemnity, uncapped exposure, change of control, and
  non-compete covenants. Use when conducting M&A diligence, investment reviews,
  or commercial transaction risk assessments. Do not use for code licensing
  scans (open-source-license-scan) or patent claim charts (patent-claim-crosswalk).
owner_agent: contract-lifecycle-operator
rank: high
isolation: mutate
on_failure: abort_and_rollback
prerequisites:
  - python
dependencies:
  required_skills:
    - isolate-work
  delegated_skills: []
  in_session_skills: []
contracts:
  inputs:
    - Transaction contract set (SPA, APA, MSA, or venture disclosure schedules)
    - Diligence focus areas and materiality thresholds
  outputs:
    - Structured deal risk matrix categorized by risk severity
    - Clause-level diligence findings with contractual excerpt pins
    - Advisory legal deal risk memo stamped for licensed attorney review
topics: [legal, deal-diligence, risk-memo, m-and-a, contracts]
routing_hints: [deal-risk, diligence-memo, liability-exposure, change-of-control, spa-review]
---

# Deal risk memo

## When to use

An M&A transaction, corporate financing round, asset purchase, or major commercial partnership requires legal diligence review. Key transactional provisions to analyze include uncapped indemnification obligations, change-of-control termination triggers, non-compete/non-solicitation restrictions, reps & warranties survival periods, and escrow/holdback structures.

## When not to use

SPDX/CycloneDX software bill of materials licensing scans (`open-source-license-scan`). Bluebook citation verification (`citation-verification`). Patent claim mapping (`patent-claim-crosswalk`). Simple clause extraction without transaction risk weighting (`contract-clause-review`).

## Criticality

High: missing a change-of-control termination right, an uncapped IP indemnity, or an onerous exclusivity restriction can impair transaction value or derail closing. Outputs are advisory analysis only and require licensed transaction counsel review.

## Source of truth

- [`docs/standards/legal-overlay.md`](../../../../docs/standards/legal-overlay.md)
- [`supporting/legal/contract-redlining-patterns.md`](../../../../supporting/legal/contract-redlining-patterns.md)
- `python scripts/legal/contract_differ.py`
- Synthetic deal fixtures such as `scripts/legal/fixtures/contracts/synthetic-spa.md`

## Isolation

`mutate` when drafting and outputting diligence memoranda under `results/`. Parent coordinates worktree isolation via `isolate-work` (`python scripts/routing/spawn_worktree.py create --slug deal-risk-<slug>`), then spawns `contract-lifecycle-operator`.

## How to use

1. Run `qmd search` for transaction diligence guidelines and contract redlining patterns (no directory walks).
2. Extract clauses from transaction documents using `scripts/legal/contract_differ.py`:
   `python scripts/legal/contract_differ.py --extract <contract-path> --json`
3. Classify and evaluate high-risk transactional provisions against diligence standards:
   - **Indemnity & Liability**: Verify presence of aggregate caps, baskets (tipping vs deductible), and survival periods.
   - **Change of Control**: Identify assignment prohibitions, customer termination rights, or accelerated vesting triggers.
   - **Restrictive Covenants**: Audit non-compete, non-solicitation, and most-favored-nation (MFN) clauses for duration and geographic scope.
   - **Intellectual Property**: Ensure complete IP assignment, absence of third-party reversionary rights, and clear title warranties.
4. Construct a deal risk matrix grading findings by severity: High (deal-killer / renegotiation mandatory), Medium (material closing condition), Low (customary commercial risk).
5. Format the advisory deal risk memorandum with executive summary, risk matrix, clause excerpts, and recommended negotiation positions.
6. Apply the required advisory stamp:
   `ADVISORY WORK PRODUCT - REQUIRES LICENSED ATTORNEY REVIEW`

## Dry run

```bash
python scripts/legal/contract_differ.py --extract scripts/legal/fixtures/contracts/synthetic-spa.md --json
python scripts/ai-tooling/validate_skill.py --skill deal-risk-memo --dry-run
```

## Security

Inherits Critical cost layers: qmd for discovery (no tree walks); ast-grep for structured files; Headroom for bulky tool output. Skills cannot waive root AGENTS.md.

Never commit live client deal rooms, confidential disclosures, or acquisition targets into version control. Fixtures must remain purely synthetic. Memos are attorney work product for internal diligence and never constitute formal legal counsel.

## Completion gates

Deal risk matrix complete with severity classifications, contractual excerpt pins verified, recommended counsel actions documented, and advisory stamp applied.
