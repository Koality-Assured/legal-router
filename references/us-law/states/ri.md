---
doc_kind: reference
canonical_id: us-law-state-ri
purpose: [reference]
topics: [us-law, rhode-island]
rag_keywords: []
version: "captured-2026-10-07"
publication: General Laws of Rhode Island
captured_at_utc: "2026-10-07T18:00:00Z"
upstream_url: https://webserver.rilegislature.gov/statutes/Statutes.html
advisory_only: true
---

# Rhode Island

This capture is a point-in-time locator for attorney review, not legal advice and not a filing.

## Identity

The General Assembly publishes the Constitution of the State of Rhode Island and a web copy of the General Laws. The fetched constitution says the supreme court has final revisory and appellate jurisdiction upon all questions of law and equity. The judiciary site has a Supreme Court page. No intermediate appellate court was named on the fetched court pages.

## Sources

| Role | Authority | Title | URL |
| --- | --- | --- | --- |
| constitution | official-primary | Constitution of the State of Rhode Island | https://www.rilegislature.gov/RIConstitution/Constitution/ConstFull.aspx |
| constitution-index | official-primary | Constitution article index | https://www.rilegislature.gov/RIConstitution/Pages/default.aspx |
| statutes | unofficial | General Laws title index (page says the web text is provisional) | https://webserver.rilegislature.gov/statutes/Statutes.html |
| session-laws | official-primary | Public laws, acts, and resolves | https://rilegislature.gov/pages/legislation.aspx |
| administrative-code | official-primary | Rhode Island rules and regulations, by organization | https://rules.sos.ri.gov/organizations |
| court-of-last-resort | official-primary | Rhode Island Supreme Court | https://www.courts.ri.gov/Courts/SupremeCourt/Pages/default.aspx |
| opinions | official-primary | Supreme Court opinions search | https://www.courts.ri.gov/Search/Pages/supreme-court-opinions.aspx |
| dockets | official-primary | Judiciary public portal | https://publicportal.courts.ri.gov/PublicPortal/ |
| court-rules | official-primary | Court rules, General Laws, and ordinances | https://www.courts.ri.gov/Legal-Resources/Pages/court-rules.aspx |
| attorney-general-opinions | official-primary | Attorney General site | https://riag.ri.gov/ |

The public portal and the Attorney General site returned HTTP 403.

## Constitution

The article index lists: Introduction; Declaration of Certain Constitutional Rights and Principles; Suffrage; Of Qualification for Office; Of Elections and Campaign Finance; Of the Distribution of Powers; Of the Legislative Power; Of the House of Representatives; Of the Senate; Of the Executive Power; Of the Judicial Power; Constitutional Amendments and Revision.

## Statutes

The legislature's web General Laws page says the text is provisional and that matters affecting legal rights should use the printed official publication. The title index on that page has 49 entries.

- Title 1. Aeronautics
- Title 2. Agriculture and Forestry
- Title 3. Alcoholic Beverages
- Title 4. Animals and Animal Husbandry
- Title 5. Businesses and Professions
- Title 6. Commercial Law - General Regulatory Provisions
- Title 6A. Uniform Commercial Code
- Title 7. Corporations, Associations and Partnerships
- Title 8. Courts and Civil Procedure - Courts
- Title 9. Courts and Civil Procedure - Procedure Generally
- Title 10. Courts and Civil Procedure - Procedure in Particular Actions
- Title 11. Criminal Offenses
- Title 12. Criminal Procedure
- Title 13. Criminals - Correctional Institutions
- Title 14. Delinquent and Dependent Children
- Title 15. Domestic Relations
- Title 16. Education
- Title 17. Elections
- Title 18. Fiduciaries
- Title 19. Financial Institutions
- Title 20. Fish and Wildlife
- Title 21. Food and Drugs
- Title 22. General Assembly
- Title 23. Health and Safety
- Title 24. Highways
- Title 25. Holidays and Days of Special Observance
- Title 26. Insane and Mentally Deficient Persons
- Title 27. Insurance
- Title 28. Labor and Labor Relations
- Title 29. Libraries
- Title 30. Military Affairs and Defense
- Title 31. Motor and Other Vehicles
- Title 32. Parks and Recreational Areas
- Title 33. Probate Practice and Procedure
- Title 34. Property
- Title 35. Public Finance
- Title 36. Public Officers and Employees
- Title 37. Public Property and Works
- Title 38. Public Records
- Title 39. Public Utilities and Carriers
- Title 40. Human Services
- Title 40.1. Behavioral Healthcare, Developmental Disabilities and Hospitals
- Title 41. Sports, Racing, and Athletics
- Title 42. State Affairs and Government
- Title 43. Statutes and Statutory Construction
- Title 44. Taxation
- Title 45. Towns and Cities
- Title 46. Waters and Navigation
- Title 47. Weights and Measures

## Administrative code

The Secretary of State rules site lists rules by organization. The General Assembly legislation page lists public laws, acts, and resolves by session, which is the session-law layer.

## Courts and dockets

The Supreme Court is the court of last resort named in the constitution. Opinions are searched from the judiciary opinions page. The public portal returned HTTP 403, so no fee statement was captured. The judiciary legal-links page, HTTP 200, points at Supreme Court opinions and at court rules.

## Court rules and attorney general opinions

Court rules are linked from the judiciary legal-resources page. `https://riag.ri.gov/` returned HTTP 403. The legal-links page points public-records and open-meetings opinions to a non-government host; that host is not recorded as an official copy.

## Matter map

Criminal matters: Titles 11 and 12. Civil procedure: Titles 8, 9, and 10. Administrative matters: the Secretary of State rules compilation and Title 42, State Affairs and Government. Towns and cities are Title 45, not a municipal code.

## Local government

Municipal ordinances are city-specific and must be located from that municipality's official code host. No fetched official page stated a county total. No county ordinance URL is listed.

## Capture notes and failed URL checks

Checked 2026-10-07 with Invoke-WebRequest, HEAD then GET, 25-second timeout. Constitution text, constitution index, General Laws index, legislation page, rules-by-organization, Supreme Court home, opinions search, and court-rules page returned HTTP 200. `https://rules.sos.ri.gov/` returned HTTP 200 on GET after HEAD 404; the organizations path above was HEAD 200.

Failed checks, with no substitute host invented:

- `https://www.courts.ri.gov/Courts/SupremeCourt/Pages/Opinions.aspx` HTTP 404.
- `https://www.courts.ri.gov/Courts/SupremeCourt/Pages/SupremeCourtRules.aspx` HTTP 404.
- `https://publicportal.courts.ri.gov/PublicPortal/` HTTP 403.
- `https://riag.ri.gov/` HTTP 403.
