---
schema_version: "2.0.0"
name: us-law-court-document-draft
description: >-
  Draft an advisory complaint, answer, motion, proposed order, or notice of
  appeal mapped to fetched court rules. Use when the person names the forum
  and document type. Do not use for legal advice, filing, or locator refresh
  (us-law-reference-maintain).
owner_agent: document-operator
rank: high
isolation: read-only
on_failure: abort_and_rollback
contracts:
  inputs:
    - Forum, matter class, document type, and facts the person supplied
  outputs:
    - Advisory draft stamped not for filing, with each section mapped to a fetched rule
---

# US law court document draft

## When to use

The person asks for a complaint, answer, motion, proposed order, notice of appeal, or similar paper grounded in a named sovereign's rules.

## When not to use

Legal advice, filing strategy, or a paper for a real client matter without facts supplied in the immediate turn. Locator refresh is `us-law-reference-maintain`. Authority research is `us-law-interpretation-research`.

## Criticality

High. The draft is not a filing. Filing deadlines, service, and local rules change the paper. A missing local rule is a stop, not a guess.

## Source of truth

- In ai-router, these are optional source references and are not included in standalone exports: `references/us-law/workflows/court-document-draft.md` and `references/us-law/federal/inferior-courts-and-rules.md`.
- In a standalone repository, use a local official locator if present. Otherwise identify and verify the named court's official rules page from a court or government publisher before drafting.

## Isolation

Return the draft in the session. Do not commit client facts. Save a draft under `scratch/` only when the person asks.

## How to use

1. Require forum (the court, not only the state), matter class, document type, and the parties as the person stated them. If the forum is missing, ask.
2. Fetch the governing rules from an official court or government URL. Use a destination-local jurisdiction page when available; otherwise verify the court's official rules page directly. If the forum's rules cannot be verified, stop.
3. Build a skeleton that maps each section to a rule from that fetch: caption, parties, jurisdiction statement, numbered grounds, relief, certificate of service, and signature. Omit a section when no fetched rule covers it, and label the omission.
4. Put no case citation in the draft unless `us-law-interpretation-research` fetched that opinion in this effort. Otherwise write `[citation unverified — do not file]`.
5. Start the draft with `ADVISORY DRAFT — NOT LEGAL ADVICE — NOT FOR FILING — REQUIRES LICENSED ATTORNEY REVIEW`.
6. Do not include a filing fee, a bar number, or a representation that the signer is counsel.

## Dry run

For a supplied federal forum, list the official rules URLs needed for a civil motion skeleton. Do not draft the motion; stop if the official rules page cannot be verified.

## Security

Inherits Critical cost layers: qmd for discovery, ast-grep for structured files, and Headroom for bulky tool output.

Do not place real personal data, account numbers, or minors' identifying facts in a repository. Do not use PACER credentials. Follow the destination's root security instructions; if none cover legal material, keep facts out of stored files and use only facts supplied in the immediate turn. Optional ai-router provenance, not shipped: `docs/agent-session-security.md`. This skill does not authorize anyone to practice law.

## Completion gates

No reference update unless a rule URL was newly verified. In ai-router, hand off to its reference-maintenance skill. Standalone repositories should use their own documented maintenance procedure; if none exists, report the capability gap and do not write a new corpus.
