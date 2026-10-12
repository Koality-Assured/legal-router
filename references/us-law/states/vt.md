---
doc_kind: reference
canonical_id: us-law-state-vt
purpose: [reference]
topics: [us-law, vermont]
rag_keywords: []
version: "captured-2026-10-07"
publication: Vermont Statutes Online
captured_at_utc: "2026-10-07T18:00:00Z"
upstream_url: https://legislature.vermont.gov/statutes/
advisory_only: true
---

# Vermont

This capture is a point-in-time locator for attorney review, not legal advice and not a filing.

## Identity

The General Assembly publishes the Constitution of the State of Vermont and the Vermont Statutes Online. The fetched constitution vests the judicial power in a unified judicial system composed of a Supreme Court, a Superior Court, and such other courts as the General Assembly establishes. The Vermont Judiciary page for the Supreme Court returned HTTP 200.

## Sources

| Role | Authority | Title | URL |
| --- | --- | --- | --- |
| constitution | official-primary | Constitution of the State of Vermont | https://legislature.vermont.gov/statutes/constitution-of-the-state-of-vermont |
| statutes | unofficial | Vermont Statutes Online (page says it is an unofficial copy of the Vermont Statutes Annotated) | https://legislature.vermont.gov/statutes/ |
| session-laws | official-primary | Acts and resolves, 2025-2026 session | https://legislature.vermont.gov/bill/acts/2026 |
| administrative-code | official-primary | Vermont Secretary of State rules service | https://secure.vermont.gov/SOS/rules/ |
| court-of-last-resort | official-primary | Vermont Supreme Court | https://www.vermontjudiciary.org/supreme-court |
| opinions | official-primary | Opinions, decisions, and orders | https://www.vermontjudiciary.org/opinions-decisions |
| dockets | official-primary | Judiciary home page | https://www.vermontjudiciary.org/ |
| court-rules | official-primary | Judiciary court-rules path | https://www.vermontjudiciary.org/attorneys/court-rules |
| attorney-general | official-primary | Office of the Attorney General | https://ago.vermont.gov/ |

The court-rules path returned HTTP 404. An opinions index separate from the office home page was not verified.

## Constitution

The legislature's constitution page is Chapter I, a declaration of the rights of the inhabitants, and Chapter II, the plan or frame of government. Chapter II, as fetched, states that the Supreme Court exercises appellate jurisdiction in criminal and civil cases and has administrative control of all courts.

## Statutes

The Vermont Statutes Online page says the statutes include the actions of the 2025 session and that the site is an unofficial copy of the Vermont Statutes Annotated. Official top-level index on that page. Count: 46 entries, including appendices.

- Title 1. General Provisions
- Title 2. Legislature
- Title 3. Executive
- Title 3 Appendix. Executive Orders
- Title 4. Judiciary
- Title 5. Aeronautics and Surface Transportation Generally
- Title 6. Agriculture
- Title 7. Alcoholic Beverages, Cannabis, and Tobacco
- Title 8. Banking and Insurance
- Title 9. Commerce and Trade
- Title 9A. Uniform Commercial Code
- Title 10. Conservation and Development
- Title 10 Appendix. Vermont Fish and Wildlife Regulations
- Title 11. Corporations, Partnerships and Associations
- Title 11A. Vermont Business Corporations
- Title 11B. Nonprofit Corporations
- Title 11C. Mutual Benefit Enterprises
- Title 12. Court Procedure
- Title 13. Crimes and Criminal Procedure
- Title 14. Decedents' Estates and Fiduciary Relations
- Title 14A. Trusts
- Title 15. Domestic Relations
- Title 15A. Adoption Act
- Title 15B. Uniform Interstate Family Support Act (1996)
- Title 15C. Parentage Proceedings
- Title 16. Education
- Title 16 Appendix. Education Charters and Agreements
- Title 17. Elections
- Title 18. Health
- Title 19. Highways
- Title 20. Internal Security and Public Safety
- Title 21. Labor
- Title 22. Libraries, History, and Information Technology
- Title 23. Motor Vehicles
- Title 24. Municipal and County Government
- Title 24 Appendix. Municipal Charters
- Title 25. Navigation and Waters
- Title 26. Professions and Occupations
- Title 27. Property
- Title 27A. Uniform Common Interest Ownership Act (1994)
- Title 28. Public Institutions and Corrections
- Title 29. Public Property and Supplies
- Title 30. Public Service
- Title 31. Recreation and Sports
- Title 32. Taxation and Finance
- Title 33. Human Services

## Administrative code

The Secretary of State rules service posts proposed and adopted agency rules. The legislature's statutes page also links a LexisNexis copy of state agency rules and of court rules. Those Lexis links were not checked and are not treated as official copies.

## Courts and dockets

The constitution names the Supreme Court as the appellate court and the Superior Court as part of the unified system. Opinions are in the judiciary opinions library. The judiciary home page offers a hearing search and does not state a fee. `https://www.vermontjudiciary.org/court-case-lookup` returned HTTP 404, so no separate docket-fee statement was captured.

## Court rules and attorney general opinions

The judiciary path `/attorneys/court-rules` returned HTTP 404. The Attorney General home page returned HTTP 200. A distinct opinions index was not verified, and no substitute host was invented.

## Matter map

Criminal matters: Title 13. Civil court procedure: Title 12. Courts: Title 4 and the constitution's judiciary chapter. Administrative matters: the Secretary of State rules service. Municipal and county government structure is Title 24, not a city ordinance code.

## Local government

Municipal ordinances are city-specific and must be located from that municipality's official code host. Title 24 Appendix lists municipal charters on the statutes site. No fetched official page stated a county total. No county ordinance URL is listed.

## Capture notes and failed URL checks

Checked 2026-10-07 with Invoke-WebRequest, HEAD then GET, 25-second timeout. Constitution, statutes index, 2026 acts, Secretary of State rules, Supreme Court, opinions library, judiciary home, and Attorney General home returned HTTP 200 on HEAD.

Failed checks, with no substitute host invented:

- `https://legislature.vermont.gov/bill/acts` HTTP 404. The session path `/bill/acts/2026` returned HTTP 200.
- `https://www.vermontjudiciary.org/court-case-lookup` HTTP 404.
- `https://www.vermontjudiciary.org/attorneys/court-rules` HTTP 404.
