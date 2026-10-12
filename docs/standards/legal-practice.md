---
doc_kind: requirement
canonical_id: legal-practice
purpose: [requirement, reinforcement]
rank: high
topics: [legal, ethics, professional-responsibility, aba-opinion-512, upl]
rag_keywords: [legal-ethics, aba-model-rules, upl, citation-authenticity, confidentiality, attorney-review]
---

# Legal practice and ethical standards

## Scope and authoritative grounding

All automated research, contract analysis, and document drafting within `legal-router` must strictly conform to professional responsibility principles established under:
1. **ABA Formal Opinion 512** (Generative Artificial Intelligence Tools, July 2024).
2. **ABA Model Rules of Professional Conduct**:
   - **Rule 1.1 (Competence)**: Requires understanding the benefits and risks of technology, including verification of all algorithmic outputs.
   - **Rule 1.6 (Confidentiality)**: Requires protecting client-confidential data; prohibiting submission of confidential matter into unvetted public LLM endpoints lacking Zero Data Retention (ZDR).
   - **Rule 5.3 (Supervision of Nonlawyer Assistance)**: Requires active, independent human attorney supervision of all automated outputs.
   - **Rule 5.5 (Unauthorized Practice of Law)**: Prohibits nonlawyer systems from practicing law or offering legal advice.

## Non-negotiable practice rules

1. **Mandatory Advisory Legend**:
   Every deliverable produced by `legal-router` MUST display the standard advisory notice prominently on the first page or header:
   `ADVISORY WORK PRODUCT - FOR PRELIMINARY RESEARCH PURPOSES ONLY - REQUIRES INDEPENDENT LICENSED ATTORNEY REVIEW - NOT LEGAL ADVICE - NOT AUTHORIZED FOR FILING OR CLIENT DELIVERY WITHOUT SUPERVISING ATTORNEY SIGN-OFF`

2. **Zero Hallucination Citation Mandate**:
   - An agent MUST NOT invent, guess, or synthesize judicial citations or statutory references.
   - Every citation must be parsed and verified against local registries or primary API locators (CourtListener, GovInfo) using `verify_citations.py`.
   - Any citation that cannot be verified against primary sources MUST be explicitly flagged as `[UNVERIFIED CITATION]` in the deliverable.

3. **No Court Filings or Client Representation**:
   - Agents MUST NOT format, caption, or sign documents intended for direct filing with a court or regulatory tribunal.
   - All drafting is strictly preliminary internal work product for supervising legal counsel.

4. **Data Minimization and Confidentiality Safeguards**:
   - Synthetic matter identifiers and anonymized party names MUST be used for test fixtures and public examples.
   - Client secrets, real PII, or confidential deal terms must never be written to Git history.
