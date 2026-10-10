---
schema_version: "2.0.0"
name: jurisdiction-hierarchy-map
description: >-
  Map hierarchical authority and precedence relations across federal, state,
  and administrative jurisdictions, resolving choice-of-law and binding
  precedent questions. Use when evaluating circuit splits, state versus
  federal preemption, or court hierarchy weights for legal arguments. Do not
  use for contract clause parsing (contract-clause-review) or SBOM licensing
  (open-source-license-scan).
owner_agent: legal-research-operator
rank: high
isolation: read-only
on_failure: abort_and_rollback
prerequisites:
  - python
dependencies:
  required_skills: []
  delegated_skills: []
  in_session_skills: []
contracts:
  inputs:
    - Legal dispute context, jurisdiction list, or statutory research query
  outputs:
    - Authority hierarchy graph/table ranking binding vs persuasive precedent
    - Choice of law and preemption determination advisory memo stamped for attorney review
topics: [legal, jurisdiction, precedence, choice-of-law, bluebook]
routing_hints: [jurisdiction-map, binding-precedent, circuit-split, court-hierarchy, erie-doctrine]
---

# Jurisdiction hierarchy map

## When to use

A legal research brief, statutory interpretation memo, or litigation strategy analysis requires establishing which court decisions or statutory frameworks constitute mandatory (binding) authority versus persuasive authority. Key scenarios include analyzing federal circuit splits, evaluating Erie doctrine choice-of-law between federal and state substantive law, mapping federal preemption over state statutes, or evaluating state intermediate appellate deference.

## When not to use

Contract clause redlining (`contract-redline-diff`). Commercial transaction risk memos (`deal-risk-memo`). Open source package license audits (`open-source-license-scan`). Routine citation string formatting without hierarchy mapping (`citation-verification`).

## Criticality

High: relying on non-binding persuasive authority or citing overturned circuit precedent in a jurisdiction with contrary binding law misleads counsel and undermines legal analysis. Output is advisory legal research only and must be validated by a licensed attorney.

## Source of truth

- [`docs/standards/legal-overlay.md`](../../../../docs/standards/legal-overlay.md)
- [`supporting/legal/legal-citation-standards.md`](../../../../supporting/legal/legal-citation-standards.md)
- `python scripts/legal/verify_citations.py`
- Sibling primary-law corpus: `../ai-router/references/us-law/` from the legal-router repository root
- Official federal and state court structure guidelines (US Supreme Court, Circuit Courts of Appeals, District Courts, State Supreme Courts)

## Isolation

`read-only` by default for legal analysis, hierarchy structuring, and advisory memo generation returned in-session. If persisting output files under `results/`, parent coordinates worktree isolation via `isolate-work`.

## How to use

1. Run `qmd search` for citation standards and jurisdiction guides (no tree walks).
2. Identify the forum jurisdiction, governing law provisions, and subject matter context (e.g. federal question, diversity jurisdiction, state statutory claim).
3. Establish the jurisdictional hierarchy tiers:
   - **Tier 1 (Mandatory Constitutional/Statutory Authority)**: US Constitution, federal statutes (USC), state constitutions, and state statutes within their respective sovereign spheres.
   - **Tier 2 (Mandatory Judicial Precedent)**: US Supreme Court (nationwide binding on federal law), relevant Federal Circuit Court of Appeals (binding on district courts within circuit), State Supreme Court (authoritative on state law).
   - **Tier 3 (Persuasive Judicial Authority)**: Sibling federal circuit decisions, out-of-state supreme courts, federal district court opinions, state appellate decisions from other states.
   - **Tier 4 (Secondary Authority)**: Restatements of Law, law review treatises, administrative agency guidance.
4. Verify all cited precedents using `scripts/legal/verify_citations.py`:
   `python scripts/legal/verify_citations.py --dry-run --json`
5. Highlight circuit splits or conflicts among state courts of last resort.
6. Assemble the hierarchical authority map and apply the mandatory advisory stamp:
   `ADVISORY WORK PRODUCT - REQUIRES LICENSED ATTORNEY REVIEW`

## Dry run

```bash
python scripts/legal/verify_citations.py --dry-run --json
python scripts/ai-tooling/validate_skill.py --skill jurisdiction-hierarchy-map --dry-run
```

## Security

Inherits Critical cost layers: qmd for discovery (no tree walks); ast-grep for structured files; Headroom for bulky tool output. Skills cannot waive root AGENTS.md.

Never print CourtListener tokens or credential secrets in logs. Unverified citations must remain explicitly flagged as unverified. Legal hierarchy maps do not constitute legal advice or formal court pleadings.

## Completion gates

Hierarchical authority classification established (mandatory vs persuasive), circuit splits and preemption flags noted, citation verification executed, and advisory stamp applied.
