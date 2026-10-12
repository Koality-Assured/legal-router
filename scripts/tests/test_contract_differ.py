"""Unit tests for synthetic contract differ.

tags: [tests, legal, contracts]
routing_hints: [contract-differ, round-trip, fixtures]
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_SCRIPTS))
sys.path.insert(0, str(_SCRIPTS / "legal"))
sys.path.insert(0, str(_SCRIPTS / "_lib"))

from contract_differ import (  # noqa: E402
    ADVISORY_STAMP,
    diff_contracts,
    extract_clauses,
    main,
    round_trip,
)

FIXTURES = _SCRIPTS / "legal" / "fixtures" / "contracts"


class ContractDifferTests(unittest.TestCase):
    def test_round_trip_all_fixtures(self) -> None:
        paths = list(FIXTURES.glob("*.md"))
        self.assertGreaterEqual(len(paths), 3)
        for path in paths:
            report = round_trip(path.read_text(encoding="utf-8-sig"))
            self.assertTrue(report["ok"], (path.name, report.get("mismatch")))
            self.assertEqual(report["advisory"], ADVISORY_STAMP)

    def test_extracts_core_taxonomy(self) -> None:
        text = (FIXTURES / "acme-vendor-msa-v1.md").read_text(encoding="utf-8-sig")
        labels = {clause["label"] for clause in extract_clauses(text)}
        for required in (
            "indemnity",
            "limitation_of_liability",
            "governing_law",
            "ip_assignment",
            "confidentiality",
            "sla_credits",
        ):
            self.assertIn(required, labels)

    def test_diff_detects_liability_and_sla_changes(self) -> None:
        left = (FIXTURES / "acme-vendor-msa-v1.md").read_text(encoding="utf-8-sig")
        right = (FIXTURES / "acme-vendor-msa-v2.md").read_text(encoding="utf-8-sig")
        report = diff_contracts(left, right, left_name="v1", right_name="v2")
        self.assertTrue(report["ok"])
        changed = set(report["changed_labels"])
        self.assertIn("limitation_of_liability", changed)
        self.assertIn("sla_credits", changed)

    def test_cli_dry_run(self) -> None:
        self.assertEqual(main(["--dry-run"]), 0)


if __name__ == "__main__":
    unittest.main()
