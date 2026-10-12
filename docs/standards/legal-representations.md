---
doc_kind: requirement
canonical_id: legal-representations
purpose: [requirement, reinforcement]
rank: high
topics: [legal, representations, registry, check-profiles]
rag_keywords: [legal-representations, contract, statutory, case-law, spdx, redline, legal-memo]
---

# Legal representations standard

## Scope and purpose

This standard establishes the normative taxonomy of legal representations recognized by `legal-router`. Each representation defines an authoritative domain asset family, valid aliases, adjacent transformation routes, allowed asset types, and mandatory check profiles.

Machine-readable mapping is codified in [`legal-representation-registry.json`](./legal-representation-registry.json).

## Representation matrix

### 1. Commercial contracts (`commercial_contract`)
Covers transactional agreements including SaaS contracts, non-disclosure agreements (NDAs), data processing agreements (DPAs), and master services agreements (MSAs).
- **Check profiles**: `contract_clause`, `privacy_crosswalk`.
- **Key controls**: Identification of mutual vs unilateral obligations, liability caps (multiple of fees paid), indemnity carve-outs, IP ownership transfer vs license grant, and governing law clauses.

### 2. Statutory provisions (`statutory_citation`)
Covers enacted federal statutes (U.S. Code, Public Laws) and state statutory codes.
- **Check profiles**: `statutory_compliance`.
- **Key controls**: Title, section, pin-cite accuracy, enactment status, effective date, and verification against official GPO GovInfo packages. Cornell LII is an informative reading copy only.

### 3. Case precedent (`case_precedent`)
Covers published and precedential judicial opinions from federal and state appellate courts.
- **Check profiles**: `case_citation`.
- **Key controls**: Bluebook citation format (Volume, Reporter, First Page, Pin Cite, Court, Year), verification against CourtListener cluster databases, and hallucination prevention. Every citation must resolve to an authentic decision or be flagged as unverified.

### 4. Open-source licenses (`spdx_license`)
Covers software package licenses, Software Bill of Materials (SBOMs), and CycloneDX manifests.
- **Check profiles**: `license_compliance`.
- **Key controls**: SPDX 3.0.1 valid identifiers, operator syntax (`AND`, `OR`, `WITH`), copyleft categorization (permissive, weak copyleft, strong copyleft, network copyleft/AGPL), and dual-license compatibility.

### 5. Regulatory crosswalk matrices (`regulatory_crosswalk`)
Covers mappings between technical/organizational architectures and regulatory frameworks (e.g. EU AI Act Annex III, GDPR Chapter V, HIPAA Security Rule).
- **Check profiles**: `privacy_crosswalk`, `statutory_compliance`.
- **Key controls**: Accurate Article/Section citation, compliance posture scoring (Compliant, Partially Compliant, Non-Compliant), and documented mitigation strategies.

### 6. Contract redlines (`contract_redline`)
Covers markup comparisons between baseline contract drafts and proposed revisions.
- **Check profiles**: `redline_diff`, `contract_clause`.
- **Key controls**: Clause-by-clause tracking, deletion/insertion categorization, materiality scoring, and preservation of standard boilerplate.

### 7. Legal analysis memos (`legal_memo`)
Covers synthesized legal research, deal risk assessments, and policy analysis documents.
- **Check profiles**: `legal_memo`, `case_citation`.
- **Key controls**: IRAC/CREAC analytical structure, Bluebook citation integration, executive summary, and mandatory advisory disclaimer.
