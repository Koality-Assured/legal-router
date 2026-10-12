"""Comprehensive unit tests for the legal scripts automation suite.

tags: [tests, legal]
routing_hints: [legal-scripts, citations, spdx, contract-diff]

Tests all parsing, validation, compatibility evaluation, playbook diffing,
and CLI execution entrypoints for verify_citations, spdx_license_checker,
and contract_differ.
"""

from __future__ import annotations

import io
import json
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

_SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_SCRIPTS))
sys.path.insert(0, str(_SCRIPTS / "legal"))
sys.path.insert(0, str(_SCRIPTS / "_lib"))

import contract_differ
import spdx_license_checker
import verify_citations


class VerifyCitationsTests(unittest.TestCase):
    """Unit tests for Bluebook citation parser and verifier."""

    def setUp(self) -> None:
        self.fixtures_dir = _SCRIPTS / "legal" / "fixtures" / "citations"
        self.suite_path = self.fixtures_dir / "citation-suite.json"
        self.memo_path = self.fixtures_dir / "mixed-memo.md"

    def test_ast_case_citation_parsing_and_validation(self) -> None:
        text = "Brown v. Board of Education, 347 U.S. 483, 492-95 (1954)"
        nodes = verify_citations.parse_citations_ast(text)
        self.assertEqual(len(nodes), 1)
        node = nodes[0]
        self.assertIsInstance(node, verify_citations.CaseCitationNode)
        self.assertEqual(node.attributes["name"], "Brown v. Board of Education")
        self.assertEqual(node.attributes["volume"], "347")
        self.assertEqual(node.attributes["reporter"], "U.S.")
        self.assertEqual(node.attributes["page"], "483")
        self.assertEqual(node.attributes["pin_cite"], "492-95")
        self.assertEqual(node.attributes["year"], 1954)
        self.assertEqual(node.validate_bluebook(), [])

    def test_ast_case_citation_invalid_properties(self) -> None:
        invalid_node = verify_citations.CaseCitationNode(
            text="Invalid v. Case, ABC Fake. Rep. XYZ (2099)",
            span=(0, 42),
            name="Invalid v. Case",
            volume="ABC",
            reporter="Fake. Rep.",
            page="XYZ",
            year=2099,
        )
        violations = invalid_node.validate_bluebook()
        self.assertIn("invalid_volume_number", violations)
        self.assertIn("unrecognized_reporter", violations)
        self.assertIn("invalid_first_page", violations)
        self.assertIn("invalid_year", violations)

    def test_ast_statutory_and_regulatory_citations(self) -> None:
        text = "5 U.S.C. § 552(a)(4)(B) and 45 C.F.R. § 164.312(a)(1)"
        nodes = verify_citations.parse_citations_ast(text)
        self.assertEqual(len(nodes), 2)

        usc_node = nodes[0]
        self.assertIsInstance(usc_node, verify_citations.USCCitationNode)
        self.assertEqual(usc_node.attributes["title"], "5")
        self.assertEqual(usc_node.attributes["section"], "552")
        self.assertEqual(usc_node.attributes["pin_cite"], "(a)(4)(B)")
        self.assertEqual(usc_node.validate_bluebook(), [])

        cfr_node = nodes[1]
        self.assertIsInstance(cfr_node, verify_citations.CFRCitationNode)
        self.assertEqual(cfr_node.attributes["title"], "45")
        self.assertEqual(cfr_node.attributes["section"], "164.312")
        self.assertEqual(cfr_node.attributes["pin_cite"], "(a)(1)")
        self.assertEqual(cfr_node.validate_bluebook(), [])

    def test_ast_federal_register_citation(self) -> None:
        text = "89 Fed. Reg. 12,345, 12,348 (Jan. 15, 2024)"
        nodes = verify_citations.parse_citations_ast(text)
        self.assertEqual(len(nodes), 1)
        fr_node = nodes[0]
        self.assertIsInstance(fr_node, verify_citations.FederalRegisterNode)
        self.assertEqual(fr_node.attributes["volume"], "89")
        self.assertEqual(fr_node.attributes["reporter"], "Fed. Reg.")
        self.assertEqual(fr_node.attributes["page"], "12345")
        self.assertEqual(fr_node.attributes["pin_cite"], "12,348")
        self.assertEqual(fr_node.attributes["year"], 2024)
        self.assertEqual(fr_node.validate_bluebook(), [])

    def test_ast_eu_regulation_citation(self) -> None:
        text = "Regulation (EU) 2024/1689"
        nodes = verify_citations.parse_citations_ast(text)
        self.assertEqual(len(nodes), 1)
        eu_node = nodes[0]
        self.assertIsInstance(eu_node, verify_citations.EURegulationNode)
        self.assertEqual(eu_node.attributes["body"], "EU")
        self.assertEqual(eu_node.attributes["year"], 2024)
        self.assertEqual(eu_node.attributes["number"], "1689")
        self.assertEqual(eu_node.validate_bluebook(), [])

    def test_classify_parsed_edge_cases(self) -> None:
        known = {"Marbury v. Madison, 5 U.S. 137 (1803)"}
        # Known fixture
        self.assertEqual(
            verify_citations.classify_parsed(
                {"text": "Marbury v. Madison, 5 U.S. 137 (1803)"}, known
            ),
            "valid_fixture",
        )
        # Out-of-bounds USC title
        self.assertEqual(
            verify_citations.classify_parsed(
                {"kind": "usc", "title": "99", "text": "99 U.S.C. § 1"}, known
            ),
            "hallucinated",
        )
        # Out-of-bounds CFR title
        self.assertEqual(
            verify_citations.classify_parsed(
                {"kind": "cfr", "title": "99", "text": "99 C.F.R. § 1"}, known
            ),
            "hallucinated",
        )
        # Out-of-bounds Federal Register volume or year
        self.assertEqual(
            verify_citations.classify_parsed(
                {
                    "kind": "federal_register",
                    "volume": "200",
                    "year": 2024,
                    "text": "200 Fed. Reg. 1",
                },
                known,
            ),
            "hallucinated",
        )
        self.assertEqual(
            verify_citations.classify_parsed(
                {
                    "kind": "federal_register",
                    "volume": "89",
                    "year": 2099,
                    "text": "89 Fed. Reg. 1 (2099)",
                },
                known,
            ),
            "hallucinated",
        )
        # Fake case reporter
        self.assertEqual(
            verify_citations.classify_parsed(
                {
                    "kind": "case",
                    "reporter": "Fake. Rep.",
                    "year": 2020,
                    "text": "X v. Y, 1 Fake. Rep. 2",
                },
                known,
            ),
            "hallucinated",
        )
        # Legitimate unverified citation
        self.assertEqual(
            verify_citations.classify_parsed(
                {
                    "kind": "case",
                    "reporter": "F.4th",
                    "year": 2022,
                    "text": "Real v. Case, 10 F.4th 20",
                },
                known,
            ),
            "unverified",
        )

    def test_verify_suite_and_memo(self) -> None:
        suite_report = verify_citations.verify_suite(self.suite_path)
        self.assertTrue(suite_report["ok"])
        self.assertEqual(suite_report["missed_hallucinations"], [])

        memo_text = self.memo_path.read_text(encoding="utf-8-sig")
        memo_report = verify_citations.verify_text(memo_text)
        self.assertGreaterEqual(memo_report["hallucinated_count"], 5)
        self.assertGreaterEqual(memo_report["valid_fixture_count"], 3)

    def test_load_suite_missing_items(self) -> None:
        with patch.object(Path, "read_text", return_value="{}"):  # noqa: SIM117
            with self.assertRaises(ValueError):
                verify_citations.load_suite(Path("dummy.json"))

    def test_live_lookup_token_handling(self) -> None:
        with self.assertRaises(ValueError):
            verify_citations.live_lookup("text", "")

    def test_cli_execution_options(self) -> None:
        # Dry run with json
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = verify_citations.main(["--dry-run", "--json"])
        self.assertEqual(code, 0)
        data = json.loads(stdout.getvalue())
        self.assertTrue(data["ok"])

        # Text parsing with --ast
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = verify_citations.main(
                ["--text", "5 U.S.C. § 552", "--ast", "--json"]
            )
        self.assertEqual(code, 0)
        data = json.loads(stdout.getvalue())
        self.assertIn("ast_nodes", data)

        # File parsing
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = verify_citations.main(["--file", str(self.memo_path), "--json"])
        self.assertEqual(code, 0)
        data = json.loads(stdout.getvalue())
        self.assertGreater(data["hallucinated_count"], 0)

        # Live without token in env
        stderr = io.StringIO()
        with redirect_stderr(stderr), patch.dict("os.environ", {}, clear=True):
            code = verify_citations.main(["--live", "--text", "5 U.S.C. § 552"])
        self.assertEqual(code, 2)

    def test_case_citation_missing_year_violation(self) -> None:
        node = verify_citations.CaseCitationNode(
            text="Roe v. Wade, 410 U.S. 113",
            span=(0, 25),
            name="Roe v. Wade",
            volume="410",
            reporter="U.S.",
            page="113",
            year=None,
        )
        violations = node.validate_bluebook()
        self.assertIn("missing_year", violations)

    def test_classify_parsed_type_guards(self) -> None:
        known = set()
        # Non-numeric usc title
        self.assertEqual(
            verify_citations.classify_parsed(
                {"kind": "usc", "title": "non_numeric"}, known
            ),
            "hallucinated",
        )
        # Non-numeric cfr title
        self.assertEqual(
            verify_citations.classify_parsed(
                {"kind": "cfr", "title": "non_numeric"}, known
            ),
            "hallucinated",
        )
        # Non-numeric federal register volume
        self.assertEqual(
            verify_citations.classify_parsed(
                {"kind": "federal_register", "volume": "non_numeric"}, known
            ),
            "hallucinated",
        )
        # Non-numeric case year
        self.assertEqual(
            verify_citations.classify_parsed(
                {"kind": "case", "year": "non_numeric"}, known
            ),
            "hallucinated",
        )

    def test_cli_file_not_found_handling(self) -> None:
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            code = verify_citations.main(["--file", "nonexistent_citations_file.txt"])
        self.assertEqual(code, 2)
        self.assertIn("error:", stderr.getvalue().lower())

        stderr2 = io.StringIO()
        with redirect_stderr(stderr2):
            code2 = verify_citations.main(["--suite", "nonexistent_suite_file.json"])
        self.assertEqual(code2, 2)
        self.assertIn("error:", stderr2.getvalue().lower())


class SpdxLicenseCheckerTests(unittest.TestCase):
    """Unit tests for SPDX license validation, compatibility matrix, and SBOM scanner."""

    def setUp(self) -> None:
        self.sbom_dir = _SCRIPTS / "legal" / "fixtures" / "sbom"
        self.spdx_path = self.sbom_dir / "example.spdx.json"
        self.cdx_path = self.sbom_dir / "example.cdx.json"

    def test_license_tokenization_and_normalization(self) -> None:
        tokens = spdx_license_checker.tokenize_expression(
            "(MIT OR Apache-2.0) AND GPL-3.0"
        )
        self.assertEqual(tokens, ["MIT", "Apache-2.0", "GPL-3.0"])

        norm, note = spdx_license_checker.normalize_gnu("GPL-3.0")
        self.assertEqual(norm, "GPL-3.0-only")
        self.assertIn("deprecated", note or "")

        norm_ok, note_ok = spdx_license_checker.normalize_gnu("MIT")
        self.assertEqual(norm_ok, "MIT")
        self.assertIsNone(note_ok)

    def test_validate_license_id(self) -> None:
        val_mit = spdx_license_checker.validate_license_id("MIT")
        self.assertTrue(val_mit["is_valid_spdx"])
        self.assertEqual(val_mit["copyleft_category"], "permissive")

        val_agpl = spdx_license_checker.validate_license_id("AGPL-3.0-only")
        self.assertTrue(val_agpl["is_valid_spdx"])
        self.assertEqual(val_agpl["copyleft_category"], "network_copyleft")

        val_custom = spdx_license_checker.validate_license_id("LicenseRef-Custom")
        self.assertFalse(val_custom["is_valid_spdx"])
        self.assertTrue(val_custom["is_custom"])

    def test_evaluate_compatibility_matrix(self) -> None:
        # Compatible permissive combination
        comp = spdx_license_checker.evaluate_compatibility(
            ["MIT", "Apache-2.0", "BSD-3-Clause"]
        )
        self.assertTrue(comp["compatible"])
        self.assertEqual(comp["highest_severity"], "none")

        # Incompatible: GPL-2.0-only + Apache-2.0
        incomp_apache_gpl2 = spdx_license_checker.evaluate_compatibility(
            ["GPL-2.0-only", "Apache-2.0"]
        )
        self.assertFalse(incomp_apache_gpl2["compatible"])
        self.assertEqual(incomp_apache_gpl2["highest_severity"], "high")

        # Incompatible: GPL-2.0-only + GPL-3.0-only
        incomp_gpl_versions = spdx_license_checker.evaluate_compatibility(
            ["GPL-2.0-only", "GPL-3.0-only"]
        )
        self.assertFalse(incomp_gpl_versions["compatible"])
        self.assertEqual(incomp_gpl_versions["highest_severity"], "critical")

        # Proprietary + Network Copyleft (AGPL)
        incomp_prop_agpl = spdx_license_checker.evaluate_compatibility(
            ["proprietary", "AGPL-3.0-only"]
        )
        self.assertFalse(incomp_prop_agpl["compatible"])
        self.assertEqual(incomp_prop_agpl["highest_severity"], "critical")

    def test_validate_license_list(self) -> None:
        deps = [
            {"name": "express", "license": "MIT"},
            {"name": "legacy-tool", "license": "GPL-3.0"},
            {"name": "internal-secret", "license": "LicenseRef-Proprietary"},
        ]
        report = spdx_license_checker.validate_license_list(deps)
        self.assertEqual(report["dependency_count"], 3)
        self.assertEqual(report["valid_spdx_token_count"], 2)
        self.assertEqual(report["deprecated_token_count"], 1)
        self.assertEqual(report["custom_token_count"], 1)
        self.assertIn("advisory", report)

    def test_assess_copyleft_risk_contexts(self) -> None:
        # AGPL under SaaS vs Proprietary Distribution
        saas_risk = spdx_license_checker.assess_copyleft_risk(
            ["AGPL-3.0-only"], context="saas_cloud"
        )
        self.assertEqual(saas_risk["overall_risk"], "critical")

        # GPL under SaaS (no distribution) vs Proprietary Distribution
        gpl_saas = spdx_license_checker.assess_copyleft_risk(
            ["GPL-3.0-only"], context="saas_cloud"
        )
        self.assertEqual(gpl_saas["overall_risk"], "low")

        gpl_dist = spdx_license_checker.assess_copyleft_risk(
            ["GPL-3.0-only"], context="proprietary_distribution"
        )
        self.assertEqual(gpl_dist["overall_risk"], "critical")

    def test_scan_path_spdx_and_cyclonedx(self) -> None:
        spdx_res = spdx_license_checker.scan_path(self.spdx_path)
        self.assertEqual(spdx_res["format"], "spdx")
        self.assertIn("network_copyleft_agpl", spdx_res["flags"])

        cdx_res = spdx_license_checker.scan_path(self.cdx_path)
        self.assertEqual(cdx_res["format"], "cyclonedx")
        self.assertIn("network_copyleft_agpl", cdx_res["flags"])

    def test_cli_execution_options(self) -> None:
        # Dry run
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = spdx_license_checker.main(["--dry-run"])
        self.assertEqual(code, 0)

        # Expression
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = spdx_license_checker.main(
                ["--expression", "MIT AND BSD-3-Clause", "--json"]
            )
        self.assertEqual(code, 0)
        data = json.loads(stdout.getvalue())
        self.assertTrue(data["ok"])

        # Dependencies JSON string
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = spdx_license_checker.main(
                [
                    "--dependencies",
                    '[{"name": "demo", "license": "Apache-2.0"}]',
                    "--json",
                ]
            )
        self.assertEqual(code, 0)

        # Missing required args
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            code = spdx_license_checker.main([])
        self.assertEqual(code, 2)

    def test_concurrent_network_and_strong_copyleft_with_proprietary(self) -> None:
        comp = spdx_license_checker.evaluate_compatibility(
            ["proprietary", "AGPL-3.0-only", "GPL-3.0-only"]
        )
        self.assertFalse(comp["compatible"])
        self.assertEqual(comp["highest_severity"], "critical")
        # Both network copyleft and strong copyleft conflicts should be recorded
        reasons = [c["reason"] for c in comp["conflicts"]]
        self.assertTrue(any("network copyleft" in r for r in reasons))
        self.assertTrue(any("strong copyleft" in r for r in reasons))

    def test_agpl_gpl2_incompatibility(self) -> None:
        comp = spdx_license_checker.evaluate_compatibility(
            ["AGPL-3.0-only", "GPL-2.0-only"]
        )
        self.assertFalse(comp["compatible"])
        self.assertEqual(comp["highest_severity"], "critical")
        self.assertTrue(
            any(
                "AGPL-3.0-only" in c["licenses"] and "GPL-2.0-only" in c["licenses"]
                for c in comp["conflicts"]
            )
        )

    def test_cli_error_handling_and_consistent_exit_codes(self) -> None:
        # File not found on --sbom
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            code = spdx_license_checker.main(["--sbom", "nonexistent_sbom.json"])
        self.assertEqual(code, 2)
        self.assertIn("error:", stderr.getvalue().lower())

        # Invalid json in dependencies string
        stderr2 = io.StringIO()
        with redirect_stderr(stderr2):
            code2 = spdx_license_checker.main(["--dependencies", "not valid json{"])
        self.assertEqual(code2, 2)
        self.assertIn("error:", stderr2.getvalue().lower())

        # Incompatible expression returns exit code 1
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code3 = spdx_license_checker.main(
                ["--expression", "GPL-2.0-only AND Apache-2.0", "--json"]
            )
        self.assertEqual(code3, 1)
        data = json.loads(stdout.getvalue())
        self.assertFalse(data["ok"])


class ContractDifferTests(unittest.TestCase):
    """Unit tests for contract clause extraction, playbook comparison, and liability/indemnity deviations."""

    def setUp(self) -> None:
        self.fixtures_dir = _SCRIPTS / "legal" / "fixtures" / "contracts"
        self.v1_path = self.fixtures_dir / "acme-vendor-msa-v1.md"
        self.v2_path = self.fixtures_dir / "acme-vendor-msa-v2.md"
        self.spa_path = self.fixtures_dir / "synthetic-spa.md"

    def test_round_trip_all_contract_fixtures(self) -> None:
        for path in self.fixtures_dir.glob("*.md"):
            text = path.read_text(encoding="utf-8-sig")
            report = contract_differ.round_trip(text)
            self.assertTrue(report["ok"], f"Failed round trip for {path.name}")
            self.assertGreater(report["clause_count"], 0)

    def test_detect_liability_deviations(self) -> None:
        # Balanced standard clause
        standard_text = (
            "Neither party shall be liable for indirect, incidental, special, or consequential damages. "
            "Each party's aggregate liability under this Agreement shall not exceed the total fees paid "
            "in the twelve (12) months preceding the claim. Carve-outs: indemnification and gross negligence."
        )
        report = contract_differ.detect_liability_deviations(standard_text)
        self.assertEqual(report["risk_level"], "low")
        self.assertTrue(report["has_consequential_waiver"])
        self.assertTrue(report["has_aggregate_cap"])
        self.assertEqual(report["deviations"], [])

        # High risk: missing consequential damages waiver
        missing_waiver = "Each party's aggregate liability shall not exceed fees paid in the last 12 months."
        rep_missing = contract_differ.detect_liability_deviations(missing_waiver)
        self.assertEqual(rep_missing["risk_level"], "high")
        codes = [d["code"] for d in rep_missing["deviations"]]
        self.assertIn("missing_consequential_damages_waiver", codes)

        # Critical risk: uncapped liability
        uncapped_text = "Vendor's liability shall not be limited and Vendor shall have unlimited liability for all damages."
        rep_uncapped = contract_differ.detect_liability_deviations(uncapped_text)
        self.assertEqual(rep_uncapped["risk_level"], "critical")
        codes = [d["code"] for d in rep_uncapped["deviations"]]
        self.assertIn("uncapped_liability_risk", codes)

    def test_detect_indemnity_deviations(self) -> None:
        # Balanced mutual indemnity with procedural triad
        balanced_text = (
            "Provider shall defend and indemnify Customer against IP infringement claims. "
            "Customer shall defend and indemnify Provider against Customer Data claims. "
            "Indemnification is conditioned on prompt written notice, sole control of defense, "
            "and no party shall settle any claim without prior written consent."
        )
        report = contract_differ.detect_indemnity_deviations(balanced_text)
        self.assertEqual(report["risk_level"], "low")
        self.assertTrue(report["is_mutual"])
        self.assertTrue(report["procedural_protections"]["prompt_notice"])
        self.assertTrue(report["procedural_protections"]["sole_control_defense"])
        self.assertTrue(report["procedural_protections"]["settlement_consent"])

        # Unilateral indemnity covering breach of contract
        high_risk_text = (
            "Vendor shall defend, indemnify, and hold harmless Customer from any claims arising "
            "out of Vendor's breach of this agreement or any representation."
        )
        rep_high = contract_differ.detect_indemnity_deviations(high_risk_text)
        self.assertEqual(rep_high["risk_level"], "high")
        codes = [d["code"] for d in rep_high["deviations"]]
        self.assertIn("unilateral_indemnity", codes)
        self.assertIn("indemnity_extends_to_breach_of_contract", codes)

    def test_diff_against_playbook(self) -> None:
        contract_text = self.v1_path.read_text(encoding="utf-8-sig")
        report = contract_differ.diff_against_playbook(contract_text)
        self.assertTrue(report["ok"])
        self.assertGreater(report["clause_count"], 5)
        self.assertIn("contract_risk", report)
        self.assertIn("comparisons", report)
        self.assertGreater(len(report["comparisons"]), 0)

    def test_diff_contracts_material_shifts(self) -> None:
        v1_text = self.v1_path.read_text(encoding="utf-8-sig")
        v2_text = self.v2_path.read_text(encoding="utf-8-sig")
        report = contract_differ.diff_contracts(
            v1_text, v2_text, left_name="v1", right_name="v2"
        )
        self.assertTrue(report["ok"])
        self.assertIn("limitation_of_liability", report["changed_labels"])
        self.assertIn("sla_credits", report["changed_labels"])

    def test_cli_execution_options(self) -> None:
        # Dry run
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = contract_differ.main(["--dry-run"])
        self.assertEqual(code, 0)

        # Extract with json
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = contract_differ.main(["--extract", str(self.v1_path), "--json"])
        self.assertEqual(code, 0)
        data = json.loads(stdout.getvalue())
        self.assertTrue(data["ok"])

        # Playbook diff
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = contract_differ.main(
                ["--playbook", "--left", str(self.v1_path), "--json"]
            )
        self.assertEqual(code, 0)
        data = json.loads(stdout.getvalue())
        self.assertIn("contract_risk", data)

        # Left and Right diff
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = contract_differ.main(
                ["--left", str(self.v1_path), "--right", str(self.v2_path), "--json"]
            )
        self.assertEqual(code, 0)

        # Missing args error
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            code = contract_differ.main([])
        self.assertEqual(code, 2)

    def test_cli_file_not_found_handling(self) -> None:
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            code = contract_differ.main(["--extract", "nonexistent_contract.md"])
        self.assertEqual(code, 2)
        self.assertIn("error:", stderr.getvalue().lower())

        stderr2 = io.StringIO()
        with redirect_stderr(stderr2):
            code2 = contract_differ.main(
                ["--left", "missing1.md", "--right", "missing2.md"]
            )
        self.assertEqual(code2, 2)
        self.assertIn("error:", stderr2.getvalue().lower())


if __name__ == "__main__":
    unittest.main()
