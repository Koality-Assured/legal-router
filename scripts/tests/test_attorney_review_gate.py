import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from scripts.legal.attorney_review_gate import main, sha256_file, verify_signoff


class AttorneyReviewGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.dir = Path(self._tmp.name)
        self.artifact = self.dir / "memo.md"
        self.artifact.write_text("Synthetic memo body.\n", encoding="utf-8")
        self.signoff = {
            "artifact": "memo.md",
            "content_sha256": sha256_file(self.artifact),
            "reviewer_id": "reviewer-001",
            "bar_jurisdiction": "XX",
            "reviewed_at": (datetime.now(timezone.utc) - timedelta(hours=1)).isoformat(),
            "status": "approved",
        }

    def test_valid_signoff_passes(self) -> None:
        self.assertEqual(verify_signoff(self.artifact, self.signoff), [])

    def test_missing_fields_fail_closed(self) -> None:
        for field in ("artifact", "content_sha256", "reviewer_id", "bar_jurisdiction", "reviewed_at", "status"):
            record = {k: v for k, v in self.signoff.items() if k != field}
            errors = verify_signoff(self.artifact, record)
            self.assertTrue(any(field in e for e in errors), field)

    def test_rejected_and_changes_requested_fail(self) -> None:
        for status in ("rejected", "changes_requested"):
            errors = verify_signoff(self.artifact, {**self.signoff, "status": status})
            self.assertTrue(any("not 'approved'" in e for e in errors), status)

    def test_unknown_status_fails(self) -> None:
        errors = verify_signoff(self.artifact, {**self.signoff, "status": "lgtm"})
        self.assertTrue(any("unknown status" in e for e in errors))

    def test_edit_after_review_is_detected(self) -> None:
        self.artifact.write_text("Synthetic memo body, edited.\n", encoding="utf-8")
        errors = verify_signoff(self.artifact, self.signoff)
        self.assertTrue(any("hash mismatch" in e for e in errors))

    def test_signoff_for_other_artifact_fails(self) -> None:
        errors = verify_signoff(self.artifact, {**self.signoff, "artifact": "other.md"})
        self.assertTrue(any("covers" in e for e in errors))

    def test_naive_and_future_timestamps_fail(self) -> None:
        naive = verify_signoff(self.artifact, {**self.signoff, "reviewed_at": "2026-01-01T00:00:00"})
        self.assertTrue(any("timezone-aware" in e for e in naive))
        future = (datetime.now(timezone.utc) + timedelta(days=1)).isoformat()
        errors = verify_signoff(self.artifact, {**self.signoff, "reviewed_at": future})
        self.assertTrue(any("future" in e for e in errors))

    def test_missing_artifact_fails(self) -> None:
        errors = verify_signoff(self.dir / "nope.md", self.signoff)
        self.assertTrue(any("not found" in e for e in errors))

    def test_cli_exit_codes(self) -> None:
        path = self.dir / "signoff.json"
        path.write_text(json.dumps(self.signoff), encoding="utf-8")
        self.assertEqual(main(["check", str(self.artifact), str(path)]), 0)
        path.write_text(json.dumps({**self.signoff, "status": "rejected"}), encoding="utf-8")
        self.assertEqual(main(["check", str(self.artifact), str(path)]), 1)
        path.write_text("not json", encoding="utf-8")
        self.assertEqual(main(["check", str(self.artifact), str(path)]), 1)
        self.assertEqual(main(["hash", str(self.dir / "absent.md")]), 1)


if __name__ == "__main__":
    unittest.main()
