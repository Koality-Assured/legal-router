---
doc_kind: reference
canonical_id: us-law-state-ky
purpose: [reference]
topics: [us-law, kentucky]
rag_keywords: [kentucky-revised-statutes, kentucky-constitution, kentucky-administrative-regulations, kentucky-supreme-court]
version: captured-2026-10-07
publication: Kentucky Legislative Research Commission and Kentucky Court of Justice
captured_at_utc: "2026-10-07T18:00:00Z"
upstream_url: https://apps.legislature.ky.gov/law/statutes/index.aspx
advisory_only: true
---

# Kentucky

This capture is a point-in-time locator for attorney review. It is not legal advice and it is not a filing.

## Identity

Kentucky (KY). The Court of Justice site lists a Supreme Court and a Court of Appeals as separate courts. The Supreme Court page retrieved here is a roster and temporary-location notice. It does not itself say "court of last resort." No separate criminal court of last resort appears on the pages read here.

## Source table

| Role | Publisher page | HTTP |
| --- | --- | --- |
| Constitution | [Constitution of Kentucky](https://apps.legislature.ky.gov/law/constitution) | 200 |
| Statutes | [Kentucky Revised Statutes](https://apps.legislature.ky.gov/law/statutes/index.aspx) | 200 |
| Session laws | [Kentucky Acts](https://legislature.ky.gov/Law/Pages/KyActs.aspx) | 200 |
| Administrative regulations | [KAR titles](https://apps.legislature.ky.gov/law/kar/titles/) | 200 |
| Supreme Court | [Supreme Court](https://www.kycourts.gov/Courts/Supreme-Court/Pages/default.aspx) | 200 |
| Court of Appeals | [Court of Appeals](https://www.kycourts.gov/Courts/Court-of-Appeals/Pages/default.aspx) | 200 |
| Dockets | [KCOJ docket](https://kcoj.kycourts.net/dockets/) | 200 |
| Local court rules | [Rules of practice](https://www.kycourts.gov/Courts/Pages/Rules-of-Practice.aspx) | 200 |
| Attorney general | [AG opinions](https://www.ag.ky.gov/Resources/Opinions/Pages/default.aspx) | 200 |

## Constitution

`https://apps.legislature.ky.gov/law/constitution` returned HTTP 200. The page says it includes amendments ratified on or before November 5, 2024. This capture does not copy the text.

## Statutes

The Legislative Research Commission statutes page (`https://legislature.ky.gov/Law/Statutes/Pages/Default.aspx`, HTTP 200) says the files on the public site are an unofficial posting of the internal database and are not the certified text. The catalog ranks that URL `unofficial`. The title index below is from `https://apps.legislature.ky.gov/law/statutes/index.aspx` (HTTP 200), which says it includes enactments through the 2026 Regular Session and that the database was last updated on October 6, 2026. Chapter catchlines on that page are informational. These lines are titles only.

- Title I. Sovereignty and Jurisdiction of the Commonwealth
- Title II. Legislative Branch
- Title III. Executive Branch
- Title IV. Judicial Branch
- Title V. Military Affairs
- Title VI. Financial Administration
- Title VII. Public Property and Public Printing
- Title VIII. Offices and Officers
- Title IX. Counties, Cities, and Other Local Units
- Title X. Elections
- Title XI. Revenue and Taxation
- Title XII. Conservation and State Development
- Title XIII. Education
- Title XIV. Libraries and Archives
- Title XV. Roads, Waterways, and Aviation
- Title XVI. Motor Vehicles
- Title XVII. Economic Security and Public Welfare
- Title XVIII. Public Health
- Title XIX. Public Safety and Morals
- Title XX. Alcoholic Beverages
- Title XXI. Agriculture and Animals
- Title XXII. Levees, Drainage, and Reclamation of Lands
- Title XXIII. Private Corporations and Associations
- Title XXIV. Public Utilities
- Title XXV. Business and Financial Institutions
- Title XXVI. Occupations and Professions
- Title XXVII. Labor and Human Rights
- Title XXVIII. Mines and Minerals
- Title XXIX. Commerce and Trade
- Title XXX. Contracts
- Title XXXI. Debtor-Creditor Relations
- Title XXXII. Ownership and Conveyance of Property
- Title XXXIII. Administration of Trusts and Estates of Persons under Disability
- Title XXXIV. Descent, Wills, and Administration of Decedents' Estates
- Title XXXV. Domestic Relations
- Title XXXVI. Statutory Actions and Limitations
- Title XXXVII. Special Proceedings
- Title XXXVIII. Witnesses, Evidence, Notaries, Commissioners of Foreign Deeds, and Legal Notices
- Title XXXIX. Provisional Remedies, Enforcement of Judgments, and Exemptions
- Title XL. Crimes and Punishments
- Title XLI. Laws
- Title XLII. Miscellaneous Practice Provisions
- Title L. Kentucky Penal Code
- Title LI. Unified Juvenile Code

That is 44 titles. Acts of the Kentucky General Assembly: `https://legislature.ky.gov/Law/Pages/KyActs.aspx` (HTTP 200).

## Administrative code

Kentucky Administrative Regulations titles: `https://apps.legislature.ky.gov/law/kar/titles/` (HTTP 200; `titles.htm` redirects there). The page lists 136 title numbers. That exceeds the 120-line capture cap, so the titles are not copied here. Open the official title page for the list.

## Courts and dockets

Court of Justice home: `https://www.kycourts.gov/` returned HTTP 200 and landed on `https://www.kycourts.gov/Pages/index.aspx`. Supreme Court and Court of Appeals each have pages (HTTP 200). The Supreme Court page says the court's Capitol offices moved to 669 Chamberlin Avenue, Frankfort, in June 2025. Dockets: `https://kcoj.kycourts.net/dockets/` (HTTP 200).

## Rules and attorney general

The Court of Justice local-rules page is `https://www.kycourts.gov/Courts/Pages/Rules-of-Practice.aspx` (HTTP 200). The Supreme Court page labels statewide rules as a Westlaw link. This capture does not adopt that commercial host as official-primary and does not record an unverified Westlaw URL. Attorney General opinions: `https://www.ag.ky.gov/Resources/Opinions/Pages/default.aspx` (HTTP 200). The page says opinions do not have the force of law.

## Matter map

- Criminal: Title XL, Crimes and Punishments, and Title L, Kentucky Penal Code.
- Civil: no single title is named civil procedure. Related titles include Title XXXVI, Title XXXVII, and Title XXXIX. Evidence is named inside Title XXXVIII.
- Administrative: Kentucky Administrative Regulations, 136 titles on the official title page. KRS Title III is the Executive Branch.

## Local government

Title IX is Counties, Cities, and Other Local Units of the Kentucky Revised Statutes. That is state law about local units. City and county ordinances are on each local government's site. See [`../local-government.md`](../local-government.md).

## Capture notes

Checked 2026-10-07 with PowerShell `Invoke-WebRequest`, HEAD then GET, 25-second timeout. The public KRS pages say they are not the certified text.
