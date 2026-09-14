---
doc_kind: recipe
canonical_id: spdx-license-scan
purpose: [recipe]
rank: medium
topics: [legal, spdx, cyclonedx]
rag_keywords: [copyleft, agpl, sbom]
---

# SPDX / CycloneDX license scan

Heuristic flags only. SPDX License List identifiers plus expressions (`AND`, `OR`, `WITH`, `+`). CycloneDX 1.7 components should carry SPDX ids.

## MUST

- Warn on bare GNU ids (`GPL-3.0`) missing `-only` or `-or-later`.
- Flag AGPL as network copyleft.
- Flag `AND` combinations of strong copyleft with permissive or proprietary ids as a heuristic, not a legal conclusion.

## Commands

```bash
python scripts/legal/spdx_license_checker.py --dry-run
python scripts/legal/spdx_license_checker.py --expression "MIT AND GPL-3.0-only" --json
```
