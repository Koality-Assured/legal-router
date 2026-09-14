"""Verify statutory and case citations against fixtures and optional registries.

tags: [legal, citations, verification]
routing_hints: [bluebook, courtlistener, hallucination, govinfo]

Offline by default. Optional live CourtListener lookup uses COURTLISTENER_API_TOKEN
from the environment and never prints that value. Outputs are advisory only.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

_LIB = Path(__file__).resolve().parents[1] / "_lib"
sys.path.insert(0, str(_LIB))
from paths import REPO_ROOT as ROOT  # noqa: E402

ADVISORY_STAMP = "ADVISORY WORK PRODUCT - REQUIRES LICENSED ATTORNEY REVIEW"
FIXTURE_SUITE = Path(__file__).resolve().parent / "fixtures" / "citations" / "citation-suite.json"
COURTLISTENER_LOOKUP = "https://www.courtlistener.com/api/rest/v4/citation-lookup/"
TOKEN_ENV = "COURTLISTENER_API_TOKEN"

KNOWN_REPORTERS = {
    "U.S.",
    "S. Ct.",
    "L. Ed.",
    "L. Ed. 2d",
    "F.",
    "F.2d",
    "F.3d",
    "F.4th",
    "F. Supp.",
    "F. Supp. 2d",
    "F. Supp. 3d",
    "Fed. Appx.",
}

FAKE_REPORTER_MARKERS = ("fake", "halluc", "invented", "bogus", "phantom")

CASE_RE = re.compile(
    r"(?P<name>[A-Z][^,\n]{1,80}?\s+v\.\s+[^,\n]{1,80}?),\s+"
    r"(?P<volume>\d+)\s+(?P<reporter>[A-Z][A-Za-z0-9.]+(?:\s+[A-Za-z0-9.]+){0,4})\s+"
    r"(?P<page>\d+)(?:\s+\((?P<parenthetical>[^)]+)\))?",
    re.UNICODE,
)

USC_RE = re.compile(r"(?P<title>\d+)\s+U\.S\.C\.\s+§+\s*(?P<section>[\d.]+[a-zA-Z]?)", re.UNICODE)
CFR_RE = re.compile(r"(?P<title>\d+)\s+C\.F\.R\.\s+§+\s*(?P<section>[\d.]+)", re.UNICODE)
EU_RE = re.compile(
    r"Regulation\s+\((?P<body>EU|EEC)\)\s+(?P<year>\d{4})/(?P<num>\d+)",
    re.IGNORECASE,
)

STATUSES = ("valid_fixture", "hallucinated", "unverified", "unparsed")


def advisory_envelope(payload: dict[str, Any]) -> dict[str, Any]:
    out = dict(payload)
    out["advisory"] = ADVISORY_STAMP
    out["not_legal_advice"] = True
    return out


def _normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def load_suite(path: Path | None = None) -> dict[str, Any]:
    target = path or FIXTURE_SUITE
    data = json.loads(target.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict) or "items" not in data:
        raise ValueError(f"citation suite missing items: {target}")
    return data


def parse_citations(text: str) -> list[dict[str, Any]]:
    """Extract case, USC, CFR, and EU regulation citations from text."""
    found: list[dict[str, Any]] = []
    occupied: list[tuple[int, int]] = []

    def overlaps(start: int, end: int) -> bool:
        return any(start < b and end > a for a, b in occupied)

    for match in CASE_RE.finditer(text):
        occupied.append((match.start(), match.end()))
        parenthetical = (match.group("parenthetical") or "").strip()
        year = None
        year_match = re.search(r"(1[7-9]\d{2}|20\d{2})", parenthetical)
        if year_match:
            year = int(year_match.group(1))
        reporter = _normalize_space(match.group("reporter"))
        found.append(
            {
                "kind": "case",
                "text": _normalize_space(match.group(0)),
                "name": _normalize_space(match.group("name")),
                "volume": match.group("volume"),
                "reporter": reporter,
                "page": match.group("page"),
                "year": year,
                "span": [match.start(), match.end()],
            }
        )

    for match in USC_RE.finditer(text):
        if overlaps(match.start(), match.end()):
            continue
        occupied.append((match.start(), match.end()))
        found.append(
            {
                "kind": "usc",
                "text": _normalize_space(match.group(0)),
                "title": match.group("title"),
                "section": match.group("section"),
                "span": [match.start(), match.end()],
            }
        )

    for match in CFR_RE.finditer(text):
        if overlaps(match.start(), match.end()):
            continue
        occupied.append((match.start(), match.end()))
        found.append(
            {
                "kind": "cfr",
                "text": _normalize_space(match.group(0)),
                "title": match.group("title"),
                "section": match.group("section"),
                "span": [match.start(), match.end()],
            }
        )

    for match in EU_RE.finditer(text):
        if overlaps(match.start(), match.end()):
            continue
        occupied.append((match.start(), match.end()))
        found.append(
            {
                "kind": "eu_regulation",
                "text": _normalize_space(match.group(0)),
                "body": match.group("body").upper(),
                "year": int(match.group("year")),
                "number": match.group("num"),
                "span": [match.start(), match.end()],
            }
        )

    return found


def _reporter_looks_fake(reporter: str) -> bool:
    lowered = reporter.lower()
    if any(marker in lowered for marker in FAKE_REPORTER_MARKERS):
        return True
    compact = reporter.replace(" ", "")
    if re.search(r"F\.\d{2,}", compact) and compact not in {"F.2d", "F.3d"}:
        return True
    return reporter not in KNOWN_REPORTERS


def classify_parsed(parsed: dict[str, Any], known_texts: set[str]) -> str:
    text = parsed.get("text", "")
    if text in known_texts:
        return "valid_fixture"
    kind = parsed.get("kind")
    if kind == "case":
        year = parsed.get("year")
        if year is not None and year > 2026:
            return "hallucinated"
        if _reporter_looks_fake(str(parsed.get("reporter", ""))):
            return "hallucinated"
        return "unverified"
    if kind == "usc":
        title = int(parsed.get("title") or 0)
        if title <= 0 or title > 54:
            return "hallucinated"
        return "unverified"
    if kind == "cfr":
        title = int(parsed.get("title") or 0)
        if title <= 0 or title > 50:
            return "hallucinated"
        return "unverified"
    if kind == "eu_regulation":
        year = int(parsed.get("year") or 0)
        if year < 1958 or year > 2026:
            return "hallucinated"
        return "unverified"
    return "unparsed"


def verify_text(text: str, *, suite: dict[str, Any] | None = None) -> dict[str, Any]:
    suite = suite or load_suite()
    known_texts = {
        _normalize_space(item["text"])
        for item in suite.get("items", [])
        if item.get("expected") == "valid_fixture"
    }
    expected_by_text = {
        _normalize_space(item["text"]): item.get("expected")
        for item in suite.get("items", [])
        if item.get("text")
    }
    parsed = parse_citations(text)
    results: list[dict[str, Any]] = []
    for item in parsed:
        status = classify_parsed(item, known_texts)
        expected = expected_by_text.get(item["text"])
        row = dict(item)
        row["status"] = status
        if expected:
            row["fixture_expected"] = expected
            row["matches_fixture"] = expected == status or (
                expected == "valid_fixture" and status == "valid_fixture"
            )
        results.append(row)

    unmatched_expected = []
    for item in suite.get("items", []):
        expected_text = _normalize_space(item.get("text", ""))
        if expected_text and expected_text in text:
            if not any(row["text"] == expected_text for row in results):
                unmatched_expected.append(item.get("id") or expected_text)

    hallucinated = [row for row in results if row["status"] == "hallucinated"]
    return advisory_envelope(
        {
            "ok": not unmatched_expected,
            "citation_count": len(results),
            "hallucinated_count": len(hallucinated),
            "unverified_count": sum(1 for row in results if row["status"] == "unverified"),
            "valid_fixture_count": sum(1 for row in results if row["status"] == "valid_fixture"),
            "unmatched_fixture_items": unmatched_expected,
            "citations": results,
        }
    )


def verify_suite(path: Path | None = None) -> dict[str, Any]:
    suite = load_suite(path)
    failures: list[str] = []
    rows: list[dict[str, Any]] = []
    known_texts = {
        _normalize_space(item["text"])
        for item in suite.get("items", [])
        if item.get("expected") == "valid_fixture"
    }
    for item in suite.get("items", []):
        text = item.get("text", "")
        expected = item.get("expected")
        parsed = parse_citations(text)
        if expected == "unparsed":
            status = "unparsed" if not parsed else classify_parsed(parsed[0], known_texts)
            if parsed:
                failures.append(f"{item.get('id')}: expected unparsed, parsed {parsed[0]['text']}")
        elif not parsed:
            status = "unparsed"
            if expected != "unparsed":
                failures.append(f"{item.get('id')}: expected {expected}, parsed nothing")
        else:
            status = classify_parsed(parsed[0], known_texts)
            if status != expected:
                failures.append(
                    f"{item.get('id')}: expected {expected}, got {status} for {parsed[0]['text']}"
                )
        rows.append(
            {
                "id": item.get("id"),
                "text": text,
                "expected": expected,
                "status": status,
                "ok": status == expected,
            }
        )
    planted = [row for row in rows if row["expected"] == "hallucinated"]
    missed_plants = [row for row in planted if not row["ok"]]
    return advisory_envelope(
        {
            "ok": not failures and not missed_plants,
            "suite": str((path or FIXTURE_SUITE).as_posix()),
            "item_count": len(rows),
            "failures": failures,
            "missed_hallucinations": [row["id"] for row in missed_plants],
            "items": rows,
        }
    )


def live_lookup(text: str, token: str) -> dict[str, Any]:
    """POST CourtListener citation-lookup. Token is never written to the result."""
    if not token:
        raise ValueError("live lookup requested without a token in the environment")
    body = urllib.parse.urlencode({"text": text}).encode("utf-8")
    request = urllib.request.Request(
        COURTLISTENER_LOOKUP,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Token {token}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        return advisory_envelope(
            {
                "ok": False,
                "live": True,
                "http_status": exc.code,
                "error": "courtlistener_http_error",
            }
        )
    except urllib.error.URLError:
        return advisory_envelope({"ok": False, "live": True, "error": "courtlistener_unreachable"})
    return advisory_envelope({"ok": True, "live": True, "hits": payload})


def _token_from_env() -> str:
    return os.environ.get(TOKEN_ENV, "").strip()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite", type=Path, help="Citation fixture JSON")
    parser.add_argument("--text", help="Raw text containing citations")
    parser.add_argument("--file", type=Path, help="Read citations from a text file")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate the fixture suite without live network calls",
    )
    parser.add_argument(
        "--live",
        action="store_true",
        help="Optional CourtListener lookup; requires COURTLISTENER_API_TOKEN",
    )
    args = parser.parse_args(argv)

    if args.live:
        token = _token_from_env()
        if not token:
            print(
                "error: --live requires COURTLISTENER_API_TOKEN in the environment",
                file=sys.stderr,
            )
            return 2
        source = args.text
        if args.file:
            source = args.file.read_text(encoding="utf-8-sig")
        if not source:
            print("error: --live requires --text or --file", file=sys.stderr)
            return 2
        report = live_lookup(source, token)
    elif args.text or args.file:
        source = args.text or ""
        if args.file:
            source = args.file.read_text(encoding="utf-8-sig")
        report = verify_text(source, suite=load_suite(args.suite) if args.suite else None)
    else:
        report = verify_suite(args.suite)

    if args.json or args.dry_run:
        print(json.dumps(report, indent=2))
    else:
        print(report["advisory"])
        print(f"ok={report.get('ok')} citations={report.get('citation_count', report.get('item_count'))}")
        if report.get("failures"):
            for failure in report["failures"]:
                print(f"FAIL {failure}")
        if report.get("hallucinated_count"):
            print(f"hallucinated={report['hallucinated_count']}")
        if report.get("missed_hallucinations"):
            print(f"missed_hallucinations={report['missed_hallucinations']}")

    return 0 if report.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
