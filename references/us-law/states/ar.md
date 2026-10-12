---
doc_kind: reference
canonical_id: us-law-state-ar
purpose: [reference]
topics: [us-law, arkansas]
rag_keywords: [arkansas-code, constitution-of-1874, code-of-arkansas-rules, arkansas-supreme-court]
version: captured-2026-10-07
publication: Arkansas General Assembly and Arkansas Judiciary
captured_at_utc: "2026-10-07T18:00:00Z"
upstream_url: https://www.arkleg.state.ar.us/ArkansasLaw/
advisory_only: true
---

# Arkansas

This capture is a point-in-time locator for attorney review. It is not legal advice and it is not a filing.

## Identity

Arkansas (AR). The Supreme Court page states that the current constitution was ratified in 1874, that Amendment 80 vests judicial power in the Supreme Court and other courts established by the constitution, and that the Supreme Court has statewide appellate jurisdiction and general superintending control over all courts of the state. The same page says the Court of Appeals may seek to transfer a case to the Supreme Court. No separate criminal court of last resort is named there.

## Source table

| Role | Publisher page | HTTP |
| --- | --- | --- |
| Code and constitution | [Arkansas Law](https://www.arkleg.state.ar.us/ArkansasLaw/) | 200 |
| Session laws | [Acts](https://www.arkleg.state.ar.us/Acts) | 200 |
| Administrative rules | [Code of Arkansas Rules](https://codeofarrules.arkansas.gov/) | 200 |
| Supreme Court | [Supreme Court](https://arcourts.gov/courts/supreme-court) | 200 |
| Court of Appeals | [Court of Appeals](https://arcourts.gov/courts/court-of-appeals) | 200 |
| Opinions and rules | [Opinions and court rules](https://opinions.arcourts.gov/ark/en/nav.do) | 200 |
| Dockets | [Case search](https://caseinfo.arcourts.gov/opad) | 200 |
| Attorney general | [AG opinions search](https://arkansasag.gov/divisions/opinions-foia/attorney-general-opinions-search/) | 200 |

## Constitution

The legislature's Arkansas Law page (HTTP 200) is titled around "Arkansas Code and Constitution of 1874." The judiciary constitutions page is `https://arcourts.gov/courts/supreme-court/library/constitutions` (HTTP 200). The Supreme Court page discusses the Constitution of 1874 and Amendment 80. This capture does not copy constitutional text. The Arkansas Law HTML did not include a code title index. It links to `advance.lexis.com` behind a leaving-site notice. That commercial host is not used as the index.

## Statutes

No top-level title list was present in the Arkansas Law HTML. Acts, which are the session laws, are at `https://www.arkleg.state.ar.us/Acts` (HTTP 200). The same host without the trailing slash also returned HTTP 200.

## Administrative code

The Code of Arkansas Rules is at `https://codeofarrules.arkansas.gov/` (HTTP 200). The page is a search front. It did not print a short title index in the text retrieved here.

## Courts and dockets

Supreme Court: `https://arcourts.gov/courts/supreme-court` (HTTP 200; `www.arcourts.gov` redirects to `arcourts.gov`). The page says opinions handed down before February 14, 2009, have an official version in the bound Arkansas Reports, and that the electronic version is the official version from that date. Slip opinions are not the final decisions until marked with the court's seal.

Court of Appeals: `https://arcourts.gov/courts/court-of-appeals` (HTTP 200).

Opinions, court rules, and administrative orders: `https://opinions.arcourts.gov/ark/en/nav.do` (HTTP 200).

Public case search: `https://caseinfo.arcourts.gov/cconnect/PROD/public/ck_public_qry_main.cp_main_idx` returned HTTP 200 and landed on `https://caseinfo.arcourts.gov/opad`.

## Rules and attorney general

Court rules are on the opinions host above and are linked from the judiciary site. Attorney General opinions search: `https://arkansasag.gov/divisions/opinions-foia/attorney-general-opinions-search/` (HTTP 200), linked from `https://arkansasag.gov/` (HTTP 200).

## Matter map

- Criminal and civil code titles were not in the legislature HTML. The Supreme Court page is the verified court-of-last-resort description: statewide appellate jurisdiction and superintending control, with the Court of Appeals able to seek transfer.
- Administrative: Code of Arkansas Rules.
- Evidence and procedure: court rules on the opinions host, not a title list this capture did not see.

## Local government

Circuit courts and district courts are courts on the judiciary site. They are not county codes. City ordinances stay on each city's site. See [`../local-government.md`](../local-government.md).

## Capture notes

Checked 2026-10-07 with PowerShell `Invoke-WebRequest`, HEAD then GET, 25-second timeout. The code title index is a gap because the official HTML named the Arkansas Code without listing titles.
