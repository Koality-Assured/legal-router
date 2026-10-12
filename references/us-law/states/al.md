---
doc_kind: reference
canonical_id: us-law-state-al
purpose: [reference]
topics: [us-law, alabama]
rag_keywords: [code-of-alabama, alabama-administrative-code, alabama-supreme-court, court-of-criminal-appeals]
version: captured-2026-10-07
publication: Alabama Legislature and Alabama Judicial System
captured_at_utc: "2026-10-07T18:00:00Z"
upstream_url: https://alison.legislature.state.al.us/code-of-alabama
advisory_only: true
---

# Alabama

This capture is a point-in-time locator for attorney review. It is not legal advice and it is not a filing.

## Identity

Alabama (AL). The Supreme Court page states that the Supreme Court of Alabama is the highest state court and that it has authority to review decisions of the other courts of the state. The judicial site also lists a Court of Civil Appeals and a Court of Criminal Appeals. Those two courts are not described on the pages read here as separate courts of last resort.

## Source table

| Role | Publisher page | HTTP |
| --- | --- | --- |
| Statutes | [Code of Alabama](https://alison.legislature.state.al.us/code-of-alabama) | 200 |
| Session laws | [Acts](https://alison.legislature.state.al.us/acts) | 200 |
| Administrative code | [Alabama Administrative Code](https://admincode.legislature.state.al.us/) | 200 |
| Supreme Court | [Supreme Court](https://judicial.alabama.gov/Appellate/SupremeCourt) | 200 |
| Criminal appeals | [Court of Criminal Appeals](https://judicial.alabama.gov/Appellate/CriminalAppeals) | 200 |
| Civil appeals | [Court of Civil Appeals](https://judicial.alabama.gov/Appellate/CivilAppeals) | 200 |
| Dockets | [Appellate public portal](https://publicportal.alappeals.gov/) | 200 |
| Court rules | [Rules of Court](https://judicial.alabama.gov/library/rulesofcourt) | 200 |
| Attorney general | [AG opinions](https://www.alabamaag.gov/opinions/) | 200 |

## Constitution

This check did not confirm a standalone current-constitution URL. The legislature's code browser at `https://alison.legislature.state.al.us/code-of-alabama` returned HTTP 200, and its HTML shell did not include a constitution table of contents. A legislature page titled as a proposed 2022 constitution was not used as the current text.

## Statutes

The code browser HTML did not include a title list. The page is a client-rendered application. This capture does not supply title names from memory or from an unofficial host. Session acts are at `https://alison.legislature.state.al.us/acts` (HTTP 200).

## Administrative code

`https://admincode.legislature.state.al.us/` returned HTTP 200 and identifies itself as the Alabama Administrative Code published by the Legislative Services Agency. `https://alabamaadministrativecode.state.al.us/` failed before an HTTP status: the TLS certificate was not trusted by this client. That host is not used.

## Courts and dockets

Supreme Court (`https://judicial.alabama.gov/Appellate/SupremeCourt`, HTTP 200): the page says the court is composed of a chief justice and eight associate justices and is the highest state court.

Court of Criminal Appeals (`https://judicial.alabama.gov/Appellate/CriminalAppeals`, HTTP 200): the page says the court hears appeals of felony and misdemeanor cases, including city-ordinance violations, and post-conviction writs in criminal cases.

Court of Civil Appeals (`https://judicial.alabama.gov/Appellate/CivilAppeals`, HTTP 200): the page says the court has original appellate jurisdiction in civil appeals where the amount in controversy does not exceed $50,000, and that the Supreme Court may transfer civil cases to it. The same paragraph mentions administrative-agency appeals. The fetched sentence names an exception that this capture does not finish from memory.

Appellate dockets: `https://publicportal.alappeals.gov/` (HTTP 200). Trial-court access portal: `https://pa.alacourt.com/default.aspx?loc=alacourt.gov` (HTTP 200). Judicial system home: `https://judicial.alabama.gov/` (HTTP 200).

## Rules and attorney general

Rules of Court: `https://judicial.alabama.gov/library/rulesofcourt` (HTTP 200). Attorney General opinions: `https://www.alabamaag.gov/opinions/` (HTTP 200).

## Matter map

- Criminal: the Court of Criminal Appeals page describes the criminal appellate docket. The code title that holds the criminal statutes was not in the HTML retrieved from the code browser.
- Civil: the Court of Civil Appeals page describes the dollar-limited civil appellate jurisdiction, with review by the Supreme Court available as that court describes it.
- Administrative: Alabama Administrative Code on the Legislative Services Agency host. The civil appeals page also states a class of administrative-agency appeals.

## Local government

The criminal appeals page treats violations of city ordinances as cases in that court. The ordinance text is still the city's code, not the Code of Alabama and not the trial-court docket. See [`../local-government.md`](../local-government.md).

## Capture notes

Checked 2026-10-07 with PowerShell `Invoke-WebRequest`, HEAD then GET, 25-second timeout. The code title index is a gap because the official HTML did not contain it.
