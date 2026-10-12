---
schema_version: "2.0.0"
name: us-law-interpretation-research
description: >-
  Research what a constitution, statute, regulation, or opinion means using
  official text fetched in the session. Use when the person asks for an
  interpretation or how a court applied a text. Do not use for a yes-or-no
  corpus check (us-law-reference-compare) or a complaint skeleton
  (us-law-court-document-draft).
owner_agent: research-operator
rank: high
isolation: read-only
on_failure: abort_and_rollback
contracts:
  inputs:
    - Sovereign, matter class, legal question, and as-of date
  outputs:
    - Advisory memo separating holdings from persuasive material, or an explicit not-found
---

# US law interpretation research

## When to use

The person asks what a constitution, statute, regulation, or opinion means, or how a court has applied it.

## When not to use

Locator maintenance (`us-law-reference-maintain`). A check against an existing page (`us-law-reference-compare`). A complaint or motion skeleton (`us-law-court-document-draft`).

## Criticality

High. A holding is the court's decision on the facts before it. Commentary, dissents, headnotes, and attorney-general opinions are not holdings. Label each one.

## Source of truth

- In ai-router, these are optional source references and are not included in standalone exports: `references/us-law/workflows/interpretation-research.md`, `references/us-law/source-ranking.md`, and `docs/standards/us-law-reference-use.md`.
- Standalone work uses official primary sources fetched for the task and the destination's local research rules, if present. The source order below applies when no local source-ranking guide exists.

## Isolation

Read a destination-local corpus first when one exists, then fetch the official texts needed for the memo. In ai-router, a requested dossier may be saved under `results/research/us-law/`; standalone repositories should use their documented output convention. A durable write is a separate mutate step after isolation.

## How to use

1. State the sovereign, the matter class, the legal question, and the as-of date.
2. Read in this order, and only sources fetched this session or already captured as official: constitutional text, statute, session law if the code may lag, regulation, binding court of that sovereign, then persuasive material labeled persuasive.
3. For a case, record the court, date, citation if the fetched page prints one, the URL, and separate the holding from any dissent or publisher summary.
4. Legislative history comes from an official congressional or legislative source. If Congress.gov returns 403, use a GovInfo or legislature page that resolves, or mark legislative history unverified.
5. Stop when the official text does not answer the question. Say what was not found.
6. Stamp the memo advisory. Attorney review. Not legal advice. Not a filing.

## Dry run

For a supplied federal question, name the official publisher or court source to fetch and the URL to verify. Do not write a memo.

## Security

Inherits Critical cost layers: qmd for discovery, ast-grep for structured files, and Headroom for bulky tool output.

Do not include sealed records, PACER credentials, or bulk opinion downloads in git. Follow the destination's root security instructions; if none cover legal research, store no client facts or captured opinions. Optional ai-router provenance, not shipped: `docs/agent-session-security.md`.

## Completion gates

Write a durable memo only on request and use the destination's output convention. In ai-router, promote a stable publisher lesson through its reference-maintenance skill. Standalone repositories should use their local maintenance procedure or report that no write path is configured; never paste a memo into an unmaintained corpus.
