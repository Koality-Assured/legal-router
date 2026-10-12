---
doc_kind: reference
canonical_id: us-law-state-ne
purpose: [reference]
topics: [us-law, nebraska, statutes, courts]
rag_keywords: [Nebraska, Revised Statutes, constitution, administrative rules, supreme court, court of appeals, attorney general]
version: captured-2026-10-07
publication: Nebraska Legislature, Nebraska Judicial Branch, and Nebraska Attorney General
captured_at_utc: 2026-10-07T18:00:00Z
upstream_url: https://nebraskalegislature.gov/laws/laws.php
advisory_only: true
---

# Nebraska law sources

This page is an advisory point-in-time map of official sources. It is not legal advice and it does not reproduce statutory text.

## Identity

Nebraska (NE) is a state with a unicameral legislature. The court of last resort is the Nebraska Supreme Court. The Judicial Branch publishes a separate Court of Appeals. Trial courts on the verified courts page include district courts, county courts, separate juvenile courts, and a workers' compensation court.

## Source table

| Role | Authority | HTTP | URL |
| --- | --- | --- | --- |
| Constitution | official-primary | 200 | https://nebraskalegislature.gov/laws/browse-constitution.php |
| Statutes | official-primary | 200 | https://nebraskalegislature.gov/laws/browse-statutes.php |
| Laws search | official-primary | 200 | https://nebraskalegislature.gov/laws/laws.php |
| Administrative rules | official-primary | 200 | https://rules.nebraska.gov/ |
| Court of last resort | official-primary | 200 | https://nebraskajudicial.gov/courts/supreme-court |
| Intermediate appellate | official-primary | 200 | https://nebraskajudicial.gov/courts/court-appeals |
| Appellate opinions | official-primary | 200 | https://www.nebraska.gov/apps-courts-epub/public/ |
| Court rules | official-primary | 200 | https://nebraskajudicial.gov/supreme-court-rules |
| Attorney general opinions | official-primary | 200 | https://ago.nebraska.gov/opinions |

## Constitution

The Legislature publishes the state constitution for browsing by article at the constitution URL. The laws pages also link a current constitution PDF on `nebraskalegislature.gov`.

## Statutes

The browse page lists 90 chapters. Each HTML label is only the chapter number. Sampled chapter pages (24, 25, 27, 28, 29, and 84) titled themselves "Revised Statutes Chapter N" and did not put a subject caption in the title element, so this list does not add subjects.

- Chapter 1
- Chapter 2
- Chapter 3
- Chapter 4
- Chapter 5
- Chapter 6
- Chapter 7
- Chapter 8
- Chapter 9
- Chapter 10
- Chapter 11
- Chapter 12
- Chapter 13
- Chapter 14
- Chapter 15
- Chapter 16
- Chapter 17
- Chapter 18
- Chapter 19
- Chapter 20
- Chapter 21
- Chapter 22
- Chapter 23
- Chapter 24
- Chapter 25
- Chapter 26
- Chapter 27
- Chapter 28
- Chapter 29
- Chapter 30
- Chapter 31
- Chapter 32
- Chapter 33
- Chapter 34
- Chapter 35
- Chapter 36
- Chapter 37
- Chapter 38
- Chapter 39
- Chapter 40
- Chapter 41
- Chapter 42
- Chapter 43
- Chapter 44
- Chapter 45
- Chapter 46
- Chapter 47
- Chapter 48
- Chapter 49
- Chapter 50
- Chapter 51
- Chapter 52
- Chapter 53
- Chapter 54
- Chapter 55
- Chapter 56
- Chapter 57
- Chapter 58
- Chapter 59
- Chapter 60
- Chapter 61
- Chapter 62
- Chapter 63
- Chapter 64
- Chapter 65
- Chapter 66
- Chapter 67
- Chapter 68
- Chapter 69
- Chapter 70
- Chapter 71
- Chapter 72
- Chapter 73
- Chapter 74
- Chapter 75
- Chapter 76
- Chapter 77
- Chapter 78
- Chapter 79
- Chapter 80
- Chapter 81
- Chapter 82
- Chapter 83
- Chapter 84
- Chapter 85
- Chapter 86
- Chapter 87
- Chapter 88
- Chapter 89
- Chapter 90

The laws search page is the official laws entry. This capture did not find a separate HTML page that used the words session laws, so no session-laws URL is cataloged.

## Administrative code

`https://rules.nebraska.gov/` returned HTTP 200. The body is a short application shell for Nebraska Rules and Regulations.

## Courts and dockets

The Supreme Court and the Court of Appeals have their own Judicial Branch pages. The appellate courts online library says it holds the official published opinions of both courts and that, effective January 1, 2016, the online certified PDF is the official opinion beginning with the volumes named on that page. A public trial-court docket URL was not verified in this capture.

## Rules and attorney general

Codified Supreme Court rules are at the rules URL. The Attorney General home page links to opinions, and `https://ago.nebraska.gov/opinions` returned HTTP 200.

## Matter map

Criminal law, civil procedure, evidence, courts, and administrative procedure sit in the 90-chapter index. This capture does not assign chapter numbers to those subjects because the index HTML had no subject captions. Administrative rules are on the rules portal.

## Local government

To locate ordinances for a named city, use that city's official website and the city clerk, or the municipal code the city itself publishes. This capture does not record county or city code URLs.

## Capture notes

Checks used PowerShell Invoke-WebRequest HEAD then GET, 25-second timeout, on 2026-10-07. Each cataloged URL returned HTTP 200 on both methods. The rules portal response was 803 bytes.
