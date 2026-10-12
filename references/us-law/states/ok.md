---
doc_kind: reference
canonical_id: us-law-state-ok
purpose: [reference]
topics: [us-law, oklahoma]
rag_keywords: [oklahoma-statutes, oklahoma-constitution, oscn, court-of-criminal-appeals, oklahoma-administrative-code]
version: captured-2026-10-07
publication: Oklahoma Legislature, Secretary of State, and OSCN
captured_at_utc: "2026-10-07T18:00:00Z"
upstream_url: https://www.oklegislature.gov/osstatuestitle.aspx
advisory_only: true
---

# Oklahoma

This capture is a point-in-time locator for attorney review. It is not legal advice and it is not a filing.

## Identity

Oklahoma (OK). The Oklahoma State Courts Network courts page states that the court system is the Supreme Court, the Court of Criminal Appeals, the Court of Civil Appeals, and 77 district courts. It states that Oklahoma has two courts of last resort: the Supreme Court determines issues of a civil nature, and the Court of Criminal Appeals decides criminal matters. The Court of Civil Appeals is not described there as a court of last resort.

## Source table

| Role | Publisher page | HTTP |
| --- | --- | --- |
| Constitution | [OSCN Oklahoma Constitution index](https://www.oscn.net/applications/oscn/Index.asp?ftdb=STOKCN&level=1) | 200 |
| Statutes | [Oklahoma Statutes title page](https://www.oklegislature.gov/osstatuestitle.aspx) | 200 |
| Session laws | [OSCN session laws](https://www.oscn.net/applications/oscn/index.asp?ftdb=STOKLG&level=1) | 200 |
| Administrative code | [rules.ok.gov home](https://rules.ok.gov/home) | 403 |
| Court opinions | [Oklahoma Supreme Court](https://oksc.oscn.net/) | 200 |
| Criminal court | [Court of Criminal Appeals](https://okcca.net/) | 200 |
| Dockets | [OSCN docket search](https://www.oscn.net/dockets/search.aspx#all) | 200 |
| Court rules | [OSCN Supreme Court Rules](https://www.oscn.net/applications/oscn/index.asp?ftdb=STOKRUCPSC&level=1) | 200 |
| Attorney general | [AG opinions](https://oklahoma.gov/oag/opinions.html) | 200 |

## Constitution

OSCN publishes an Oklahoma Constitution document index (database STOKCN). The legislature also publishes a constitution page at `https://www.oklegislature.gov/ok_constitution.aspx` (HTTP 200). Use the live page for article text. This capture does not copy it.

## Statutes

The official title page `https://www.oklegislature.gov/osstatuestitle.aspx` (HTTP 200) embeds `https://www.oklegislature.gov/osStatuesTitle.html` (HTTP 200). That embedded index says the constitution and statutes were last updated on November 18, 2025. Each listed title links to a PDF under `https://www.oklegislature.gov/OK_Statutes/CompleteTitles/`. This capture did not request each PDF.

The index lists Title 38 twice, once before Title 37A and once after it. The lines below keep one line per title, in first-seen order. Numbers absent from the index are 35, 48, 55, 77, and 81. Parenthetical "see" notes are the index's own cross-references, not statute text.

- Title 1. Abstracting (See 74, State Government)
- Title 2. Agriculture
- Title 3. Aircraft and Airports
- Title 3A. Amusements and Sports
- Title 4. Animals
- Title 5. Attorneys and State Bar
- Title 6. Banks and Trust Companies
- Title 7. Blind Persons
- Title 8. Cemeteries
- Title 9. Census (See 14, Congressional and Legislative Districts)
- Title 10. Children
- Title 10A. Children and Juvenile Code
- Title 11. Cities and Towns
- Title 12. Civil Procedure
- Title 12A. Commercial Code
- Title 13. Common Carriers
- Title 14. Congressional and Legislative Districts
- Title 14A. Consumer Credit Code
- Title 15. Contracts
- Title 16. Conveyances
- Title 17. Corporation Commission
- Title 18. Corporations
- Title 19. Counties and County Officers
- Title 20. Courts
- Title 21. Crimes and Punishments
- Title 22. Criminal Procedure
- Title 23. Damages
- Title 24. Debtor and Creditor
- Title 25. Definitions and General Provisions
- Title 26. Elections
- Title 27. Eminent Domain
- Title 27A. Environment and Natural Resources
- Title 28. Fees
- Title 29. Game and Fish
- Title 30. Guardian and Ward
- Title 31. Homestead and Exemptions
- Title 32. Husband and Wife (See 43, Marriage and Family)
- Title 33. Inebriates (See 63, Public Health and Safety)
- Title 34. Initiative and Referendum
- Title 36. Insurance
- Title 37. Intoxicating Liquors
- Title 37A. Alcoholic Beverage
- Title 38. Jurors
- Title 39. Justices and Constables (See 12, Civil Procedure and 22, Criminal Procedure)
- Title 40. Labor
- Title 41. Landlord and Tenant
- Title 42. Liens
- Title 43. Marriage and Family
- Title 43A. Mental Health
- Title 44. Militia
- Title 45. Mines and Mining
- Title 46. Mortgages
- Title 47. Motor Vehicles
- Title 49. Notaries Public
- Title 50. Nuisances
- Title 51. Officers
- Title 52. Oil and Gas
- Title 53. Oklahoma Historical Societies and Associations
- Title 54. Partnership
- Title 56. Poor Persons
- Title 57. Prisons and Reformatories
- Title 58. Probate Procedure
- Title 59. Professions and Occupations
- Title 60. Property
- Title 61. Public Buildings and Public Works
- Title 62. Public Finance
- Title 63. Public Health and Safety
- Title 64. Public Lands
- Title 65. Public Libraries
- Title 66. Railroads
- Title 67. Records
- Title 68. Revenue and Taxation
- Title 69. Roads Bridges and Ferries
- Title 70. Schools
- Title 71. Securities
- Title 72. Soldiers and Sailors
- Title 73. State Capital and Capitol Building
- Title 74. State Government
- Title 74E. Ethics Rules
- Title 75. Statutes and Reports
- Title 76. Torts
- Title 78. Trademarks and Labels
- Title 79. Trusts and Pools
- Title 80. United States
- Title 82. Waters and Water Rights
- Title 83. Weights and Measures
- Title 84. Wills and Succession
- Title 85. Workers' Compensation
- Title 85A. Administrative Workers' Compensation System

The Secretary of State distribution page (`https://www.sos.ok.gov/gov/annualDistribution.aspx`, HTTP 200) describes electronic official statutes, session laws, and the constitution, and it links those compilations to `govt.westlaw.com`. This capture does not rank that Westlaw host as official-primary and does not copy it.

## Administrative code

The Secretary of State sitemap points at `https://rules.ok.gov/` and at older Office of Administrative Rules paths. On this check, `https://rules.ok.gov/home` and `https://rules.ok.gov/code` returned HTTP 403. `https://www.sos.ok.gov/oar/online/viewCode.aspx`, `https://www.sos.ok.gov/oar/onlineRegister.aspx`, and `https://www.sos.ok.gov/oar/contact.aspx` returned HTTP 401. No browsable Oklahoma Administrative Code text is included. `https://www.sos.ok.gov/home/rules.aspx` (HTTP 200) is the Secretary of State's own rules page, not the code.

## Courts and dockets

OSCN (`https://www.oscn.net/`, HTTP 200) is the court network. The Supreme Court site is `https://oksc.oscn.net/` (HTTP 200). Supreme Court orders are at `https://www.oscn.net/orders/` (HTTP 200). The Court of Criminal Appeals site is `https://okcca.net/` (HTTP 200). OSCN also indexes Attorney General opinions (STOKAG, HTTP 200) and Supreme Court opinions through the network search.

Docket search: `https://www.oscn.net/dockets/search.aspx#all`. HEAD and GET of the URL without the fragment returned HTTP 200. The fragment is not sent to the server. The courts page says there are 77 district courts and lists counties. That list is the district-court map, not 77 county codes.

## Rules and attorney general

OSCN indexes Oklahoma Supreme Court Rules (STOKRUCPSC, HTTP 200). Rule amendments also appear on the orders page. Attorney General opinions are at `https://oklahoma.gov/oag/opinions.html` (HTTP 200). The page describes opinion practice; this capture does not copy opinions. OSCN's STOKAG index is a second official opinions locator (HTTP 200).

## Matter map

- Criminal: Title 21, Crimes and Punishments, and Title 22, Criminal Procedure, on the legislature index. Appellate criminal matters go to the Court of Criminal Appeals, which OSCN describes as the criminal court of last resort.
- Civil: Title 12, Civil Procedure, and the Supreme Court for civil issues. The Court of Civil Appeals is the intermediate civil appellate court named on the OSCN courts page.
- Administrative: agency rules are the Oklahoma Administrative Code, whose public portal did not return a readable page on this check. Title 75 on the statutes index is Statutes and Reports.

## Local government

Do not invent 77 county codes. OSCN district-court dockets are case records for the district courts. A city ordinance is published by that city. Start from the city's official site. See [`../local-government.md`](../local-government.md). Title 11 on the statutes index is Cities and Towns, which is state law about municipalities, not a municipal code.

## Capture notes

Checked 2026-10-07 with PowerShell `Invoke-WebRequest`, HEAD then GET, 25-second timeout. The three supplied locators resolved: docket search HTTP 200, statutes title page HTTP 200, and Supreme Court orders HTTP 200. The administrative-code portal and the older OAR viewer did not. Session laws are also on the Secretary of State enrolled-legislation page `https://www.sos.ok.gov/gov/legislation.aspx` (HTTP 200) and the OSCN session-law index (HTTP 200).
