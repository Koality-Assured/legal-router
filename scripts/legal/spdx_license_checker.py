"""Scan SPDX / CycloneDX SBOMs for copyleft heuristics.

tags: [legal, licensing, spdx, cyclonedx]
routing_hints: [sbom, copyleft, gpl, agpl]

Compatibility flags are heuristics, not a legal opinion. Advisory only.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

_LIB = Path(__file__).resolve().parents[1] / "_lib"
sys.path.insert(0, str(_LIB))
from paths import REPO_ROOT as ROOT  # noqa: E402

ADVISORY_STAMP = "ADVISORY WORK PRODUCT - REQUIRES LICENSED ATTORNEY REVIEW"
FIXTURE_DIR = Path(__file__).resolve().parent / "fixtures" / "sbom"

BARE_GNU = {"GPL-2.0", "GPL-3.0", "AGPL-3.0", "LGPL-2.1", "LGPL-3.0"}
STRONG_COPYLEFT = {
    "GPL-2.0-only",
    "GPL-2.0-or-later",
    "GPL-3.0-only",
    "GPL-3.0-or-later",
    "AGPL-3.0-only",
    "AGPL-3.0-or-later",
}
WEAK_COPYLEFT = {
    "LGPL-2.1-only",
    "LGPL-2.1-or-later",
    "LGPL-3.0-only",
    "LGPL-3.0-or-later",
    "MPL-2.0",
}
PERMISSIVE = {"MIT", "BSD-2-Clause", "BSD-3-Clause", "Apache-2.0", "ISC", "0BSD", "Unlicense"}
PROPRIETARY_MARKERS = ("licenseref-proprietary", "proprietary", "commercial", "unlicensed", "closed")
ID_RE = re.compile(r"[A-Za-z0-9.+-]+")


def advisory_envelope(payload: dict[str, Any]) -> dict[str, Any]:
    out = dict(payload)
    out["advisory"] = ADVISORY_STAMP
    out["not_legal_advice"] = True
    out["heuristic_only"] = True
    return out


def tokenize_expression(expr: str) -> list[str]:
    return [tok for tok in ID_RE.findall(expr) if tok.upper() not in {"AND", "OR", "WITH"}]


def normalize_gnu(license_id: str) -> tuple[str, str | None]:
    if license_id in BARE_GNU:
        return f"{license_id}-only", f"{license_id} is deprecated; SPDX requires -only or -or-later"
    return license_id, None


def classify_id(license_id: str) -> str:
    normalized, _ = normalize_gnu(license_id)
    lowered = normalized.lower()
    if normalized in STRONG_COPYLEFT or lowered.startswith("agpl-"):
        return "strong_copyleft"
    if normalized in WEAK_COPYLEFT:
        return "weak_copyleft"
    if normalized in PERMISSIVE:
        return "permissive"
    if any(marker in lowered for marker in PROPRIETARY_MARKERS):
        return "proprietary"
    return "other"


def analyze_expression(expr: str, *, package: str | None = None) -> dict[str, Any]:
    raw_ids = tokenize_expression(expr)
    notes: list[str] = []
    normalized_ids: list[str] = []
    for raw in raw_ids:
        normalized, note = normalize_gnu(raw)
        normalized_ids.append(normalized)
        if note:
            notes.append(note)
    families = {classify_id(item) for item in normalized_ids}
    flags: list[str] = []
    if "strong_copyleft" in families:
        flags.append("contains_strong_copyleft")
    if any(item.lower().startswith("agpl-") for item in normalized_ids):
        flags.append("network_copyleft_agpl")
    if re.search(r"\bAND\b", expr, re.I) and "strong_copyleft" in families and (
        "permissive" in families or "proprietary" in families
    ):
        flags.append("and_combines_copyleft_with_other")
    if "proprietary" in families and "strong_copyleft" in families:
        flags.append("proprietary_and_copyleft")
    return {
        "package": package,
        "expression": expr,
        "license_ids": normalized_ids,
        "families": sorted(families),
        "flags": flags,
        "notes": notes,
    }


def _spdx_packages(data: dict[str, Any]) -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    for pkg in data.get("packages") or []:
        name = pkg.get("name") or pkg.get("SPDXID") or "unknown"
        expr = pkg.get("licenseDeclared") or pkg.get("licenseConcluded") or pkg.get("license")
        if expr:
            found.append((str(name), str(expr)))
    for pkg in data.get("packages") or []:
        for attr in pkg.get("hasConcludedLicense") or []:
            expr = attr if isinstance(attr, str) else attr.get("license")
            if expr:
                found.append((str(pkg.get("name") or "unknown"), str(expr)))
    if not found and isinstance(data.get("licenseDeclared"), str):
        found.append((str(data.get("name") or "document"), data["licenseDeclared"]))
    return found


def _cyclonedx_components(data: dict[str, Any]) -> list[tuple[str, str]]:
    found: list[tuple[str, str]] = []
    for component in data.get("components") or []:
        name = component.get("name") or "unknown"
        licenses = component.get("licenses") or []
        for entry in licenses:
            license_obj = entry.get("license") if isinstance(entry, dict) else None
            if isinstance(license_obj, dict):
                expr = license_obj.get("id") or license_obj.get("name") or license_obj.get("expression")
            elif isinstance(entry, dict):
                expr = entry.get("expression")
            else:
                expr = None
            if expr:
                found.append((str(name), str(expr)))
    return found


def scan_document(data: dict[str, Any], *, source: str) -> dict[str, Any]:
    if data.get("bomFormat") == "CycloneDX" or "components" in data and "packages" not in data:
        pairs = _cyclonedx_components(data)
        fmt = "cyclonedx"
    else:
        pairs = _spdx_packages(data)
        fmt = "spdx"
    findings = [analyze_expression(expr, package=name) for name, expr in pairs]
    flags = sorted({flag for item in findings for flag in item["flags"]})
    return advisory_envelope(
        {
            "ok": True,
            "source": source,
            "format": fmt,
            "package_count": len(findings),
            "flags": flags,
            "findings": findings,
        }
    )


def scan_path(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} is not a JSON object")
    return scan_document(data, source=path.as_posix())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sbom", type=Path, help="SPDX JSON or CycloneDX bom.json")
    parser.add_argument("--expression", help="Scan a single SPDX license expression")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--dry-run", action="store_true", help="Scan bundled fixtures")
    args = parser.parse_args(argv)

    if args.expression:
        report = advisory_envelope({"ok": True, "findings": [analyze_expression(args.expression)]})
    elif args.dry_run and not args.sbom:
        reports = [scan_path(path) for path in sorted(FIXTURE_DIR.glob("*.json"))]
        report = advisory_envelope({"ok": all(r.get("ok") for r in reports), "fixtures": reports})
    elif args.sbom:
        report = scan_path(args.sbom)
    else:
        print("error: pass --sbom, --expression, or --dry-run", file=sys.stderr)
        return 2

    print(json.dumps(report, indent=2) if args.json or args.dry_run else json.dumps(report, indent=2))
    return 0 if report.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
