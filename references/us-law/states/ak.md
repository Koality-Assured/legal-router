---
doc_kind: reference
canonical_id: us-law-state-ak
purpose: [reference]
topics: [us-law, alaska]
rag_keywords: [alaska, alaska-statutes, alaska-constitution, alaska-administrative-code, alaska-supreme-court]
version: captured-2026-10-07
publication: Alaska Legislature, Office of the Lieutenant Governor, and Alaska Court System
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://www.akleg.gov/basis/Statutes.asp
advisory_only: true
---

# Alaska law

Advisory only. This is a point-in-time map of official entry points captured on 2026-10-07. It is not legal advice and it does not reproduce statute text.

## Identity

The Legislature posts the Alaska Statutes 2025 and the Alaska Administrative Code. The Lieutenant Governor posts a constitution page, and the Legislature posts a constitution PDF. The court system's legal-resources page points to those legislative collections and to the appellate opinion search. The court-information page describes the Supreme Court and the Court of Appeals.

## Sources

Catalog: [`../catalogs/states/ak.json`](../catalogs/states/ak.json)

| Role | Title | Status |
| --- | --- | --- |
| Constitution | [Alaska's Constitution](https://ltgov.alaska.gov/information/alaskas-constitution/) | 200 |
| Constitution | [Alaska Constitution PDF](https://akleg.gov/docs/pdf/Alaska_Constitution.pdf) | 200 |
| Statutes | [Alaska Statutes 2025](https://www.akleg.gov/basis/Statutes.asp) | 200 |
| Session laws | [Bills and laws, 34th Legislature](https://www.akleg.gov/basis/Home/Law/34) | 200 |
| Administrative code | [Alaska Administrative Code](https://www.akleg.gov/basis/aac.asp) | 200 |
| Court of last resort | [Court system information](https://courts.alaska.gov/main/ctinfo.htm) | 200 |
| Intermediate appellate courts | [Court of Appeals on the court-information page](https://courts.alaska.gov/main/ctinfo.htm#appeals) | 200 |
| Court opinions | [Supreme Court opinions](https://appellate-records.courts.alaska.gov/CMSPublic/Home/Opinions?isCOA=False) | 200 |
| Court opinions | [Court of Appeals opinions](https://appellate-records.courts.alaska.gov/CMSPublic/Home/Opinions?isCOA=True) | 200 |
| Dockets | [CourtView](https://records.courts.alaska.gov/eaccess/home.page) | 200 |
| Court rules | [Court rules](https://courts.alaska.gov/rules/index.htm) | 200 |
| Attorney general opinions | [Attorney General opinions](https://law.alaska.gov/doclibrary/opinions_index.html) | 200 |

## Constitution

The Lieutenant Governor's [Alaska's Constitution](https://ltgov.alaska.gov/information/alaskas-constitution/) returned GET 200. An older path on that site redirected there. The Legislature PDF [Alaska Constitution](https://akleg.gov/docs/pdf/Alaska_Constitution.pdf) also returned GET 200.

## Statutes index

[Alaska Statutes 2025](https://www.akleg.gov/basis/Statutes.asp) returned GET 200. The index includes Title 9, Code of Civil Procedure; Title 11, Criminal Law; Title 12, Code of Criminal Procedure; and Title 22, Judiciary. This capture does not descend into sections.

## Administrative code

The Legislature's [Alaska Administrative Code](https://www.akleg.gov/basis/aac.asp) returned GET 200. The court legal-resources page says the official print publisher of the AAC is LexisNexis. This capture does not link that commercial edition.

## Courts and dockets

The [court-information page](https://courts.alaska.gov/main/ctinfo.htm) returned GET 200 and covers the Supreme Court and the Court of Appeals. Older paths `courts/supreme.htm` and `courts/coa.htm` returned 404. Opinions are on a separate host: [Supreme Court opinions](https://appellate-records.courts.alaska.gov/CMSPublic/Home/Opinions?isCOA=False) and [Court of Appeals opinions](https://appellate-records.courts.alaska.gov/CMSPublic/Home/Opinions?isCOA=True). Trial-court records are [CourtView](https://records.courts.alaska.gov/eaccess/home.page). `appellate.courts.alaska.gov` did not resolve and was not used.

## Rules and Attorney General

[Court rules](https://courts.alaska.gov/rules/index.htm) returned GET 200. [Attorney General opinions](https://law.alaska.gov/doclibrary/opinions_index.html) returned GET 200. The court library links that index. `https://law.alaska.gov/department/opinions.html` returned HTTP 200 with a "Page Not Found" title and was not used.

## Matter map

- Criminal matters: Alaska Statutes Title 11, Criminal Law, and Title 12, Code of Criminal Procedure.
- Civil matters: Title 9, Code of Civil Procedure.
- Courts: Title 22, Judiciary, and the court rules.
- Administrative matters: the Alaska Administrative Code and Attorney General opinions.

## Local government

The court legal-resources page links a Department of Commerce municipal code library. That URL returned 403, so this capture does not catalog a municipal-code URL. City and borough ordinances are obtained from that local government.

## Capture notes

Checks used PowerShell `Invoke-WebRequest` HEAD, then GET, with a 25-second timeout. `https://www.akleg.gov/publications.php` returned 404. The laws page used here is the 34th Legislature bills-and-laws page linked from the Legislature.
