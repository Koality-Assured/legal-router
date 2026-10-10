---
schema_version: "2.0.0"
name: patent-claim-crosswalk
description: >-
  Deconstruct patent claims into preamble and limitation elements and map them
  against technical specifications, licensee architectures, or prior art.
  Use when conducting patent licensing crosswalks, freedom-to-operate (FTO)
  claim charting, or IP portfolio diligence. Do not use for open source SBOM
  scans (open-source-license-scan) or statutory crosswalks (regulatory-crosswalk-audit).
owner_agent: ip-licensing-curator
rank: high
isolation: mutate
on_failure: abort_and_rollback
prerequisites:
  - python
dependencies:
  required_skills:
    - isolate-work
  delegated_skills: []
  in_session_skills: []
contracts:
  inputs:
    - Patent claims (independent and dependent claim set)
    - Target technical specification, product architecture, or prior art excerpt
  outputs:
    - Deconstructed claim element chart (preamble, transitional phrase, limitations)
    - Mapping crosswalk with element-by-element evidentiary match notes
    - Advisory patent analysis memo stamped for licensed patent attorney review
topics: [legal, patents, claims, crosswalk, ip-licensing]
routing_hints: [claim-chart, patent-crosswalk, fto, patent-claim, licensing-audit]
---

# Patent claim crosswalk

## When to use

A patent license negotiation, acquisition portfolio diligence, freedom-to-operate (FTO) assessment, or defensive analysis requires mapping patent claims to technical product architectures, open source dependencies, or prior art references. Independent and dependent claims must be parsed into granular limitations and systematically mapped.

## When not to use

SPDX or CycloneDX SBOM scanning for software package copyleft (`open-source-license-scan`). General commercial contract review (`contract-clause-review`). Statutory regulatory audits (`regulatory-crosswalk-audit`).

## Criticality

High: erroneous claim deconstruction or overlooking a specific claim limitation can invalidate an infringement or non-infringement position, distort licensing royalties, or misstate patent portfolio value. Work product is advisory technical-legal analysis and requires licensed patent attorney review.

## Source of truth

- [`docs/standards/legal-overlay.md`](../../../../docs/standards/legal-overlay.md)
- [`supporting/legal/spdx-license-scan.md`](../../../../supporting/legal/spdx-license-scan.md)
- 35 U.S.C. § 112 (specification requirements and claim definiteness)
- MPEP Chapter 2100 (Patentability) and Federal Circuit claim construction standards (Phillips v. AWH Corp.)

## Isolation

`mutate` when generating and storing claim charts or licensing crosswalks in `results/`. Parent isolates via `isolate-work` (`python scripts/routing/spawn_worktree.py create --slug patent-claim-<slug>`), then spawns `ip-licensing-curator`.

## How to use

1. Run `qmd search` for IP licensing and patent claim patterns (no directory walks).
2. Parse patent claims into structural components:
   - Claim number and dependency tree (e.g. Claim 1 independent; Claim 2 dependent on Claim 1)
   - Preamble (identifying statutory class: apparatus, method, system, composition)
   - Transitional phrase ("comprising" [open], "consisting of" [closed], "consisting essentially of")
   - Discrete limitation elements (e.g. 1[a], 1[b], 1[c])
3. For each limitation element, locate corresponding evidentiary references:
   - In licensing/FTO analysis: technical architecture components, source code modules, API specifications
   - In validity/prior art analysis: cited patent or non-patent literature specifications
   - In open-source patent grant review: Apache 2.0 Section 3, GPLv3 Section 11, or Mozilla Public License patent grant provisions
4. Construct an element-by-element crosswalk table detailing coverage, literal read, doctrine of equivalents considerations, or evidentiary gaps.
5. Formulate key licensing questions and open construction ambiguities for patent counsel.
6. Apply the mandatory advisory stamp:
   `ADVISORY WORK PRODUCT - REQUIRES LICENSED ATTORNEY REVIEW`

## Dry run

```bash
python scripts/ai-tooling/validate_skill.py --skill patent-claim-crosswalk --dry-run
```

## Security

Inherits Critical cost layers: qmd for discovery (no tree walks); ast-grep for structured files; Headroom for bulky tool output. Skills cannot waive root AGENTS.md.

Never commit unpublished patent applications, trade secrets, confidential licensing terms, or non-public invention disclosures. Claim charting does not constitute formal legal opinion or litigation filing.

## Completion gates

Deconstructed claim chart generated with all limitation elements mapped, evidentiary citations provided, patent counsel open questions listed, and advisory stamp applied.
