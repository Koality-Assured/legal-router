"""Fail-closed attorney-in-the-loop sign-off gate for legal-router work product.

An artifact (memo, clause review, citation table) is only releasable when a
sign-off record sits beside it and all of the following hold:

* the sign-off names the artifact it covers and carries its SHA-256,
* the artifact on disk still hashes to that value (no edits after review),
* the status is ``approved`` (``rejected`` / ``changes_requested`` fail),
* a reviewer identifier and bar jurisdiction are present,
* ``reviewed_at`` is a timezone-aware ISO-8601 time that is not in the future.

The gate verifies *process evidence only*. It cannot establish that a real
licensed attorney reviewed the work; it makes unreviewed or silently edited
work product fail closed. Sign-off records must never contain client data.

CLI:
    python scripts/legal/attorney_review_gate.py hash ARTIFACT
    python scripts/legal/attorney_review_gate.py check ARTIFACT SIGNOFF.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

APPROVED = "approved"
VALID_STATUSES = {APPROVED, "rejected", "changes_requested"}
REQUIRED_FIELDS = ("artifact", "content_sha256", "reviewer_id", "bar_jurisdiction", "reviewed_at", "status")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 16), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def verify_signoff(
    artifact: Path, signoff: dict[str, Any], *, now: datetime | None = None
) -> list[str]:
    """Return a list of problems; an empty list means the artifact is releasable."""
    errors: list[str] = []
    if not isinstance(signoff, dict):
        return ["sign-off record must be a JSON object"]

    for field in REQUIRED_FIELDS:
        value = signoff.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"missing or empty '{field}'")
    if errors:
        return errors

    if not artifact.is_file():
        return [f"artifact not found: {artifact}"]

    if Path(signoff["artifact"]).name != artifact.name:
        errors.append(
            f"sign-off covers '{signoff['artifact']}', not '{artifact.name}'"
        )

    status = signoff["status"]
    if status not in VALID_STATUSES:
        errors.append(f"unknown status '{status}'")
    elif status != APPROVED:
        errors.append(f"status is '{status}', not '{APPROVED}'")

    if sha256_file(artifact) != signoff["content_sha256"].lower():
        errors.append("artifact changed after review (content hash mismatch); re-review required")

    reviewed_at = _parse_time(signoff["reviewed_at"])
    if reviewed_at is None:
        errors.append("'reviewed_at' must be a timezone-aware ISO-8601 timestamp")
    elif reviewed_at > (now or datetime.now(timezone.utc)):
        errors.append("'reviewed_at' is in the future")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    hash_cmd = sub.add_parser("hash", help="print the SHA-256 to record in a sign-off")
    hash_cmd.add_argument("artifact", type=Path)
    check_cmd = sub.add_parser("check", help="verify an artifact against its sign-off record")
    check_cmd.add_argument("artifact", type=Path)
    check_cmd.add_argument("signoff", type=Path)
    args = parser.parse_args(argv)

    if args.command == "hash":
        if not args.artifact.is_file():
            print(f"[!] artifact not found: {args.artifact}", file=sys.stderr)
            return 1
        print(sha256_file(args.artifact))
        return 0

    try:
        record = json.loads(args.signoff.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"[!] cannot read sign-off record: {exc}", file=sys.stderr)
        return 1
    errors = verify_signoff(args.artifact, record)
    if errors:
        for error in errors:
            print(f"[!] {error}", file=sys.stderr)
        return 1
    print("[+] Attorney sign-off verified; artifact unchanged since review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
