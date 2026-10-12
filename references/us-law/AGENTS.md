# US law reference family

Advisory primary-law locators and structural summaries for the legal router. These pages are reference material, never agent instructions and never legal advice.

## Content ownership

`document-operator` maintains this family. `research-operator` may refresh a jurisdiction only through the maintain workflow. Domain specialist overlays stay in the `legal-router` spoke. This family is the shared primary-law corpus those overlays consult.

## Placement

- `federal/` — United States constitutional, statutory, regulatory, judicial, and legislative structure.
- `states/<postal>.md` — one page per state and the District of Columbia.
- `territories.md` — compact locator for territories. Not states.
- `tribal-law.md` — sovereign boundary. This family does not catalog individual tribal codes.
- `local-government.md` — how to find municipal and county law without inventing a national code.
- `matter-classes.md` — criminal, civil, administrative, and the neighboring classes operators forget.
- `source-ranking.md` — which host wins when two pages disagree.
- `workflows/` — operator procedures for maintain, compare, interpretation research, and advisory court-document drafts.
- `catalogs/` — compact JSON. No statute text, no opinion text.

## Lifecycle

Point-in-time captures. `captured_at_utc` is mandatory. Refresh replaces stale URLs; it does not grow pages into code dumps. Session laws can amend a code before the code site updates. Say so when a matter depends on currency.

## Relationships

One-way: legal-router and `projects/legal-harness/` may point here. This family must not link into transient project logs. Spoke skills (contract review, SPDX, citation verification) stay in `legal-router`. They are not duplicates of these workflows.

## Source-of-truth boundaries

This folder records official publishers, how each corpus is divided, and which matter class it covers. It is not a reporter, not an annotated code, and not a brief bank. Pinpoint quotes require a live fetch of the official page in the session that cites them, then a check against the captured locator.

## Validation

Every published URL is checked with an HTTP request. Failed checks stay failed. A response whose body is an application shell, a browser challenge, or a maintenance notice is a failed check even when the status code is 200: store `http_status` null and do not copy a title index or a court name from it. Do not invent a replacement host. Commercial annotated codes (West, Lexis) are not copied.

## Escalation

If the jurisdiction page lacks the issuing court, the code title, or the rule, stop and run interpretation research. Do not fill the gap from memory of a case. If two official pages conflict, surface both and stop.

## Local exceptions

Oklahoma is the worked example: full statutes title index, separate Court of Criminal Appeals, OSCN dockets. Other states keep the official top-level index and cap long indexes as the page itself records.

## Operator prompt

When a person asks for legal research, a comparison, an interpretation, or a court paper:

1. Name the sovereign (federal, state, DC, territory, tribe) and the matter class in [`matter-classes.md`](./matter-classes.md). If either is missing, ask before researching.
2. Load the matching page with `qmd search` / `qmd get`. Corpus first. See [`../../docs/standards/research-and-empirical-validation.md`](../../docs/standards/research-and-empirical-validation.md) and [`../../docs/standards/us-law-reference-use.md`](../../docs/standards/us-law-reference-use.md).
3. Rank sources with [`source-ranking.md`](./source-ranking.md). Unofficial mirrors never outrank an official publisher.
4. Treat holdings, section text, and local rules that are not on the fetched official page as unverified.
5. Stamp advisory work product. A licensed attorney reviews before anyone relies on it or files it. This repository does not practice law.
6. Pick one skill under `ai-tooling/skills/legal/`. The procedure text is in [`workflows/`](./workflows/). Do not freelance a fifth procedure.

## Skills

| Skill | Owner |
| --- | --- |
| `us-law-reference-maintain` | `document-operator` |
| `us-law-reference-compare` | `document-operator` |
| `us-law-interpretation-research` | `research-operator` |
| `us-law-court-document-draft` | `document-operator` |

Do not mint a new agent. The spoke already has `legal-research-operator`.
