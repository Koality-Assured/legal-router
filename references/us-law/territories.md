---
doc_kind: reference
canonical_id: us-law-territories
purpose: [reference]
topics: [us-law, territories]
rag_keywords: [puerto-rico, guam, us-virgin-islands, american-samoa, northern-mariana-islands, territorial-court]
version: "captured-2026-10-07"
publication: Territorial codes and courts
captured_at_utc: "2026-10-07T18:00:00Z"
upstream_url: https://www.govinfo.gov/help/uscode
advisory_only: true
---

# United States territories

This capture is a point-in-time locator and structural summary for attorney review, not legal advice and not a filing.

## Purpose

Puerto Rico, Guam, the U.S. Virgin Islands, American Samoa, and the Northern Mariana Islands are territories. They are not states. Each has its own legislature and courts. Federal statutes that apply in a territory are a different corpus: Title 48 of the 2023 United States Code edition is “Territories and Insular Possessions,” and it is not a positive-law title on the GovInfo help page. This page lists only territorial legislature, code, and court hosts that answered an HTTP check.

## Source ranking

Official territorial hosts are `official-primary`. The American Samoa Bar Association code page is `unofficial`. Failed hosts are listed under capture notes and are not sources.

## Structural summary

### Puerto Rico

- Legislature and laws: the [Oficina de Servicios Legislativos](https://www.oslpr.org/) identifies itself as an office of the Asamblea Legislativa. Approved laws are on [SUTRA](https://sutra.oslpr.org/prontuarios/leyes-aprobadas). The [Senado](https://senado.pr.gov/) resolved. The House host `https://www.camara.pr.gov/` did not connect.
- Court of last resort: [Poder Judicial](https://poderjudicial.pr/) lists the Tribunal Supremo, with a section for the court and for its decisions, above the other courts in the navigation.

### Guam

- Legislature: [guamlegislature.gov](https://guamlegislature.gov/) is the Guam Legislature and links the Organic Act, the Guam Code Annotated, and public laws.
- Code: the [Compiler of Laws](https://col.guamcourts.gov/) says it is the official publisher of the Guam Code Annotated, session laws, administrative rules, and Supreme Court of Guam opinions. The page says a compiler’s certification is what makes the online code an official publication.
- Courts: the [Judiciary of Guam](https://www.guamcourts.gov/) is the official judiciary site and lists the Supreme Court of Guam and the Superior Court. `guamcourts.org` and `guamsupremecourt.com` did not connect; they were not used.

### U.S. Virgin Islands

- Legislature: [legvi.org](https://legvi.org/) is the 36th Legislature. Under “Bills and Code” the page lists a “VI CODE” entry and a Revised Organic Act of 1954 PDF. The code entry’s destination URL was not separately fetched, so it is not repeated here.
- Courts: [vicourts.org](https://www.vicourts.org/) is the Judicial Branch. Navigation includes the Supreme Court and the Superior Court. The welcome on the page is signed by the Chief Justice.

### American Samoa

- Legislature: [asfono.gov](https://www.asfono.gov/) is titled “The Legislature of American Samoa” (the Fono). The territorial portal page [americansamoa.gov/fono](https://www.americansamoa.gov/fono) points readers to that legislature site.
- Code: the [Secretary of American Samoa](https://www.osas.as/) is an official office. The fetched page says the Secretary’s authority comes from the Revised Constitution and the American Samoa Code Annotated, and the menu includes public laws. The page did not itself present the code text. The [American Samoa Bar Association](https://asbar.org/legal-resources/code-annotated/) hosts a “Code Annotated” and is unofficial.
- Court: no separate High Court host responded in this capture. A court URL is not invented.

### Northern Mariana Islands

- Legislature: [cnmileg.net](https://cnmileg.net/) is the Northern Marianas Commonwealth Legislature, with a House and a Senate.
- Code and court: [cnmilaw.gov](https://cnmilaw.gov/) identifies itself as an official site of the CNMI Law Revision Commission. The navigation includes the Commonwealth Code and a Judiciary section with the Supreme Court and the Superior Court. `cnmilaw.org` redirected there. `https://www.cnmileg.gov.mp/` failed the TLS handshake and was not used.

## Matter map

| Class | Where to look |
| --- | --- |
| Criminal | The territory’s penal title or code, then that territory’s trial court. Federal prosecution is Title 18 in a federal district court, which may sit in the territory. |
| Civil | The territory’s code and its court of last resort, listed above where a host resolved. |
| Administrative | The territory’s administrative compilation where the code site publishes one (Guam’s compiler publishes administrative rules; the CNMI commission publishes an administrative code). |
| Constitutional | The territory’s own constitution or organic act, plus the United States Constitution where it applies. Title 48 is the federal statutory layer, not the territorial code. |

## What is stored locally vs what still needs a live fetch

Stored here: hosts that answered, and a one-line description of what each homepage said it was. Not stored: any territorial statute, rule, or opinion. American Samoa still needs a live fetch for a court-of-last-resort site and for an official code text. The Virgin Islands code link on the legislature homepage was not followed.

## Capture notes

Captured 2026-10-07. Connection or TLS failures, not used as sources: `https://www.camara.pr.gov/`, `https://guamcourts.org/`, `https://www.guamsupremecourt.com/`, `https://www.cnmileg.gov.mp/`.
