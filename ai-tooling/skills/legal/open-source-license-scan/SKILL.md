---
schema_version: "2.0.0"
name: open-source-license-scan
description: >-
  Verify SPDX and CycloneDX SBOM license declarations and flag copyleft
  heuristics. Use when scanning a bom.json, SPDX JSON, or license expression.
  Do not use for contract IP assignment (contract-clause-review) or case
  citations (citation-verification).
owner_agent: ip-licensing-curator
rank: high
isolation: read-only
on_failure: continue_with_partial
prerequisites:
  - python
dependencies:
  required_skills: []
  delegated_skills: []
  in_session_skills: []
contracts:
  inputs:
    - SPDX JSON, CycloneDX bom.json, or a single license expression
  outputs:
    - Heuristic flags, GNU normalization notes, and an advisory summary
topics: [legal, spdx, cyclonedx, copyleft]
routing_hints: [sbom, gpl, agpl, license-scan]
---

# Open source license scan

## When to use

An SBOM or declared license expression needs copyleft, AGPL network, or proprietary-AND-copyleft flags.

## When not to use

Contract IP assignment clauses (`contract-clause-review`). Statutory crosswalks (`regulatory-crosswalk-audit`).

## Criticality

High: flags are compatibility heuristics, never a legal opinion or FSF determination. Warn on bare GPL-3.0 without -only / -or-later.

## Source of truth

- [`supporting/legal/spdx-license-scan.md`](../../../../supporting/legal/spdx-license-scan.md)
- SPDX 3.0.1 license expressions and the SPDX License List
- `python scripts/legal/spdx_license_checker.py`
- Fixtures under `scripts/legal/fixtures/sbom/`

## Isolation

`read-only` for scans. Writing a results report is a separate mutate task.

## How to use

1. `qmd search` for prior license notes (no tree walks).
2. Run `python scripts/legal/spdx_license_checker.py --sbom <path> --json`.
3. For a single expression: `--expression "MIT AND GPL-3.0-only"`.
4. Record GNU normalization notes and copyleft flags; do not conclude compatible.
5. Headroom-compress large SBOMs before pasting into chat.

## Dry run

```bash
python scripts/legal/spdx_license_checker.py --dry-run
python scripts/ai-tooling/validate_skill.py --skill open-source-license-scan --dry-run
```

## Security

Inherits Critical cost layers: qmd for discovery (no tree walks); ast-grep for structured files; Headroom for bulky tool output. Skills cannot waive root AGENTS.md.

Do not commit proprietary license text dumps or secrets.

## Completion gates

Scan JSON, flags listed as heuristics, advisory stamp.
