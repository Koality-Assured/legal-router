"""Scan SPDX / CycloneDX SBOMs and validate dependency license lists for copyleft heuristics.

tags: [legal, licensing, spdx, cyclonedx]
routing_hints: [sbom, copyleft, gpl, agpl, compatibility-matrix]

Compatibility flags are heuristics, not a legal opinion. Advisory only.
Validates dependency license lists against canonical SPDX license lists,
evaluates compatibility matrices between licenses, and flags copyleft risks.
"""

from __future__ import annotations

import argparse
import itertools
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

# Canonical SPDX License Identifiers (SPDX 3.20+ subset)
PERMISSIVE_LICENSES = {
    "0BSD",
    "AFL-3.0",
    "Apache-1.0",
    "Apache-1.1",
    "Apache-2.0",
    "Artistic-2.0",
    "BSD-1-Clause",
    "BSD-2-Clause",
    "BSD-2-Clause-Patent",
    "BSD-3-Clause",
    "BSD-3-Clause-Clear",
    "BSD-4-Clause",
    "BlueOak-1.0.0",
    "CC0-1.0",
    "CC-BY-3.0",
    "CC-BY-4.0",
    "ISC",
    "MIT",
    "MIT-0",
    "MS-PL",
    "PostgreSQL",
    "Python-2.0",
    "Unlicense",
    "WTFPL",
    "Zlib",
}

WEAK_COPYLEFT_LICENSES = {
    "CDDL-1.0",
    "CDDL-1.1",
    "CPL-1.0",
    "EPL-1.0",
    "EPL-2.0",
    "EUPL-1.1",
    "EUPL-1.2",
    "IPL-1.0",
    "LGPL-2.0-only",
    "LGPL-2.0-or-later",
    "LGPL-2.1-only",
    "LGPL-2.1-or-later",
    "LGPL-3.0-only",
    "LGPL-3.0-or-later",
    "MPL-1.1",
    "MPL-2.0",
    "MS-RL",
}

STRONG_COPYLEFT_LICENSES = {
    "GPL-1.0-only",
    "GPL-1.0-or-later",
    "GPL-2.0-only",
    "GPL-2.0-or-later",
    "GPL-3.0-only",
    "GPL-3.0-or-later",
    "OSL-1.0",
    "OSL-2.0",
    "OSL-3.0",
    "SISSL",
}

NETWORK_COPYLEFT_LICENSES = {
    "AGPL-1.0-only",
    "AGPL-1.0-or-later",
    "AGPL-3.0-only",
    "AGPL-3.0-or-later",
    "SSPL-1.0",
}

BARE_GNU = {
    "GPL-1.0",
    "GPL-2.0",
    "GPL-3.0",
    "LGPL-2.0",
    "LGPL-2.1",
    "LGPL-3.0",
    "AGPL-1.0",
    "AGPL-3.0",
}

CANONICAL_SPDX_IDS = (
    PERMISSIVE_LICENSES
    | WEAK_COPYLEFT_LICENSES
    | STRONG_COPYLEFT_LICENSES
    | NETWORK_COPYLEFT_LICENSES
)

PROPRIETARY_MARKERS = (
    "licenseref-proprietary",
    "proprietary",
    "commercial",
    "unlicensed",
    "closed",
)

ID_RE = re.compile(r"[A-Za-z0-9.+-]+")

# Known license incompatibility pairs with rationale and severity
KNOWN_INCOMPATIBILITIES: list[dict[str, Any]] = [
    {
        "pair": {"GPL-2.0-only", "Apache-2.0"},
        "severity": "high",
        "reason": (
            "Apache-2.0 contains patent termination provisions that GPLv2 treats as "
            "prohibited further restrictions under GPLv2 Section 6 (FSF position)."
        ),
    },
    {
        "pair": {"GPL-2.0-only", "GPL-3.0-only"},
        "severity": "critical",
        "reason": (
            "GPLv2-only cannot be upgraded to GPLv3, and GPLv3 cannot be downgraded to GPLv2. "
            "Code under both cannot be linked into a single binary."
        ),
    },
    {
        "pair": {"GPL-2.0-only", "CDDL-1.0"},
        "severity": "high",
        "reason": "CDDL-1.0 and GPLv2 have mutually contradictory source distribution requirements.",
    },
    {
        "pair": {"GPL-3.0-only", "CDDL-1.0"},
        "severity": "high",
        "reason": "CDDL-1.0 choice of law and notice requirements conflict with GPLv3 terms.",
    },
    {
        "pair": {"GPL-2.0-only", "EPL-1.0"},
        "severity": "high",
        "reason": "EPL-1.0 patent and choice of forum provisions conflict with GPLv2 Section 6.",
    },
]


def advisory_envelope(payload: dict[str, Any]) -> dict[str, Any]:
    """Wrap output dictionary with the required non-legal-advice advisory stamp."""
    out = dict(payload)
    out["advisory"] = ADVISORY_STAMP
    out["not_legal_advice"] = True
    out["heuristic_only"] = True
    return out


def tokenize_expression(expr: str) -> list[str]:
    """Extract individual license IDs from a compound SPDX license expression."""
    return [tok for tok in ID_RE.findall(expr) if tok.upper() not in {"AND", "OR", "WITH"}]


def normalize_gnu(license_id: str) -> tuple[str, str | None]:
    """Normalize deprecated bare GNU identifiers to SPDX standard -only format."""
    if license_id in BARE_GNU:
        return f"{license_id}-only", f"{license_id} is deprecated; SPDX requires -only or -or-later"
    return license_id, None


def classify_id(license_id: str) -> str:
    """Classify a license ID into its legal/risk family."""
    normalized, _ = normalize_gnu(license_id)
    lowered = normalized.lower()
    if normalized in NETWORK_COPYLEFT_LICENSES or lowered.startswith("agpl-"):
        return "strong_copyleft"  # Backwards-compatible family classification
    if normalized in STRONG_COPYLEFT_LICENSES:
        return "strong_copyleft"
    if normalized in WEAK_COPYLEFT_LICENSES:
        return "weak_copyleft"
    if normalized in PERMISSIVE_LICENSES:
        return "permissive"
    if any(marker in lowered for marker in PROPRIETARY_MARKERS):
        return "proprietary"
    return "other"


def get_copyleft_category(license_id: str) -> str:
    """Return specific copyleft category: permissive, weak_copyleft, strong_copyleft, network_copyleft, proprietary, or unknown."""
    normalized, _ = normalize_gnu(license_id)
    lowered = normalized.lower()
    if normalized in NETWORK_COPYLEFT_LICENSES or lowered.startswith("agpl-") or lowered.startswith("sspl-"):
        return "network_copyleft"
    if normalized in STRONG_COPYLEFT_LICENSES or lowered.startswith("gpl-"):
        return "strong_copyleft"
    if normalized in WEAK_COPYLEFT_LICENSES or lowered.startswith("lgpl-") or lowered.startswith("mpl-"):
        return "weak_copyleft"
    if normalized in PERMISSIVE_LICENSES:
        return "permissive"
    if any(marker in lowered for marker in PROPRIETARY_MARKERS):
        return "proprietary"
    return "unknown"


def validate_license_id(license_id: str) -> dict[str, Any]:
    """Validate an individual license identifier against the official SPDX registry."""
    normalized, note = normalize_gnu(license_id)
    is_valid = normalized in CANONICAL_SPDX_IDS
    category = get_copyleft_category(normalized)
    family = classify_id(normalized)
    is_deprecated = license_id in BARE_GNU
    is_custom = license_id.lower().startswith("licenseref-")

    return {
        "raw_id": license_id,
        "normalized_id": normalized,
        "is_valid_spdx": is_valid,
        "is_deprecated": is_deprecated,
        "is_custom": is_custom,
        "deprecation_note": note,
        "copyleft_category": category,
        "family": family,
    }


def evaluate_compatibility(license_ids: list[str]) -> dict[str, Any]:
    """Evaluate pairwise compatibility matrix between a set of license identifiers."""
    normalized_list = [normalize_gnu(lid)[0] for lid in license_ids]
    distinct_ids = sorted(set(normalized_list))

    conflicts: list[dict[str, Any]] = []
    highest_severity = "none"

    # 1. Check known specific incompatibility pairs
    for item in KNOWN_INCOMPATIBILITIES:
        pair_set = item["pair"]
        if pair_set.issubset(set(distinct_ids)):
            p_list = sorted(pair_set)
            conflicts.append(
                {
                    "licenses": p_list,
                    "severity": item["severity"],
                    "reason": item["reason"],
                }
            )
            if item["severity"] == "critical":
                highest_severity = "critical"
            elif highest_severity != "critical" and item["severity"] == "high":
                highest_severity = "high"

    # 2. Check general category incompatibilities (Proprietary + Copyleft)
    has_proprietary = any(get_copyleft_category(lid) == "proprietary" for lid in distinct_ids)
    strong_copyleft_items = [lid for lid in distinct_ids if get_copyleft_category(lid) == "strong_copyleft"]
    network_copyleft_items = [lid for lid in distinct_ids if get_copyleft_category(lid) == "network_copyleft"]

    if has_proprietary and network_copyleft_items:
        conflicts.append(
            {
                "licenses": ["proprietary", *network_copyleft_items],
                "severity": "critical",
                "reason": (
                    "Combining proprietary code with network copyleft (AGPL/SSPL) requires "
                    "source code disclosure over network services."
                ),
            }
        )
        highest_severity = "critical"
    elif has_proprietary and strong_copyleft_items:
        conflicts.append(
            {
                "licenses": ["proprietary", *strong_copyleft_items],
                "severity": "high",
                "reason": (
                    "Combining proprietary code with strong copyleft (GPL) requires "
                    "entire combined work to be licensed under copyleft upon distribution."
                ),
            }
        )
        if highest_severity != "critical":
            highest_severity = "high"

    categories = [get_copyleft_category(lid) for lid in distinct_ids]
    copyleft_summary = {
        "permissive_count": sum(1 for c in categories if c == "permissive"),
        "weak_copyleft_count": sum(1 for c in categories if c == "weak_copyleft"),
        "strong_copyleft_count": sum(1 for c in categories if c == "strong_copyleft"),
        "network_copyleft_count": sum(1 for c in categories if c == "network_copyleft"),
        "proprietary_count": sum(1 for c in categories if c == "proprietary"),
        "unknown_count": sum(1 for c in categories if c == "unknown"),
    }

    recommendations: list[str] = []
    if highest_severity == "critical":
        recommendations.append("Immediate legal escalation required: severe license conflict or viral copyleft risk.")
    elif highest_severity == "high":
        recommendations.append("Legal review required: incompatible license combination in distributed components.")
    elif copyleft_summary["weak_copyleft_count"] > 0:
        recommendations.append("Ensure weak copyleft components (e.g. LGPL) are dynamically linked to avoid derivative work claims.")
    else:
        recommendations.append("No copyleft conflicts detected; standard attribution notices required.")

    return {
        "compatible": len(conflicts) == 0,
        "conflict_count": len(conflicts),
        "conflicts": conflicts,
        "highest_severity": highest_severity,
        "copyleft_summary": copyleft_summary,
        "recommendations": recommendations,
    }


def validate_license_list(
    dependencies: list[str] | list[dict[str, Any]],
) -> dict[str, Any]:
    """Validate a list of dependency licenses against SPDX standards and evaluate compatibility."""
    entries: list[dict[str, Any]] = []
    all_raw_ids: list[str] = []

    for dep in dependencies:
        if isinstance(dep, str):
            pkg_name = "unnamed"
            expr = dep
        elif isinstance(dep, dict):
            pkg_name = dep.get("name") or dep.get("package") or "unnamed"
            expr = dep.get("license") or dep.get("licenseDeclared") or dep.get("id") or "UNKNOWN"
        else:
            continue

        raw_ids = tokenize_expression(expr)
        all_raw_ids.extend(raw_ids)
        validated_tokens = [validate_license_id(rid) for rid in raw_ids]
        analysis = analyze_expression(expr, package=pkg_name)

        entries.append(
            {
                "package": pkg_name,
                "expression": expr,
                "tokens": validated_tokens,
                "analysis": analysis,
            }
        )

    compatibility = evaluate_compatibility(all_raw_ids)

    valid_spdx_count = sum(
        1 for entry in entries for tok in entry["tokens"] if tok["is_valid_spdx"]
    )
    deprecated_count = sum(
        1 for entry in entries for tok in entry["tokens"] if tok["is_deprecated"]
    )
    custom_count = sum(
        1 for entry in entries for tok in entry["tokens"] if tok["is_custom"]
    )
    unknown_count = sum(
        1
        for entry in entries
        for tok in entry["tokens"]
        if not tok["is_valid_spdx"] and not tok["is_custom"]
    )

    return advisory_envelope(
        {
            "ok": compatibility["compatible"],
            "dependency_count": len(entries),
            "valid_spdx_token_count": valid_spdx_count,
            "deprecated_token_count": deprecated_count,
            "custom_token_count": custom_count,
            "unknown_token_count": unknown_count,
            "compatibility": compatibility,
            "dependencies": entries,
        }
    )


def assess_copyleft_risk(
    license_ids: list[str],
    context: str = "proprietary_distribution",
) -> dict[str, Any]:
    """Assess copyleft risk given a deployment or distribution context."""
    normalized_list = [normalize_gnu(lid)[0] for lid in license_ids]
    categories = [get_copyleft_category(lid) for lid in normalized_list]

    risks: list[dict[str, Any]] = []
    overall_risk = "low"

    for lid, cat in zip(normalized_list, categories):
        if cat == "network_copyleft":
            if context in {"saas_cloud", "proprietary_distribution"}:
                risks.append(
                    {
                        "license": lid,
                        "risk": "critical",
                        "reason": f"Network copyleft ({lid}) triggers source disclosure upon network access.",
                    }
                )
                overall_risk = "critical"
            else:
                risks.append(
                    {
                        "license": lid,
                        "risk": "medium",
                        "reason": f"Network copyleft ({lid}) requires source availability if service exposed externally.",
                    }
                )
                if overall_risk != "critical":
                    overall_risk = "medium"
        elif cat == "strong_copyleft":
            if context == "proprietary_distribution":
                risks.append(
                    {
                        "license": lid,
                        "risk": "critical",
                        "reason": f"Strong copyleft ({lid}) requires entire distributed binary source release.",
                    }
                )
                if overall_risk != "critical":
                    overall_risk = "critical"
            elif context == "saas_cloud":
                risks.append(
                    {
                        "license": lid,
                        "risk": "low",
                        "reason": f"GPL ({lid}) does not trigger on SaaS backend execution without distribution.",
                    }
                )
        elif cat == "weak_copyleft":
            risks.append(
                {
                    "license": lid,
                    "risk": "medium",
                    "reason": f"Weak copyleft ({lid}) requires dynamic linking and library source modifications disclosure.",
                }
            )
            if overall_risk not in {"critical", "high"}:
                overall_risk = "medium"

    return {
        "context": context,
        "overall_risk": overall_risk,
        "risk_items": risks,
    }


def analyze_expression(expr: str, *, package: str | None = None) -> dict[str, Any]:
    """Analyze a single license expression for copyleft flags and GNU deprecations."""
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

    compat = evaluate_compatibility(normalized_ids) if len(normalized_ids) > 1 else None

    return {
        "package": package,
        "expression": expr,
        "license_ids": normalized_ids,
        "families": sorted(families),
        "flags": flags,
        "notes": notes,
        "compatibility": compat,
    }


def _spdx_packages(data: dict[str, Any]) -> list[tuple[str, str]]:
    """Extract package name and license pairs from SPDX JSON document."""
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
    """Extract component name and license pairs from CycloneDX BOM."""
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
    """Scan parsed SBOM JSON document (SPDX or CycloneDX) for licensing heuristics."""
    if data.get("bomFormat") == "CycloneDX" or "components" in data and "packages" not in data:
        pairs = _cyclonedx_components(data)
        fmt = "cyclonedx"
    else:
        pairs = _spdx_packages(data)
        fmt = "spdx"
    findings = [analyze_expression(expr, package=name) for name, expr in pairs]
    flags = sorted({flag for item in findings for flag in item["flags"]})

    all_ids = [lid for item in findings for lid in item["license_ids"]]
    compat = evaluate_compatibility(all_ids) if all_ids else None

    return advisory_envelope(
        {
            "ok": True,
            "source": source,
            "format": fmt,
            "package_count": len(findings),
            "flags": flags,
            "compatibility": compat,
            "findings": findings,
        }
    )


def scan_path(path: Path) -> dict[str, Any]:
    """Load and scan an SBOM file from disk."""
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} is not a JSON object")
    return scan_document(data, source=path.as_posix())


def main(argv: list[str] | None = None) -> int:
    """CLI entrypoint for SPDX license analysis and SBOM checking."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--sbom", type=Path, help="SPDX JSON or CycloneDX bom.json")
    parser.add_argument("--expression", help="Scan a single SPDX license expression")
    parser.add_argument(
        "--dependencies",
        help="JSON file path or inline JSON string of dependency licenses to validate",
    )
    parser.add_argument(
        "--compatibility-check",
        action="store_true",
        help="Evaluate compatibility matrix on provided licenses",
    )
    parser.add_argument(
        "--context",
        default="proprietary_distribution",
        choices=["proprietary_distribution", "saas_cloud", "internal_only"],
        help="Distribution context for copyleft risk assessment",
    )
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--dry-run", action="store_true", help="Scan bundled fixtures")
    args = parser.parse_args(argv)

    if args.expression:
        finding = analyze_expression(args.expression)
        risk = assess_copyleft_risk(finding["license_ids"], context=args.context)
        report = advisory_envelope(
            {
                "ok": True,
                "findings": [finding],
                "risk_assessment": risk,
            }
        )
    elif args.dependencies:
        dep_path = Path(args.dependencies)
        if dep_path.is_file():
            deps = json.loads(dep_path.read_text(encoding="utf-8-sig"))
        else:
            deps = json.loads(args.dependencies)
        if not isinstance(deps, list):
            print("error: dependencies must be a JSON array of strings or objects", file=sys.stderr)
            return 2
        report = validate_license_list(deps)
    elif args.dry_run and not args.sbom:
        reports = [scan_path(path) for path in sorted(FIXTURE_DIR.glob("*.json"))]
        report = advisory_envelope({"ok": all(r.get("ok") for r in reports), "fixtures": reports})
    elif args.sbom:
        report = scan_path(args.sbom)
    else:
        print("error: pass --sbom, --expression, --dependencies, or --dry-run", file=sys.stderr)
        return 2

    print(json.dumps(report, indent=2))
    return 0 if report.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
