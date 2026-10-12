---
doc_kind: reference
canonical_id: us-law-state-ca
purpose: [reference]
topics: [us-law, california]
rag_keywords: [california, california-codes, penal-code, code-of-civil-procedure, california-code-of-regulations]
version: captured-2026-10-07
publication: California Legislative Counsel, Office of Administrative Law, and Judicial Branch of California
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://courts.ca.gov/courts/supreme-court
advisory_only: true
---

# California law

Advisory only. This is a point-in-time map of official entry points captured on 2026-10-07. It is not legal advice and it does not reproduce statute text.

## Identity

The Legislative Counsel code-search page returned HTTP 403, so this capture does not store a code-name list. The Office of Administrative Law page that returned HTTP 200 describes the California Code of Regulations and says the online official text is provided under contract with Barclays. The Judicial Branch pages that returned HTTP 200 post the Supreme Court, the Courts of Appeal, opinions, and the Rules of Court.

## Sources

Catalog: [`../catalogs/states/ca.json`](../catalogs/states/ca.json)

| Role | Title | Status |
| --- | --- | --- |
| Constitution | [California Law code search](https://leginfo.legislature.ca.gov/faces/codes.xhtml) | 403 |
| Statutes | [California Law code search](https://leginfo.legislature.ca.gov/faces/codes.xhtml) | 403 |
| Session laws | [Bill search](https://leginfo.legislature.ca.gov/faces/billSearchClient.xhtml) | 403 |
| Administrative code | [California Code of Regulations](https://oal.ca.gov/publications/ccr/) | 200 |
| Administrative code | [Official CCR host named by OAL](https://govt.westlaw.com/calregs/Index) | 403 |
| Court of last resort | [Supreme Court](https://courts.ca.gov/courts/supreme-court) | 200 |
| Intermediate appellate courts | [Courts of Appeal](https://courts.ca.gov/courts/courts-appeal) | 200 |
| Court opinions | [Opinions](https://courts.ca.gov/opinions) | 200 |
| Dockets | [Appellate case information](https://appellatecases.courtinfo.ca.gov/) | 403 |
| Court rules | [Rules of Court](https://www.courts.ca.gov/cms/rules/index.cfm) | 200 |
| Attorney general opinions | [Legal opinions of the Attorney General](https://oag.ca.gov/opinions) | 200 |

## Constitution

The constitution is the CONS entry on the Legislative Counsel code-search page. Invoke-WebRequest recorded 403 for that page. No unofficial code host was substituted.

## Statutes index

The Legislative Counsel code-search page returned HTTP 403. No code names are stored. Use that host again when it returns the code list. Do not fill the names from memory.

## Administrative code

The [Office of Administrative Law CCR page](https://oal.ca.gov/publications/ccr/) returned GET 200. It states that the online official CCR is provided under contract with Barclays. That host, [govt.westlaw.com/calregs/Index](https://govt.westlaw.com/calregs/Index), returned 403. It is recorded as the contracted official publication host, not as an independent research site. No other regulations host was substituted.

## Courts and dockets

The court of last resort is the [Supreme Court of California](https://courts.ca.gov/courts/supreme-court). [supreme.courts.ca.gov](https://supreme.courts.ca.gov/) also returned GET 200. Intermediate appellate courts are the [Courts of Appeal](https://courts.ca.gov/courts/courts-appeal). [Opinions](https://courts.ca.gov/opinions) are posted on the judicial branch site, separate from [appellate case information](https://appellatecases.courtinfo.ca.gov/), which returned 403. This capture does not list superior-court or county docket URLs.

## Rules and Attorney General

The [California Rules of Court](https://www.courts.ca.gov/cms/rules/index.cfm) returned GET 200. [Attorney General legal opinions](https://oag.ca.gov/opinions) returned GET 200.

## Matter map

- Criminal and civil code names were not stored. The Legislative Counsel code-search page returned HTTP 403.
- Administrative matters start at the California Code of Regulations page on the Office of Administrative Law site, which returned HTTP 200.

## Local government

This capture does not list city or county code URLs. Cities and counties adopt their own ordinances. Obtain them from that government's clerk.

## Capture notes

Checks used PowerShell `Invoke-WebRequest` HEAD, then GET, with a 25-second timeout. Legislative Counsel hosts returned 403, so no code-name list is stored. `https://leginfo.legislature.ca.gov/` also returned 403.
