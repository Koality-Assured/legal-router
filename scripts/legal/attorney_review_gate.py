import argparse
import json
import sys
from pathlib import Path


def verify_attorney_review(case: dict) -> list[str]:
    errors = []
    case_id = case.get("case_id", "unknown")

    review = case.get("attorney_review")
    if not review:
        return [f"[{case_id}] Missing 'attorney_review' object"]

    if not review.get("process_in_use"):
        errors.append(f"[{case_id}] 'process_in_use' must be true")

    metadata = review.get("metadata", {})
    if not metadata:
        errors.append(f"[{case_id}] Missing 'metadata' in attorney_review")
    else:
        if "timestamp" not in metadata:
            errors.append(f"[{case_id}] Missing 'timestamp' in metadata")
        if "status" not in metadata:
            errors.append(f"[{case_id}] Missing 'status' in metadata")
        if "hash" not in metadata:
            errors.append(f"[{case_id}] Missing 'hash' in metadata")

    return errors


def main():
    parser = argparse.ArgumentParser(
        description="Verify attorney-in-the-loop process is in use"
    )
    parser.add_argument(
        "--manifest", type=Path, required=True, help="Path to manifest JSON"
    )
    args = parser.parse_args()

    if not args.manifest.is_file():
        print(f"[!] File not found: {args.manifest}", file=sys.stderr)
        sys.exit(1)

    with args.manifest.open("r", encoding="utf-8") as f:
        data = json.load(f)

    cases = data.get("cases", [])
    all_errors = []
    for c in cases:
        all_errors.extend(verify_attorney_review(c))

    if all_errors:
        for err in all_errors:
            print(f"[!] {err}", file=sys.stderr)
        sys.exit(1)

    print("[+] Attorney-in-the-loop verification passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
