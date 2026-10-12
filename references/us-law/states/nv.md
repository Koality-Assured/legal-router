---
doc_kind: reference
canonical_id: us-law-state-nv
purpose: [reference]
topics: [us-law, nevada]
rag_keywords: [nevada, nevada-revised-statutes, nevada-administrative-code, nevada-constitution, nevada-supreme-court]
version: captured-2026-10-07
publication: Nevada Legislature and Nevada Attorney General
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://www.leg.state.nv.us/law1.html
advisory_only: true
---

# Nevada law

Advisory only. This is a point-in-time map of official entry points captured on 2026-10-07. It is not legal advice and it does not reproduce statute text.

## Identity

The Nevada Law Library, posted by the Legislature, describes the Nevada Revised Statutes as the current codified laws, the Statutes of Nevada as the compilation of legislation passed in a session, and the Nevada Administrative Code as the codified executive-branch regulations. The same library posts the Nevada Constitution, court rules, and city charters, and it links Supreme Court advance opinions on nvcourts.gov.

## Sources

Catalog: [`../catalogs/states/nv.json`](../catalogs/states/nv.json)

| Role | Title | Status |
| --- | --- | --- |
| Constitution | [Constitution of the State of Nevada](https://www.leg.state.nv.us/Const/NvConst.html) | 200 |
| Statutes | [Nevada Revised Statutes](https://www.leg.state.nv.us/NRS/) | 200 |
| Session laws | [Nevada Statutes Search](http://search.leg.state.nv.us/Statutes/Statutes.html) | 200 |
| Administrative code | [Nevada Administrative Code](https://www.leg.state.nv.us/NAC/) | 200 |
| Court of last resort | [Nevada Supreme Court](https://nvcourts.gov/supreme) | 403 |
| Intermediate appellate courts | [Nevada Court of Appeals](https://nvcourts.gov/courtofappeals) | 403 |
| Court opinions | [Advance opinions](https://nvcourts.gov/supreme/decisions/advance_opinions/) | 403 |
| Dockets | [Find a case](https://nvcourts.gov/supreme/how_do_i/find_a_case) | 403 |
| Court rules | [Court Rules of Nevada](https://www.leg.state.nv.us/CourtRules/index.html) | 200 |
| Attorney general opinions | [Official Attorney General opinions](https://ag.nv.gov/Publications/Opinions/) | 200 |
| City charters | [City Charters of Nevada](https://www.leg.state.nv.us/CityCharters/index.html) | 200 |

## Constitution

The Legislature's [Constitution of the State of Nevada](https://www.leg.state.nv.us/Const/NvConst.html) returned GET 200.

## Statutes index

The [Nevada Revised Statutes](https://www.leg.state.nv.us/NRS/) table of titles and chapters returned GET 200. This capture stops at that index. The [Nevada Law Library](https://www.leg.state.nv.us/law1.html) is the Legislature's hub for the NRS, the constitution, the administrative code, court rules, and the Statutes of Nevada.

## Administrative code

The [Nevada Administrative Code](https://www.leg.state.nv.us/NAC/) returned GET 200.

## Courts and dockets

The court of last resort is the Supreme Court of Nevada. The intermediate appellate court is the Nevada Court of Appeals. `https://nvcourts.gov/supreme` and `https://nvcourts.gov/courtofappeals` returned 403. The Law Library links [advance opinions](https://nvcourts.gov/supreme/decisions/advance_opinions/) on the Supreme Court site; that URL also returned 403. [Find a case](https://nvcourts.gov/supreme/how_do_i/find_a_case) returned 403. No replacement court host was substituted. `https://caseinfo.nvsupremecourt.us/` did not connect and is not cataloged.

## Rules and Attorney General

[Court Rules of Nevada](https://www.leg.state.nv.us/CourtRules/index.html) are posted with the Law Library and returned GET 200. [Attorney General opinions](https://ag.nv.gov/Publications/Opinions/) returned GET 200. The page says formal opinions are issued to public officials named in statute and are published for their persuasive authority.

## Matter map

- Criminal and civil matters start at the Nevada Revised Statutes index and the Court Rules of Nevada. This capture does not assign NRS title numbers.
- Administrative matters start at the Nevada Administrative Code and at Attorney General opinions.

## Local government

The Legislature posts [City Charters of Nevada](https://www.leg.state.nv.us/CityCharters/index.html) (GET 200). Those charters are state legislative compilations. This capture does not list separate city or county ordinance-code URLs. Ordinances that are not in the charter compilation are obtained from the city or county clerk.

## Capture notes

Checks used PowerShell `Invoke-WebRequest` HEAD, then GET, with a 25-second timeout. `https://www.leg.state.nv.us/law1.cfm` returned 503; `law1.html` returned 200. `https://www.leg.state.nv.us/Statutes/` returned 403. The session-laws search linked from the Law Library returned 200 on `http://search.leg.state.nv.us/Statutes/Statutes.html`.
