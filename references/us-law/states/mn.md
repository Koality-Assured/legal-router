---
doc_kind: reference
canonical_id: us-law-state-mn
purpose: [reference]
topics: [us-law, minnesota, statutes, courts]
rag_keywords: [Minnesota, Minnesota Constitution, Minnesota Statutes, Minnesota Rules, Minnesota Supreme Court]
version: captured-2026-10-07
publication: Minnesota Office of the Revisor of Statutes
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://www.revisor.mn.gov/
advisory_only: true
---

# Minnesota

This is a point-in-time locator captured on 2026-10-07. It is not legal advice and it is not a filing.

The Office of the Revisor of Statutes publishes the constitution, statutes, session laws, administrative rules, and court rules. The statutes page is titled "2025 MN Statutes" and describes Minnesota Statutes as a compilation of the general and permanent laws of the state. Chapter 480 is the Supreme Court and Chapter 480A is the Court of Appeals. The court website returned HTTP 403 to this capture. Appellate docket status is on P-MACS.

## Sources

| Role | Authority | Title | URL | Status |
| --- | --- | --- | --- | --- |
| Constitution | official-primary | MN Constitution | https://www.revisor.mn.gov/constitution/ | 200 |
| Statutes | official-primary | 2025 MN Statutes | https://www.revisor.mn.gov/statutes/ | 200 |
| Session laws | official-primary | MN Laws | https://www.revisor.mn.gov/laws/ | 200 |
| Administrative code | official-primary | MN Rules | https://www.revisor.mn.gov/rules/ | 200 |
| Judicial branch | official-primary | Minnesota Judicial Branch | https://www.mncourts.gov/ | 403 |
| Intermediate appellate | official-primary | Chapter 480A, Court of Appeals | https://www.revisor.mn.gov/statutes/cite/480A | 200 |
| Dockets | official-primary | P-MACS public site | https://macsnc.courts.state.mn.us/ctrack/publicLogin.do | 200 |
| Court rules | official-primary | MN Court Rules | https://www.revisor.mn.gov/court_rules/ | 200 |
| Attorney general opinions | official-primary | Attorney General Opinions | https://www.ag.state.mn.us/office/opinions/ | 200 |

## Constitution

The revisor publishes the constitution at `/constitution/`. The page title is "MN Constitution."

## Statutes

The statute browse is 105 chapter ranges, from chapters 1-2A through 645-648, so the full chapter list is over the 120-line cap. Chapters opened for this capture:

- Chapter 14. Administrative Procedure
- Chapter 480. Supreme Court
- Chapter 480A. Court of Appeals
- Chapter 609. Criminal Code

## Administrative code

Minnesota Rules are published by the revisor at `/rules/`. The page title is "MN Rules."

## Courts and dockets

`https://www.mncourts.gov/`, `/SupremeCourt.aspx`, `/CourtOfAppeals.aspx`, and the same paths on `mncourts.gov` without `www` returned HTTP 403. Chapter 480 is titled "CHAPTER 480. SUPREME COURT." Chapter 480A is titled "CHAPTER 480A. COURT OF APPEALS." P-MACS returned HTTP 200 on GET. HEAD returned HTTP 403. The page is titled "C-Track - Public Site" and says it is the public access site for the Minnesota Appellate Courts Case Management System, covering the Supreme Court and the Court of Appeals.

## Rules and attorney general opinions

The revisor's court-rules index includes Criminal Procedure, Civil Procedure, Evidence, General Rules of Practice, and Appellate Procedure. The Attorney General opinions page says written opinions are issued to constitutional executive officers, state agencies, bodies of the legislature, and attorneys for local governments or pension funds, and that opinions from 1993 forward are linked from that page.

## Matter map

Criminal code is Chapter 609. Criminal procedure, civil procedure, and evidence are court-rule sets on the revisor's court-rules index. The Supreme Court is Chapter 480. The Court of Appeals is Chapter 480A. Administrative procedure is Chapter 14. Agency rules are Minnesota Rules.

## Local government

Ordinances are adopted by the local unit. The revisor browse is a set of chapter ranges, and this capture did not open a local-government heading. This capture does not supply a municipal code URL.

## Capture notes

Checked with Invoke-WebRequest, HEAD then GET, 25-second timeout, on 2026-10-07. The court-site 403 results are recorded as failed checks. No replacement court host was substituted.
