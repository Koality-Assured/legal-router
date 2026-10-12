---
doc_kind: reference
canonical_id: us-law-state-la
purpose: [reference]
topics: [us-law, louisiana, civil-law]
rag_keywords: [louisiana-civil-code, louisiana-revised-statutes, louisiana-constitution, louisiana-administrative-code]
version: captured-2026-10-07
publication: Louisiana State Legislature, Division of Administration, and Louisiana Supreme Court
captured_at_utc: "2026-10-07T18:00:00Z"
upstream_url: https://www.legis.la.gov/legis/lawsearch.aspx
advisory_only: true
---

# Louisiana

This capture is a point-in-time locator for attorney review. It is not legal advice and it is not a filing.

## Identity

Louisiana (LA) is a civil-law jurisdiction. The legislature publishes a Civil Code as its own code, beside the Revised Statutes, the Code of Civil Procedure, the Code of Criminal Procedure, the Code of Evidence, and the Children's Code. Do not describe Louisiana as a common-law state whose only compilation is a revised code. The Supreme Court of Louisiana is the court named on the supreme court site. This capture did not read a separate criminal court of last resort on that site.

## Source table

| Role | Publisher page | HTTP |
| --- | --- | --- |
| Codes and constitution | [Laws search](https://www.legis.la.gov/legis/lawsearch.aspx) | 200 |
| Revised Statutes titles | [Revised Statutes table of contents](https://legis.la.gov/legis/Laws_Toc.aspx?folder=75) | 200 |
| Administrative code | [Louisiana Administrative Code](https://www.doa.louisiana.gov/doa/osr/louisiana-administrative-code/) | 200 |
| Court opinions | [Supreme Court opinions](https://www.lasc.org/CourtActions/opinions) | 200 |
| Court rules | [Supreme Court rules](https://www.lasc.org/SupremeCourtRules) | 200 |
| Attorney general | [AG opinions](https://www.ag.state.la.us/Opinions) | 200 |

## Constitution

The laws search and the laws table of contents both name "Louisiana Constitution" and "Constitution Ancillaries" (HTTP 200). A constitution section page, `https://legis.la.gov/legis/Law.aspx?d=206475`, returned HTTP 200 and is the legislature's text of the supreme court provision. This capture does not copy that text. The fetched provision describes the supreme court's supervisory and appellate jurisdiction, including criminal matters limited to questions of law.

## Statutes

Official names on the legislature laws search (HTTP 200), which is the top-level index:

- Louisiana Constitution
- Constitution Ancillaries
- Civil Code
- Code of Civil Procedure
- Code of Criminal Procedure
- Code of Evidence
- Children's Code
- Revised Statutes

The same search page also lists House Rules, Senate Rules, and Joint Rules. Those are legislative rules, not the civil codes above. The search page states that laws have been updated through the 2025 First Extraordinary Session and points to a 2026 regular-session update list.

Revised Statutes titles on `https://legis.la.gov/legis/Laws_Toc.aspx?folder=75` (HTTP 200). Numbers 5 and 7 are not on that table. Title 14 is named Criminal Law on this official table.

- Title 1. General Provisions
- Title 2. Aeronautics
- Title 3. Agriculture and Forestry
- Title 4. Amusements and Sports
- Title 6. Banks and Banking
- Title 8. Cemeteries
- Title 9. Civil Code-Ancillaries
- Title 10. Commercial Laws
- Title 11. Consolidated Public Retirement
- Title 12. Corporations and Associations
- Title 13. Courts and Judicial Procedure
- Title 14. Criminal Law
- Title 15. Criminal Procedure
- Title 16. District Attorneys
- Title 17. Education
- Title 18. Louisiana Election Code
- Title 19. Expropriation
- Title 20. Homesteads and Exemptions
- Title 21. Hotels and Lodging Houses
- Title 22. Insurance
- Title 23. Labor and Worker's Compensation
- Title 24. Legislature and Laws
- Title 25. Libraries, Museums, and Other Scientific
- Title 26. Liquors-Alcoholic Beverages
- Title 27. Louisiana Gaming Control
- Title 28. Mental Health
- Title 29. Military, Naval, and Veteran's Affairs
- Title 30. Minerals, Oil, and Gas and Environmental Quality
- Title 31. Mineral Code
- Title 32. Motor Vehicles and Traffic Regulation
- Title 33. Municipalities and Parishes
- Title 34. Navigation and Shipping
- Title 35. Notaries Public and Commissioners
- Title 36. Organization of the Executive Branch
- Title 37. Professions and Occupations
- Title 38. Public Contracts, Works and Improvements
- Title 39. Public Finance
- Title 40. Public Health and Safety
- Title 41. Public Lands
- Title 42. Public Officers and Employees
- Title 43. Public Printing and Advertisements
- Title 44. Public Records and Recorders
- Title 45. Public Utilities and Carriers
- Title 46. Public Welfare and Assistance
- Title 47. Revenue and Taxation
- Title 48. Roads, Bridges and Ferries
- Title 49. State Administration
- Title 50. Surveys and Surveyors
- Title 51. Trade and Commerce
- Title 52. United States
- Title 53. War Emergency
- Title 54. Warehouses
- Title 55. Weights and Measures
- Title 56. Wildlife and Fisheries

## Administrative code

The Division of Administration, Office of the State Register, publishes the Louisiana Administrative Code at `https://www.doa.louisiana.gov/doa/osr/louisiana-administrative-code/` (HTTP 200). The page describes the code as the codified rules promulgated in the Louisiana Register. This capture does not copy rule text.

## Courts and dockets

`https://www.lasc.org/` returned HTTP 200. The home response is a client-rendered shell, so this check did not read a courts-of-appeal list from it. Opinion releases: `https://www.lasc.org/CourtActions/opinions` (HEAD 302, GET 200). No separate docket URL was verified. No separate criminal court of last resort was confirmed.

## Rules and attorney general

Supreme Court rules: `https://www.lasc.org/SupremeCourtRules` (HEAD 302, GET 200). The response body did not include a document title. Attorney General opinions: `https://www.ag.state.la.us/Opinions` (HTTP 200). The page describes opinions as advisory.

## Matter map

- Criminal: Code of Criminal Procedure, and Revised Statutes Title 14, Criminal Law, as named on the legislature table. The supreme court provision covers criminal appellate review of questions of law.
- Civil: Civil Code and Code of Civil Procedure. These are civil-law codes, not a common-law restatement.
- Administrative: Louisiana Administrative Code. Revised Statutes Title 49 is State Administration. Code of Evidence is its own code on the laws search.

## Local government

Revised Statutes Title 33 is Municipalities and Parishes. That is state law. Parish and municipal ordinances are published by each parish or municipality. This capture does not invent those codes. See [`../local-government.md`](../local-government.md).

## Capture notes

Checked 2026-10-07 with PowerShell `Invoke-WebRequest`, HEAD then GET, 25-second timeout. A separate acts pamphlet URL was not verified. The laws search page states the session through which the codified laws were updated.
