---
doc_kind: reference
canonical_id: us-law-state-nm
purpose: [reference]
topics: [us-law, new-mexico, statutes, courts]
rag_keywords: [New Mexico, NMSA, constitution, NMAC, supreme court, court of appeals, case lookup]
version: captured-2026-10-07
publication: New Mexico Compilation Commission, Commission of Public Records, and New Mexico Courts
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://www.nmcompcomm.us/
advisory_only: true
---

# New Mexico law sources

This page is an advisory point-in-time map of official sources. It is not legal advice and it does not reproduce statutory text.

## Identity

New Mexico (NM) is a state. The court of last resort is the New Mexico Supreme Court. The state has a Court of Appeals. District, magistrate, metropolitan, probate, and municipal courts are described on the courts site.

## Source table

| Role | Authority | HTTP | URL |
| --- | --- | --- | --- |
| Official publisher | official-primary | 200 | https://www.nmcompcomm.us/ |
| Statutes, constitution, rules, session laws | official-primary | 200 | https://nmonesource.com/ |
| How to search | official-primary | 200 | https://www.nmcompcomm.us/search-laws/ |
| Administrative code | official-primary | 200 | https://www.srca.nm.gov/nmac-home/ |
| NMAC titles | official-primary | 200 | https://www.srca.nm.gov/nmac-home/nmac-titles/ |
| Court of last resort | official-primary | 200 | https://supremecourt.nmcourts.gov/ |
| Intermediate appellate | official-primary | 200 | https://coa.nmcourts.gov/ |
| Dockets | official-primary | 200 | https://caselookup.nmcourts.gov/caselookup/ |
| Courts overview | official-primary | 200 | https://nmcourts.gov/courts-in-new-mexico/ |

## Constitution

The Compilation Commission is the official publisher of state laws. Its search page says NMOneSource is the official research tool for a session law, statute, appellate opinion, or court rule. `https://nmonesource.com/` returned HTTP 200 and landed on `https://nmonesource.com/nmos/en/nav.do`. That response is an application shell, so this capture does not list constitution articles or statute chapters.

## Statutes

Use NMOneSource for the current New Mexico Statutes Annotated, historical statutes, and session laws, as described by the Compilation Commission. No chapter index was present in the shell HTML, so no chapter list is printed here.

## Administrative code

The State Records Center and Archives publishes the New Mexico Administrative Code. The NMAC home page and the NMAC titles page both returned HTTP 200. The titles page is the agency-title index for the administrative code.

## Courts and dockets

The Supreme Court and the Court of Appeals have their own sites, linked from the verified courts-in-New-Mexico page. Case Lookup at the URL above is the statewide electronic court-records search. It returned HTTP 200.

## Rules and attorney general

Court rules are part of the NMOneSource collection described on the Compilation Commission search page. `https://nmdoj.gov/publications/opinions/` returned HTTP 403, so no separate attorney general opinions URL is cataloged.

## Matter map

Criminal, civil, evidence, courts, and administrative-procedure statutes are in the statutes collection on NMOneSource. This capture does not assign chapter numbers. Administrative rules are the NMAC. Appeals run from the trial courts to the Court of Appeals and the Supreme Court, as those two courts are published on the judicial site.

## Local government

To locate ordinances for a named city, use that city's official website and the city clerk, or the municipal code the city itself publishes. This capture does not record county or city code URLs. The courts overview identifies municipal courts; it is not an ordinance code.

## Capture notes

Checks used PowerShell Invoke-WebRequest HEAD then GET, 25-second timeout, on 2026-10-07. Cataloged URLs returned HTTP 200. The Department of Justice opinions URL returned HTTP 403 and is omitted. NMOneSource is the state's official publisher site; a commercial research brand is not cataloged.
