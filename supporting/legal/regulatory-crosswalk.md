---
doc_kind: recipe
canonical_id: regulatory-crosswalk
purpose: [recipe]
rank: high
topics: [legal, eu-ai-act, gdpr]
rag_keywords: [annex-iii, celex, article-32]
---

# Regulatory crosswalk

Pin primary law. Checklist against Annex III and Articles 6-7, not an automated verdict.

## Pins

- EU AI Act: Regulation (EU) 2024/1689, CELEX 32024R1689, consolidated 02024R1689-20260727, ELI `http://data.europa.eu/eli/reg/2024/1689/oj`.
- GDPR: Regulation (EU) 2016/679 Arts. 28 and 32.
- HIPAA Security Rule technical safeguards: 45 C.F.R. § 164.312 when a fixture names HIPAA.

## MUST

- Use `scripts/legal/fixtures/regulatory/annex-iii-checklist.json` for the eight Annex III areas.
- Record whether Annex III point 8(a) (judicial-authority legal research) could apply; counsel decides.
- Re-pin CELEX when the Commission amends Annex III (Article 7).

## MUST NOT

- Output "high-risk" or "compliant" as a system decision.
