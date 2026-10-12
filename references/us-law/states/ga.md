---
doc_kind: reference
canonical_id: us-law-state-ga
purpose: [reference]
topics: [us-law, georgia]
rag_keywords: [Georgia, Official Code of Georgia Annotated, Supreme Court of Georgia, Court of Appeals of Georgia, Georgia Rules and Regulations]
version: captured-2026-10-07
publication: Georgia General Assembly
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://www.legis.ga.gov/laws/codes
advisory_only: true
---

# Georgia

Advisory capture of official entry points. This is not legal advice and it does not reproduce statutory, regulatory, or opinion text.

## Identity

The Georgia General Assembly laws pages for the code and the constitution returned HTTP 200 as an application shell without a title index in the HTML. The Secretary of State publishes the Rules and Regulations of the State of Georgia. The Supreme Court of Georgia and the Court of Appeals of Georgia publish opinions, rules, and docket search on their own sites.

## Sources

| Role | Authority | HTTP | Entry |
| --- | --- | --- | --- |
| constitution | official-primary | 200 | [Georgia General Assembly constitution path](https://www.legis.ga.gov/laws/constitution) |
| statutes | official-primary | 200 | [Georgia General Assembly codes path](https://www.legis.ga.gov/laws/codes) |
| session laws | official-primary | 200 | [Legislation Search - Georgia General Assembly](https://www.legis.ga.gov/legislation/all) |
| administrative code | official-primary | 200 | [Rules and Regulations of the State of Georgia](https://rules.sos.ga.gov/) |
| court of last resort opinions | official-primary | 200 | [2026 Opinions - Supreme Court of Georgia](https://www.gasupreme.us/2026-opinions/) |
| intermediate appellate court | official-primary | 200 | [Court of Appeals of the State of Georgia](https://www.gaappeals.gov/) |
| intermediate appellate court | official-primary | 200 | [Opinion Search - Georgia Court of Appeals](https://www.gaappeals.gov/opinion-search/) |
| dockets | official-primary | 200 | [Docket Search - Supreme Court of Georgia](https://www.gasupreme.us/docket-search/) |
| court rules | official-primary | 200 | [Supreme Court of Georgia Rules](https://www.gasupreme.us/rules/) |
| attorney general opinions | official-primary | 200 | [Opinions - Office of the Attorney General](https://law.georgia.gov/opinions) |
| court of last resort opinions | official-primary | 200 | [Supreme Court of Georgia](https://www.gasupreme.us/) |
| court rules | official-primary | 200 | [Georgia Supreme Court Rules - Georgia Courts](https://georgiacourts.gov/georgia-supreme-court-rules/) |

## Constitution

The General Assembly constitution URL returned HTTP 200 as an application shell. The HTML did not include the constitution text. `https://sos.ga.gov/page/georgia-constitution` returned HTTP 403 and is not used.

## Statutes

The General Assembly codes URL returned HTTP 200 as an application shell. The HTML did not include an Official Code of Georgia Annotated title list, so no title index is recorded. The Judicial Council legal-professionals page links the code text to a commercial host. That commercial URL is not cataloged.

## Administrative code

The Secretary of State publishes the Rules and Regulations of the State of Georgia as the compilation of agency rules filed with that office. The fetched page describes that electronic compilation. It does not expose a static title list in the HTML without JavaScript.

## Courts and dockets

The Supreme Court of Georgia is the court of last resort. Its 2026 opinions page and docket search returned HTTP 200. The Court of Appeals of Georgia is the intermediate appellate court; its home page and opinion search returned HTTP 200. `https://www.gaappeals.us/` redirected to a docket host and is not the cataloged court home page.

## Rules and attorney general opinions

Supreme Court of Georgia rules are on the court's site. The Judicial Council also publishes a rules page at `https://georgiacourts.gov/georgia-supreme-court-rules/`, which returned HTTP 200. Attorney General opinions are on law.georgia.gov.

## Matter map

Criminal, civil procedure, evidence, and courts titles are not listed here because the official codes page did not return a title index in the HTML. Administrative rules are the Secretary of State compilation above.

## Local government

County and municipal ordinances are adopted by those governments. This capture does not supply county or city ordinance-host URLs.

## Capture notes

Checked 2026-10-07 with Invoke-WebRequest HEAD then GET, 25 second timeout. Failed checks: `https://www.gasupreme.us/opinions/` returned HEAD 404 and the GET connection closed; `https://sos.ga.gov/page/georgia-constitution` returned HTTP 403. The Supreme Court home page `https://www.gasupreme.us/` returned HTTP 200.
