---
doc_kind: reference
canonical_id: us-law-state-nh
purpose: [reference]
topics: [us-law, new-hampshire]
rag_keywords: []
version: "captured-2026-10-07"
publication: New Hampshire Revised Statutes
captured_at_utc: "2026-10-07T18:00:00Z"
upstream_url: https://www.gencourt.state.nh.us/rsa/html/nhtoc.htm
advisory_only: true
---

# New Hampshire

This capture is a point-in-time locator for attorney review, not legal advice and not a filing.

## Identity

The General Court publishes the Revised Statutes Online. Title LI of that code is Courts. Its chapter index names Chapter 490 Supreme Court and Chapter 491 Superior Court. The judicial-branch host returned HTTP 403, so this capture does not add a court description from that host.

## Sources

| Role | Authority | Title | URL |
| --- | --- | --- | --- |
| statutes | official-primary | Revised Statutes Online, table of contents | https://www.gencourt.state.nh.us/rsa/html/nhtoc.htm |
| statutes-currency | official-primary | Revised Statutes Online indexes | https://gencourt.state.nh.us/rsa/html/indexes/default.aspx |
| constitution | official-primary | State Constitution on NH.gov | https://www.nh.gov/glance/state-constitution |
| session-laws | official-primary | 2026 chaptered final versions | https://gencourt.state.nh.us/bill_status/misc/chaptered_final_version.aspx |
| administrative-code | official-primary | New Hampshire Code of Administrative Rules | https://gencourt.state.nh.us/rules |
| court-of-last-resort | official-primary | RSA Title LI, chapter index | https://www.gencourt.state.nh.us/rsa/html/NHTOC/NHTOC-LI.htm |
| dockets | official-primary | Superior Court case access | https://www.courts.nh.gov/our-courts/superior-court/case-access |
| court-rules | official-primary | New Hampshire court rules | https://www.courts.nh.gov/rules-court |
| attorney-general-opinions | official-primary | Department of Justice opinions path | https://www.doj.nh.gov/public-documents/opinions.htm |

Constitution, case access, court rules, and the opinions path returned HTTP 403. They are not treated as verified copies.

## Constitution

The Revised Statutes index links the constitution at NH.gov. Invoke-WebRequest returned HTTP 403 for that URL. Article headings are not stored.

## Statutes

The General Court table of contents is the top-level index. The indexes page says these RSAs are current through the 2025 regular legislative session, or December 2025, and that the printed and online Revised Statutes Annotated do not immediately reflect every new law. The List of Sections Affected is the update layer. Official index count: 67 titles.

- Title I. The State and Its Government
- Title II. Counties
- Title III. Towns, Cities, Village Districts, and Unincorporated Places
- Title IV. Elections (entire title repealed)
- Title V. Taxation
- Title VI. Public Officers and Employees
- Title VII. Sheriffs, Constables, and Police Officers
- Title VIII. Public Defense and Veterans' Affairs
- Title IX. Acquisition of Lands by United States; Federal Aid
- Title X. Public Health
- Title XI. Hospitals and Sanitaria
- Title XII. Public Safety and Welfare
- Title XIII. Alcoholic Beverages
- Title XIV. Milk and Milk Products
- Title XV. Education
- Title XVI. Libraries
- Title XVII. Housing and Redevelopment
- Title XVIII. Fish and Game
- Title XIX. Public Recreation
- Title XIX-A. Forestry
- Title XX. Transportation
- Title XXI. Motor Vehicles
- Title XXII. Navigation; Harbors; Coast Survey
- Title XXIII. Labor
- Title XXIV. Games, Amusements, and Athletic Exhibitions
- Title XXV. Holidays
- Title XXVI. Cemeteries; Burials; Dead Bodies
- Title XXVII. Corporations, Associations, and Proprietors of Common Lands
- Title XXVIII. Partnerships
- Title XXIX. Religious Societies
- Title XXX. Occupations and Professions
- Title XXXI. Trade and Commerce
- Title XXXII. Chattel Mortgages
- Title XXXIII. Conditional Sales
- Title XXXIII-A. Retail Installment Sales
- Title XXXIV. Public Utilities
- Title XXXIV-A. Uniform Commercial Code
- Title XXXV. Banks and Banking; Loan Associations; Credit Unions
- Title XXXVI. Pawnbrokers and Moneylenders
- Title XXXVII. Insurance
- Title XXXVIII. Securities
- Title XXXIX. Aeronautics
- Title XL. Agriculture, Horticulture and Animal Husbandry
- Title XLI. Liens
- Title XLII. Notaries, Commissioners, Justices of the Peace, and Acknowledgments
- Title XLIII. Domestic Relations
- Title XLIV. Guardians and Conservators
- Title XLV. Animals
- Title XLVI. Lost Property; Strays
- Title XLVII. Boundaries, Fences and Common Fields
- Title XLVIII. Conveyances and Mortgages of Realty
- Title XLIX. Homesteads
- Title L. Water Management and Protection
- Title LI. Courts
- Title LII. Actions, Process, and Service of Process
- Title LIII. Proceedings in Court
- Title LIV. Executions, Levies, Bail, and the Relief of Poor Debtors
- Title LV. Proceedings in Special Cases
- Title LVI. Probate Courts and Decedents' Estates
- Title LVII. Insolvency Proceedings and Assignments for Creditors
- Title LVIII. Public Justice
- Title LIX. Proceedings in Criminal Cases
- Title LX. Correction and Punishment
- Title LXI. Acts Repealed
- Title LXII. Criminal Code
- Title LXIII. Elections
- Title LXIV. Planning and Zoning

## Administrative code

The Office of Legislative Services, Administrative Rules, says proposed and adopted rules under RSA 541-A are filed there, and that the effective rules are the New Hampshire Code of Administrative Rules. The 2026 chaptered-final-version page is the session-law layer.

## Courts and dockets

Title LI's fetched chapter index names a Supreme Court, a Superior Court, a circuit court, and district and municipal court chapters. It does not label a separate intermediate appellate court. Opinion, docket, and rules URLs on courts.nh.gov returned HTTP 403. No fee statement was available from those failed checks.

## Court rules and attorney general opinions

`https://www.courts.nh.gov/rules-court` and `https://www.doj.nh.gov/public-documents/opinions.htm` returned HTTP 403. No substitute host was invented.

## Matter map

Criminal matters: Title LXII, Criminal Code, and Title LIX, Proceedings in Criminal Cases. Civil procedure: Titles LII through LV. Courts: Title LI. Administrative matters: the Code of Administrative Rules and RSA 541-A as described on the rules office page.

## Local government

Municipal ordinances are city-specific and must be located from that municipality's official code host. Title II is Counties and Title III is towns, cities, village districts, and unincorporated places. Neither fetched page stated a county total. No county ordinance URL is listed.

## Capture notes and failed URL checks

Checked 2026-10-07 with Invoke-WebRequest, HEAD then GET, 25-second timeout. The RSA table of contents, RSA indexes, Title LI chapter index, 2026 chaptered laws, and administrative-rules office returned HTTP 200 on HEAD.

Failed checks, HTTP 403 on HEAD and GET:

- `https://www.nh.gov/glance/state-constitution`
- `https://www.courts.nh.gov/our-courts/supreme-court`
- `https://www.courts.nh.gov/our-courts/supreme-court/orders-and-opinions`
- `https://www.courts.nh.gov/our-courts/superior-court/case-access`
- `https://www.courts.nh.gov/rules-court`
- `https://www.doj.nh.gov/`
- `https://www.doj.nh.gov/public-documents/opinions.htm`
- `https://www.courts.state.nh.us/supreme/`
- `https://www.courts.state.nh.us/supreme/opinions/index.htm`

`https://www.gencourt.state.nh.us/rsa/html/NHTOC/NHTOC-CONST.htm` and `http://www.gencourt.state.nh.us/rsa/html/CONST/CONST.htm` returned HTTP 404.
