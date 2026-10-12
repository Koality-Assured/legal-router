---
doc_kind: reference
canonical_id: us-law-state-mi
purpose: [reference]
topics: [us-law, michigan, statutes, courts]
rag_keywords: [Michigan, Michigan Constitution, Michigan Compiled Laws, Michigan Court Rules, Michigan Supreme Court]
version: captured-2026-10-07
publication: Michigan Legislature
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://www.legislature.mi.gov/
advisory_only: true
---

# Michigan

This is a point-in-time locator captured on 2026-10-07. It is not legal advice and it is not a filing.

The legislature site publishes the Constitution of Michigan of 1963 and the Michigan Compiled Laws. On the capture date the laws banner read "Michigan Compiled Laws Complete Through PA 103 of 2026." The courts host returned an application shell, so this capture does not name a court of last resort from that response.

## Sources

| Role | Authority | Title | URL | Status |
| --- | --- | --- | --- | --- |
| Constitution | official-primary | Constitution of Michigan of 1963 | https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-Constitution | 200 |
| Statutes | official-primary | MCL Chapter Index | https://www.legislature.mi.gov/Laws/ChapterIndex | 200 |
| Session laws | official-primary | Public and Local Acts | https://www.legislature.mi.gov/Laws/PublicActs | 200 |
| Administrative code | official-primary | Administrative Rules, MOAHR | https://www.michigan.gov/lara/bureau-list/moahr/admin-rules | 200 |
| Court site | official-primary | Michigan courts, supreme court route | https://www.courts.michigan.gov/courts/supreme-court/ | shell |
| Court site | official-primary | Michigan courts, court of appeals route | https://www.courts.michigan.gov/courts/court-of-appeals/ | shell |
| Court site | official-primary | Michigan courts case search route | https://www.courts.michigan.gov/case-search/ | shell |
| Court rules | official-primary | Michigan Court Rules, Chapter 1 | https://www.courts.michigan.gov/siteassets/rules-instructions-administrative-orders/michigan-court-rules/michigan-court-rules-responsive-html5.zip/Michigan_Court_Rules/Court_Rules_Chapter_1/Court_Rules_Chapter_1.htm | 200 |
| Attorney general opinions | official-primary | Attorney General opinions | https://www.michigan.gov/ag/news/opinions | 200 |

## Constitution

The constitution page is the Constitution of Michigan of 1963. It lists Articles I through XII and a schedule: Declaration of Rights, Elections, General Government, Legislative Branch, Executive Branch, Judicial Branch, Local Government, Education, Finance and Taxation, Property, Public Officers and Employment, and Amendment and Revision.

## Statutes

The chapter index contains 227 numbered chapter links, so this page does not list every chapter. Entries opened for this capture:

- Chapter 24. Printing and State Documents. The chapter page also lists Act 306 of 1969 among the acts in the chapter.
- Chapter 600. Revised Judicature Act of 1961.
- Chapter 750. Michigan Penal Code.
- Chapters 760-777. Code of Criminal Procedure.

## Administrative code

The Michigan Office of Administrative Hearings and Rules page on michigan.gov returned HTTP 200 and is titled Administrative Rules. `https://ars.apps.lara.state.mi.us/AdminCode` redirected to an error page and is not used as the code URL.

## Courts and dockets

`/courts/supreme-court/`, `/courts/court-of-appeals/`, and `/case-search/` each returned HTTP 200. The static HTML is a short application shell and did not include a text heading, so those routes do not establish the court of last resort or an intermediate court. Article VI of the fetched constitution is titled Judicial Branch. That article heading is not a court name.

## Rules and attorney general opinions

Michigan Court Rules Chapter 1 returned HTTP 200 from the courts site, title "Court Rules Chapter 1." A shorter path, `/rules-admin-orders-and-jury-instructions/`, returned HTTP 404. The Attorney General opinions page returned HTTP 200. Legislature HEAD requests often returned HTTP 405; GET returned HTTP 200.

## Matter map

Criminal offenses are Chapter 750. Criminal procedure is Chapters 760-777. Courts and civil procedure are in Chapter 600, the Revised Judicature Act of 1961. Administrative rules are on the MOAHR administrative-rules page. Evidence rules were not opened as a separate chapter heading in this capture; court procedure is in the Michigan Court Rules.

## Local government

Article VII of the constitution is Local Government. Ordinances are adopted by the local unit. This capture does not supply a municipal code URL.

## Capture notes

Checked with Invoke-WebRequest, HEAD then GET, 25-second timeout, on 2026-10-07. The courts sitemap URL returned HTTP 404. `/courts/rules/` returned HTTP 404.
