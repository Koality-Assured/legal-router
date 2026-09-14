"""Unit tests for SPDX / CycloneDX license heuristics.

tags: [tests, legal, licensing]
routing_hints: [spdx, cyclonedx, copyleft]
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_SCRIPTS))
sys.path.insert(0, str(_SCRIPTS / "legal"))
sys.path.insert(0, str(_SCRIPTS / "_lib"))

from spdx_license_checker import (  # noqa: E402
    ADVISORY_STAMP,
    analyze_expression,
    main,
    scan_path,
)

SBOM = _SCRIPTS / "legal" / "fixtures" / "sbom"


class SpdxLicenseCheckerTests(unittest.TestCase):
    def test_and_combo_flags_copyleft_with_permissive(self) -> None:
        finding = analyze_expression("MIT AND GPL-3.0-only")
        self.assertIn("and_combines_copyleft_with_other", finding["flags"])
        self.assertIn("contains_strong_copyleft", finding["flags"])

    def test_bare_gnu_note(self) -> None:
        finding = analyze_expression("GPL-3.0")
        self.assertTrue(finding["notes"])
        self.assertIn("GPL-3.0-only", finding["license_ids"])

    def test_spdx_fixture(self) -> None:
        report = scan_path(SBOM / "example.spdx.json")
        self.assertEqual(report["advisory"], ADVISORY_STAMP)
        self.assertIn("network_copyleft_agpl", report["flags"])
        self.assertIn("proprietary_and_copyleft", report["flags"])

    def test_cyclonedx_fixture(self) -> None:
        report = scan_path(SBOM / "example.cdx.json")
        self.assertEqual(report["format"], "cyclonedx")
        self.assertIn("network_copyleft_agpl", report["flags"])

    def test_cli_dry_run(self) -> None:
        self.assertEqual(main(["--dry-run"]), 0)


if __name__ == "__main__":
    unittest.main()
