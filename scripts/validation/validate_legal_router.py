"""Validate legal-router case manifests, representation registries, and request contracts.

tags: [validation, legal-router, scripts]
routing_hints: [manifest, fixtures, ethics, upl, request-contract, spdx, citations]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = REPO_ROOT / "docs" / "standards" / "legal-representation-registry.json"
SCHEMA_PATH = REPO_ROOT / "docs" / "standards" / "legal-request-v1.schema.json"
DEFAULT_FIXTURE = Path(__file__).resolve().parent / "fixtures" / "contract-cases.json"

MANDATORY_ADVISORY_PREFIX = "ADVISORY WORK PRODUCT"


def route_token(value: str) -> str:
    return value.strip().lower().replace("-", "_").replace(" ", "_")


def load_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"Missing required file: {path}")
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_registry(registry_data: dict[str, Any]) -> dict[str, Any]:
    if "representations" not in registry_data:
        raise ValueError("Registry missing 'representations' list")
    
    representations_by_id: dict[str, dict[str, Any]] = {}
    medium_aliases: dict[str, str] = {}

    for rep in registry_data["representations"]:
        rep_id = rep["id"]
        representations_by_id[rep_id] = rep
        for alias in [rep_id, *rep.get("aliases", [])]:
            token = route_token(alias)
            if token in medium_aliases and medium_aliases[token] != rep_id:
                raise ValueError(f"Duplicate alias '{alias}' in registry")
            medium_aliases[token] = rep_id

    for rep in registry_data["representations"]:
        for adj in rep.get("adjacent_routes", []):
            if adj not in representations_by_id:
                raise ValueError(f"Unknown adjacent route '{adj}' in representation '{rep['id']}'")
        
        asset_type_aliases: dict[str, str] = {}
        for asset_type in rep.get("asset_types", []):
            at_id = asset_type["id"]
            for at_name in [at_id, *asset_type.get("aliases", [])]:
                at_token = route_token(at_name)
                if at_token in asset_type_aliases and asset_type_aliases[at_token] != at_id:
                    raise ValueError(f"Duplicate asset type alias '{at_name}' in representation '{rep['id']}'")
                asset_type_aliases[at_token] = at_id

    return {
        "representations_by_id": representations_by_id,
        "medium_aliases": medium_aliases,
    }


def validate_case(
    case: dict[str, Any],
    representations_by_id: dict[str, dict[str, Any]],
    medium_aliases: dict[str, str],
) -> list[str]:
    errors: list[str] = []
    case_id = case.get("case_id", "unknown")

    req = case.get("request")
    if not req:
        return [f"[{case_id}] Case missing 'request' object"]

    # Privilege and safeguards check
    priv = req.get("privilege_and_safeguards", {})
    if not priv.get("upl_disclaimer_required"):
        errors.append(f"[{case_id}] upl_disclaimer_required must be true")
    if not priv.get("supervising_attorney_required"):
        errors.append(f"[{case_id}] supervising_attorney_required must be true")

    # Hard constraints check
    constraints = req.get("constraints", [])
    for idx, c in enumerate(constraints):
        if not c.get("text"):
            errors.append(f"[{case_id}] constraint[{idx}] missing text")
        if c.get("hardness") not in ("hard", "soft"):
            errors.append(f"[{case_id}] constraint[{idx}] invalid hardness: {c.get('hardness')}")

    # Representation routing check
    reps = req.get("representations", [])
    if not reps:
        errors.append(f"[{case_id}] request has no representations declared")

    primary_count = 0
    for r in reps:
        role = r.get("role")
        if role == "primary":
            primary_count += 1
        route = r.get("route", "")
        resolved_route = medium_aliases.get(route_token(route))
        if not resolved_route:
            errors.append(f"[{case_id}] Unknown representation route: '{route}'")
        else:
            rep_def = representations_by_id[resolved_route]
            asset_type = r.get("asset", {}).get("type")
            valid_asset_ids = {at["id"] for at in rep_def.get("asset_types", [])}
            valid_asset_aliases = {
                alias
                for at in rep_def.get("asset_types", [])
                for alias in at.get("aliases", [])
            }
            if asset_type not in valid_asset_ids and asset_type not in valid_asset_aliases:
                errors.append(
                    f"[{case_id}] Invalid asset type '{asset_type}' for route '{resolved_route}'"
                )

    if primary_count != 1:
        errors.append(f"[{case_id}] Exactly one primary representation required, got {primary_count}")

    # Review handoff check
    review = req.get("review_handoff", {})
    if review.get("reviewer") != "legal-ethics-reviewer":
        errors.append(
            f"[{case_id}] review_handoff.reviewer must be 'legal-ethics-reviewer', got '{review.get('reviewer')}'"
        )

    # Deliverables check
    deliverables = case.get("deliverables", [])
    for idx, d in enumerate(deliverables):
        stamp = d.get("advisory_stamp", "")
        if not stamp.startswith(MANDATORY_ADVISORY_PREFIX):
            errors.append(f"[{case_id}] deliverable[{idx}] missing mandatory advisory stamp")
        if not d.get("citations_verified"):
            errors.append(f"[{case_id}] deliverable[{idx}] citations must be verified")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate legal-router case manifests and registry")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=DEFAULT_FIXTURE,
        help="Path to case manifest JSON (default: fixtures/contract-cases.json)",
    )
    args = parser.parse_args()

    print("[*] Validating legal representation registry...")
    try:
        registry_data = load_json(REGISTRY_PATH)
        validated = validate_registry(registry_data)
        print(f"    Loaded {len(validated['representations_by_id'])} representations successfully.")
    except Exception as exc:
        print(f"[!] Registry validation error: {exc}", file=sys.stderr)
        return 1

    print("[*] Validating legal request JSON schema...")
    try:
        load_json(SCHEMA_PATH)
        print("    Request schema parsed successfully.")
    except Exception as exc:
        print(f"[!] Request schema error: {exc}", file=sys.stderr)
        return 1

    manifest_path = args.manifest
    print(f"[*] Validating manifest cases in: {manifest_path}...")
    try:
        manifest_data = load_json(manifest_path)
    except Exception as exc:
        print(f"[!] Manifest load error: {exc}", file=sys.stderr)
        return 1

    cases = manifest_data.get("cases", [])
    if not cases:
        print("[!] No cases found in manifest", file=sys.stderr)
        return 1

    total_errors: list[str] = []
    for c in cases:
        case_errors = validate_case(c, validated["representations_by_id"], validated["medium_aliases"])
        total_errors.extend(case_errors)

    if total_errors:
        print(f"[!] Validation failed with {len(total_errors)} errors:", file=sys.stderr)
        for err in total_errors:
            print(f"    - {err}", file=sys.stderr)
        return 1

    print(f"[+] All {len(cases)} cases passed legal domain validation successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
