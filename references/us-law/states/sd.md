---
doc_kind: reference
canonical_id: us-law-state-sd
purpose: [reference]
topics: [us-law, south-dakota, statutes, courts]
rag_keywords: [South Dakota, Codified Laws, constitution, administrative rules, supreme court, attorney general]
version: captured-2026-10-07
publication: South Dakota Legislature, Unified Judicial System, and Attorney General
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://sdlegislature.gov/Statutes
advisory_only: true
---

# South Dakota law sources

This page is an advisory point-in-time map of official sources. It is not legal advice and it does not reproduce statutory text.

## Identity

South Dakota (SD) is a state. The court of last resort is the South Dakota Supreme Court. The Unified Judicial System court-structure page describes circuit courts and the Supreme Court. No intermediate appellate court page was found on the verified court navigation.

## Source table

| Role | Authority | HTTP | URL |
| --- | --- | --- | --- |
| Constitution | official-primary | 200 | https://sdlegislature.gov/Constitution |
| Codified laws | official-primary | 200 | https://sdlegislature.gov/Statutes |
| Session laws | official-primary | 200 | https://sdlegislature.gov/Statutes/Session_Laws/ |
| Administrative rules | official-primary | 200 | https://sdlegislature.gov/Rules/Administrative |
| Court of last resort | official-primary | 200 | https://ujs.sd.gov/supreme-court/ |
| Court structure | official-primary | 200 | https://ujs.sd.gov/self-help/understanding-the-courts/court-structure/ |
| Dockets | official-primary | 200 | https://ujs.sd.gov/cases-and-records/court-records-search/ |
| Court rules | official-primary | 200 | https://ujs.sd.gov/supreme-court/published-rules/ |
| Supreme Court opinions | official-primary | 200 | https://ujs.sd.gov/supreme-court/opinions/ |
| Attorney general opinions | official-primary | 200 | https://atg.sd.gov/OurOffice/OfficialOpinions/default.aspx |

## Constitution

`https://sdlegislature.gov/Statutes/Constitution` returned HTTP 200 and landed on `https://sdlegislature.gov/Constitution`. The response is the legislature’s JavaScript application shell (about 6 KB). Article text was not in that HTML.

## Statutes

The codified-laws route `https://sdlegislature.gov/Statutes/Codified_Laws` returned HTTP 200 and landed on `https://sdlegislature.gov/Statutes`. The same shell was returned, so this capture does not list title captions. Use the legislature site’s codified-laws application for the title index. Do not treat a private publisher as the official code.

Session laws are routed at `https://sdlegislature.gov/Statutes/Session_Laws/`, which also returned the application shell with HTTP 200.

## Administrative code

Administrative rules are routed at `https://sdlegislature.gov/Rules/Administrative` (HTTP 200, same application shell). The legislature application also exposes a registers route in its script. The Unified Judicial System legal-research page points readers to that administrative-rules collection and to the codified laws.

## Courts and dockets

The Supreme Court is the court of last resort. Its opinions page states that posted opinions are slip opinions and that the official opinions are those in the bound North Western Reporter. The court-structure page title and description cover circuit courts and the Supreme Court. Court-records search is the public docket entry on the Unified Judicial System site. `https://ecourts.sd.gov/` returned HTTP 200 and redirected to an account login page.

## Rules and attorney general

Published Supreme Court rules are on the Unified Judicial System site. The Attorney General’s official-opinions page describes opinions issued under state law to listed public officers, with opinions since 1968 on that site.

## Matter map

Criminal, civil, evidence, courts, and administrative-procedure statutes are inside the Codified Laws application. This capture did not receive a server-rendered title list, so it does not assign title numbers. Administrative rules are the separate administrative-rules collection. Appeals in the state system go to the Supreme Court from the circuit courts.

## Local government

To locate ordinances for a named city, use that city’s official website and the city clerk, or the municipal code the city itself publishes. This capture does not record county or city code URLs. The Unified Judicial System court-finder pages identify circuit courts; they are not ordinance codes.

## Capture notes

Checks used PowerShell `Invoke-WebRequest` HEAD then GET, 25-second timeout, on 2026-10-07. Legislature routes above returned HTTP 200 on both methods. A Secretary of State constitution PDF URL, `https://sdsos.gov/2025%20South%20Dakota%20Constitution%2020250919.pdf`, returned HTTP 404 and is not used. Route names were read from the legislature application script fetched from `https://sdlegislature.gov/js/app.84949f1c.js`.
