---
doc_kind: reference
canonical_id: us-law-state-tx
purpose: [reference]
topics: [us-law, texas]
rag_keywords: [texas-constitution, texas-statutes, texas-administrative-code, court-of-criminal-appeals, supreme-court-of-texas]
version: captured-2026-10-07
publication: Texas Legislature, Secretary of State, and Texas Judicial Branch
captured_at_utc: "2026-10-07T18:00:00Z"
upstream_url: https://statutes.capitol.texas.gov/
advisory_only: true
---

# Texas

This capture is a point-in-time locator for attorney review. It is not legal advice and it is not a filing.

## Identity

Texas (TX). The Court of Criminal Appeals page on the Texas Judicial Branch site states that the Court of Criminal Appeals is Texas's highest court for criminal cases. That site lists the Supreme Court as a separate court, and it lists the 1st through 15th Courts of Appeals as further separate courts. This capture treats the Court of Criminal Appeals as the criminal court of last resort because that page says so. It does not copy a jurisdiction sentence from the Supreme Court page beyond the fact that the court is a distinct publisher on the same site.

## Source table

| Role | Publisher page | HTTP |
| --- | --- | --- |
| Constitution and statutes | [Texas Constitution and Statutes](https://statutes.capitol.texas.gov/) | 200 |
| Session laws | [General and Special Laws](https://lrl.texas.gov/collections/sessionlaws.cfm) | 200 |
| Administrative code | [Texas Administrative Code welcome](https://www.sos.texas.gov/tac/index.shtml) | 200 |
| Supreme Court | [Supreme Court](https://www.txcourts.gov/supreme/) | 200 |
| Criminal court | [Court of Criminal Appeals](https://www.txcourts.gov/cca/) | 200 |
| Dockets | [TAMES case search](https://search.txcourts.gov/) | 200 |
| Court rules | [Rules and standards](https://www.txcourts.gov/rules-forms/rules-standards/) | 200 |
| Attorney general | [AG opinions](https://www.texasattorneygeneral.gov/opinions) | 200 |

## Constitution

The statutes home page lists "Texas Constitution" as the first entry in the code menu (HTTP 200). Read articles from that official index. This capture does not copy constitutional text.

## Statutes

Top-level entries on `https://statutes.capitol.texas.gov/` (HTTP 200), one line per menu entry. The index does not list a separate evidence code. Court rules cover evidence.

- Texas Constitution
- Agriculture Code
- Alcoholic Beverage Code
- Auxiliary Water Laws
- Business & Commerce Code
- Business Organizations Code
- Civil Practice and Remedies Code
- Code of Criminal Procedure
- Education Code
- Election Code
- Estates Code
- Family Code
- Finance Code
- Government Code
- Health and Safety Code
- Human Resources Code
- Insurance Code
- Insurance Code - Not Codified
- Labor Code
- Local Government Code
- Natural Resources Code
- Occupations Code
- Parks and Wildlife Code
- Penal Code
- Probate Code
- Property Code
- Special District Local Laws Code
- Tax Code
- Transportation Code
- Utilities Code
- Water Code
- Vernon's Civil Statutes

That is 32 entries. Texas Legislature Online (`https://capitol.texas.gov/`, HTTP 200) is the bill system, not this code index.

## Administrative code

The Secretary of State welcome page (`https://www.sos.texas.gov/tac/index.shtml`, HTTP 200; the `sos.state.tx.us` host also returned HTTP 200) says the Texas Administrative Code is the compilation of state agency rules and that there are 17 titles. The current viewer linked from that page is `https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC` (HTTP 200). The older `texreg.sos.state.tx.us` viewer returned GET 200 with a "Site Has Moved" body (HEAD 401) and pointed at the Appian portal. This capture does not list the 17 titles because the welcome page stated the count without printing the title names in the text retrieved here.

## Courts and dockets

Supreme Court: `https://www.txcourts.gov/supreme/` (HTTP 200). Court of Criminal Appeals: `https://www.txcourts.gov/cca/` (HTTP 200). The CCA page's navigation lists 15 courts of appeals. An older judicial-branch overview PDF that says 14 courts of appeals was not used for the current count.

Case search: `https://search.txcourts.gov/` returned HTTP 200 and landed on `https://search.txcourts.gov/CaseSearch.aspx?coa=cossup`. The search form lists the Supreme Court, the Court of Criminal Appeals, and the 1st through 15th Courts of Appeals.

## Rules and attorney general

Statewide rules are at `https://www.txcourts.gov/rules-forms/rules-standards/` (HTTP 200). The rules-history page on the same host (HTTP 200) describes rulemaking by the Supreme Court and by the Court of Criminal Appeals as separate grants. Attorney General opinions: `https://www.texasattorneygeneral.gov/opinions` (HTTP 200).

## Matter map

- Criminal: Penal Code and Code of Criminal Procedure on the statutes index. The Court of Criminal Appeals page states it is the highest court for criminal cases. The 15 courts of appeals are the intermediate appellate courts listed on that site.
- Civil: Civil Practice and Remedies Code on the statutes index. The Supreme Court is a separate court from the Court of Criminal Appeals.
- Administrative: Texas Administrative Code for agency rules. The statutes index has a Government Code and does not label a separate administrative-procedure code in the top-level menu.

## Local government

The statutes index includes a Local Government Code and a Special District Local Laws Code. Those are state statutes. City charters and ordinances are published by each city. County trial-court records are not a county code. See [`../local-government.md`](../local-government.md).

## Capture notes

Checked 2026-10-07 with PowerShell `Invoke-WebRequest`, HEAD then GET, 25-second timeout. The Court of Criminal Appeals sentence was read from the CCA page body, not assumed from the court name alone.
