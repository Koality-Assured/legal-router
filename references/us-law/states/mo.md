---
doc_kind: reference
canonical_id: us-law-state-mo
purpose: [reference]
topics: [us-law, missouri, statutes, courts]
rag_keywords: [Missouri, Missouri Constitution, Revised Statutes of Missouri, Code of State Regulations, Missouri supreme court]
version: captured-2026-10-07
publication: Missouri Revisor of Statutes
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://revisor.mo.gov/main/Home.aspx
advisory_only: true
---

# Missouri

This is a point-in-time locator captured on 2026-10-07. It is not legal advice and it is not a filing.

The Revisor of Statutes publishes the Revised Statutes of Missouri and calls the site the official website for those statutes. The constitution view is `Home.aspx?constit=y`. Article V is the Judicial Department, and the constitution text on that page uses the words "supreme court," including "Jurisdiction of the supreme court." The Secretary of State publishes the Code of State Regulations. `https://www.courts.mo.gov/` did not complete a TLS handshake from this client.

## Sources

| Role | Authority | Title | URL | Status |
| --- | --- | --- | --- | --- |
| Constitution | official-primary | Missouri Constitution | https://revisor.mo.gov/main/Home.aspx?constit=y | 200 |
| Statutes | official-primary | Revised Statutes of Missouri | https://revisor.mo.gov/main/Home.aspx | 200 |
| Session laws | official-primary | Revisor publications, session laws | https://revisor.mo.gov/main/Info.aspx | 200 |
| Administrative code | official-primary | Administrative Rules Division | https://www.sos.mo.gov/adrules | 200 |
| Court of last resort | official-primary | Missouri courts | https://www.courts.mo.gov/ | failed |
| Intermediate appellate | official-primary | Missouri courts | https://www.courts.mo.gov/ | failed |
| Dockets | official-primary | Case.net | https://www.courts.mo.gov/casenet/base/welcome.do | failed |
| Court rules | official-primary | Missouri court rules path | https://www.courts.mo.gov/page.jsp?id=46 | failed |
| Attorney general opinions | official-primary | AG Opinions | https://ago.mo.gov/other-resources/ag-opinions/ | 200 |

## Constitution

`?chapter=Const` redirected to `nofish.aspx`. `Home.aspx?constit=y` returned the constitution. Articles on that page:

- Article I. Bill of Rights
- Article II. The Distribution of Powers
- Article III. Legislative Department
- Article IV. Executive Department
- Article V. Judicial Department
- Article VI. Local Government
- Article VII. Public Officers
- Article VIII. Suffrage and Elections
- Article IX. Education
- Article X. Taxation
- Article XI. Corporations
- Article XII. Amending the Constitution
- Article XIII. Public Employees
- Article XIV. Marijuana Use and Regulation

## Statutes

The revisor home page lists 41 titles:

- Title I. Laws and Statutes
- Title II. Sovereignty, Jurisdiction and Emblems
- Title III. Legislative Branch
- Title IV. Executive Branch
- Title V. Military Affairs and Police
- Title VI. County, Township and Political Subdivision Government
- Title VII. Cities, Towns and Villages
- Title VIII. Public Officers and Employees, Bonds and Records
- Title IX. Suffrage and Elections
- Title X. Taxation and Revenue
- Title XI. Education and Libraries
- Title XII. Public Health and Welfare
- Title XIII. Correctional and Penal Institutions
- Title XIV. Roads and Waterways
- Title XV. Lands, Levees, Drainage, Sewers and Public Water Supply
- Title XVI. Conservation, Resources and Development
- Title XVII. Agriculture and Animals
- Title XVIII. Labor and Industrial Relations
- Title XIX. Motor Vehicles, Watercraft and Aviation
- Title XX. Alcoholic Beverages
- Title XXI. Public Safety and Morals
- Title XXII. Occupations and Professions
- Title XXIII. Corporations, Associations and Partnerships
- Title XXIV. Business and Financial Institutions
- Title XXV. Incorporation and Regulation of Certain Utilities and Carriers
- Title XXVI. Trade and Commerce
- Title XXVII. Debtor-Creditor Relations
- Title XXVIII. Contracts and Contractual Relations
- Title XXIX. Ownership and Conveyance of Property
- Title XXX. Domestic Relations
- Title XXXI. Trusts and Estates of Decedents and Persons under Disability
- Title XXXII. Courts
- Title XXXIII. Evidence and Legal Advertisements
- Title XXXIV. Juries
- Title XXXV. Civil Procedure and Limitations
- Title XXXVI. Statutory Actions and Torts
- Title XXXVII. Criminal Procedure
- Title XXXVIII. Crimes and Punishment; Peace Officers and Public Defenders
- Title XXXIX. Conduct of Public Business
- Title XL. Additional Executive Departments
- Title XLI. Codes and Standards

## Administrative code

The Secretary of State Administrative Rules Division page returned HTTP 200. `https://www.sos.mo.gov/adrules/csr/csr` returned HTTP 200 and is titled "Current Code of State Regulations." HEAD on both SOS URLs failed without a status code; GET returned HTTP 200.

## Courts and dockets

Article V is the Judicial Department, and the constitution page refers to the supreme court. Title XXXII of the statutes is Courts. The court host `www.courts.mo.gov`, including `page.jsp?id=27`, `page.jsp?id=261`, `page.jsp?id=46`, and Case.net `casenet/base/welcome.do`, failed before a status code: "Could not create SSL/TLS secure channel." No replacement docket or rules URL was substituted.

## Rules and attorney general opinions

Court rules were not read because the courts host failed the TLS handshake. Attorney General opinions at `https://ago.mo.gov/other-resources/ag-opinions/` returned HTTP 200. The page title is "AG Opinions."

## Matter map

Crimes are Title XXXVIII. Criminal procedure is Title XXXVII. Courts are Title XXXII. Evidence is Title XXXIII. Civil procedure and limitations are Title XXXV. Administrative rules are the Code of State Regulations.

## Local government

Title VI is County, Township and Political Subdivision Government. Title VII is Cities, Towns and Villages. Article VI of the constitution is Local Government. Ordinances are adopted by the local unit. This capture does not supply a municipal code URL.

## Capture notes

Checked with Invoke-WebRequest, HEAD then GET, 25-second timeout, on 2026-10-07. The publications page lists session-law PDFs for 2009 through 2025. `SessionLaws.aspx` and a Senate session-laws path returned HTTP 404.
