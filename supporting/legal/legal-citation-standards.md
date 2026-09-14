---
doc_kind: recipe
canonical_id: legal-citation-standards
purpose: [recipe]
rank: high
topics: [legal, citations]
rag_keywords: [courtlistener, govinfo, bluebook, hallucination]
---

# Legal citation standards

Offline fixture verification is the baseline. Live registries are opt-in.

## MUST

- Stamp every report `ADVISORY WORK PRODUCT - REQUIRES LICENSED ATTORNEY REVIEW`.
- Flag planted fake reporters (`Fake. Rep.`, `F.4d`, `Halluc. 2d`) as hallucinated.
- Leave parsed-but-unknown cites as `unverified`. Do not silently accept them.
- Read `COURTLISTENER_API_TOKEN` from the environment only. Never log it.
- Prefer GovInfo packages for USC / Federal Register. Cornell LII is human-facing, not a documented public REST twin.

## MUST NOT

- Redistribute The Bluebook tables.
- Claim zero hallucination.
- Scrape LII HTML as a substitute for GovInfo when an official package exists.

## Commands

```bash
python scripts/legal/verify_citations.py --dry-run --json
python scripts/legal/verify_citations.py --file scripts/legal/fixtures/citations/mixed-memo.md --json
```

CourtListener lookup (optional): POST `https://www.courtlistener.com/api/rest/v4/citation-lookup/` with documented caps (60 valid cites/minute, 250 lookups/request). Status 200 found, 404 valid-but-not-in-CL, 400 unknown reporter.
