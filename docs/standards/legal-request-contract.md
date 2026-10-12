---
doc_kind: requirement
canonical_id: legal-request-contract
purpose: [requirement, reinforcement]
rank: high
topics: [legal, request-contract, ethics, review, constraints]
rag_keywords: [legal-request, contract-normalization, ethics-review, upl-disclaimer, deviation-ledger, aba-opinion-512]
---

# Legal request contract standard

## Scope and relationship to legal standards

This standard governs the normalization, execution, and validation of legal research, contract review, redlining, regulatory crosswalks, and SBOM license audits within `legal-router`. It enforces the ethical requirements of ABA Formal Opinion 512, ABA Model Rules of Professional Conduct (Rules 1.1, 1.6, 5.3, 5.5), and mandatory licensed attorney supervision.

Every work product produced under this standard is advisory only. This spoke does not practice law and does not provide legal advice to any person.

## Normalized request contract

Before executing any legal analysis, drafting, or audit, the agent MUST convert the user brief or task instructions into a normalized, machine-readable record conforming to [`legal-request-v1.schema.json`](./legal-request-v1.schema.json).

```text
Request/version: [id; version; operation: draft | review | redline | crosswalk | verify_citations | sbom_audit | memo]
Matter: [type: commercial | regulatory | IP | governance | privacy | dispute; confidentiality tier; matter id]
Jurisdiction: [primary jurisdiction; governing law; dispute resolution forum]
Intent: [primary objective; legal basis; risk tolerance; clauses to preserve]
Representations: [canonical representations; primary vs supporting; delivery format]
Constraints: [clause limits, liability caps, statutory deadlines, required provisions] (hard | soft)
References: [statutes, regulations, court dockets, precedent cases, SBOM manifests]
Privilege & safeguards: [supervising attorney required; UPL disclaimer required; ZDR endpoint; client data scrubbed]
Audience & delivery: [recipient role; format: markdown | docx | pdf | json; filing prohibited: true]
Provenance: [model tier; citation verifier run; timestamp]
Open questions: [jurisdictional ambiguities, missing factual predicates, conflicting authorities]
Review & handoff: [owner: authoring operator; reviewer: legal-ethics-reviewer; acceptance tests; advisory stamp]
```

## Hard and soft constraint rules

1. **Hard constraints**: Mandatory statutory requirements, non-negotiable contractual thresholds (e.g. mutual indemnification, 12-month liability cap, governing law), or procedural rules. If a hard constraint cannot be satisfied, the operation MUST halt and report the block to the reviewer.
2. **Soft constraints**: Style preferences, secondary negotiating points, or non-mandatory fallback provisions. Deviations must be recorded in the deliverable's deviation ledger.

## Mandatory advisory stamp and UPL safeguards

All generated memos, redlines, clause extracts, and compliance matrices MUST carry the non-waivable advisory legend:

```text
ADVISORY WORK PRODUCT - FOR PRELIMINARY RESEARCH PURPOSES ONLY - REQUIRES INDEPENDENT LICENSED ATTORNEY REVIEW - NOT LEGAL ADVICE - NOT AUTHORIZED FOR FILING OR CLIENT DELIVERY WITHOUT SUPERVISING ATTORNEY SIGN-OFF
```

Any attempt to produce filings for courts, agencies, or client signature without this stamp violates repository directives and will fail validation.
