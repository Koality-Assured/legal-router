---
doc_kind: process
canonical_id: us-law-workflow-compare
purpose: [process]
topics: [us-law, references]
rag_keywords: [us-law-reference-compare, citation-check, matter-class]
rank: high
---

# Compare against US law references

Future skill name: `us-law-reference-compare`. Owner: `document-operator`. Isolation: read-only.

## When to use

A person supplies a proposition, memo, or draft and asks whether the captured primary-law corpus supports it.

## When not to use

Refreshing pages (`maintain.md`). Building a new interpretation from opinions (`interpretation-research.md`). Writing a court paper (`court-document-draft.md`).

## Criticality

High. An unsupported sentence must stay unsupported. Do not repair it from memory.

## Source of truth

The jurisdiction page, [`../source-ranking.md`](../source-ranking.md), and [`../matter-classes.md`](../matter-classes.md).

## Isolation

Read-only against `references/us-law/`. Live HTTP is allowed only to confirm a pinpoint the corpus already locates. Do not edit pages in this workflow.

## How to use

1. Require a sovereign and a matter class. If either is absent, ask.
2. `qmd get` the federal and or state page. Corpus first.
3. For each material sentence, mark one status:
   - **Supported** — the captured structural summary, or a page fetched this session from an `official-primary` URL on that locator, states it.
   - **Conflict** — two fetched official sources disagree. Quote neither as the winner. Stop.
   - **Not in corpus** — the locator has no such title, court, or rule.
   - **Unverified** — the sentence needs a case holding, a section, or a local rule that this session did not fetch.
4. Unofficial mirrors cannot support a sentence when an official URL is on the page and was not checked.
5. Return the stamp: advisory, attorney review required, not a filing.

## Dry run

Classify one sentence against Oklahoma or the federal USC page and show the four status labels without writing.

## Security

No client confidential facts in git. Do not send matter files to an unvetted public model endpoint. See ABA Formal Opinion 512 notes in `projects/legal-harness/` when that spec is in the checkout. This workflow does not practice law.

## Completion gates

No page edits, so no reference write-back. A repeated unverified official URL is a maintain handoff, advisory only.
