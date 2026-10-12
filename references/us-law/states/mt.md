---
doc_kind: reference
canonical_id: us-law-state-mt
purpose: [reference]
topics: [us-law, montana, statutes, courts]
rag_keywords: [Montana, Montana Code Annotated, constitution, session laws, administrative rules, supreme court]
version: captured-2026-10-07
publication: Montana Legislature and Montana Judicial Branch
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://mca.legmt.gov/bills/mca/index.html
advisory_only: true
---

# Montana law sources

This page is an advisory point-in-time map of official sources. It is not legal advice and it does not reproduce statutory text.

## Identity

Montana (MT) is a state. The court of last resort is the Montana Supreme Court. The verified courts index lists the Supreme Court, district courts, the Water Court, courts of limited jurisdiction, and specialty courts. It does not list an intermediate court of appeals.

## Source table

| Role | Authority | HTTP | URL |
| --- | --- | --- | --- |
| Constitution | official-primary | 200 | https://mca.legmt.gov/bills/mca/title_0000/chapters_index.html |
| Statutes | official-primary | 200 | https://mca.legmt.gov/bills/mca/index.html |
| Statutes portal | official-primary | 200 | https://www.legmt.gov/statute/ |
| Session laws | official-primary | 200 | https://www.legmt.gov/statute/archives/ |
| Administrative rules | official-primary | 200 | https://rules.mt.gov/ |
| Court of last resort | official-primary | 200 | https://courts.mt.gov/Courts/Supreme/ |
| Dockets | official-primary | 200 | https://juddocumentservice.mt.gov/instructions |
| Clerk of court | official-primary | 200 | https://courts.mt.gov/clerk/ |
| Court rules | official-primary | 200 | https://courts.mt.gov/Courts/Rules/ |

## Constitution

The constitution is Title 0000 of the Montana Code Annotated. `https://leg.mt.gov/bills/mca/title_0000/chapters_index.html` returned HTTP 200 and landed on the `mca.legmt.gov` URL in the table.

## Statutes

The MCA index HTML lists 67 titles. Some numbers are marked Reserved.

- TITLE 1. GENERAL LAWS AND DEFINITIONS
- TITLE 2. GOVERNMENT STRUCTURE AND ADMINISTRATION
- TITLE 3. JUDICIARY, COURTS
- TITLE 4. Reserved
- TITLE 5. LEGISLATIVE BRANCH
- TITLE 6. Reserved
- TITLE 7. LOCAL GOVERNMENT
- TITLE 10. MILITARY AFFAIRS AND DISASTER AND EMERGENCY SERVICES
- TITLE 13. ELECTIONS
- TITLE 14. Reserved
- TITLE 15. TAXATION
- TITLE 16. ALCOHOL, TOBACCO, AND MARIJUANA
- TITLE 17. STATE FINANCE
- TITLE 18. PUBLIC CONTRACTS
- TITLE 19. PUBLIC RETIREMENT SYSTEMS
- TITLE 20. EDUCATION
- TITLE 21. Reserved
- TITLE 22. LIBRARIES, ARTS, AND ANTIQUITIES
- TITLE 23. PARKS, RECREATION, SPORTS, AND GAMBLING
- TITLE 24. Reserved
- TITLE 25. CIVIL PROCEDURE
- TITLE 26. EVIDENCE
- TITLE 27. CIVIL LIABILITY, REMEDIES, AND LIMITATIONS
- TITLE 28. CONTRACTS AND OTHER OBLIGATIONS
- TITLE 29. Reserved
- TITLE 30. TRADE AND COMMERCE
- TITLE 31. CREDIT TRANSACTIONS AND RELATIONSHIPS
- TITLE 32. FINANCIAL INSTITUTIONS
- TITLE 33. INSURANCE AND INSURANCE COMPANIES
- TITLE 34. Reserved
- TITLE 35. CORPORATIONS, PARTNERSHIPS, AND ASSOCIATIONS
- TITLE 36. Reserved
- TITLE 37. PROFESSIONS AND OCCUPATIONS
- TITLE 38. Reserved
- TITLE 39. LABOR
- TITLE 40. FAMILY LAW
- TITLE 41. MINORS
- TITLE 42. ADOPTION
- TITLE 43. Reserved
- TITLE 44. LAW ENFORCEMENT
- TITLE 45. CRIMES
- TITLE 46. CRIMINAL PROCEDURE
- TITLE 47. ACCESS TO LEGAL SERVICES
- TITLE 48. Reserved
- TITLE 49. HUMAN RIGHTS
- TITLE 50. HEALTH AND SAFETY
- TITLE 51. Reserved
- TITLE 52. FAMILY SERVICES
- TITLE 53. SOCIAL SERVICES AND INSTITUTIONS
- TITLE 60. HIGHWAYS AND TRANSPORTATION
- TITLE 61. MOTOR VEHICLES
- TITLE 67. AERONAUTICS
- TITLE 68. Reserved
- TITLE 69. PUBLIC UTILITIES AND CARRIERS
- TITLE 70. PROPERTY
- TITLE 71. MORTGAGES, PLEDGES, AND LIENS
- TITLE 72. ESTATES, TRUSTS, AND FIDUCIARY RELATIONSHIPS
- TITLE 75. ENVIRONMENTAL PROTECTION
- TITLE 76. LAND RESOURCES AND USE
- TITLE 77. STATE LANDS
- TITLE 80. AGRICULTURE
- TITLE 81. LIVESTOCK
- TITLE 82. MINERALS, OIL, AND GAS
- TITLE 85. WATER USE
- TITLE 86. Reserved
- TITLE 87. FISH AND WILDLIFE
- TITLE 90. PLANNING, RESEARCH, AND DEVELOPMENT

The Legislature statute page describes the MCA as the constitution plus codified statutes, updated after each session. The archives page lists session-law PDF volumes, including 2025.

## Administrative code

`https://rules.mt.gov/` returned HTTP 200 as a short shell for the Administrative Rules of Montana.

## Courts and dockets

The Supreme Court page is the court of last resort. The clerk page points to a public docket search. `https://juddocumentservice.mt.gov/instructions` returned HTTP 200 as the docket-search instructions. The Water Court is a specialized court on the courts index, not a general intermediate appellate court.

## Rules and attorney general

Court rules are at the rules URL above. `https://dojmt.gov/attorney-generals-office/attorney-general-opinions/` returned HTTP 403, so no attorney general opinions URL is cataloged.

## Matter map

Crimes are Title 45 and criminal procedure is Title 46. Civil procedure is Title 25 and evidence is Title 26. Courts are Title 3. Administrative rules are the ARM. Title 2 is Government Structure and Administration.

## Local government

Title 7 is Local Government. To locate ordinances for a named city, use that city's official website and the city clerk, or the municipal code the city itself publishes. This capture does not record county or city code URLs.

## Capture notes

Checks used PowerShell Invoke-WebRequest HEAD then GET, 25-second timeout, on 2026-10-07. Title lines were taken from the MCA index HTML. The legacy `leg.mt.gov` MCA URLs redirected to `mca.legmt.gov` with HTTP 200.
