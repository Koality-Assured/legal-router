---
doc_kind: reference
canonical_id: us-law-federal-code-of-federal-regulations
purpose: [reference]
topics: [us-law, federal]
rag_keywords: [cfr, ecfr, code-of-federal-regulations, title-3, annual-edition, list-of-sections-affected]
version: "captured-2026-10-07"
publication: Code of Federal Regulations
captured_at_utc: "2026-10-07T18:00:00Z"
upstream_url: https://www.govinfo.gov/help/cfr
advisory_only: true
---

# Code of Federal Regulations

This capture is a point-in-time locator and structural summary for attorney review, not legal advice and not a filing.

## Purpose

The Code of Federal Regulations is the codification of the general and permanent rules published in the Federal Register by federal departments and agencies. The annual edition on GovInfo is the online counterpart of the print edition. The Electronic Code of Federal Regulations (eCFR) is a different product: a daily editorial compilation, not that annual edition.

## Source ranking

| Rank | Source | What it is |
| --- | --- | --- |
| official-primary | [GovInfo CFR help](https://www.govinfo.gov/help/cfr) | Annual edition, update cycle, and the statement that the eCFR is an unofficial editorial compilation. Help page last updated 2024-12-03. |
| official-primary | [GovInfo CFR collection](https://www.govinfo.gov/app/collection/cfr) | GPO collection. Titles from 1997 forward; selected volumes back to 1996. |
| official-mirror | [eCFR](https://www.ecfr.gov/) | OFR/GPO informational compilation. The eCFR’s own page says it is not yet an ACFR-recognized legal edition. |
| official-mirror | [eCFR title API](https://www.ecfr.gov/api/versioner/v1/titles) | Title names below. API `meta.date` was 2026-10-05. |
| official-primary | [Archives CFR page](https://www.archives.gov/federal-register/cfr) | OFR’s archives.gov entry point for the CFR. |

## Structural summary

GovInfo is current with the published print version. A title or volume missing from the browse has not been published yet. Prior editions stay online when a new one is added. The 50 titles are revised once a year on a stagger:

- Titles 1–16 as of January 1
- Titles 17–27 as of April 1
- Titles 28–41 as of July 1
- Titles 42–50 as of October 1

Inside a title, chapters usually carry the issuing agency’s name, then parts, subparts, and sections. A citation such as 21 CFR 310.502 is title, part, and section. The year in “Revised as of” is the edition year and is not always present in a citation.

The eCFR page states that the eCFR is a web version updated daily to reflect the current status, built from CFR material and Federal Register amendments. The Administrative Committee of the Federal Register authorized the Office of the Federal Register and GPO to maintain it as an informational resource, with a stated aim of eventual official recognition. Until then, legal research is supposed to be checked against the current official CFR edition, the daily Federal Register, and the List of CFR Sections Affected. GovInfo’s help page uses the same distinction and calls the eCFR unofficial.

Title names below are the eCFR API list, not a reprint of any part. Title 35 is reserved. Title 2’s name on this fetch is “Federal Financial Assistance.”

- 1 — General Provisions
- 2 — Federal Financial Assistance
- 3 — The President
- 4 — Accounts
- 5 — Administrative Personnel
- 6 — Domestic Security
- 7 — Agriculture
- 8 — Aliens and Nationality
- 9 — Animals and Animal Products
- 10 — Energy
- 11 — Federal Elections
- 12 — Banks and Banking
- 13 — Business Credit and Assistance
- 14 — Aeronautics and Space
- 15 — Commerce and Foreign Trade
- 16 — Commercial Practices
- 17 — Commodity and Securities Exchanges
- 18 — Conservation of Power and Water Resources
- 19 — Customs Duties
- 20 — Employees' Benefits
- 21 — Food and Drugs
- 22 — Foreign Relations
- 23 — Highways
- 24 — Housing and Urban Development
- 25 — Indians
- 26 — Internal Revenue
- 27 — Alcohol, Tobacco Products and Firearms
- 28 — Judicial Administration
- 29 — Labor
- 30 — Mineral Resources
- 31 — Money and Finance: Treasury
- 32 — National Defense
- 33 — Navigation and Navigable Waters
- 34 — Education
- 35 — Reserved
- 36 — Parks, Forests, and Public Property
- 37 — Patents, Trademarks, and Copyrights
- 38 — Pensions, Bonuses, and Veterans' Relief
- 39 — Postal Service
- 40 — Protection of Environment
- 41 — Public Contracts and Property Management
- 42 — Public Health
- 43 — Public Lands: Interior
- 44 — Emergency Management and Assistance
- 45 — Public Welfare
- 46 — Shipping
- 47 — Telecommunication
- 48 — Federal Acquisition Regulations System
- 49 — Transportation
- 50 — Wildlife and Fisheries

Title 3 is “The President.” Executive orders are compiled there annually; they are not codified the way agency rules are. See the Federal Register page.

## Matter map

| Class | Where this corpus fits |
| --- | --- |
| Administrative | This is the corpus. An agency rule lives in a CFR title; the statute that authorizes it lives in the United States Code. |
| Criminal | Some titles implement criminal statutes. The offense is still Title 18 unless Congress placed it elsewhere. |
| Civil | Procedure is the civil rules and Title 28. A CFR title can create duties that a civil case then enforces. |
| Constitutional | Not this corpus. |

## What is stored locally vs what still needs a live fetch

Stored here: the annual-versus-eCFR distinction, the revision stagger, and the title names as of the 2026-10-05 API snapshot. Not stored: any section. For a citation, open the annual GovInfo edition for the revision year and then the Federal Register and the List of Sections Affected for later amendments. The eCFR is the daily view, not the legal edition.

## Capture notes

Captured 2026-10-07. The eCFR titles page `https://www.ecfr.gov/titles` returned HTTP 200; the name list used here is the versioner API, which returned the names in JSON. No title name was taken from an unofficial mirror.
