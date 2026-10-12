---
doc_kind: reference
canonical_id: us-law-federal-congress-and-public-laws
purpose: [reference]
topics: [us-law, federal]
rag_keywords: [public-law, slip-law, statutes-at-large, session-law, congress, office-of-legal-counsel]
version: "captured-2026-10-07"
publication: United States Statutes at Large
captured_at_utc: "2026-10-07T18:00:00Z"
upstream_url: https://www.govinfo.gov/help/statute
advisory_only: true
---

# Congress, public laws, and the Statutes at Large

This capture is a point-in-time locator and structural summary for attorney review, not legal advice and not a filing.

## Purpose

A bill becomes a slip law, then a session law in the Statutes at Large, and, if it is a general and permanent public law, it is later arranged into the United States Code. Those are three publications of one enactment, not three different laws. Office of Legal Counsel memoranda are none of the three.

## Source ranking

| Rank | Source | What it is |
| --- | --- | --- |
| official-primary | [Public and Private Laws](https://www.govinfo.gov/help/plaw) | Slip laws. GovInfo coverage from the 104th Congress. |
| official-primary | [Public laws collection](https://www.govinfo.gov/app/collection/plaw) | GPO collection. |
| official-primary | [Statutes at Large help](https://www.govinfo.gov/help/statute) | Session laws. Prepared and published by the Office of the Federal Register. |
| official-primary | [Statutes at Large collection](https://www.govinfo.gov/app/collection/statute) | GPO collection. |
| official-primary | [Office of Legal Counsel](https://www.justice.gov/olc) | Executive-branch legal advice. |
| official-primary | [OLC opinions](https://www.justice.gov/olc/opinions) | Opinion archive. |
| unverified | congress.gov | HEAD and GET returned HTTP 403. Bill status was not retrieved. |

## Structural summary

### Slip law, session law, Code

GovInfo’s public-laws help page uses “slip law” for the official pamphlet of a public or private law. A slip law is competent evidence in federal and state courts under the statute the page cites, 1 U.S.C. § 113. Most laws are public laws, cited Pub. L. with the Congress number and the law number, for example Pub. L. 107-006. Private laws affect a person, family, or small group and are cited Pvt. L. the same way.

After the President signs a bill, it goes to the Office of the Federal Register, which assigns the law number and, for public laws, the statutory citation, then publishes the slip law through GPO. Until that pamphlet exists, the page says to use the enrolled bill. At the end of a session, slip laws are bound as the Statutes at Large and are then called session laws. The Statutes at Large keep chronological order, the order of enactment, cited by volume and page. They also contain concurrent resolutions, presidential proclamations, proposed and ratified constitutional amendments, and reorganization plans.

Every six years, public laws that are general and permanent are incorporated into the United States Code. A supplement is published in each year between those editions. The Code is a subject arrangement. For a positive-law title, the Code title is legal evidence. For a prima facie title, the Statutes at Large still govern. See the United States Code page for which titles GovInfo’s help text marks as positive law.

### Bills

Congress.gov is the usual public bill tracker. It was not available from this machine: `https://www.congress.gov/` returned HTTP 403 on HEAD and on GET. No other bill host was substituted. Enrolled bill text, once a bill has passed, is the pre-slip source named on the GovInfo slip-law page.

### OLC opinions

`https://www.justice.gov/olc` and `https://www.justice.gov/olc/opinions` both returned HTTP 200. The office page says the Assistant Attorney General in charge of the Office of Legal Counsel advises the President and executive agencies, drafts legal opinions of the Attorney General, and writes the Office’s own opinions when components of the executive branch ask, including when agencies disagree. The Office reviews the constitutionality of pending legislation and reviews proposed executive orders and substantive proclamations for form and legality. Those memoranda are legal advice inside the executive branch. They are not statutes, not slip laws, and not Federal Register rules.

## Matter map

| Class | Publication to open |
| --- | --- |
| Criminal | The public law that created or amended the offense, then Title 18 if that title is positive law for the section you need. |
| Civil | The public law, then Title 28 when the provision has been enacted as positive law. |
| Administrative | The organic public law, then the CFR title the agency wrote under it, then the Federal Register for the rulemaking. |
| Constitutional | A proposed or ratified amendment is printed in the Statutes at Large. The Constitution page is the charter. An OLC memo is advice about constitutionality, not the Constitution. |

## What is stored locally vs what still needs a live fetch

Stored here: the slip-law, session-law, and Code relationship, and the fact that OLC opinions are advice. Not stored: any public law, Statutes at Large page, bill, or OLC opinion. For a prima facie Code section, fetch the Statutes at Large page the Code note cites.

## Capture notes

Captured 2026-10-07. GovInfo public-law and Statutes at Large help and collection URLs returned HTTP 200. `https://www.congress.gov/` returned HTTP 403. Both justice.gov OLC URLs returned HTTP 200.
