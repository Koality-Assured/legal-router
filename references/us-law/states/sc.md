---
doc_kind: reference
canonical_id: us-law-state-sc
purpose: [reference]
topics: [us-law, south-carolina]
rag_keywords: [South Carolina, South Carolina Code of Laws, Supreme Court of South Carolina, South Carolina Court of Appeals]
version: captured-2026-10-07
publication: South Carolina Legislature Online
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://www.scstatehouse.gov/code/statmast.php
advisory_only: true
---

# South Carolina

Advisory capture of official entry points. This is not legal advice and it does not reproduce statutory, regulatory, or opinion text.

## Identity

The South Carolina General Assembly publishes the Code of Laws, the constitution, and the Code of Regulations. The code page says the website version is not official and that the published volumes contain the official text. The Judicial Branch identifies the Supreme Court and the Court of Appeals.

## Sources

| Role | Authority | HTTP | Entry |
| --- | --- | --- | --- |
| constitution | official-primary | 200 | [South Carolina Constitution](https://www.scstatehouse.gov/scconstitution/scconst.php) |
| statutes | official-mirror | 200 | [South Carolina Code of Laws](https://www.scstatehouse.gov/code/statmast.php) |
| session laws | official-primary | 200 | [South Carolina Legislature Online - Legislation](https://www.scstatehouse.gov/legislation.php) |
| administrative code | official-mirror | 200 | [South Carolina Code of Regulations](https://www.scstatehouse.gov/coderegs/statmast.php) |
| court of last resort opinions | official-primary | 200 | [Opinions - South Carolina Judicial Branch](https://www.sccourts.org/opinions-orders/opinions/) |
| intermediate appellate court | official-primary | 200 | [Court of Appeals - South Carolina Judicial Branch](https://www.sccourts.org/courts/court-of-appeals/) |
| court rules | official-primary | 200 | [Court Rules - South Carolina Judicial Branch](https://www.sccourts.org/resources/judicial-community/court-rules/) |
| attorney general opinions | official-primary | 200 | [Opinions - South Carolina Attorney General](https://www.scag.gov/opinions/) |
| administrative code | official-primary | 200 | [South Carolina State Register](https://www.scstatehouse.gov/state_register.php) |
| court of last resort opinions | official-primary | 200 | [Supreme Court - South Carolina Judicial Branch](https://www.sccourts.org/courts/supreme-court/) |

## Constitution

The General Assembly publishes the South Carolina Constitution on the legislature site.

## Statutes

The Code of Laws index has 63 titles. The page says the website copy is not the official text and that the current published volumes are the official version.

- Title 1 - Administration of the Government
- Title 2 - General Assembly
- Title 3 - U.S. Government, Agreements and Relations With
- Title 4 - Counties
- Title 5 - Municipal Corporations
- Title 6 - Local Government - Provisions Applicable to Special Purpose Districts and Other Political Subdivisions
- Title 7 - Elections
- Title 8 - Public Officers and Employees
- Title 9 - Retirement Systems
- Title 10 - Public Buildings and Property
- Title 11 - Public Finance
- Title 12 - Taxation
- Title 13 - Planning, Research and Development
- Title 14 - Courts
- Title 15 - Civil Remedies and Procedures
- Title 16 - Crimes and Offenses
- Title 17 - Criminal Procedures
- Title 18 - Appeals
- Title 19 - Evidence
- Title 20 - Domestic Relations
- Title 21 - Estates, Trusts, Guardians and Fiduciaries
- Title 22 - Magistrates and Constables
- Title 23 - Law Enforcement and Public Safety
- Title 24 - Corrections, Jails, Probations, Paroles and Pardons
- Title 25 - Military, Civil Defense and Veterans Affairs
- Title 26 - Notaries Public and Acknowledgements
- Title 27 - Property and Conveyances
- Title 28 - Eminent Domain
- Title 29 - Mortgages and Other Liens
- Title 30 - Public Records
- Title 31 - Housing and Redevelopment
- Title 32 - Contracts and Agents
- Title 33 - Corporations, Partnerships and Associations
- Title 34 - Banking, Financial Institutions and Money
- Title 35 - Securities
- Title 36 - Commercial Code
- Title 37 - Consumer Protection Code
- Title 38 - Insurance
- Title 39 - Trade and Commerce
- Title 40 - Professions and Occupations
- Title 41 - Labor and Employment
- Title 42 - Workers' Compensation
- Title 43 - Social Services
- Title 44 - Health
- Title 45 - Hotels, Motels, Restaurants and Boardinghouses
- Title 46 - Agriculture
- Title 47 - Animals, Livestock and Poultry
- Title 48 - Environmental Protection and Conservation
- Title 49 - Waters, Water Resources and Drainage
- Title 50 - Fish, Game and Watercraft
- Title 51 - Parks, Recreation and Tourism
- Title 52 - Amusements and Athletic Contests
- Title 53 - Sundays, Holidays and Other Special Days
- Title 54 - Ports and Maritime Matters
- Title 55 - Aeronautics
- Title 56 - Motor Vehicles
- Title 57 - Highways, Bridges and Ferries
- Title 58 - Public Utilities, Services and Carriers
- Title 59 - Education
- Title 60 - Libraries, Archives, Museums and Arts
- Title 61 - Alcohol and Alcoholic Beverages
- Title 62 - South Carolina Probate Code
- Title 63 - South Carolina Children's Code

## Administrative code

The same legislature site publishes the Code of Regulations index and a State Register page. The State Register URL `https://www.scstatehouse.gov/state_register.php` returned HTTP 200.

## Courts and dockets

The Judicial Branch identifies the Supreme Court and the Court of Appeals. Opinions are on the opinions-and-orders path. `https://www.sccourts.org/opinions/` returned HTTP 404 and is not used. No separate public docket URL was confirmed from the fetched court pages, so none is cataloged.

## Rules and attorney general opinions

Court rules are on the Judicial Branch site. Attorney General opinions are on the Attorney General site.

## Matter map

- Criminal: Title 16 - Crimes and Offenses. Title 17 - Criminal Procedures.
- Civil: Title 15 - Civil Remedies and Procedures.
- Evidence: Title 19 - Evidence.
- Courts: Title 14 - Courts. Title 18 - Appeals.
- Administrative: South Carolina Code of Regulations.

## Local government

Title 4 covers counties, Title 5 covers municipal corporations, and Title 6 covers special purpose districts and other political subdivisions, all as state law. Ordinances are adopted by the local government. This capture does not supply county or municipal ordinance-host URLs.

## Capture notes

Checked 2026-10-07 with Invoke-WebRequest HEAD then GET, 25 second timeout. A TLS 1.2-only client could not open `www.scstatehouse.gov`. The same URLs returned HTTP 200 when the client used default TLS negotiation. `https://www.sccourts.org/opinions/` returned HTTP 404. The Supreme Court page `https://www.sccourts.org/courts/supreme-court/` returned HTTP 200.
