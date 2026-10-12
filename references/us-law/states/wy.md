---
doc_kind: reference
canonical_id: us-law-state-wy
purpose: [reference]
topics: [us-law, wyoming, statutes, courts]
rag_keywords: [Wyoming, Wyoming Statutes, constitution, administrative rules, supreme court, attorney general]
version: captured-2026-10-07
publication: Wyoming Legislative Service Office, Secretary of State, and Judicial Branch
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://wyoleg.gov/stateStatutes/StatutesDownload
advisory_only: true
---

# Wyoming law sources

This page is an advisory point-in-time map of official sources. It is not legal advice and it does not reproduce statutory text.

## Identity

Wyoming (WY) is a state. The court of last resort is the Wyoming Supreme Court. The verified court navigation lists the Supreme Court, district courts, circuit courts, and a chancery court. It does not list an intermediate court of appeals. The chancery court is a trial court on that navigation.

## Source table

| Role | Authority | HTTP | URL |
| --- | --- | --- | --- |
| Statutes and constitution | official-primary | shell | https://wyoleg.gov/stateStatutes/StatutesDownload |
| Statutes application | official-primary | shell | https://www.wyoleg.gov/StateStatutes/StatutesConstitution |
| Administrative rules | official-primary | 200 | https://rules.wyo.gov/ |
| Agency rule index | official-primary | 200 | https://rules.wyo.gov/Agencies.aspx |
| Court of last resort | official-primary | 200 | https://www.wyocourts.gov/supreme-court/ |
| Dockets | official-primary | 200 | https://ctefiling.wyocourts.gov/portal/home |
| Court rules | official-primary | 200 | https://www.wyocourts.gov/court-rules/ |
| Supreme Court opinions | official-primary | 200 | https://www.wyocourts.gov/wy-supreme-court-opinions/ |
| Attorney general opinions | official-primary | 200 | https://ag.wyo.gov/formal-opinions |

## Constitution

The download URL is the legislature's statutes-and-constitution route. The unauthenticated GET returned an application shell. The HTML did not include the constitution text, so no article headings are stored. A separate session-laws index URL was not verified.

## Statutes

The unauthenticated GET of the download URL and of the statutes application returned the same application shell. The HTML did not include a title index, so no title list is stored.

## Administrative code

The Secretary of State rules site is the repository for agency rules and describes the Wyoming Administrative Code. The agencies page returned HTTP 200.

## Courts and dockets

The Supreme Court page is the court of last resort. Public docket access is the e-filing portal home, which returned HTTP 200. Opinions are on the Supreme Court opinions page.

## Rules and attorney general

Court rules are on the Judicial Branch rules page. The Attorney General formal-opinions page lists opinions by year and notes that one 2016 opinion was withdrawn.

## Matter map

No statute title index is stored, because the statute HTML was an application shell. Administrative rules are on `rules.wyo.gov`.

## Local government

To locate ordinances for a named city, use that city's official website and the city clerk, or the municipal code the city itself publishes. This capture does not record county or city code URLs.

## Capture notes

Checks used PowerShell Invoke-WebRequest HEAD then GET, 25-second timeout, on 2026-10-07. A later GET of the statute download URL on 2026-10-07 returned HTTP 200 and an application shell whose HTML did not contain a title list. That shell is a failed document check (`http_status` null). A guessed script URL under that application returned HTTP 404 and is not used.
