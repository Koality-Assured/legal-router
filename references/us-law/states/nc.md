---
doc_kind: reference
canonical_id: us-law-state-nc
purpose: [reference]
topics: [us-law, north-carolina]
rag_keywords: [North Carolina, North Carolina General Statutes, Supreme Court of North Carolina, North Carolina Court of Appeals, NCAC]
version: captured-2026-10-07
publication: North Carolina General Assembly
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://www.ncleg.gov/Laws/GeneralStatutes
advisory_only: true
---

# North Carolina

Advisory capture of official entry points. This is not legal advice and it does not reproduce statutory, regulatory, or opinion text.

## Identity

The North Carolina General Assembly publishes the General Statutes, the constitution, and session laws. The statutes page says the website text is not the official version. The Judicial Branch identifies the Supreme Court as the state's highest court and maintains a Court of Appeals. The Office of Administrative Hearings points to the North Carolina Administrative Code.

## Sources

| Role | Authority | HTTP | Entry |
| --- | --- | --- | --- |
| constitution | official-primary | 200 | [NC Constitution](https://www.ncleg.gov/Laws/Constitution) |
| statutes | official-mirror | 200 | [North Carolina General Statutes](https://www.ncleg.gov/Laws/GeneralStatutes) |
| session laws | official-primary | 200 | [Session Laws](https://www.ncleg.gov/Laws/SessionLaws) |
| administrative code | official-primary | 200 | [North Carolina Administrative Code](http://reports.oah.state.nc.us/ncac.asp) |
| court of last resort opinions | official-primary | 200 | [Appellate Court Opinions](https://www.nccourts.gov/documents/appellate-court-opinions) |
| intermediate appellate court | official-primary | 200 | [Court of Appeals](https://www.nccourts.gov/courts/court-of-appeals) |
| dockets | official-primary | 200 | [Supreme Court Docket Sheets](https://appellate.nccourts.org/dockets.php?c=1) |
| court rules | official-primary | 200 | [Court Rules](https://www.nccourts.gov/courts/supreme-court/court-rules) |
| court of last resort opinions | official-primary | 200 | [Supreme Court - North Carolina Judicial Branch](https://www.nccourts.gov/courts/supreme-court) |

## Constitution

The General Assembly publishes the North Carolina Constitution on its laws site.

## Statutes

The General Statutes landing index lists 396 chapters by number and states that the website text is not the official version. That count exceeds 120, so this capture keeps these chapter headings, read from the General Assembly chapter pages (each HEAD 200 and GET 200):

- Chapter 1A - Rules of Civil Procedure.
- Chapter 7A - Judicial Department.
- Chapter 8C - Evidence Code.
- Chapter 14 - Criminal Law.
- Chapter 15A - Criminal Procedure Act.
- Chapter 150B - Administrative Procedure Act.

## Administrative code

The Office of Administrative Hearings Rules Division links the North Carolina Administrative Code. The linked `http://reports.oah.state.nc.us/ncac.asp` page returned HTTP 200 and is titled as NCAC browsing. `https://reports.oah.state.nc.us/ncac.asp` did not connect.

## Courts and dockets

The Supreme Court page describes that court as the state's highest court, with no further appeal on matters of state law. The Court of Appeals is the intermediate appellate court. Slip opinions of both courts are on the appellate opinions page. Supreme Court docket sheets are on the appellate courts host. Court rules are on the Judicial Branch site.

## Rules and attorney general opinions

Court rules are cataloged above. `https://ncdoj.gov/` and `https://www.ncdoj.gov/` both returned HTTP 403, so no Attorney General opinions URL is cataloged.

## Matter map

- Criminal: Chapter 14 - Criminal Law. Chapter 15A - Criminal Procedure Act.
- Civil: Chapter 1A - Rules of Civil Procedure.
- Evidence: Chapter 8C - Evidence Code.
- Courts: Chapter 7A - Judicial Department.
- Administrative: Chapter 150B - Administrative Procedure Act, and the North Carolina Administrative Code.

## Local government

County and municipal ordinances are adopted by those governments. The General Statutes site is state law. This capture does not supply county or city ordinance-host URLs.

## Capture notes

Checked 2026-10-07 with Invoke-WebRequest HEAD then GET, 25 second timeout. Failed checks: https to `reports.oah.state.nc.us` did not connect; both Department of Justice host names returned HTTP 403. The Supreme Court description page `https://www.nccourts.gov/courts/supreme-court` returned HTTP 200 and is the source of the highest-court statement.
