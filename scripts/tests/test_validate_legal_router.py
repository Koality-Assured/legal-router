import unittest
import json
from pathlib import Path
from scripts.validation.validate_legal_router import validate_case, validate_registry

REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURES_DIR = Path(__file__).resolve().parents[1] / "validation" / "fixtures"
REGISTRY_PATH = REPO_ROOT / "docs" / "standards" / "legal-representation-registry.json"

class TestValidateLegalRouter(unittest.TestCase):
    def setUp(self):
        with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
            registry_data = json.load(f)
        self.registry = validate_registry(registry_data)
        
    def test_valid_cases(self):
        with open(FIXTURES_DIR / "contract-cases.json", "r", encoding="utf-8") as f:
            manifest = json.load(f)
        for case in manifest.get("cases", []):
            errors = validate_case(case, self.registry["representations_by_id"], self.registry["medium_aliases"])
            self.assertEqual(errors, [])

    def test_failing_cases(self):
        with open(FIXTURES_DIR / "failing-cases.json", "r", encoding="utf-8") as f:
            manifest = json.load(f)
        case = manifest["cases"][0]
        errors = validate_case(case, self.registry["representations_by_id"], self.registry["medium_aliases"])
        
        self.assertIn("[bad-case-001] upl_disclaimer_required must be true", errors)
        self.assertIn("[bad-case-001] supervising_attorney_required must be true", errors)
        self.assertIn("[bad-case-001] Unknown representation route: 'nonexistent_route'", errors)
        self.assertIn("[bad-case-001] review_handoff.reviewer must be 'legal-ethics-reviewer', got 'wrong-reviewer'", errors)
        self.assertTrue(any("missing mandatory advisory stamp" in e for e in errors))
        self.assertIn("[bad-case-001] deliverable[0] citations must be verified", errors)

if __name__ == '__main__':
    unittest.main()
