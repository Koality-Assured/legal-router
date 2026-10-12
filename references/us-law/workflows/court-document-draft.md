---
doc_kind: process
canonical_id: us-law-workflow-court-document
purpose: [process]
topics: [us-law, courts]
rag_keywords: [us-law-court-document-draft, advisory-stamp, pleading, motion]
rank: high
---

# Draft advisory court documents

Future skill name: `us-law-court-document-draft`. Owner: `document-operator`. Isolation: mutate only the draft the person asked to store. Default is to return the draft in session.

## When to use

The person asks for a complaint, answer, motion, proposed order, notice of appeal, or similar paper grounded in a named sovereign's rules.

## When not to use

Legal advice, filing strategy, or a paper for a real client matter without the person supplying the facts in the immediate turn. Locator refresh is `maintain.md`. Authority research is `interpretation-research.md`.

## Criticality

High. The draft is not a filing. Filing deadlines, service, and local rules change the paper. Missing a local rule is a stop, not a guess.

## Source of truth

Court-rules links on the jurisdiction page, plus the federal rules page when the forum is federal. Caption and signature blocks follow the fetched rule, not a generic sample.

## Isolation

Do not commit client facts. If a draft must be saved, put it under `scratch/` and say so. Promote nothing to `results/` unless the person asks for a finished, de-identified example.

## How to use

1. Require forum (court, not just state), matter class, document type, and parties as the person stated them. If the forum is missing, ask. Oklahoma criminal cases are not automatically Oklahoma Supreme Court cases; use the criminal court of last resort only when `states/ok.md` confirms it and the matter is criminal.
2. Fetch the governing rules from the official URL on the jurisdiction page: civil, criminal, evidence, or appellate, matching the document type.
3. Build a skeleton that maps each section to a rule cited from that fetch: caption, parties, jurisdiction statement, numbered allegations or grounds, prayer or relief, certificate of service, signature. Omit a section when no fetched rule covers it, and label the omission.
4. Put no case citation in the draft unless `interpretation-research.md` fetched that opinion in this effort. Otherwise write `[citation unverified — do not file]`.
5. Top of the draft, verbatim:

   `ADVISORY DRAFT — NOT LEGAL ADVICE — NOT FOR FILING — REQUIRES LICENSED ATTORNEY REVIEW`

6. Do not include a filing fee, a bar number, or a representation that the signer is counsel.

## Dry run

List the rule URLs a federal civil motion skeleton would need from the inferior-courts page. Do not draft the motion.

## Security

No real personal data, account numbers, or minors' identifying facts in the repository. No PACER login. This workflow does not authorize anyone to practice law.

## Completion gates

No reference update unless a rule URL was newly verified. That update is a maintain handoff.
