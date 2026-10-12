"""Unit tests for legal citation verification.

tags: [tests, legal, citations]
routing_hints: [verify-citations, hallucination, fixtures]
"""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_SCRIPTS))
sys.path.insert(0, str(_SCRIPTS / "legal"))
sys.path.insert(0, str(_SCRIPTS / "_lib"))

from verify_citations import (  # noqa: E402
    ADVISORY_STAMP,
    main,
    parse_citations,
    verify_suite,
    verify_text,
)


class VerifyCitationsTests(unittest.TestCase):
    def test_suite_flags_every_planted_hallucination(self) -> None:
        report = verify_suite()
        self.assertTrue(report["ok"], report.get("failures"))
        self.assertEqual(report["missed_hallucinations"], [])
        planted = [row for row in report["items"] if row["expected"] == "hallucinated"]
        self.assertGreaterEqual(len(planted), 5)
        self.assertTrue(all(row["ok"] for row in planted))

    def test_mixed_memo_catches_fakes_and_keeps_valid(self) -> None:
        memo = (_SCRIPTS / "legal" / "fixtures" / "citations" / "mixed-memo.md").read_text(
            encoding="utf-8-sig"
        )
        report = verify_text(memo)
        self.assertEqual(report["advisory"], ADVISORY_STAMP)
        self.assertGreaterEqual(report["hallucinated_count"], 5)
        self.assertGreaterEqual(report["valid_fixture_count"], 3)
        fake_texts = {row["text"] for row in report["citations"] if row["status"] == "hallucinated"}
        self.assertTrue(any("Fake. Rep." in text for text in fake_texts))
        self.assertTrue(any("F.4d" in text for text in fake_texts))
        self.assertTrue(any("99 U.S.C." in text for text in fake_texts))

    def test_cli_suite_ok(self) -> None:
        self.assertEqual(main(["--dry-run", "--json"]), 0)

    def test_unverified_not_silently_accepted(self) -> None:
        parsed = parse_citations("Example Corp. v. Widget LLC, 12 F.4th 345 (3d Cir. 2021)")
        self.assertEqual(len(parsed), 1)
        report = verify_text(parsed[0]["text"])
        statuses = {row["status"] for row in report["citations"]}
        self.assertIn("unverified", statuses)
        self.assertNotIn("valid_fixture", statuses)


if __name__ == "__main__":
    unittest.main()
