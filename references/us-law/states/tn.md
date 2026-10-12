---
doc_kind: reference
canonical_id: us-law-state-tn
purpose: [reference]
topics: [us-law, tennessee]
rag_keywords: [tennessee-constitution, tennessee-code, tennessee-rules-and-regulations, public-acts]
version: captured-2026-10-07
publication: Tennessee Secretary of State and Tennessee General Assembly
captured_at_utc: "2026-10-07T18:00:00Z"
upstream_url: https://sos.tn.gov/publications/services/tennessee-constitution
advisory_only: true
---

# Tennessee

This capture is a point-in-time locator for attorney review. It is not legal advice and it is not a filing.

## Identity

Tennessee (TN). The Secretary of State publishes the constitution and the official compilation of rules and regulations. The General Assembly publications page describes the Tennessee Code as the official compilation updated by the annual codification bill. The Administrative Office of the Courts host returned a browser-validation page to this check, so this capture does not describe appellate structure from that host and does not name a separate criminal court of last resort.

## Source table

| Role | Publisher page | HTTP |
| --- | --- | --- |
| Constitution | [Tennessee Constitution](https://sos.tn.gov/publications/services/tennessee-constitution) | 200 |
| Code landing | [Legislative publications](https://wapp.capitol.tn.gov/apps/WebPublications/) | 200 |
| Session laws | [Acts and resolutions](https://sos.tn.gov/publications/services/acts-and-resolutions) | 200 |
| Administrative rules | [Rules and regulations](https://sos.tn.gov/publications/services/effective-rules-and-regulations-of-the-state-of-tennessee) | 200 |
| Courts host | [tncourts.gov](https://www.tncourts.gov/) | 200 challenge page, not verified |
| Commercial code text | [LexisNexis Tennessee Code](https://www.lexisnexis.com/hottopics/tncode) | 200 |

## Constitution

`https://sos.tn.gov/publications/services/tennessee-constitution` returned HTTP 200. The page title is Tennessee Constitution and the retrieved text says the constitution was updated January 11, 2023. This capture does not copy the text.

## Statutes

`https://wapp.capitol.tn.gov/apps/WebPublications/` returned HTTP 200. It describes the annual code bill as integrating public acts into the Tennessee Code so that the updated code is the official compilation. The page links the code text to `https://www.lexisnexis.com/hottopics/tncode`, which returned HTTP 200. That host is unofficial. This capture does not copy a title index from it. The publications page itself did not embed a title list. General Assembly home: `https://www.capitol.tn.gov/` (HTTP 200).

## Administrative code

`https://sos.tn.gov/publications/services/effective-rules-and-regulations-of-the-state-of-tennessee` returned HTTP 200. The page says these are the current official rules and regulations, cited as the Rules and Regulations of the State of Tennessee, including amendments, repeals, and deletions. The retrieved page is an agency-number list, not a short subject-title index. It is longer than the 120-line cap, so the agency numbers are not copied.

## Courts and dockets

`https://www.tncourts.gov/`, `https://www.tncourts.gov/general-public`, and `https://www.tncourts.gov/courts/supreme-court` each returned HTTP 200. The body was a JavaScript browser-validation challenge, not the court page. No docket URL, opinion URL, or intermediate-court URL was confirmed from a readable official response. Do not treat a commercial reporter as a substitute.

## Rules and attorney general

Court rules were not read from tncourts.gov. Administrative rules are the Secretary of State compilation above. An Attorney General opinions URL was not verified. The legislative library page that mentions opinions in a collection list was not part of this HTTP set.

## Matter map

- Criminal, civil, and evidence titles of the Tennessee Code were not copied from the Lexis host. Use the publications page and then the commercial text only as an unofficial reading copy.
- Administrative: Rules and Regulations of the State of Tennessee on the Secretary of State site.
- Session laws: `https://sos.tn.gov/publications/services/acts-and-resolutions` (HTTP 200). The request to `https://sos.tn.gov/division-publications/acts-and-resolutions` redirected there.

## Local government

No county or city code was captured. Ordinances stay on each local government's site. See [`../local-government.md`](../local-government.md).

## Capture notes

Checked 2026-10-07 with PowerShell `Invoke-WebRequest`, HEAD then GET, 25-second timeout. The courts host is an HTTP 200 failure of content, not a DNS failure. The code title index is intentionally absent because the only resolved full-text host is LexisNexis.
