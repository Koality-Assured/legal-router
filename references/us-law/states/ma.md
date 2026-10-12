---
doc_kind: reference
canonical_id: us-law-state-ma
purpose: [reference]
topics: [us-law, massachusetts]
rag_keywords: []
version: "captured-2026-10-07"
publication: General Laws of Massachusetts
captured_at_utc: "2026-10-07T18:00:00Z"
upstream_url: https://malegislature.gov/Laws/GeneralLaws/
advisory_only: true
---

# Massachusetts

This capture is a point-in-time locator for attorney review, not legal advice and not a filing.

## Identity

The General Court publishes the Constitution of the Commonwealth of Massachusetts. Its preamble establishes the Declaration of Rights and the Frame of Government as that constitution. The constitution's judiciary chapter refers to the judges of the supreme judicial court. The Reporter of Decisions opinions URL returned HTTP 403, so this capture does not add an Appeals Court description from that host.

## Sources

| Role | Authority | Title | URL |
| --- | --- | --- | --- |
| constitution | official-primary | Constitution of the Commonwealth of Massachusetts | https://malegislature.gov/Laws/Constitution |
| statutes | unofficial | General Laws browse by part (legislature site; page disclaims the Official Edition) | https://malegislature.gov/Laws/GeneralLaws/ |
| session-laws | official-primary | Session laws | https://malegislature.gov/Laws/SessionLaws |
| administrative-code | official-primary | Secretary of the Commonwealth regulations manual (CMR and Massachusetts Register) | https://www.sec.state.ma.us/divisions/pubs-regs/download/manual.pdf |
| dockets | official-primary | MassCourts | https://www.masscourts.org/eservices/home.page |
| opinions | official-primary | New opinions, Reporter of Decisions | https://www.mass.gov/info-details/new-opinions |
| intermediate-appellate | official-primary | Appeals Court organization page | https://www.mass.gov/orgs/appeals-court |
| court-rules | official-primary | Massachusetts court rules, Trial Court law libraries | https://www.mass.gov/law-library/massachusetts-court-rules |

The mass.gov court, rules, and opinions URLs returned HTTP 403. They are not verified copies. No attorney-general opinions URL was confirmed, so none is listed.

## Constitution

The General Court page is a preamble, Part the First (A Declaration of the Rights of the Inhabitants), Part the Second (the Frame of Government), and Articles of Amendment. Part the Second chapters on the fetched page are: I legislative power; II executive power; III judiciary power; IV delegates to Congress; V the university at Cambridge and encouragement of literature; VI oaths and office-holding. The page also lists amendments rejected by the people.

## Statutes

The General Court browse is by part, not by a flat title list. The page says this site is not the official version of the General Laws and that the official version is published every two years. It says the site includes amendments passed before January 6, 2026, and points later enactments to the 2026 session laws. Official top-level index on that page:

- Part I. Administration of the Government (chapters 1-182)
- Part II. Real and Personal Property and Domestic Relations (chapters 183-210)
- Part III. Courts, Judicial Officers and Proceedings in Civil Cases (chapters 211-262)
- Part IV. Crimes, Punishments and Proceedings in Criminal Cases (chapters 263-280)
- Part V. The General Laws, and Express Repeal of Certain Acts and Resolves (chapters 281-282)

## Administrative code

The Secretary of the Commonwealth's 2026 regulations manual, HTTP 200, states that the Code of Massachusetts Regulations is the body of administrative law, published by the Secretary, and that the Massachusetts Register is the biweekly update. The fetched manual text also refers to Attorney General material in the Register. A mass.gov CMR reading page returned HTTP 403 and is not used as a verified copy.

## Courts and dockets

The constitution names the supreme judicial court. MassCourts returned HTTP 200. This capture did not read a fee statement from that home page. The opinions, Appeals Court, and trial-court organization URLs returned HTTP 403, so those pages were not used.

## Court rules and attorney general opinions

The court-rules URL returned HTTP 403. The regulations manual is the verified statement that the Massachusetts Register carries Attorney General material. No opinions host was verified.

## Matter map

Criminal matters: Part IV of the General Laws browse. Civil court proceedings: Part III. Administrative matters: the CMR and Massachusetts Register described in the Secretary's manual. The General Laws page itself says it is not the Official Edition.

## Local government

Municipal ordinances are city-specific and must be located from that municipality's official code host. No fetched official page stated a county total. No county ordinance URL is listed.

## Capture notes and failed URL checks

Checked 2026-10-07 with Invoke-WebRequest, HEAD then GET, 25-second timeout. Constitution, General Laws, session laws, the regulations manual PDF, and MassCourts returned HTTP 200 on HEAD.

Failed checks, HTTP 403 on HEAD and GET, with no substitute host invented:

- `https://www.mass.gov/info-details/learn-about-the-code-of-massachusetts-regulations`
- `https://www.mass.gov/info-details/new-opinions`
- `https://www.mass.gov/orgs/massachusetts-supreme-judicial-court`
- `https://www.mass.gov/orgs/appeals-court`
- `https://www.mass.gov/law-library/massachusetts-court-rules`
- `https://www.mass.gov/lists/attorney-general-formal-opinions`
- `https://www.mass.gov/orgs/massachusetts-trial-court`
