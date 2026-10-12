---
doc_kind: reference
canonical_id: us-law-state-md
purpose: [reference]
topics: [us-law, maryland]
rag_keywords: [Maryland, Maryland Code, COMAR, Supreme Court of Maryland, Appellate Court of Maryland]
version: captured-2026-10-07
publication: Maryland General Assembly
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://mgaleg.maryland.gov/mgawebsite/laws/statutes
advisory_only: true
---

# Maryland

Advisory capture of official entry points. This is not legal advice and it does not reproduce statutory, regulatory, or opinion text.

## Identity

The Maryland General Assembly publishes the code by article on its statutes page. The Maryland State Archives publishes the constitution now in force, adopted in September 1867. The Judiciary site identifies the Supreme Court of Maryland and the Appellate Court of Maryland. COMAR is published by the Division of State Documents.

## Sources

| Role | Authority | HTTP | Entry |
| --- | --- | --- | --- |
| constitution | official-primary | 200 | [Maryland Constitution - Maryland State Archives](https://msa.maryland.gov/msa/mdmanual/43const/html/const.html) |
| statutes | official-primary | 200 | [Laws - Statutes - Maryland General Assembly](https://mgaleg.maryland.gov/mgawebsite/laws/statutes) |
| session laws | official-primary | 200 | [Bills Enacted (Chapters)](https://mgaleg.maryland.gov/mgawebsite/Legislation/Report?ID=chapters) |
| administrative code | official-primary | 200 | [Code of Maryland Regulations](https://regs.maryland.gov/) |
| court of last resort opinions | official-primary | 200 | [Maryland Appellate Court Opinions](https://www.mdcourts.gov/opinions/opinions) |
| intermediate appellate court | official-primary | 200 | [Appellate Court of Maryland](https://www.mdcourts.gov/acm) |
| court rules | official-primary | 200 | [Maryland Rules](https://www.mdcourts.gov/rules) |
| attorney general opinions | official-primary | 200 | [Search Opinions of the Attorney General](https://oag.maryland.gov/resources-info/Pages/search-opinions.aspx) |
| local government | official-primary | 200 | [Laws - Municipalities](https://mgaleg.maryland.gov/mgawebsite/Laws/Municipalities) |

## Constitution

The Maryland State Archives page states that Maryland has had four constitutions and that state government now functions under the fourth, adopted by the voters in September 1867, with amendments ratified through November 5, 2024. The General Assembly statutes browser also lists constitutional articles in its select list. A guessed General Assembly path ending in `/Laws/Constitution` returned a soft 404 and is not used.

## Statutes

The statutes page lists 36 code articles.

- Agriculture
- Alcoholic Beverages and Cannabis
- Business Occupations and Professions
- Business Regulation
- Commercial Law
- Corporations and Associations
- Correctional Services
- Courts and Judicial Proceedings
- Criminal Law
- Criminal Procedure
- Economic Development
- Education
- Election Law
- Environment
- Estates and Trusts
- Family Law
- Financial Institutions
- General Provisions
- Health - General
- Health Occupations
- Housing and Community Development
- Human Services
- Insurance
- Labor and Employment
- Land Use
- Local Government
- Natural Resources
- Public Safety
- Public Utilities
- Real Property
- State Finance and Procurement
- State Government
- State Personnel and Pensions
- Tax - General
- Tax - Property
- Transportation

## Administrative code

The Code of Maryland Regulations (COMAR) is on the Division of State Documents site at regs.maryland.gov. The fetched page says COMAR contains regulations of Maryland state agencies and departments and is updated every two weeks. The older COMAR Online page at dsd.maryland.gov returned HTTP 200 and points readers to that site.

## Courts and dockets

The Judiciary identifies the Supreme Court of Maryland as the highest court and the Appellate Court of Maryland as the intermediate appellate court. Reported and unreported opinions of both courts are indexed at the appellate opinions page. The case-search host `https://casesearch.courts.state.md.us/casesearch/` returned HTTP 403, and `https://www.mdcourts.gov/casesearch` also returned HTTP 403. No docket URL is cataloged.

## Rules and attorney general opinions

The Maryland Rules entry is the Judiciary rules path. Attorney General opinions are searched on the Attorney General's site. The fetched opinions page says full-text search was unavailable at capture.

## Matter map

- Criminal: Criminal Law article and Criminal Procedure article.
- Civil: Courts and Judicial Proceedings article.
- Administrative: COMAR, and the State Government article. The article list has no separate Evidence article.

## Local government

The Local Government article is state law. The same statutes browser lists public local laws by county and a municipal-charter choice, and the General Assembly maintains a municipalities page. Municipal ordinances are adopted by municipalities. This capture does not supply county ordinance-host URLs.

## Capture notes

Checked 2026-10-07 with Invoke-WebRequest HEAD then GET, 25 second timeout. Failed checks: `https://mgaleg.maryland.gov/mgawebsite/Laws/Constitution` and `https://mgaleg.maryland.gov/mgawebsite/Laws/SessionLaws` both ended at an application not-found page; both case-search URLs returned HTTP 403.
