---
doc_kind: reference
canonical_id: us-law-source-ranking
purpose: [reference]
topics: [us-law, sources]
rag_keywords: [official-primary, govinfo, uscode, ecfr, slip-opinion, unofficial-mirror]
version: "captured-2026-10-07"
publication: AI Router US law source ranking
captured_at_utc: "2026-10-07T18:00:00Z"
upstream_url: https://www.govinfo.gov/
advisory_only: true
---

# Source ranking for US primary law

This capture is a point-in-time locator for attorney review. It is not legal advice and it is not a filing.

## Rank

Use the highest row that was actually fetched for the proposition.

| Rank | Authority value | What counts | Examples checked 2026-10-07 |
| --- | --- | --- | --- |
| 1 | `official-primary` | The government or court that issues the text | GovInfo (`https://www.govinfo.gov/`, HTTP 200), including the USC collection while the Law Revision Counsel site is down; eCFR (`https://www.ecfr.gov/`, HTTP 200), Federal Register (`https://www.federalregister.gov/`, HTTP 200), Supreme Court (`https://www.supremecourt.gov/opinions/opinions.aspx`, HTTP 200), uscourts.gov rules (`https://www.uscourts.gov/forms-rules/current-rules-practice-procedure`, HTTP 200), National Archives Constitution (`https://www.archives.gov/founding-docs/constitution`, HTTP 200), OLC (`https://www.justice.gov/olc`, HTTP 200), USSC guidelines (`https://www.ussc.gov/guidelines`, HTTP 200), state legislature and state court sites named on that state's page |
| 2 | `official-mirror` | A second official publisher of the same text | GovInfo CFR beside eCFR. GovInfo's USC collection is the working Code publisher for this capture, not a fallback behind a live OLRC page. |
| 3 | `unofficial` | A private host republishing law | Cornell LII USC HTML (`https://www.law.cornell.edu/uscode/text`, HTTP 200). Useful as a reading copy. It does not outrank GovInfo. |

## Not authority

- Commercial annotated codes and reporters. Headnotes and key numbers are copyrighted compilation. Do not copy them.
- Justia, FindLaw, and similar mirrors, unless a jurisdiction page records a specific page as unofficial after a successful fetch.
- Blogs, bar CLE slides, and Wikipedia. See the empirical standard's disallowed tier.
- Model and uniform acts, until the jurisdiction's official code shows an enactment.
- Attorney general opinions and OLC memos. They explain the author's view. They are not statutes and not judicial holdings. OLC's site resolved HTTP 200 on capture day.

## Dockets

PACER (`https://pacer.uscourts.gov/`, HTTP 200) is the official federal docket system. It is fee-based. Do not scrape it. Opinion sites and docket sites are different products. A slip opinion does not prove the docket sheet, and a docket entry does not prove the opinion text.

`https://www.congress.gov/` returned HTTP 403 to this workstation on 2026-10-07. It remains the Library of Congress bill system. Enacted text that this workstation could fetch is on GovInfo public laws (`https://www.govinfo.gov/app/collection/plaw`, HTTP 200). Do not describe Congress.gov as verified-200 from this capture.

`https://uscode.house.gov/` returned HTTP 200 on 2026-10-07 with the title "Under Maintenance". That response is not the United States Code. Use the GovInfo USC collection until a fetch returns the Code itself. The Office of the Law Revision Counsel remains the issuing office.

A 200 whose body is an application shell, a browser challenge, or a maintenance notice is a failed document check. Record `http_status` null. Do not copy a title index or a court name from that body.

## Slip path segments

`https://www.supremecourt.gov/opinions/slipopinion/25` resolved HTTP 200. The `25` segment is a Court term path, not a permanent collection name. Prefer the opinions index when citing the publisher, and record the term path actually used.

## When ranks conflict

Quote neither from memory. Fetch both official pages, record both URLs and the capture time, and stop for a person if the wording differs.
