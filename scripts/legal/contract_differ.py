"""Diff and extract clauses from synthetic contract fixtures.

tags: [legal, contracts, diff]
routing_hints: [redline, clause-extraction, msa, nvca]

Clause labels are harness-invented taxonomy, not a WorldCC scrape.
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


def advisory_envelope(payload: dict[str, Any]) -> dict[str, Any]:
    out = dict(payload)
    out["advisory"] = ADVISORY_STAMP
    out["not_legal_advice"] = True
    out["taxonomy"] = "synthetic-harness-labels"
    return out


def _label_blob(blob: str) -> str:
    lowered = blob.lower()
    for label, needles in TAXONOMY:
        if any(needle in lowered for needle in needles):
            return label
    return "other"


def classify_heading(heading: str, body: str) -> str:
    heading_hit = _label_blob(heading)
    if heading_hit != "other":
        return heading_hit
    return _label_blob(body)


def _skip_line(stripped: str) -> bool:
    if not stripped:
        return False
    if stripped.startswith("<!--") or "ADVISORY WORK PRODUCT" in stripped:
        return True
    if stripped.startswith("# ") and not stripped.startswith("## "):
        return True
    return False


def extract_clauses(text: str) -> list[dict[str, Any]]:
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
    parts = [f"<!-- {ADVISORY_STAMP} -->", ""]
    for clause in clauses:
        parts.append(f"## {clause['heading']}")
        parts.append("")
        parts.append(clause["body"])
        parts.append("")
    return "\n".join(parts).strip() + "\n"


def round_trip(text: str) -> dict[str, Any]:
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


def diff_contracts(left_text: str, right_text: str, *, left_name: str, right_name: str) -> dict[str, Any]:
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
        changes.append(
            {
                "label": label,
                "left_headings": [c["heading"] for c in left_by_label.get(label, [])],
                "right_headings": [c["heading"] for c in right_by_label.get(label, [])],
                "unified_diff": diff,
            }
        )
    return advisory_envelope(
        {
            "ok": True,
            "left_clause_count": len(left),
            "right_clause_count": len(right),
            "changed_labels": [c["label"] for c in changes],
            "changes": changes,
        }
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--extract", type=Path, help="Extract clauses from one contract")
    parser.add_argument("--left", type=Path, help="Left/base contract for diff")
    parser.add_argument("--right", type=Path, help="Right/updated contract for diff")
    parser.add_argument("--round-trip", dest="round_trip_path", type=Path, help="Round-trip a contract fixture")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--dry-run", action="store_true", help="Round-trip bundled fixtures")
    args = parser.parse_args(argv)

    if args.dry_run and not (args.extract or args.left or args.round_trip_path):
        reports = []
        ok = True
        for path in sorted(FIXTURE_DIR.glob("*.md")):
            report = round_trip(path.read_text(encoding="utf-8-sig"))
            report["file"] = path.name
            reports.append(report)
            ok = ok and bool(report.get("ok"))
        payload = advisory_envelope({"ok": ok, "fixtures": reports})
        print(json.dumps(payload, indent=2))
        return 0 if ok else 1

    if args.round_trip_path:
        report = round_trip(args.round_trip_path.read_text(encoding="utf-8-sig"))
    elif args.left and args.right:
        report = diff_contracts(
            args.left.read_text(encoding="utf-8-sig"),
            args.right.read_text(encoding="utf-8-sig"),
            left_name=args.left.name,
            right_name=args.right.name,
        )
    elif args.extract:
        clauses = extract_clauses(args.extract.read_text(encoding="utf-8-sig"))
        report = advisory_envelope({"ok": True, "clauses": clauses})
    else:
        print("error: pass --extract, --left/--right, --round-trip, or --dry-run", file=sys.stderr)
        return 2

    print(json.dumps(report, indent=2) if args.json or args.dry_run else json.dumps(report, indent=2))
    return 0 if report.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
