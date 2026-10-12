---
doc_kind: reference
canonical_id: us-law-state-in
purpose: [reference]
topics: [us-law, indiana, statutes, courts]
rag_keywords: [Indiana, Indiana Code, Indiana Constitution, Indiana Administrative Code, Indiana Supreme Court]
version: captured-2026-10-07
publication: Indiana General Assembly
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://iga.in.gov/
advisory_only: true
---

# Indiana

This is a point-in-time locator captured on 2026-10-07. It is not legal advice and it is not a filing.

The Indiana General Assembly site is the laws host. A plain HTTP GET of the laws routes returns a 691-byte application shell titled "Indiana General Assembly." That shell does not include a code title index. The Indiana Supreme Court and the Court of Appeals of Indiana publish their own pages. MyCase is the courts' case search.

## Sources

| Role | Authority | Title | URL | Status |
| --- | --- | --- | --- | --- |
| Constitution | official-primary | Constitution route | https://iga.in.gov/laws/constitution | shell |
| Statutes | official-primary | Indiana Code titles route | https://iga.in.gov/laws/current/ic/titles/ | shell |
| Session laws | official-primary | Acts route | https://iga.in.gov/laws/acts | shell |
| Administrative code | official-primary | Indiana Register route | https://iar.iga.in.gov/code | shell |
| Court of last resort | official-primary | Indiana Supreme Court | https://www.in.gov/courts/supreme/ | 200 |
| Intermediate appellate | official-primary | Court of Appeals of Indiana | https://www.in.gov/courts/appeals/ | 200 |
| Dockets | official-primary | Indiana Courts Case Search - MyCase | https://public.courts.in.gov/mycase | 200 |
| Court rules | official-primary | Indiana Rules of Trial Procedure | https://rules.incourts.gov/Content/trial/default.htm | 200 |
| Attorney general opinions | official-primary | Attorney General Advisory | https://www.in.gov/attorneygeneral/about-the-office/advisory/ | 200 |

## Constitution

The laws menu entry is "Constitution (as amended 2024)." The static GET does not include the article text. Article headings were not copied from a rendered constitution page.

## Statutes

`https://iga.in.gov/laws/current/ic/titles/` returned HTTP 200 and a 691-byte application shell. The HTML did not include a title index, so no title list is stored.

## Administrative code

`https://iar.iga.in.gov/code` returned HTTP 200 with a short shell titled "Indiana Register." The General Assembly laws page links "Administrative Code" to a new tab. The shell does not contain the title list.

## Courts and dockets

The Indiana Supreme Court page title is "Indiana Supreme Court: Home." The Court of Appeals page title is "Court of Appeals of Indiana: Home." MyCase is titled "Indiana Courts Case Search - MyCase."

## Rules and attorney general opinions

`https://rules.incourts.gov/` is a script shell. The trial-rules page returned HTTP 200 and is titled "Trial Procedure Rules," with the text "Indiana Rules of Trial Procedure." The Attorney General Advisory page says the Advisory Division publishes official opinions on significant state issues.

## Matter map

No statute title index is stored, because the code route returned an application shell. Trial procedure text that this capture did retrieve is the Indiana Rules of Trial Procedure. The Indiana Register host is the administrative-rules route, and its static body is also a shell.

## Local government

Ordinances are adopted by the local unit. This capture does not supply a municipal code URL.

## Capture notes

Checked with Invoke-WebRequest, HEAD then GET, 25-second timeout, on 2026-10-07. A later GET of the titles route returned HTTP 200 and a 691-byte shell with no title lines. That shell is a failed document check (`http_status` null). `https://www.in.gov/courts/rules/` returned HTTP 404.
