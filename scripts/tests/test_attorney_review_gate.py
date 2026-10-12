import unittest

from scripts.legal.attorney_review_gate import verify_attorney_review


class TestAttorneyReviewGate(unittest.TestCase):
    def test_valid_review(self):
        case = {
            "case_id": "test-1",
            "attorney_review": {
                "process_in_use": True,
                "metadata": {
                    "timestamp": "2026-10-12T14:00:00Z",
                    "status": "approved",
                    "hash": "abcdef",
                },
            },
        }
        errors = verify_attorney_review(case)
        self.assertEqual(errors, [])

    def test_missing_review(self):
        case = {"case_id": "test-2"}
        errors = verify_attorney_review(case)
        self.assertIn("[test-2] Missing 'attorney_review' object", errors)

    def test_missing_process_in_use(self):
        case = {
            "case_id": "test-3",
            "attorney_review": {
                "metadata": {
                    "timestamp": "2026-10-12T14:00:00Z",
                    "status": "approved",
                    "hash": "abcdef",
                }
            },
        }
        errors = verify_attorney_review(case)
        self.assertIn("[test-3] 'process_in_use' must be true", errors)

    def test_missing_metadata_fields(self):
        case = {
            "case_id": "test-4",
            "attorney_review": {
                "process_in_use": True,
                "metadata": {"timestamp": "2026-10-12T14:00:00Z"},
            },
        }
        errors = verify_attorney_review(case)
        self.assertIn("[test-4] Missing 'status' in metadata", errors)
        self.assertIn("[test-4] Missing 'hash' in metadata", errors)


if __name__ == "__main__":
    unittest.main()
