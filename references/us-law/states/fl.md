---
doc_kind: reference
canonical_id: us-law-state-fl
purpose: [reference]
topics: [us-law, florida]
rag_keywords: [Florida, Florida Statutes, Florida Constitution, Florida Supreme Court, Florida Administrative Code]
version: captured-2026-10-07
publication: Online Sunshine
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://www.leg.state.fl.us/statutes/
advisory_only: true
---

# Florida

Advisory capture of official entry points. This is not legal advice and it does not reproduce statutory, regulatory, or opinion text.

## Identity

Online Sunshine publishes the 2026 Florida Statutes. The Florida Senate publishes the Florida Constitution. The 2026 Laws of Florida are on laws.flrules.org. The Department of State publishes the Florida Administrative Code and Register. The Florida Supreme Court publishes an opinion search that also covers other appellate courts.

## Sources

| Role | Authority | HTTP | Entry |
| --- | --- | --- | --- |
| constitution | official-primary | 200 | [The Florida Constitution](https://www.flsenate.gov/Laws/Constitution) |
| statutes | official-primary | 200 | [2026 Florida Statutes - Online Sunshine](https://www.leg.state.fl.us/statutes/) |
| statutes | official-mirror | 200 | [2026 Florida Statutes - The Florida Senate](https://www.flsenate.gov/Laws/Statutes) |
| session laws | official-primary | 200 | [2026 Laws of Florida](https://laws.flrules.org/) |
| administrative code | official-primary | 200 | [Florida Administrative Code and Register](https://www.flrules.org/) |
| court of last resort opinions | official-primary | 200 | [Opinion Search For All Appellate Courts](https://supremecourt.flcourts.gov/case-information/Opinions/Opinion-Search-For-All-Appellate-Courts) |
| intermediate appellate court | official-primary | 200 | [Florida Courts](https://www.flcourts.gov/) |
| dockets | official-primary | 200 | [Appellate Case Information System](https://acis.flcourts.gov/) |
| court rules | official-primary | 200 | [Practice and Procedures - Florida Supreme Court](https://supremecourt.flcourts.gov/Practice-Procedures) |
| attorney general opinions | official-primary | 200 | [Attorney General Opinions](https://www.myfloridalegal.com/ag-opinions) |
| court of last resort opinions | official-primary | 200 | [Florida Supreme Court](https://supremecourt.flcourts.gov/) |

## Constitution

The Florida Senate publishes the Florida Constitution.

## Statutes

Online Sunshine publishes the 2026 Florida Statutes. The title index has 49 titles.

- TITLE I - CONSTRUCTION OF STATUTES
- TITLE II - STATE ORGANIZATION
- TITLE III - LEGISLATIVE BRANCH; COMMISSIONS
- TITLE IV - EXECUTIVE BRANCH
- TITLE V - JUDICIAL BRANCH
- TITLE VI - CIVIL PRACTICE AND PROCEDURE
- TITLE VII - EVIDENCE
- TITLE VIII - LIMITATIONS
- TITLE IX - ELECTORS AND ELECTIONS
- TITLE X - PUBLIC OFFICERS, EMPLOYEES, AND RECORDS
- TITLE XI - COUNTY ORGANIZATION AND INTERGOVERNMENTAL RELATIONS
- TITLE XII - MUNICIPALITIES
- TITLE XIII - PLANNING AND DEVELOPMENT
- TITLE XIV - TAXATION AND FINANCE
- TITLE XV - HOMESTEAD AND EXEMPTIONS
- TITLE XVI - TEACHERS' RETIREMENT SYSTEM; HIGHER EDUCATIONAL FACILITIES BONDS
- TITLE XVII - MILITARY AFFAIRS AND RELATED MATTERS
- TITLE XVIII - PUBLIC LANDS AND PROPERTY
- TITLE XIX - PUBLIC BUSINESS
- TITLE XX - VETERANS
- TITLE XXI - DRAINAGE
- TITLE XXII - PORTS AND HARBORS
- TITLE XXIII - MOTOR VEHICLES
- TITLE XXIV - VESSELS
- TITLE XXV - AVIATION
- TITLE XXVI - PUBLIC TRANSPORTATION
- TITLE XXVII - RAILROADS AND OTHER REGULATED UTILITIES
- TITLE XXVIII - NATURAL RESOURCES; CONSERVATION, RECLAMATION, AND USE
- TITLE XXIX - PUBLIC HEALTH
- TITLE XXX - SOCIAL WELFARE
- TITLE XXXI - LABOR
- TITLE XXXII - REGULATION OF PROFESSIONS AND OCCUPATIONS
- TITLE XXXIII - REGULATION OF TRADE, COMMERCE, INVESTMENTS, AND SOLICITATIONS
- TITLE XXXIV - ALCOHOLIC BEVERAGES AND TOBACCO
- TITLE XXXV - AGRICULTURE, HORTICULTURE, AND ANIMAL INDUSTRY
- TITLE XXXVI - BUSINESS ORGANIZATIONS
- TITLE XXXVII - INSURANCE
- TITLE XXXVIII - BANKS AND BANKING
- TITLE XXXIX - COMMERCIAL RELATIONS
- TITLE XL - REAL AND PERSONAL PROPERTY
- TITLE XLI - STATUTE OF FRAUDS, FRAUDULENT TRANSFERS, AND GENERAL ASSIGNMENTS
- TITLE XLII - ESTATES AND TRUSTS
- TITLE XLIII - DOMESTIC RELATIONS
- TITLE XLIV - CIVIL RIGHTS
- TITLE XLV - TORTS
- TITLE XLVI - CRIMES
- TITLE XLVII - CRIMINAL PROCEDURE AND CORRECTIONS
- TITLE XLVIII - EARLY LEARNING-20 EDUCATION CODE
- TITLE XLIX - PARENTS' BILL OF RIGHTS; TEACHERS' BILL OF RIGHTS

## Administrative code

The Department of State publishes the Florida Administrative Code and the Florida Administrative Register at flrules.org.

## Courts and dockets

The Supreme Court of Florida is the court of last resort. Its opinion search covers Supreme Court opinions and other appellate court opinions. The Florida Courts site refers to district courts of appeal, which are the intermediate appellate courts. Appellate case information is at ACIS. `https://www.flsenate.gov/Laws/LawsOfFlorida` returned HTTP 404; session laws are cataloged at laws.flrules.org.

## Rules and attorney general opinions

Practice and procedures resources are on the Supreme Court site. Attorney General opinions are on the Attorney General's site.

## Matter map

- Criminal: TITLE XLVI - CRIMES. TITLE XLVII - CRIMINAL PROCEDURE AND CORRECTIONS.
- Civil: TITLE VI - CIVIL PRACTICE AND PROCEDURE.
- Evidence: TITLE VII - EVIDENCE.
- Courts: TITLE V - JUDICIAL BRANCH.
- Administrative: Florida Administrative Code, and TITLE IV - EXECUTIVE BRANCH.

## Local government

Title XI covers county organization and Title XII covers municipalities as state law. County and municipal ordinances are adopted by those governments. This capture does not supply county or city ordinance-host URLs.

## Capture notes

Checked 2026-10-07 with Invoke-WebRequest HEAD then GET, 25 second timeout. Failed check: `https://www.flsenate.gov/Laws/LawsOfFlorida` returned HTTP 404. The Senate statutes mirror returned GET 200 and HEAD 404. The Supreme Court home page `https://supremecourt.flcourts.gov/` returned HTTP 200.
