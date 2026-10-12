---
doc_kind: reference
canonical_id: us-law-federal-register-and-presidential-documents
purpose: [reference]
topics: [us-law, federal]
rag_keywords: [federal-register, executive-order, proclamation, proposed-rule, final-rule, compilation-of-presidential-documents]
version: "captured-2026-10-07"
publication: Federal Register
captured_at_utc: "2026-10-07T18:00:00Z"
upstream_url: https://www.govinfo.gov/help/fr
advisory_only: true
---

# Federal Register and presidential documents

This capture is a point-in-time locator and structural summary for attorney review, not legal advice and not a filing.

## Purpose

The Federal Register is the official daily publication for agency rules, proposed rules, and notices, and for executive orders and other presidential documents. It is published by the Office of the Federal Register at the National Archives, Monday through Friday except federal holidays, and GovInfo updates it daily by 6 a.m. Volumes 60 (1995) forward are on GovInfo as full issues or smaller sections.

## Source ranking

| Rank | Source | What it is |
| --- | --- | --- |
| official-primary | [GovInfo Federal Register help](https://www.govinfo.gov/help/fr) | Official daily publication, including proposed rules and final rules. |
| official-primary | [GovInfo FR collection](https://www.govinfo.gov/app/collection/fr) | GPO electronic edition. FederalRegister.gov calls this the official electronic version. |
| official-primary | [Compilation of Presidential Documents](https://www.govinfo.gov/help/cpd) | Official OFR publication of White House Press Secretary releases. Not the same series as the Register. |
| official-mirror | [federalregister.gov](https://www.federalregister.gov/) | OFR/GPO XML site. Its banner says it is not an official legal edition and does not provide legal notice until the Administrative Committee says otherwise. Each document links to the GovInfo PDF. |
| official-primary | [Archives executive-order FAQ](https://www.archives.gov/federal-register/executive-orders/about.html) | What an executive order is, and what a disposition table records. Page last reviewed 2019-05-20. |
| official-primary | [White House presidential actions](https://www.whitehouse.gov/presidential-actions/) | Issuing office’s site. Not the Federal Register citation. |

## Structural summary

### Path segments the human asked about

`https://www.federalregister.gov/presidential-documents/executive-orders` returned HTTP 200. The page title is “Federal Register :: Executive Orders.” The page offers “view all Presidential Documents,” so `presidential-documents` is that section and `executive-orders` is this document type. The proclamations path `.../presidential-documents/proclamations` is titled “Federal Register :: Proclamations.”

### Proposed rules and final rules

GovInfo describes the Register as the daily home of rules, proposed rules, and notices of federal agencies, plus executive orders and other presidential documents. A proposed rule is the agency’s proposal, published for comment. A final rule is the rule as adopted and published. Codification of a final rule into the annual CFR happens later, on that title’s revision date. The eCFR folds Federal Register amendments in daily, but it is not the legal edition. See the CFR page.

### How an executive order gets a Federal Register citation

The pieces below are what the fetched OFR pages say, in order:

1. An executive order is a numbered official document through which the President manages the operations of the federal government.
2. After the President signs it, the White House sends it to the Office of the Federal Register. The White House cannot send it before signature, so publication lags the signature by at least one day and typically by several days.
3. The OFR numbers each order consecutively as it is received, as part of one series, and publishes it in the daily Federal Register shortly after receipt. Presidential documents get priority processing and appear on public inspection the business day before publication.
4. The OFR disposition tables, kept by administration and year of signature, record the order number, the date the President signed it, the Federal Register volume, page number, and issue date, the title, later amendments, and current status where the editors track it. That volume-page-date triple is the Federal Register citation. The tables are informational listings, not definitive legal authority, and they change when later orders, proclamations, rules, or public laws amend an order.
5. Beginning with Executive Order 7316 (March 13, 1936), the text also appears in the sequential editions of Title 3 of the CFR. The [OFR tutorial](https://www.archives.gov/federal-register/tutorial/text) states that executive orders are reprinted annually in Title 3, compiled rather than codified: an amendment is not merged back into an earlier order inside the CFR. Proclamations are numbered the same way, as received by the OFR, and are likewise reprinted in Title 3 rather than codified. The tutorial describes ceremonial proclamations and substantive ones and says subject matter, not a difference in legal form, decides which document type is used.

The Compilation of Presidential Documents is the official series of materials released by the White House Press Secretary (daily compilation from January 20, 2009, and the weekly compilation back to 1993 electronically). It is the press record. The Register is the publication that carries the legal citation.

## Matter map

| Class | Where this corpus fits |
| --- | --- |
| Administrative | Proposed and final rules, and agency notices. |
| Constitutional | An executive order can be the act under review. The Register publishes it; it does not decide its validity. |
| Criminal | A rule or order may implement a criminal statute. The offense is still in the Code. |
| Civil | Same pattern: the Register is the publication, not the civil procedure. |

## What is stored locally vs what still needs a live fetch

Stored here: the publication path from signature to a volume-page-date citation, and the split among the Register, Title 3, and the Compilation of Presidential Documents. Not stored: any order, proclamation, or rule. For a citation, open the GovInfo PDF. FederalRegister.gov is useful for finding that PDF and says so on the page.

## Capture notes

Captured 2026-10-07. The three FederalRegister.gov presidential paths, the GovInfo Register and CPD help pages, the Archives FAQ, and the Archives tutorial all returned HTTP 200. No citation example was copied from a sample order.
