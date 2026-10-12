---
doc_kind: reference
canonical_id: us-law-state-id
purpose: [reference]
topics: [us-law, idaho]
rag_keywords: [idaho, idaho-statutes, idaho-constitution, idaho-administrative-rules, idaho-supreme-court]
version: captured-2026-10-07
publication: Idaho Legislature and Idaho Supreme Court
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://legislature.idaho.gov/statutesrules/idstat/
advisory_only: true
---

# Idaho law

Advisory only. This is a point-in-time map of official entry points captured on 2026-10-07. It is not legal advice and it does not reproduce statute text.

## Identity

The Legislature posts Idaho Statutes, the Idaho Constitution, and Idaho Session Laws, and it links Idaho Administrative Rules. The Idaho Supreme Court posts its opinions, Court of Appeals opinions, and rules and procedures. The court homepage links iCourt. A separate Idaho Court Data site posts criminal and civil filing dashboards.

## Sources

Catalog: [`../catalogs/states/id.json`](../catalogs/states/id.json)

| Role | Title | Status |
| --- | --- | --- |
| Constitution | [Idaho Constitution](https://legislature.idaho.gov/statutesrules/idconst/) | 200 |
| Statutes | [Idaho Statutes](https://legislature.idaho.gov/statutesrules/idstat/) | 200 |
| Session laws | [Idaho Session Laws](https://legislature.idaho.gov/statutesrules/sessionlaws/) | 200 |
| Administrative code | [Idaho Administrative Rules, current](https://adminrules.idaho.gov/rules/current/) | 200 |
| Court of last resort | [Idaho Supreme Court](https://isc.idaho.gov/) | 200 |
| Intermediate appellate courts | [Court of Appeals opinions](https://isc.idaho.gov/cases-opinions/ica-opinions) | 200 |
| Court opinions | [Idaho Supreme Court opinions](https://isc.idaho.gov/cases-opinions/isc-opinions) | 200 |
| Dockets | [iCourt](https://icourt.idaho.gov/) | 403 |
| Court data | [Idaho Court Data](https://courtdata.idaho.gov/) | 200 |
| Court rules | [Rules and procedures](https://isc.idaho.gov/rules-procedure) | 200 |
| Attorney general opinions | [Attorney General opinions](https://www.ag.idaho.gov/office-resources/opinions/) | 200 |

## Constitution

The Legislature's [Idaho Constitution](https://legislature.idaho.gov/statutesrules/idconst/) returned GET 200. The page says the constitution on the site is updated on July 1 after the legislative session.

## Statutes index

The [Idaho Statutes](https://legislature.idaho.gov/statutesrules/idstat/) title index returned GET 200. This capture stops at that index. The index includes Title 1, Courts and Court Officials; Title 5, Proceedings in Civil Actions in Courts of Record; Title 9, Evidence; Title 18, Crimes and Punishments; and Title 19, Criminal Procedure.

## Administrative code

[Current Idaho Administrative Rules](https://adminrules.idaho.gov/rules/current/) returned GET 200. The Legislature laws-and-rules page links [adminrules.idaho.gov](https://adminrules.idaho.gov/).

## Courts and dockets

The court of last resort is the [Idaho Supreme Court](https://isc.idaho.gov/). Court of Appeals opinions are posted at [ica-opinions](https://isc.idaho.gov/cases-opinions/ica-opinions). Supreme Court opinions are on the same site at [isc-opinions](https://isc.idaho.gov/cases-opinions/isc-opinions). Those opinion pages are separate from iCourt. The court homepage links [iCourt](https://icourt.idaho.gov/), which returned 403. [Idaho Court Data](https://courtdata.idaho.gov/) returned 200 and describes criminal and civil filing dashboards, which is a data report rather than a case-docket viewer.

## Rules and Attorney General

[Rules and procedures](https://isc.idaho.gov/rules-procedure) returned GET 200. [Attorney General opinions](https://www.ag.idaho.gov/office-resources/opinions/) returned GET 200.

## Matter map

- Criminal matters: Idaho Statutes Titles 18 and 19 on the statutes index, plus court rules.
- Civil matters: Titles 5 and 9 on that index, plus court rules.
- Administrative matters: current Idaho Administrative Rules, and Attorney General opinions.

## Local government

This capture does not list city or county code URLs. Cities and counties adopt their own ordinances. Obtain them from that government's clerk. Idaho Statutes include state law on municipal corporations; that is not a city ordinance code.

## Capture notes

Checks used PowerShell `Invoke-WebRequest` HEAD, then GET, with a 25-second timeout. `https://isc.idaho.gov/appeals-court` and `https://isc.idaho.gov/rules` returned HEAD 404 and the GET connection closed. `https://mycourts.idaho.gov/` returned 403 and is not the portal linked from the court homepage.
