"""Diff and extract clauses from synthetic contract fixtures and evaluate playbook deviations.

tags: [legal, contracts, diff]
routing_hints: [redline, clause-extraction, msa, nvca, playbook-deviations]

Clause labels are harness-invented taxonomy, not a WorldCC scrape.
Performs structural clause diffing against standard contract playbook clauses,
detecting material liability, indemnity, and governing law deviations.
Outputs are advisory only and require licensed attorney review.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from difflib import unified_diff
from pathlib import Path
from typing import Any

_LIB = Path(__file__).resolve().parents[1] / "_lib"
sys.path.insert(0, str(_LIB))
from paths import REPO_ROOT as ROOT  # noqa: E402

ADVISORY_STAMP = "ADVISORY WORK PRODUCT - REQUIRES LICENSED ATTORNEY REVIEW"
FIXTURE_DIR = Path(__file__).resolve().parent / "fixtures" / "contracts"

HEADING_RE = re.compile(r"^(#{2,3}|Article\s+\d+[.:]?|Section\s+\d+[.:]?)\s+(.*)$", re.IGNORECASE)
NUMBERED_RE = re.compile(r"^(\d+(?:\.\d+)*)[.)]\s+(.*)$")

TAXONOMY: list[tuple[str, tuple[str, ...]]] = [
    ("indemnity", ("indemnif", "hold harmless", "defend")),
    ("limitation_of_liability", ("limitation of liability", "liability cap", "consequential damage", "liability shall not exceed")),
    ("governing_law", ("governing law", "jurisdiction", "venue", "choice of law")),
    ("ip_assignment", ("intellectual property", "work made for hire", "assignment of", "moral rights")),
    ("confidentiality", ("confidential", "non-disclosure", "nondisclosure")),
    ("termination", ("terminat", "expiration of this")),
    ("sla_credits", ("service level", "service credit", "uptime", "availability credit")),
    ("data_protection", ("personal data", "gdpr", "data processing", "data protection", "hipaa", "phi")),
    ("insurance", ("insurance", "cyber liability", "policy limits")),
    ("payment", ("fees", "invoices", "payment terms", "late interest")),
    ("definitions", ("definitions", "means", "interpreted")),
    ("preamble", ("preamble", "this agreement", "whereas", "parties")),
]

# Standard balanced commercial contract playbook clauses
STANDARD_PLAYBOOK: dict[str, str] = {
    "limitation_of_liability": (
        "Except for indemnification obligations under this Agreement, gross negligence, "
        "or willful misconduct, neither party shall be liable to the other for any indirect, "
        "incidental, consequential, special, or punitive damages. Each party's aggregate "
        "liability arising out of or relating to this Agreement shall be limited to the total "
        "fees paid or payable by Customer in the twelve (12) months preceding the claim."
    ),
    "indemnity": (
        "Provider shall defend, indemnify, and hold harmless Customer against third-party "
        "claims alleging that the Services infringe any intellectual property right, provided "
        "Customer gives prompt written notice, sole control of defense, and reasonable cooperation. "
        "Customer shall defend, indemnify, and hold harmless Provider against third-party claims "
        "arising from Customer Data. Neither party shall settle any claim admitting liability "
        "without the other party's prior written consent."
    ),
    "governing_law": (
        "This Agreement shall be governed by and construed in accordance with the laws of the "
        "State of Delaware, without regard to conflict of laws principles. The parties consent "
        "to the exclusive jurisdiction of the state and federal courts located in Delaware."
    ),
    "confidentiality": (
        "Each party agrees to maintain the other party's Confidential Information in strict "
        "confidence and protect it with the same degree of care it uses for its own confidential "
        "information, but no less than reasonable care, for three (3) years from disclosure."
    ),
    "ip_assignment": (
        "Provider retains all intellectual property rights in the Services and Deliverables. "
        "Customer retains all rights, title, and interest in Customer Data. Neither party "
        "acquires any rights other than those expressly granted herein."
    ),
    "sla_credits": (
        "Provider warrants 99.9% monthly availability for the Services. If Provider fails to meet "
        "the availability target, Customer shall be eligible for service credits as the sole and "
        "exclusive remedy for service downtime."
    ),
    "termination": (
        "Either party may terminate this Agreement for cause upon thirty (30) days' prior written "
        "notice if the other party materially breaches this Agreement and fails to cure such breach "
        "within thirty (30) days."
    ),
    "data_protection": (
        "Each party shall comply with all applicable privacy and data protection laws and implement "
        "reasonable technical and organizational measures to safeguard personal data."
    ),
}


def advisory_envelope(payload: dict[str, Any]) -> dict[str, Any]:
    """Wrap output dictionary with the required non-legal-advice advisory stamp."""
    out = dict(payload)
    out["advisory"] = ADVISORY_STAMP
    out["not_legal_advice"] = True
    out["taxonomy"] = "synthetic-harness-labels"
    return out


def _label_blob(blob: str) -> str:
    """Classify arbitrary text segment against synthetic contract clause taxonomy."""
    lowered = blob.lower()
    for label, needles in TAXONOMY:
        if any(needle in lowered for needle in needles):
            return label
    return "other"


def classify_heading(heading: str, body: str) -> str:
    """Classify a section by inspecting heading first, falling back to body content."""
    heading_hit = _label_blob(heading)
    if heading_hit != "other":
        return heading_hit
    return _label_blob(body)


def _skip_line(stripped: str) -> bool:
    """Skip HTML comments, advisory headers, or top-level Markdown title lines."""
    if not stripped:
        return False
    if stripped.startswith("<!--") or "ADVISORY WORK PRODUCT" in stripped:
        return True
    if stripped.startswith("# ") and not stripped.startswith("## "):
        return True
    return False


def extract_clauses(text: str) -> list[dict[str, Any]]:
    """Extract structural clauses from markdown or numbered text."""
    lines = text.replace("\r\n", "\n").split("\n")
    clauses: list[dict[str, Any]] = []
    current_heading = "Preamble"
    current_body: list[str] = []

    def flush() -> None:
        body = "\n".join(current_body).strip()
        heading = current_heading.strip() or "Preamble"
        if not body:
            return
        clauses.append(
            {
                "id": f"c{len(clauses) + 1:02d}",
                "heading": heading,
                "label": classify_heading(heading, body),
                "body": body,
            }
        )

    for line in lines:
        stripped = line.strip()
        if _skip_line(stripped):
            continue
        heading_match = HEADING_RE.match(stripped)
        numbered_match = NUMBERED_RE.match(stripped) if heading_match is None else None
        if heading_match:
            flush()
            current_heading = heading_match.group(2).strip()
            current_body = []
        elif numbered_match and len(numbered_match.group(2)) < 80:
            flush()
            current_heading = numbered_match.group(0).strip()
            current_body = [numbered_match.group(2).strip()]
        else:
            current_body.append(line)
    flush()
    return clauses


def canonical_markdown(clauses: list[dict[str, Any]]) -> str:
    """Render extracted clauses back into canonical markdown with advisory banner."""
    parts = [f"<!-- {ADVISORY_STAMP} -->", ""]
    for clause in clauses:
        parts.append(f"## {clause['heading']}")
        parts.append("")
        parts.append(clause["body"])
        parts.append("")
    return "\n".join(parts).strip() + "\n"


def round_trip(text: str) -> dict[str, Any]:
    """Test extract -> canonical_markdown -> extract round-trip idempotency."""
    first = extract_clauses(text)
    rendered = canonical_markdown(first)
    second = extract_clauses(rendered)
    headings_first = [c["heading"] for c in first]
    headings_second = [c["heading"] for c in second]
    labels_first = [c["label"] for c in first]
    labels_second = [c["label"] for c in second]
    ok = headings_first == headings_second and labels_first == labels_second and len(first) > 0
    return advisory_envelope(
        {
            "ok": ok,
            "clause_count": len(first),
            "headings": headings_first,
            "labels": labels_first,
            "mismatch": None
            if ok
            else {"headings": headings_second, "labels": labels_second},
        }
    )


def detect_liability_deviations(clause_text: str) -> dict[str, Any]:
    """Detect high-risk deviations in Limitation of Liability clauses."""
    lowered = clause_text.lower()
    deviations: list[dict[str, Any]] = []

    # 1. Consequential damages waiver check
    consequential_needles = ("consequential", "indirect", "punitive", "special", "incidental")
    has_consequential_waiver = any(needle in lowered for needle in consequential_needles)
    if not has_consequential_waiver:
        deviations.append(
            {
                "code": "missing_consequential_damages_waiver",
                "severity": "high",
                "description": (
                    "Clause lacks an express waiver of indirect, consequential, or punitive damages. "
                    "This exposes the enterprise to open-ended lost profit and business interruption claims."
                ),
                "recommendation": "Insert mutual waiver of indirect, special, and consequential damages.",
            }
        )

    # 2. Uncapped liability risk check
    uncapped_markers = (
        "unlimited liability",
        "without limitation",
        "no limitation shall apply",
        "shall not be limited",
    )
    is_uncapped = any(marker in lowered for marker in uncapped_markers)
    if is_uncapped:
        deviations.append(
            {
                "code": "uncapped_liability_risk",
                "severity": "critical",
                "description": "Language indicates potential uncapped or unconstrained financial liability.",
                "recommendation": "Establish a clear aggregate monetary liability cap (e.g. 12 months fees).",
            }
        )

    # 3. Aggregate liability cap presence
    cap_markers = ("aggregate liability", "maximum liability", "liability shall not exceed", "total fees paid")
    has_aggregate_cap = any(marker in lowered for marker in cap_markers)
    if not has_aggregate_cap and not is_uncapped:
        deviations.append(
            {
                "code": "missing_aggregate_liability_cap",
                "severity": "critical",
                "description": "No explicit aggregate monetary limitation of liability cap was detected.",
                "recommendation": "Add a standard 12-month fees paid or payable cap.",
            }
        )

    # 4. Mutuality check
    unilateral_customer = "customer's liability shall" in lowered and "provider's liability" not in lowered
    unilateral_provider = "provider's liability shall" in lowered and "customer's liability" not in lowered
    is_mutual = not (unilateral_customer or unilateral_provider)
    if not is_mutual:
        deviations.append(
            {
                "code": "unilateral_liability_cap",
                "severity": "high",
                "description": "Liability limitation is one-sided rather than mutual.",
                "recommendation": "Make the liability limitation reciprocal for both parties.",
            }
        )

    # 5. Carve-outs analysis
    carve_out_needles = [
        "indemnif",
        "gross negligence",
        "willful misconduct",
        "confidential",
        "data protection",
        "ip infringement",
    ]
    carve_outs_detected = [needle for needle in carve_out_needles if needle in lowered]

    risk_level = "low"
    if any(d["severity"] == "critical" for d in deviations):
        risk_level = "critical"
    elif any(d["severity"] == "high" for d in deviations):
        risk_level = "high"
    elif deviations:
        risk_level = "medium"

    return {
        "clause_label": "limitation_of_liability",
        "risk_level": risk_level,
        "has_consequential_waiver": has_consequential_waiver,
        "has_aggregate_cap": has_aggregate_cap,
        "is_mutual": is_mutual,
        "carve_outs_detected": carve_outs_detected,
        "deviations": deviations,
    }


def detect_indemnity_deviations(clause_text: str) -> dict[str, Any]:
    """Detect high-risk deviations in Indemnification clauses."""
    lowered = clause_text.lower()
    deviations: list[dict[str, Any]] = []

    # 1. Mutuality check
    has_provider_indemnity = any(p in lowered for p in ("provider shall defend", "vendor shall defend", "provider shall indemnify"))
    has_customer_indemnity = any(c in lowered for c in ("customer shall defend", "customer shall indemnify", "client shall defend"))
    is_mutual = has_provider_indemnity and has_customer_indemnity
    if (has_provider_indemnity and not has_customer_indemnity) or (has_customer_indemnity and not has_provider_indemnity):
        deviations.append(
            {
                "code": "unilateral_indemnity",
                "severity": "high",
                "description": "Indemnification obligations are unilateral rather than balanced between parties.",
                "recommendation": "Structure reciprocal indemnity (Provider for IP infringement, Customer for Customer Data).",
            }
        )

    # 2. Scope: IP infringement vs general breach of contract
    covers_ip = any(needle in lowered for needle in ("intellectual property", "infring", "patent", "copyright"))
    covers_breach = any(needle in lowered for needle in ("breach of this agreement", "breach of any representation", "breach of warranty"))
    if covers_breach:
        deviations.append(
            {
                "code": "indemnity_extends_to_breach_of_contract",
                "severity": "high",
                "description": (
                    "Indemnity covers general breaches of contract. In many jurisdictions, this can "
                    "bypass the limitation of liability cap and convert contract claims into indemnity claims."
                ),
                "recommendation": "Limit indemnity to specific third-party risks (IP infringement, gross negligence, bodily injury).",
            }
        )

    # 3. Procedural defense protections (Notice, Defense Control, Settlement Consent)
    has_prompt_notice = any(n in lowered for n in ("prompt written notice", "prompt notice", "promptly notify"))
    has_sole_control = any(c in lowered for c in ("sole control", "exclusive control", "sole right to defend", "control of defense"))
    has_settlement_consent = "settle" in lowered and "consent" in lowered

    procedural = {
        "prompt_notice": has_prompt_notice,
        "sole_control_defense": has_sole_control,
        "settlement_consent": has_settlement_consent,
    }

    if not has_prompt_notice:
        deviations.append(
            {
                "code": "missing_prompt_notice_requirement",
                "severity": "medium",
                "description": "Lacks requirement for prompt written notice of indemnified third-party claims.",
                "recommendation": "Condition indemnification on prompt written notice from the indemnified party.",
            }
        )
    if not has_sole_control:
        deviations.append(
            {
                "code": "missing_sole_control_of_defense",
                "severity": "medium",
                "description": "Indemnifying party is not explicitly granted sole control over defense and counsel selection.",
                "recommendation": "Include clause granting indemnitor sole control over defense of third-party claims.",
            }
        )
    if not has_settlement_consent:
        deviations.append(
            {
                "code": "missing_settlement_consent_restriction",
                "severity": "medium",
                "description": "No restriction preventing settlements that admit fault without consent.",
                "recommendation": "Require prior written consent for settlements admitting liability or imposing monetary duties.",
            }
        )

    risk_level = "low"
    if any(d["severity"] == "critical" for d in deviations):
        risk_level = "critical"
    elif any(d["severity"] == "high" for d in deviations):
        risk_level = "high"
    elif deviations:
        risk_level = "medium"

    return {
        "clause_label": "indemnity",
        "risk_level": risk_level,
        "is_mutual": is_mutual,
        "covers_ip_infringement": covers_ip,
        "covers_breach_of_contract": covers_breach,
        "procedural_protections": procedural,
        "deviations": deviations,
    }


def detect_clause_deviations(label: str, clause_text: str) -> dict[str, Any]:
    """Route clause to specific deviation detector based on taxonomy label."""
    if label == "limitation_of_liability":
        return detect_liability_deviations(clause_text)
    if label == "indemnity":
        return detect_indemnity_deviations(clause_text)
    return {
        "clause_label": label,
        "risk_level": "low",
        "deviations": [],
    }


def diff_against_playbook(
    contract_text: str,
    playbook: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Diff all extracted contract clauses against standard playbook clauses."""
    active_playbook = playbook or STANDARD_PLAYBOOK
    clauses = extract_clauses(contract_text)
    clauses_by_label: dict[str, list[dict[str, Any]]] = {}
    for clause in clauses:
        clauses_by_label.setdefault(clause["label"], []).append(clause)

    comparisons: list[dict[str, Any]] = []
    overall_deviations: list[dict[str, Any]] = []

    for label, playbook_text in active_playbook.items():
        matched_clauses = clauses_by_label.get(label, [])
        if not matched_clauses:
            missing_dev = {
                "code": f"missing_{label}_clause",
                "severity": "high" if label in {"limitation_of_liability", "indemnity"} else "medium",
                "description": f"Standard playbook clause for '{label}' was not found in the contract.",
                "recommendation": f"Add standard '{label}' clause from contract playbook.",
            }
            comparisons.append(
                {
                    "label": label,
                    "present_in_contract": False,
                    "contract_text": "",
                    "playbook_text": playbook_text,
                    "deviations": [missing_dev],
                    "diff": [],
                }
            )
            overall_deviations.append(missing_dev)
            continue

        c_body = "\n\n".join(c["body"] for c in matched_clauses)
        diff = list(
            unified_diff(
                playbook_text.splitlines(),
                c_body.splitlines(),
                fromfile=f"playbook:{label}",
                tofile=f"contract:{label}",
                lineterm="",
            )
        )
        dev_report = detect_clause_deviations(label, c_body)
        comparisons.append(
            {
                "label": label,
                "present_in_contract": True,
                "contract_headings": [c["heading"] for c in matched_clauses],
                "deviations": dev_report.get("deviations", []),
                "risk_level": dev_report.get("risk_level", "low"),
                "diff": diff,
            }
        )
        overall_deviations.extend(dev_report.get("deviations", []))

    critical_count = sum(1 for d in overall_deviations if d.get("severity") == "critical")
    high_count = sum(1 for d in overall_deviations if d.get("severity") == "high")
    contract_risk = "low"
    if critical_count > 0:
        contract_risk = "critical"
    elif high_count > 0:
        contract_risk = "high"
    elif overall_deviations:
        contract_risk = "medium"

    return advisory_envelope(
        {
            "ok": True,
            "contract_risk": contract_risk,
            "total_deviations": len(overall_deviations),
            "critical_count": critical_count,
            "high_count": high_count,
            "clause_count": len(clauses),
            "playbook_clauses_evaluated": len(active_playbook),
            "comparisons": comparisons,
            "all_deviations": overall_deviations,
        }
    )


def diff_contracts(
    left_text: str,
    right_text: str,
    *,
    left_name: str,
    right_name: str,
) -> dict[str, Any]:
    """Diff two contracts clause-by-clause and analyze liability/indemnity shifts."""
    left = extract_clauses(left_text)
    right = extract_clauses(right_text)
    left_by_label: dict[str, list[dict[str, Any]]] = {}
    right_by_label: dict[str, list[dict[str, Any]]] = {}
    for clause in left:
        left_by_label.setdefault(clause["label"], []).append(clause)
    for clause in right:
        right_by_label.setdefault(clause["label"], []).append(clause)
    labels = sorted(set(left_by_label) | set(right_by_label))
    changes: list[dict[str, Any]] = []
    material_shifts: list[dict[str, Any]] = []

    for label in labels:
        l_body = "\n\n".join(c["body"] for c in left_by_label.get(label, []))
        r_body = "\n\n".join(c["body"] for c in right_by_label.get(label, []))
        if l_body == r_body:
            continue
        diff = list(
            unified_diff(
                l_body.splitlines(),
                r_body.splitlines(),
                fromfile=f"{left_name}:{label}",
                tofile=f"{right_name}:{label}",
                lineterm="",
            )
        )

        left_dev = detect_clause_deviations(label, l_body) if l_body else None
        right_dev = detect_clause_deviations(label, r_body) if r_body else None

        materiality = "low"
        if label in {"limitation_of_liability", "indemnity"}:
            materiality = "high"
        elif label in {"sla_credits", "confidentiality", "termination", "ip_assignment"}:
            materiality = "medium"

        # Check for specific material risk shifts between left and right
        if label == "limitation_of_liability" and left_dev and right_dev:
            if left_dev.get("has_consequential_waiver") and not right_dev.get("has_consequential_waiver"):
                material_shifts.append(
                    {
                        "label": label,
                        "type": "consequential_waiver_removed",
                        "severity": "high",
                        "description": "Consequential damages waiver was removed in the revised agreement.",
                    }
                )
            if not left_dev.get("deviations") and right_dev.get("deviations"):
                material_shifts.append(
                    {
                        "label": label,
                        "type": "new_liability_deviations",
                        "severity": "high",
                        "description": f"New liability deviations introduced in revised version: {[d['code'] for d in right_dev['deviations']]}",
                    }
                )

        if label == "indemnity" and left_dev and right_dev:
            if left_dev.get("is_mutual") and not right_dev.get("is_mutual"):
                material_shifts.append(
                    {
                        "label": label,
                        "type": "indemnity_made_unilateral",
                        "severity": "high",
                        "description": "Mutual indemnification was replaced with unilateral indemnity.",
                    }
                )

        changes.append(
            {
                "label": label,
                "materiality": materiality,
                "left_headings": [c["heading"] for c in left_by_label.get(label, [])],
                "right_headings": [c["heading"] for c in right_by_label.get(label, [])],
                "left_deviations": left_dev.get("deviations", []) if left_dev else [],
                "right_deviations": right_dev.get("deviations", []) if right_dev else [],
                "unified_diff": diff,
            }
        )

    return advisory_envelope(
        {
            "ok": True,
            "left_clause_count": len(left),
            "right_clause_count": len(right),
            "changed_labels": [c["label"] for c in changes],
            "material_shifts": material_shifts,
            "changes": changes,
        }
    )


def main(argv: list[str] | None = None) -> int:
    """CLI entrypoint for contract clause extraction, playbook diffing, and redlines."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--extract", type=Path, help="Extract clauses and check deviations for one contract")
    parser.add_argument("--left", type=Path, help="Left/base contract for diff")
    parser.add_argument("--right", type=Path, help="Right/updated contract for diff")
    parser.add_argument(
        "--playbook",
        action="store_true",
        help="Compare contract (--left or --extract) against standard contract playbook clauses",
    )
    parser.add_argument("--round-trip", dest="round_trip_path", type=Path, help="Round-trip a contract fixture")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--dry-run", action="store_true", help="Round-trip bundled fixtures and test playbook")
    args = parser.parse_args(argv)

    try:
        if args.dry_run and not (args.extract or args.left or args.round_trip_path):
            reports = []
            ok = True
            for path in sorted(FIXTURE_DIR.glob("*.md")):
                report = round_trip(path.read_text(encoding="utf-8-sig"))
                report["file"] = path.name
                reports.append(report)
                ok = ok and bool(report.get("ok"))
            # Also run playbook diff on first fixture
            first_fixture = next(FIXTURE_DIR.glob("*.md"), None)
            playbook_report = None
            if first_fixture:
                playbook_report = diff_against_playbook(first_fixture.read_text(encoding="utf-8-sig"))
            payload = advisory_envelope({"ok": ok, "fixtures": reports, "playbook_sample": playbook_report})
            print(json.dumps(payload, indent=2))
            return 0 if ok else 1

        if args.round_trip_path:
            report = round_trip(args.round_trip_path.read_text(encoding="utf-8-sig"))
        elif args.playbook:
            target_path = args.left or args.extract
            if not target_path:
                print("error: --playbook requires --left or --extract specifying the contract", file=sys.stderr)
                return 2
            report = diff_against_playbook(target_path.read_text(encoding="utf-8-sig"))
        elif args.left and args.right:
            report = diff_contracts(
                args.left.read_text(encoding="utf-8-sig"),
                args.right.read_text(encoding="utf-8-sig"),
                left_name=args.left.name,
                right_name=args.right.name,
            )
        elif args.extract:
            clauses = extract_clauses(args.extract.read_text(encoding="utf-8-sig"))
            deviations = [
                detect_clause_deviations(c["label"], c["body"])
                for c in clauses
                if c["label"] in {"limitation_of_liability", "indemnity"}
            ]
            report = advisory_envelope({"ok": True, "clauses": clauses, "deviations": deviations})
        else:
            print("error: pass --extract, --left/--right, --playbook, --round-trip, or --dry-run", file=sys.stderr)
            return 2
    except (FileNotFoundError, PermissionError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    print(json.dumps(report, indent=2))
    return 0 if report.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
