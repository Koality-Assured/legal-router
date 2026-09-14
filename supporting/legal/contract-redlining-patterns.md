---
doc_kind: recipe
canonical_id: contract-redlining-patterns
purpose: [recipe]
rank: high
topics: [legal, contracts]
rag_keywords: [redline, clause, nvca, worldcc]
---

# Contract redlining patterns

Harness-invented clause labels, not a WorldCC scrape. NVCA model documents are public starting points only and are not copied here.

## Taxonomy (synthetic)

indemnity, limitation_of_liability, governing_law, ip_assignment, confidentiality, termination, sla_credits, data_protection, insurance, payment, definitions, preamble, other.

## MUST

- Use `scripts/legal/contract_differ.py` on synthetic fixtures or operator-supplied files.
- Round-trip fixtures with `--dry-run` before claiming parser health.
- Keep client contracts out of git.

## MUST NOT

- Scrape WorldCC / IACCM member libraries or the Conformed Clause Standard Library.
- Treat NVCA optionality commentary as a required market term.
- File, serve, or sign a redline.

## Commands

```bash
python scripts/legal/contract_differ.py --dry-run
python scripts/legal/contract_differ.py --left scripts/legal/fixtures/contracts/acme-vendor-msa-v1.md --right scripts/legal/fixtures/contracts/acme-vendor-msa-v2.md --json
```
