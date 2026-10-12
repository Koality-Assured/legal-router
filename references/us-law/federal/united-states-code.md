---
doc_kind: reference
canonical_id: us-law-federal-united-states-code
purpose: [reference]
topics: [us-law, federal]
rag_keywords: [united-states-code, positive-law, prima-facie, title-18, title-28, title-5, olrc, govinfo]
version: "captured-2026-10-07"
publication: United States Code
captured_at_utc: "2026-10-07T18:00:00Z"
upstream_url: https://www.govinfo.gov/help/uscode
advisory_only: true
---

# United States Code

This capture is a point-in-time locator and structural summary for attorney review, not legal advice and not a filing.

## Purpose

The United States Code is the subject-matter codification of the general and permanent laws of the United States, divided into titles and published by the Office of the Law Revision Counsel of the House. GovInfo carries virtual main editions from 1994 forward, supplied by that office. Main editions run every six years, with annual supplements between them. The first edition was 1926; the next was 1934.

## Source ranking

| Rank | Source | What it is |
| --- | --- | --- |
| official-primary | [GovInfo USC help](https://www.govinfo.gov/help/uscode) | GPO explanation. Page last updated 2025-02-11. Positive-law numbers below are from this page. |
| official-primary | [GovInfo 2023 title browse](https://www.govinfo.gov/wssearch/rb/uscode/2023?fetchChildrenOnly=1) | Machine browse of the 2023 edition. Title names below are these package titles. |
| official-primary | [GovInfo USC collection](https://www.govinfo.gov/app/collection/uscode) | Collection home. The HTML shell did not include the title table; the browse endpoint did. |
| not verified | [uscode.house.gov](https://uscode.house.gov/) | HTTP 200 was a House.gov maintenance page, not the Code. The help page tells readers to use this host for the current title list. |
| unofficial | [Cornell LII `/uscode/text`](https://www.law.cornell.edu/uscode/text) | Convenience table of contents. See the path note below. |

## Structural summary

A positive-law title is legal evidence of the law. A title that has not been enacted into positive law is only prima facie evidence, and the Statutes at Large still govern. GovInfo’s help page lists these positive-law titles: 1, 3, 4, 5, 9, 10, 11, 13, 14, 17, 18, 23, 28, 31, 32, 35, 36, 37, 38, 39, 40, 41, 44, 46, 49, 51, and 54. It calls Title 52 editorially created and Title 53 reserved. That help text points at uscode.house.gov for the current list. Because the OLRC site was in maintenance, these marks were not re-checked against the OLRC table.

Names are the 2023 GovInfo edition (packages dated December 31, 2023). The edition index also lists a 2024 year node; that node reported no child titles in the same browse response, so 2024 names are not listed. Title 53 has no 2023 package.

- 1 — General Provisions — positive law
- 2 — The Congress — prima facie
- 3 — The President — positive law
- 4 — Flag and Seal, Seat of Government, and the States — positive law
- 5 — Government Organization and Employees — positive law
- 6 — Domestic Security — prima facie
- 7 — Agriculture — prima facie
- 8 — Aliens and Nationality — prima facie
- 9 — Arbitration — positive law
- 10 — Armed Forces — positive law
- 11 — Bankruptcy — positive law
- 12 — Banks and Banking — prima facie
- 13 — Census — positive law
- 14 — Coast Guard — positive law
- 15 — Commerce and Trade — prima facie
- 16 — Conservation — prima facie
- 17 — Copyrights — positive law
- 18 — Crimes and Criminal Procedure — positive law
- 19 — Customs Duties — prima facie
- 20 — Education — prima facie
- 21 — Food and Drugs — prima facie
- 22 — Foreign Relations and Intercourse — prima facie
- 23 — Highways — positive law
- 24 — Hospitals and Asylums — prima facie
- 25 — Indians — prima facie
- 26 — Internal Revenue Code — prima facie
- 27 — Intoxicating Liquors — prima facie
- 28 — Judiciary and Judicial Procedure — positive law
- 29 — Labor — prima facie
- 30 — Mineral Lands and Mining — prima facie
- 31 — Money and Finance — positive law
- 32 — National Guard — positive law
- 33 — Navigation and Navigable Waters — prima facie
- 34 — Crime Control and Law Enforcement — prima facie
- 35 — Patents — positive law
- 36 — Patriotic and National Observances, Ceremonies, and Organizations — positive law
- 37 — Pay and Allowances of the Uniformed Services — positive law
- 38 — Veterans' Benefits — positive law
- 39 — Postal Service — positive law
- 40 — Public Buildings, Property, and Works — positive law
- 41 — Public Contracts — positive law
- 42 — The Public Health and Welfare — prima facie
- 43 — Public Lands — prima facie
- 44 — Public Printing and Documents — positive law
- 45 — Railroads — prima facie
- 46 — Shipping — positive law
- 47 — Telecommunications — prima facie
- 48 — Territories and Insular Possessions — prima facie
- 49 — Transportation — positive law
- 50 — War and National Defense — prima facie
- 51 — National and Commercial Space Programs — positive law
- 52 — Voting and Elections — editorial; not in the positive-law list
- 53 — Reserved — help-page note; no 2023 package
- 54 — National Park Service and Related Programs — positive law

Cornell’s `/uscode/text` page is titled “U.S. Code: Table Of Contents.” The path opens that table. The page heading is “U.S. Code”; the page does not define the token `text` in a legend. LII also lists editorial appendices (Titles 5a, 11a, 18a, 28a, and 50a) that are not packages in the GovInfo 2023 list. Do not treat those appendices as Code titles.

## Matter map

| Class | Title |
| --- | --- |
| Criminal | Title 18, Crimes and Criminal Procedure. Title 34 is crime control and law enforcement, a different title. |
| Civil | Title 28, Judiciary and Judicial Procedure, for jurisdiction and much of the civil-procedure framework. |
| Administrative | Title 5, Government Organization and Employees, including administrative procedure. Agency rules themselves are in the CFR. |
| Constitutional | Not a Code title. Use the Constitution page. Title 28 is the judiciary, not the Constitution. |

## What is stored locally vs what still needs a live fetch

Stored here: the 2023 title names, the GovInfo help page’s positive-law numbers, and the locators. Not stored: any section text. GovInfo’s help page says researchers should still verify against the printed Code at GPO or a Federal Depository Library. A positive-law title is evidence; a prima facie title yields to the Statutes at Large.

## Capture notes

Captured 2026-10-07. `https://uscode.house.gov/`, `/browse.xhtml`, `/about_code.xhtml`, and `/download/download.shtml` each returned HTTP 200 with a House maintenance page. Those URLs are not treated as verified Code text. `https://www.govinfo.gov/bulkdata/USCODE` returned HTTP 404. No other OLRC host was invented.
