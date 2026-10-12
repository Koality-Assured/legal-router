---
doc_kind: reference
canonical_id: us-law-state-az
purpose: [reference]
topics: [us-law, arizona]
rag_keywords: [arizona, arizona-revised-statutes, arizona-constitution, arizona-administrative-code, arizona-supreme-court]
version: captured-2026-10-07
publication: Arizona State Legislature and Arizona Judicial Branch
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://www.azleg.gov/arstitle/
advisory_only: true
---

# Arizona law

Advisory only. This is a point-in-time map of official entry points captured on 2026-10-07. It is not legal advice and it does not reproduce statute text.

## Identity

The Legislature posts the Arizona Revised Statutes and the Arizona Constitution. The statutes page says that online text is maintained for legislative drafting and that Thomson Reuters publishes the official print version. The session-laws page describes session laws as the enactments of a legislative session. The judicial branch posts the Arizona Supreme Court and the Court of Appeals.

## Sources

Catalog: [`../catalogs/states/az.json`](../catalogs/states/az.json)

| Role | Title | Status |
| --- | --- | --- |
| Constitution | [Arizona State Constitution](https://www.azleg.gov/constitution/) | 200 |
| Statutes | [Arizona Revised Statutes](https://www.azleg.gov/arstitle/) | 200 |
| Session laws | [Session Laws](https://www.azleg.gov/sessionlaws/) | 200 |
| Administrative code | [Arizona Administrative Code](https://azsos.gov/rules/arizona-administrative-code) | 403 |
| Court of last resort | [AZ Supreme Court](https://www.azcourts.gov/azsupremecourt) | 200 |
| Intermediate appellate courts | [Court of Appeals, Division One](https://www.azcourts.gov/coa1) | 200 |
| Intermediate appellate courts | [Court of Appeals, Division Two](https://www.appeals2.az.gov/) | 200 |
| Court opinions | [Opinions and memorandum decisions](https://opinions.azcourts.gov/cld) | 200 |
| Dockets | [Public Access Case Lookup](https://apps.azcourts.gov/publicAccess/caselookup.aspx) | 200 |
| Court rules | [Rules](https://www.azcourts.gov/rules) | 200 |
| Attorney general opinions | [Attorney General opinions](https://www.azag.gov/opinions) | 200 |

## Constitution

The Legislature's [Arizona State Constitution](https://www.azleg.gov/constitution/) returned GET 200.

## Statutes index

The [Arizona Revised Statutes](https://www.azleg.gov/arstitle/) title index returned GET 200. This capture stops at that index.

## Administrative code

The Secretary of State page [Arizona Administrative Code](https://azsos.gov/rules/arizona-administrative-code) returned 403 on HEAD and GET. No other host was substituted.

## Courts and dockets

The court of last resort is the [Arizona Supreme Court](https://www.azcourts.gov/azsupremecourt). Intermediate appellate courts are [Division One](https://www.azcourts.gov/coa1) and [Division Two](https://www.appeals2.az.gov/). The Division Two host is the one linked from the Division One site. Opinions and memorandum decisions are on a separate host, [opinions.azcourts.gov](https://opinions.azcourts.gov/cld). That opinions site is separate from [Public Access Case Lookup](https://apps.azcourts.gov/publicAccess/caselookup.aspx). The opinions home page states that only the bound volumes of Arizona Reports are the final official report.

## Rules and Attorney General

Court rules are posted at [azcourts.gov/rules](https://www.azcourts.gov/rules). [Attorney General opinions](https://www.azag.gov/opinions) are issued when requested by the Legislature, a state public officer, or a county attorney. The office states that those opinions are advisory.

## Matter map

- Criminal and civil matters start at the Arizona Revised Statutes title index and the court rules. This capture does not assign title numbers.
- Administrative matters start at the Arizona Administrative Code page (403 on this check) and at Attorney General opinions.

## Local government

This capture does not list city or county code URLs. Cities, towns, and counties adopt their own ordinances. Obtain them from that government's clerk.

## Capture notes

Checks used PowerShell `Invoke-WebRequest` HEAD, then GET, with a 25-second timeout. `https://www.azcourts.gov/coa2` returned 404. `https://azsos.gov/rules` and `https://apps.azsos.gov/public_services/` also returned 403.
