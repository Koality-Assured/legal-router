---
doc_kind: reference
canonical_id: us-law-state-ny
purpose: [reference]
topics: [us-law, new-york]
rag_keywords: []
version: "captured-2026-10-07"
publication: Consolidated Laws of New York
captured_at_utc: "2026-10-07T18:00:00Z"
upstream_url: "http://public.leginfo.state.ny.us/lawssrch.cgi?NVLWO:"
advisory_only: true
---

# New York

This capture is a point-in-time locator for attorney review, not legal advice and not a filing.

## Identity

The Senate Open Legislation URL and the Law Reporting Bureau decisions URL both returned HTTP 403. This capture does not name a court of last resort from those responses. The verified statute entry point is the Legislative Bill Drafting Commission laws search, which returned HTTP 200.

## Sources

| Role | Authority | Title | URL |
| --- | --- | --- | --- |
| statutes | official-primary | Consolidated Laws of New York | https://www.nysenate.gov/legislation/laws/CONSOLIDATED |
| constitution | official-primary | Constitution (CNS) | https://www.nysenate.gov/legislation/laws/CNS |
| session-laws | official-primary | Laws of New York, Legislative Bill Drafting Commission | http://public.leginfo.state.ny.us/lawssrch.cgi?NVLWO: |
| session-laws | official-primary | New York State Assembly bill search | https://nyassembly.gov/leg/ |
| administrative-code | official-primary | Department of State, State Register and NYCRR compiler | https://dos.ny.gov/state-register |
| administrative-code | unofficial | Unofficial NYCRR on Westlaw, under contract with the Department of State | https://govt.westlaw.com/nycrr/Index |
| decisions | official-primary | New York Official Reports decisions | https://nycourts.gov/reporter/Decisions.htm |
| intermediate-appellate | official-primary | Appellate Division courts page | https://www.nycourts.gov/courts/appellatedivisions.shtml |
| dockets | official-primary | WebCivil | https://iapps.courts.state.ny.us/webcivil/FCASMain |
| court-rules | official-primary | Trial court rules | https://www.nycourts.gov/rules/trialcourts/index.shtml |
| attorney-general-opinions | official-primary | Attorney General opinions path | https://ag.ny.gov/opinions |

The Legislative Bill Drafting Commission laws search and the Assembly bill search returned HTTP 200. The other rows failed Invoke-WebRequest. Do not treat a 403 body as a stored copy.

## Constitution

`https://www.nysenate.gov/legislation/laws/CNS` returned HTTP 403, and a later content fetch timed out. Article titles are not listed.

## Statutes

The Senate consolidated-laws URL returned HTTP 403 to Invoke-WebRequest on 2026-10-07, including a retry with a browser user-agent. No consolidated-law index is stored. The Legislative Bill Drafting Commission laws search returned HTTP 200 and says the Laws database is current. It showed a chapter range (Chapters 1-312 on that page) and links for consolidated and unconsolidated laws. Open that page for the live index. Do not treat a blocked Senate copy as the title list.

## Administrative code

The Department of State State Register URL and the Westlaw NYCRR URL both returned HTTP 403. No administrative-code description is stored from those responses.

## Courts and dockets

The Law Reporting Bureau, WebCivil, and trial-rules URLs returned HTTP 403. No court structure or fee statement was stored from those responses.

## Court rules and attorney general opinions

Trial-court rules returned HTTP 403. `https://ag.ny.gov/opinions` returned HTTP 404. No substitute opinions host was invented.

## Matter map

Criminal, civil, and administrative titles were not stored. The Senate index returned HTTP 403. Use the Legislative Bill Drafting Commission page that returned HTTP 200, and do not fill title names from memory.

## Local government

Municipal ordinances are city-specific and must be located from that municipality's official code host. `https://dos.ny.gov/local-laws` returned HTTP 403, and no fetched page stated a county total. No county ordinance URL is listed.

## Capture notes and failed URL checks

Checked 2026-10-07 with Invoke-WebRequest, HEAD then GET, 25-second timeout. `http://public.leginfo.state.ny.us/lawssrch.cgi?NVLWO:` and `https://nyassembly.gov/leg/` returned HTTP 200 on HEAD. The https form of the Legislative Bill Drafting Commission laws search did not return a status.

The Senate consolidated-laws and constitution URLs, Department of State register and local-laws URLs, Westlaw NYCRR, Court of Appeals, Official Reports, Appellate Division, WebCivil, and trial-rules URLs returned HTTP 403. `https://ag.ny.gov/opinions` returned HTTP 404. Status for each URL is in the catalog JSON. No substitute host was invented.
