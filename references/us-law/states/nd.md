---
doc_kind: reference
canonical_id: us-law-state-nd
purpose: [reference]
topics: [us-law, north-dakota, statutes, courts]
rag_keywords: [North Dakota, Century Code, constitution, administrative code, supreme court, attorney general]
version: captured-2026-10-07
publication: North Dakota Legislative Branch, North Dakota Court System, and Office of Attorney General
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://ndlegis.gov/constitution
advisory_only: true
---

# North Dakota law sources

This page is an advisory point-in-time map of official sources. It is not legal advice and it does not reproduce statutory text.

## Identity

North Dakota (ND) is a state. The court of last resort is the North Dakota Supreme Court. The Judicial Branch about-us page also identifies a Court of Appeals. Trial courts are district courts. Municipal courts are listed separately on the court site.

## Source table

| Role | Authority | HTTP | URL |
| --- | --- | --- | --- |
| Constitution | official-primary | 200 | https://ndlegis.gov/constitution |
| Statutes | official-primary | 200 | https://ndlegis.gov/prod/general-information/north-dakota-century-code/ |
| Session laws | official-primary | 200 | https://ndlegis.gov/research-and-archives/session-laws |
| Administrative code | official-primary | 200 | https://ndlegis.gov/prod/agency-rules/north-dakota-administrative-code/ |
| Court of last resort | official-primary | 200 | https://www.ndcourts.gov/supreme-court |
| Intermediate appellate | official-primary | 200 | https://www.ndcourts.gov/about-us |
| Appellate dockets | official-primary | 200 | https://www.ndcourts.gov/supreme-court/docket-search |
| Trial-court public access | official-primary | 200 | https://www.ndcourts.gov/public-access |
| Court rules | official-primary | 200 | https://www.ndcourts.gov/legal-resources/rules |
| Attorney general opinions | official-primary | 200 | https://attorneygeneral.nd.gov/attorney-generals-office/legal-opinions/ |

## Constitution

The Legislative Branch publishes the current constitution, with articles and the transition schedule, at the constitution URL above.

## Statutes

The Legislative Branch states that the Century Code text on its site is the official version. The same page’s title index, captured from the HTML, has 74 top-level titles:

- Title 1 - General Provisions
- Title 2 - Aeronautics
- Title 3 - Agency
- Title 4 - Agriculture
- Title 4.1 - Agriculture
- Title 5 - Alcoholic Beverages
- Title 6 - Banks and Banking
- Title 7 - Building and Loan Associations
- Title 8 - Carriage
- Title 9 - Contracts and Obligations
- Title 10 - Corporations
- Title 11 - Counties
- Title 12 - Corrections, Parole, and Probation
- Title 12.1 - Criminal Code
- Title 13 - Debtor and Creditor Relationship
- Title 14 - Domestic Relations and Persons
- Title 15 - Education
- Title 15.1 - Elementary and Secondary Education
- Title 16 - Elections
- Title 16.1 - Elections
- Title 17 - Energy
- Title 18 - Fires
- Title 19 - Foods, Drugs, Oils, and Compounds
- Title 20 - Game, Fish, and Predators
- Title 20.1 - Game, Fish, Predators, and Boating
- Title 21 - Governmental Finance
- Title 22 - Guaranty, Indemnity, and Suretyship
- Title 23 - Health and Safety
- Title 23.1 - Environmental Quality
- Title 24 - Highways, Bridges, and Ferries
- Title 25 - Mental and Physical Illness or Disability
- Title 26 - Insurance
- Title 26.1 - Insurance
- Title 27 - Judicial Branch of Government
- Title 28 - Judicial Procedure, Civil
- Title 29 - Judicial Procedure, Criminal
- Title 30 - Judicial Procedure, Probate
- Title 30.1 - Uniform Probate Code
- Title 31 - Judicial Proof
- Title 32 - Judicial Remedies
- Title 33 - County Justice Court
- Title 34 - Labor and Employment
- Title 35 - Liens
- Title 36 - Livestock
- Title 37 - Military
- Title 38 - Mining and Gas and Oil Production
- Title 39 - Motor Vehicles
- Title 40 - Municipal Government
- Title 41 - Uniform Commercial Code
- Title 42 - Nuisances
- Title 43 - Occupations and Professions
- Title 44 - Offices and Officers
- Title 45 - Partnerships
- Title 46 - Printing Laws
- Title 47 - Property
- Title 48 - Public Buildings
- Title 49 - Public Utilities
- Title 50 - Public Welfare
- Title 51 - Sales and Exchanges
- Title 52 - Social Security
- Title 53 - Sports and Amusements
- Title 54 - State Government
- Title 55 - State Historical Society and State Parks
- Title 56 - Succession and Wills
- Title 57 - Taxation
- Title 58 - Townships
- Title 59 - Trusts, Uses, and Powers
- Title 60 - Warehousing and Deposits
- Title 61 - Waters
- Title 62 - Weapons
- Title 62.1 - Weapons
- Title 63 - Weeds
- Title 64 - Weights, Measures, and Grades
- Title 65 - Workforce Safety and Insurance

Session laws for regular and special sessions are indexed by the Legislative Branch at the session-laws URL.

## Administrative code

The North Dakota Administrative Code is the Legislative Branch compilation of administrative agency rules. The title index on that page is an agency list, longer than the statutory title list, and is not copied here.

## Courts and dockets

The Supreme Court page is the court of last resort. Appellate public records are searched from the docket-search page. District-court case search and fine payment are on the public-access page. The about-us page names the Court of Appeals alongside the Supreme Court and district courts.

## Rules and attorney general

Court rules are published by the court system. The Attorney General publishes legal opinions and states that an opinion governs public officials until a court decides the question. The opinions page also limits who may request an opinion.

## Matter map

Criminal matters are indexed under Title 12.1, Criminal Code, and Title 29, Judicial Procedure, Criminal. Civil procedure is Title 28, Judicial Procedure, Civil. Judicial proof is Title 31. Courts are Title 27. Administrative rules are in the Administrative Code. The published Century Code also contains an Administrative Agencies Practice Act chapter under the civil judicial-procedure title.

## Local government

Title 40 is Municipal Government. To locate ordinances for a named city, use that city’s official website and the city clerk, or the municipal code the city itself publishes. This capture does not record county or city code URLs. The court site’s municipal-courts page identifies municipal courts; it is not an ordinance code.

## Capture notes

Checks used PowerShell `Invoke-WebRequest` HEAD then GET, 25-second timeout, on 2026-10-07. Cited URLs returned HTTP 200 on both methods. `https://www.ndcourts.gov/supreme-court/opinions` returned HTTP 403 on HEAD and GET, so it is not listed. The Century Code title lines were taken from that page’s HTML, not from statute section text.
