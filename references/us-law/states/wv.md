---
doc_kind: reference
canonical_id: us-law-state-wv
purpose: [reference]
topics: [us-law, west-virginia]
rag_keywords: [West Virginia, West Virginia Code, Supreme Court of Appeals, Intermediate Court of Appeals, Code of State Rules]
version: captured-2026-10-07
publication: West Virginia Legislature
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://code.wvlegislature.gov/
advisory_only: true
---

# West Virginia

Advisory capture of official entry points. This is not legal advice and it does not reproduce statutory, regulatory, or opinion text.

## Identity

The West Virginia Legislature publishes the West Virginia Code and the Constitution of West Virginia, which the constitution page describes as ratified in 1872 and subsequently amended. The Judiciary identifies the Supreme Court of Appeals and the Intermediate Court of Appeals. The Secretary of State publishes the Code of State Rules.

## Sources

| Role | Authority | HTTP | Entry |
| --- | --- | --- | --- |
| constitution | official-primary | 200 | [The Constitution of West Virginia](https://code.wvlegislature.gov/west-virginia-constitution) |
| statutes | official-primary | 200 | [West Virginia Code](https://code.wvlegislature.gov/) |
| session laws | official-primary | 200 | [Publications - WV Legislative Library](https://library.wvlegislature.gov/pubs/) |
| administrative code | official-primary | 200 | [Code of State Rules](https://apps.sos.wv.gov/adlaw/csr/default.aspx) |
| court of last resort opinions | official-primary | 200 | [Supreme Court - Opinions](https://www.courtswv.gov/appellate-courts/supreme-court-of-appeals/opinions) |
| intermediate appellate court | official-primary | 200 | [Intermediate Court of Appeals](https://www.courtswv.gov/appellate-courts/intermediate-court-of-appeals/about-the-court) |
| intermediate appellate court | official-primary | 200 | [Intermediate Court - Opinions](https://www.courtswv.gov/appellate-courts/intermediate-court-of-appeals/opinions) |
| dockets | official-primary | 200 | [Supreme Court - Current Docket](https://www.courtswv.gov/appellate-courts/supreme-court-of-appeals/current-docket) |
| court rules | official-primary | 200 | [Court Rules](https://www.courtswv.gov/legal-community/court-rules) |
| attorney general opinions | official-primary | 200 | [Attorney General Opinions](https://ago.wv.gov/transparency/attorney-general-opinions) |

## Constitution

The code site publishes the Constitution of West Virginia as ratified in 1872 and subsequently amended. The fetched article list begins with Article I, relations to the United States, through Article VIII, the judiciary, and Article XIV, amendments.

## Statutes

The code index lists 138 chapters. That exceeds 120, so this capture keeps the constitution on its own page and these chapter captions:

- CHAPTER 29A. STATE ADMINISTRATIVE PROCEDURES ACT.
- CHAPTER 51. COURTS AND THEIR OFFICERS.
- CHAPTER 56. PLEADING AND PRACTICE.
- CHAPTER 57. EVIDENCE AND WITNESSES.
- CHAPTER 61. CRIMES AND THEIR PUNISHMENT.
- CHAPTER 62. CRIMINAL PROCEDURE.

## Administrative code

The Secretary of State publishes the Code of State Rules. Chapter 29A is the State Administrative Procedures Act in the code index.

## Courts and dockets

The Supreme Court of Appeals is the court of last resort. The Intermediate Court of Appeals is the intermediate appellate court; both the court page and its opinions page returned HTTP 200. The Supreme Court current-docket page returned HTTP 200. Shorter paths `/intermediate-court` and `/supreme-court/opinions` returned HTTP 404 and are not used.

## Rules and attorney general opinions

Court rules are on the West Virginia Judiciary site. Attorney General opinions are on the Attorney General site. The fetched opinions page says the Attorney General issues written opinions on questions of law when requested by designated state officers.

## Matter map

- Criminal: Chapter 61, crimes and their punishment. Chapter 62, criminal procedure.
- Civil: Chapter 56, pleading and practice.
- Evidence: Chapter 57, evidence and witnesses.
- Courts: Chapter 51, courts and their officers.
- Administrative: Chapter 29A, and the Code of State Rules.

## Local government

County and municipal ordinances are adopted locally. The code includes chapters on local subdivisions, but this capture does not supply county or municipal ordinance-host URLs.

## Capture notes

Checked 2026-10-07 with Invoke-WebRequest HEAD then GET, 25 second timeout. Failed checks: `https://www.courtswv.gov/intermediate-court` and `https://www.courtswv.gov/supreme-court/opinions` returned HTTP 404.
