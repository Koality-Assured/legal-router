---
doc_kind: reference
canonical_id: us-law-state-ut
purpose: [reference]
topics: [us-law, utah]
rag_keywords: [utah, utah-code, utah-constitution, utah-administrative-code, utah-supreme-court]
version: captured-2026-10-07
publication: Utah Legislature, Office of Administrative Rules, and Utah Courts
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://le.utah.gov/xcode/code.html
advisory_only: true
---

# Utah law

Advisory only. This is a point-in-time map of official entry points captured on 2026-10-07. It is not legal advice and it does not reproduce statute text.

## Identity

The Legislature posts a Utah Code index and a Utah Constitution index. Its code-and-constitution page links recent laws. The Office of Administrative Rules describes the Utah Administrative Code as its official publication and as evidence of the administrative law of the state. The courts post the Utah Supreme Court, the Court of Appeals, a separate opinions archive, and Xchange for case search.

## Sources

Catalog: [`../catalogs/states/ut.json`](../catalogs/states/ut.json)

| Role | Title | Status |
| --- | --- | --- |
| Constitution | [Utah Constitution Index](https://le.utah.gov/xcode/constitution.html) | 200 |
| Statutes | [Utah Code Index](https://le.utah.gov/xcode/code.html) | 200 |
| Session laws | [Recent Laws](https://le.utah.gov/documents/laws-recent.htm) | 200 |
| Administrative code | [Utah Office of Administrative Rules](https://adminrules.utah.gov/) | 200 |
| Court of last resort | [Utah Supreme Court](https://www.utcourts.gov/en/courts/court-types/appellate-courts/sup.html) | 200 |
| Intermediate appellate courts | [Court of Appeals](https://www.utcourts.gov/en/courts/court-types/appellate-courts/coa.html) | 200 |
| Court opinions | [Utah Court Opinions, Decisions, and Orders](https://legacy.utcourts.gov/opinions/) | 200 |
| Dockets | [Xchange](https://www.utcourts.gov/en/court-records-publications/records/xchange.html) | 200 |
| Court rules | [Utah Court Rules](https://legacy.utcourts.gov/rules/) | 200 |

## Constitution

The [Utah Constitution Index](https://le.utah.gov/xcode/constitution.html) returned GET 200.

## Statutes index

The [Utah Code Index](https://le.utah.gov/xcode/code.html) returned GET 200. This capture stops at that index.

## Administrative code

The [Utah Office of Administrative Rules](https://adminrules.utah.gov/) returned GET 200. The office describes the Utah Administrative Code as the official compilation of agency rules.

## Courts and dockets

The court of last resort is the [Utah Supreme Court](https://www.utcourts.gov/en/courts/court-types/appellate-courts/sup.html). The intermediate appellate court is the [Utah Court of Appeals](https://www.utcourts.gov/en/courts/court-types/appellate-courts/coa.html). Opinions, decisions, and orders are archived on a separate host, [legacy.utcourts.gov/opinions](https://legacy.utcourts.gov/opinions/). Case search is [Xchange](https://www.utcourts.gov/en/court-records-publications/records/xchange.html), which the courts page titles as public case search. This capture did not confirm a subscription fee from that page.

## Rules and Attorney General

[Utah Court Rules](https://legacy.utcourts.gov/rules/) returned GET 200. The Attorney General site at [attorneygeneral.utah.gov](https://attorneygeneral.utah.gov/) returned GET 200, and its fetched navigation did not expose a stable opinions index. Candidate paths `/opinions/` and `/resources/opinions/` closed the connection. No opinions URL is cataloged.

## Matter map

- Criminal and civil matters start at the Utah Code index and the Utah Court Rules. This capture does not assign title numbers.
- Administrative matters start at the Utah Administrative Code.

## Local government

This capture does not list city or county code URLs. Cities, towns, and counties adopt their own ordinances. Obtain them from that government's clerk or recorder. The Utah Code is state law governing local government, not a municipal ordinance code.

## Capture notes

Checks used PowerShell `Invoke-WebRequest` HEAD, then GET, with a 25-second timeout. `https://le.utah.gov/Documents/laws.htm` returned 404; the code-and-constitution page links Recent Laws instead. `https://www.utcourts.gov/en/rules.html` returned HEAD 404 and the GET connection closed.
