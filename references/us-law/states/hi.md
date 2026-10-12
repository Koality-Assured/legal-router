---
doc_kind: reference
canonical_id: us-law-state-hi
purpose: [reference]
topics: [us-law, hawaii]
rag_keywords: [hawaii, hawaii-revised-statutes, hawaii-constitution, hawaii-administrative-rules, hawaii-supreme-court]
version: captured-2026-10-07
publication: Hawaii Legislature, Office of the Lieutenant Governor, and Hawaii State Judiciary
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://lrb.hawaii.gov/par/finding-the-laws/
advisory_only: true
---

# Hawaii law

Advisory only. This is a point-in-time map of official entry points captured on 2026-10-07. It is not legal advice and it does not reproduce statute text.

## Identity

The Legislative Reference Bureau's finding-the-laws page describes the Hawaii Revised Statutes as the codified laws, the Session Laws of Hawaii as the annual acts, and the Hawaii Administrative Rules as agency rules posted by the Lieutenant Governor. The Judiciary posts the Supreme Court, the Intermediate Court of Appeals, appellate opinions and orders, court rules, and a court-records search.

## Sources

Catalog: [`../catalogs/states/hi.json`](../catalogs/states/hi.json)

| Role | Title | Status |
| --- | --- | --- |
| Constitution | [State Constitution](https://www.capitol.hawaii.gov/hrscurrent/Vol01_Ch0001-0042F/05-CONST/CONST_.htm) | 403 |
| Statutes | [Hawaii Revised Statutes](https://www.capitol.hawaii.gov/hrsall/) | 403 |
| Session laws | [Session Laws of Hawaiʻi](https://www.capitol.hawaii.gov/session/slh.aspx) | 403 |
| Administrative code | [Administrative Rules](https://ltgov.hawaii.gov/the-office/administrative-rules/) | 200 |
| Court of last resort | [Supreme Court](https://www.courts.state.hi.us/courts/supreme) | 200 |
| Intermediate appellate courts | [Intermediate Court of Appeals](https://www.courts.state.hi.us/courts/appeals) | 200 |
| Court opinions | [Appellate opinions and orders](https://www.courts.state.hi.us/opinions_and_orders) | 200 |
| Dockets | [Search court records](https://www.courts.state.hi.us/legal_references/records/search_court_records) | 200 |
| Court rules | [Rules of Court](https://www.courts.state.hi.us/legal_references/rules) | 200 |
| Attorney general opinions | [Attorney General opinions](https://ag.hawaii.gov/publications/ag-opinions/) | 200 |

## Constitution

The Legislature's constitution page returned 403 on HEAD and GET. The Legislative Reference Bureau points to the Legislature for the current code, which includes the constitution. No unofficial constitution host was substituted.

## Statutes index

[Hawaii Revised Statutes](https://www.capitol.hawaii.gov/hrsall/) returned 403. [Session Laws of Hawaiʻi](https://www.capitol.hawaii.gov/session/slh.aspx) returned 403. The Bureau's [finding-the-laws](https://lrb.hawaii.gov/par/finding-the-laws/) page returned GET 200 and identifies those Legislature URLs. This capture does not list chapter or section names from a blocked code index.

## Administrative code

The Lieutenant Governor's [Administrative Rules](https://ltgov.hawaii.gov/the-office/administrative-rules/) page returned GET 200. The Bureau page says executive-agency rules are posted there.

## Courts and dockets

The court of last resort is the [Supreme Court](https://www.courts.state.hi.us/courts/supreme). The intermediate appellate court is the [Intermediate Court of Appeals](https://www.courts.state.hi.us/courts/appeals). [Opinions and orders](https://www.courts.state.hi.us/opinions_and_orders) are posted on the Judiciary site. The opinions page says dispositions are posted the day they are filed. [Search court records](https://www.courts.state.hi.us/legal_references/records/search_court_records) is the Judiciary's records search and is separate from the opinions list.

## Rules and Attorney General

[Rules of Court](https://www.courts.state.hi.us/legal_references/rules) returned GET 200. [Attorney General opinions](https://ag.hawaii.gov/publications/ag-opinions/) returned GET 200. `https://ag.hawaii.gov/publications/opinions/` returned 404.

## Matter map

- Criminal and civil matters are in the Hawaii Revised Statutes. The code index itself returned 403, so this capture does not name chapters.
- Court procedure is in the Rules of Court.
- Administrative matters start at the Lieutenant Governor's administrative-rules page and at Attorney General opinions.

## Local government

Hawaii's local governments are the counties. This capture does not list county ordinance URLs. Obtain ordinances from the county clerk. The Hawaii Revised Statutes are state law, not a county code.

## Capture notes

Checks used PowerShell `Invoke-WebRequest` HEAD, then GET, with a 25-second timeout. The three Legislature URLs above returned 403. The Bureau finding-the-laws page returned 200 and is the source for those URLs.
