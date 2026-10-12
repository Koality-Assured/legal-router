---
doc_kind: reference
canonical_id: us-law-state-oh
purpose: [reference]
topics: [us-law, ohio, statutes, courts]
rag_keywords: [Ohio, Ohio Constitution, Ohio Revised Code, Ohio Administrative Code, Supreme Court of Ohio]
version: captured-2026-10-07
publication: Ohio Laws (codes.ohio.gov)
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://codes.ohio.gov/
advisory_only: true
---

# Ohio

This is a point-in-time locator captured on 2026-10-07. It is not legal advice and it is not a filing.

codes.ohio.gov describes itself as Ohio's official online publication of state laws and regulations. The same page says Ohio law consists of the Ohio Constitution, the Ohio Revised Code, and the Ohio Administrative Code. The Supreme Court of Ohio site is the court of last resort. The Ohio Court of Appeals page is the intermediate appellate court.

## Sources

| Role | Authority | Title | URL | Status |
| --- | --- | --- | --- | --- |
| Constitution | official-primary | Ohio Constitution | https://codes.ohio.gov/ohio-constitution | 200 |
| Statutes | official-primary | Ohio Revised Code | https://codes.ohio.gov/ohio-revised-code | 200 |
| Session laws | official-primary | Acts, Ohio Legislature | https://www.legislature.ohio.gov/legislation/acts | 200 |
| Administrative code | official-primary | Ohio Administrative Code | https://codes.ohio.gov/ohio-administrative-code | 200 |
| Court of last resort | official-primary | Supreme Court of Ohio | https://www.supremecourt.ohio.gov/ | 200 |
| Intermediate appellate | official-primary | Ohio Court of Appeals | https://www.supremecourt.ohio.gov/courts/judicial-system/ohio-court-of-appeals/ | 200 |
| Dockets | official-primary | Public Docket | https://www.supremecourt.ohio.gov/clerk/ecms/ | 200 |
| Court rules | official-primary | Ohio Rules of Court | https://www.supremecourt.ohio.gov/laws-rules/ohio-rules-of-court/ | 200 |
| Attorney general opinions | official-primary | Opinions, Ohio Attorney General | https://www.ohioattorneygeneral.gov/About-AG/Service-Divisions/Formal-Opinions | 200 |

## Constitution

The constitution page links Articles I through XIX, plus a preamble. Article names beyond the roman numerals were not copied here.

## Statutes

The Revised Code page lists these titles:

- Title 1. State Government
- Title 3. Counties
- Title 5. Townships
- Title 7. Municipal Corporations
- Title 9. Agriculture-Animals-Fences
- Title 11. Banks-Savings and Loan Associations
- Title 13. Commercial Transactions
- Title 15. Conservation of Natural Resources
- Title 17. Corporations-Partnerships
- Title 19. Courts-Municipal-Mayor's-County
- Title 21. Courts-Probate-Juvenile
- Title 23. Courts-Common Pleas
- Title 25. Courts-Appellate
- Title 27. Courts-General Provisions-Special Remedies
- Title 29. Crimes-Procedure
- Title 31. Domestic Relations-Children
- Title 33. Education-Libraries
- Title 35. Elections
- Title 37. Health-Safety-Morals
- Title 39. Insurance
- Title 41. Labor and Industry
- Title 43. Liquor
- Title 45. Motor Vehicles-Aeronautics-Watercraft
- Title 47. Occupations-Professions
- Title 49. Public Utilities
- Title 51. Public Welfare
- Title 53. Real Property
- Title 55. Roads-Highways-Bridges
- Title 57. Taxation
- Title 58. Trusts
- Title 59. Veterans-Military Affairs
- Title 61. Water Supply-Sanitation-Ditches
- Title 63. Workforce Development

## Administrative code

The Ohio Administrative Code is published on codes.ohio.gov beside the Revised Code. The captured page is an agency index, not a second statutory title list.

## Courts and dockets

The Supreme Court of Ohio is the court of last resort. The Ohio Court of Appeals is the intermediate appellate court. The clerk's public docket at `/clerk/ecms/` returned HTTP 200. The static response is the online-docket application shell, with the description "Supreme Court of Ohio Online Docket."

## Rules and attorney general opinions

Ohio Rules of Court are published by the Supreme Court. The request to `/laws-rules/` redirected to `/laws-rules/ohio-rules-of-court/`. Formal opinions are published by the Ohio Attorney General.

## Matter map

Criminal matters start in Revised Code Title 29 (Crimes-Procedure). Court structure is in Titles 19, 21, 23, 25, and 27. Civil and evidence practice is in the Ohio Rules of Court. Administrative rules are in the Ohio Administrative Code.

## Local government

Counties are Title 3, townships are Title 5, and municipal corporations are Title 7. Those titles are state law about local units. Ordinances are adopted by the unit. This capture does not supply a municipal code URL.

## Capture notes

Checked with Invoke-WebRequest, HEAD then GET, 25-second timeout, on 2026-10-07. The acts URL redirected to `https://www.legislature.ohio.gov/legislation/acts/136`. Secretary of State Laws of Ohio pages returned HTTP 403: `https://www.ohiosos.gov/legislation-and-ballot-issues/laws-of-ohio/` and `.../bill-effective-dates/`. Two guessed Court of Appeals paths returned HTTP 404; the path recorded above returned HTTP 200.
