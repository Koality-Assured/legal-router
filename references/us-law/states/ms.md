---
doc_kind: reference
canonical_id: us-law-state-ms
purpose: [reference]
topics: [us-law, mississippi]
rag_keywords: [mississippi-legislature, mississippi-judiciary, mississippi-code, court-rules]
version: captured-2026-10-07
publication: Mississippi Legislature and Mississippi Judiciary
captured_at_utc: "2026-10-07T18:00:00Z"
upstream_url: https://legislature.ms.gov/
advisory_only: true
---

# Mississippi

This capture is a point-in-time locator for attorney review. It is not legal advice and it is not a filing.

## Identity

Mississippi (MS). The judiciary site lists a Supreme Court and a Court of Appeals as separate appellate pages. The Supreme Court page body retrieved here is site navigation, not a sentence that says "court of last resort." No separate criminal court of last resort was confirmed. Secretary of State pages for the constitution, the unannotated code, and the administrative code returned HTTP 403, so those texts are not linked as verified reading copies.

## Source table

| Role | Publisher page | HTTP |
| --- | --- | --- |
| Legislature | [Mississippi Legislature](https://legislature.ms.gov/) | 200 |
| Session measures | [Legislation search](https://legislature.ms.gov/legislation-search/) | 200 |
| Supreme Court | [Supreme Court](https://courts.ms.gov/appellatecourts/sc/sc.php) | 200 |
| Court of Appeals | [Court of Appeals](https://courts.ms.gov/appellatecourts/coa/coa.php) | 200 |
| Dockets | [Appellate docket login](https://courts.ms.gov/appellatecourts/docket/login.php) | 200 |
| Court rules | [Rules of court](https://courts.ms.gov/research/rules/rules.php) | 200 |
| Commercial code | [LexisNexis Mississippi Code](https://www.lexisnexis.com/hottopics/mscode/) | 200 |
| Secretary of State | [sos.ms.gov](https://www.sos.ms.gov/) | 403 |

## Constitution

`https://www.sos.ms.gov/publications-external-affairs/publications/mississippi-constitution` and the constitution PDF under `sos.ms.gov` returned HTTP 403. No other official constitution URL was verified. This capture does not substitute an unofficial constitution text.

## Statutes

`https://legislature.ms.gov/` returned HTTP 200. The judiciary research navigation links the code to `https://www.lexisnexis.com/hottopics/mscode/`, which returned HTTP 200. That host is unofficial. This capture does not copy a title index from it. The Secretary of State code page `https://www.sos.ms.gov/publications-external-affairs/mississippi-law` returned HTTP 403. Legislation search for bills and resolutions: `https://legislature.ms.gov/legislation-search/` (HTTP 200).

## Administrative code

`https://www.sos.ms.gov/regulation-enforcement/administrative-code` returned HTTP 403. No replacement administrative-code URL was verified.

## Courts and dockets

Judiciary home: `https://courts.ms.gov/` (HTTP 200). Supreme Court: `https://courts.ms.gov/appellatecourts/sc/sc.php` (HTTP 200). Court of Appeals: `https://courts.ms.gov/appellatecourts/coa/coa.php` (HTTP 200). Appellate docket login: `https://courts.ms.gov/appellatecourts/docket/login.php` (HTTP 200). The home page describes trial courts, including chancery, circuit, county, justice, and municipal courts. Those are court levels, not municipal codes.

## Rules and attorney general

Rules: `https://courts.ms.gov/research/rules/rules.php` (HTTP 200). `https://www.ago.ms.gov/` did not resolve: the remote name could not be resolved. No Attorney General opinions URL is included.

## Matter map

- Criminal and civil code titles were not copied from LexisNexis. The judiciary site is the verified court publisher.
- Administrative: the Secretary of State administrative-code URL returned HTTP 403.
- Evidence and procedure rules: start at the rules page above rather than at an unofficial code.

## Local government

Municipal court is a court listed on the judiciary site. A municipal ordinance is not that docket. See [`../local-government.md`](../local-government.md).

## Capture notes

Checked 2026-10-07 with PowerShell `Invoke-WebRequest`, HEAD then GET, 25-second timeout. Secretary of State hosts failed closed at HTTP 403. The code title index is absent because the only resolved full-text host is LexisNexis.
