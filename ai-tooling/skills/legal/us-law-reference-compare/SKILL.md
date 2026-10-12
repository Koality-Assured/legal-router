---
schema_version: "2.0.0"
name: us-law-reference-compare
description: >-
  Compare a proposition or draft to the captured US primary-law corpus and
  mark each sentence supported, conflicting, missing, or unverified. Use when
  a person asks whether a memo matches official locators. Do not use to
  refresh pages (us-law-reference-maintain) or to draft a court paper
  (us-law-court-document-draft).
owner_agent: document-operator
rank: high
isolation: read-only
on_failure: abort_and_rollback
contracts:
  inputs:
    - Sovereign, matter class, and the proposition or draft to check
  outputs:
    - Sentence statuses plus the advisory attorney-review stamp
---

# US law reference compare

## When to use

A person supplies a proposition, memo, or draft and asks whether the captured primary-law corpus supports it.

## When not to use

Refreshing pages (`us-law-reference-maintain`). Building a new interpretation (`us-law-interpretation-research`). Writing a court paper (`us-law-court-document-draft`).

## Criticality

High. An unsupported sentence stays unsupported. Do not repair it from memory.

## Source of truth

- In ai-router, these are optional source references and are not included in standalone exports: `references/us-law/workflows/compare.md`, `references/us-law/source-ranking.md`, and `references/us-law/matter-classes.md`.
- Standalone work uses a destination-local corpus when present. Otherwise, compare against the official primary text supplied or fetched for the task and mark any unavailable authority unverified.

## Isolation

In ai-router, this is read-only against `references/us-law/`; live HTTP only confirms a pinpoint the corpus already locates. Standalone repositories may read their local corpus or fetch official primary text for the task, but must not create or update a corpus in this skill.

## How to use

1. Require a sovereign and a matter class. If either is absent, ask.
2. Read a destination-local federal or state page if available. Otherwise fetch the official primary text needed for the proposition; do not claim corpus support for material that is absent locally.
3. For each material sentence, mark one status: supported, conflict, not in corpus, or unverified.
4. Unofficial mirrors cannot support a sentence when an official URL is on the page and was not checked.
5. Return the stamp: advisory, attorney review required, not a filing.

## Dry run

Classify one sentence against supplied or destination-local official primary text; if none is available, mark it not in corpus or unverified. Show all four status labels without writing.

## Security

Inherits Critical cost layers: qmd for discovery, ast-grep for structured files, and Headroom for bulky tool output.

Do not place client confidential facts in git. Follow the destination's root security instructions; if none cover legal material, keep client facts out of stored files. Optional ai-router provenance, not shipped: `docs/agent-session-security.md`. This skill does not practice law.

## Completion gates

No page edits in this skill. In ai-router, a repeated unverified official URL may be handed to its reference-maintenance skill. Standalone repositories should use their local documented process or report the maintenance capability gap; do not invoke a private router procedure.
