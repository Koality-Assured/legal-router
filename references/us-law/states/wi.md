---
doc_kind: reference
canonical_id: us-law-state-wi
purpose: [reference]
topics: [us-law, wisconsin, statutes, courts]
rag_keywords: [Wisconsin, Wisconsin Constitution, Wisconsin Statutes, Wisconsin Administrative Code, Wisconsin Supreme Court]
version: captured-2026-10-07
publication: Wisconsin Legislature
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://docs.legis.wisconsin.gov/
advisory_only: true
---

# Wisconsin

This is a point-in-time locator captured on 2026-10-07. It is not legal advice and it is not a filing.

The Legislative Reference Bureau publishes the statutes, the annotated Wisconsin Constitution, acts, the administrative code, supreme court rules, and opinions of the attorney general on docs.legis.wisconsin.gov. The statutes page says the 2023-24 Wisconsin Statutes are updated through 2025 Wis. Act 247 and through supreme court orders and Controlled Substances Board orders filed before and in effect on October 1, 2026, and that they are published and certified under s. 35.18. The Wisconsin Court System publishes the Supreme Court and the Court of Appeals. WSCCA is the appellate case-access system.

## Sources

| Role | Authority | Title | URL | Status |
| --- | --- | --- | --- | --- |
| Constitution | official-primary | Annotated Wisconsin Constitution | https://docs.legis.wisconsin.gov/constitution/wi | 200 |
| Statutes | official-primary | Wisconsin Statutes | https://docs.legis.wisconsin.gov/statutes/statutes | 200 |
| Session laws | official-primary | 2025 acts | https://docs.legis.wisconsin.gov/2025/related/acts | 200 |
| Administrative code | official-primary | Administrative Code | https://docs.legis.wisconsin.gov/code/admin_code | 200 |
| Court of last resort | official-primary | Wisconsin Supreme Court | https://www.wicourts.gov/courts/supreme/index.htm | 200 |
| Intermediate appellate | official-primary | Wisconsin Court of Appeals | https://www.wicourts.gov/courts/appeals/index.htm | 200 |
| Dockets | official-primary | WSCCA case search | https://wscca.wicourts.gov/ | 200 |
| Court rules | official-primary | Wisconsin Supreme Court Rules | https://docs.legis.wisconsin.gov/misc/scr | 200 |
| Attorney general opinions | official-primary | Opinions of the Attorney General | https://docs.legis.wisconsin.gov/misc/oag | 200 |

## Constitution

`https://docs.legis.wisconsin.gov/document/wisconsinconstitution/top` redirected to the annotated constitution at `/constitution/wi`. The page title is "Wisconsin Legislature: Annotated Wisconsin Constitution."

## Statutes

The statutes table of contents has 470 chapter entries, so this page keeps the subjects below and that total.

- Chapter 227. Administrative Procedure And Review
- Chapter 751. Supreme Court
- Chapter 752. Court Of Appeals
- Chapter 753. Circuit Courts
- Chapter 801. Civil Procedure - Commencement Of Action And Venue
- Chapter 901. Evidence - General Provisions
- Chapter 939. Crimes - General Provisions
- Chapter 967. Criminal Procedure - General Provisions

## Administrative code

The administrative code is published at `/code/admin_code` on the same legislative docs host as the statutes.

## Courts and dockets

The Supreme Court page is titled "Wisconsin Court System - Supreme Court." The Court of Appeals page is titled "Wisconsin Court System - Court of Appeals." `https://wscca.wicourts.gov/` and `https://wscca-prod.wicourts.gov/` both returned HTTP 200 and the title "Wisconsin Supreme Court and Court of Appeals Access."

## Rules and attorney general opinions

Supreme court rules are at `/misc/scr`. Opinions of the Attorney General are at `/misc/oag`. `https://www.wicourts.gov/sc/scrules.jsp` returned HTTP 500. Department of Justice opinion paths redirected to the DOJ home page and are not the opinions collection.

## Matter map

Criminal offenses begin at Chapter 939. Criminal procedure begins at Chapter 967. Civil procedure begins at Chapter 801. Evidence begins at Chapter 901. The Supreme Court is Chapter 751 and the Court of Appeals is Chapter 752. Administrative procedure and review is Chapter 227. Agency rules are in the administrative code.

## Local government

Local ordinances are adopted by the local unit. The statutes table of contents is the state-law index. This capture does not supply a municipal code URL.

## Capture notes

Checked with Invoke-WebRequest, HEAD then GET, 25-second timeout, on 2026-10-07. `https://docs.legis.wisconsin.gov/acts` returned HTTP 404. The 2025 acts URL above is the redirect target of `/document/acts/2025/top`.
