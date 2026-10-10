"""Verify statutory and case citations against fixtures and optional registries.

tags: [legal, citations, verification]
routing_hints: [bluebook, courtlistener, hallucination, govinfo]

Offline by default. Provides regex and AST parsing for strict Bluebook legal
citation formatting (reporters, US Code, CFR, Federal Register, pin cites).
Optional live CourtListener lookup uses COURTLISTENER_API_TOKEN from the
environment and never prints that value. Outputs are advisory only.
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
    # Federal Courts (SCOTUS, Appellate, District, Bankruptcy, Claims)
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
    "U.S. App. D.C.",
    "B.R.",
    "Fed. Cl.",
    "Ct. Cl.",
    # Regional Reporters
    "A.",
    "A.2d",
    "A.3d",
    "N.E.",
    "N.E.2d",
    "N.E.3d",
    "N.W.",
    "N.W.2d",
    "P.",
    "P.2d",
    "P.3d",
    "S.E.",
    "S.E.2d",
    "So.",
    "So. 2d",
    "So. 3d",
    "S.W.",
    "S.W.2d",
    "S.W.3d",
    # State-Specific Reporters
    "Cal. App.",
    "Cal. App. 2d",
    "Cal. App. 3d",
    "Cal. App. 4th",
    "Cal. App. 5th",
    "Cal. Rptr.",
    "Cal. Rptr. 2d",
    "Cal. Rptr. 3d",
    "N.Y.S.",
    "N.Y.S.2d",
    "N.Y.S.3d",
}

FAKE_REPORTER_MARKERS = ("fake", "halluc", "invented", "bogus", "phantom")

# Case citation regex: matches case name, volume, reporter, initial page, optional pin cite, and parenthetical (court/year)
CASE_RE = re.compile(
    r"(?:(?:See(?:\s+also)?|Cf\.|Accord|But\s+see)\s+)?"
    r"(?P<name>[A-Z][^,\n();]{1,80}?\s+v\.\s+[^,\n();]{1,80}?),\s+"
    r"(?P<volume>\d+)\s+(?P<reporter>[A-Z][A-Za-z0-9.]+(?:\s+[A-Za-z0-9.]+){0,4})\s+"
    r"(?P<page>\d+)"
    r"(?:,\s*(?P<pin_cite>\d+(?:[-–]\d+)?))?"
    r"(?:\s+\((?P<parenthetical>[^)]+)\))?",
    re.UNICODE,
)

# US Code citation regex: matches title, U.S.C., section symbol, section number, optional subsections/pin cites, and optional et seq.
USC_RE = re.compile(
    r"(?P<title>\d+)\s+U\.S\.C\.\s+§+\s*(?P<section>[\d.]+[a-zA-Z]?)"
    r"(?P<subsections>(?:\([a-zA-Z0-9]+\))*)?"
    r"(?:\s+(?P<et_seq>et\s+seq\.?))?",
    re.UNICODE,
)

# Code of Federal Regulations regex: matches title, C.F.R., section symbol, section number, and optional pin cite subsections
CFR_RE = re.compile(
    r"(?P<title>\d+)\s+C\.F\.R\.\s+§+\s*(?P<section>[\d.]+)"
    r"(?P<subsections>(?:\([a-zA-Z0-9]+\))*)?",
    re.UNICODE,
)

# Federal Register regex: matches volume, Fed. Reg. / FR / Federal Register, page, optional pin cite, and optional date
FED_REG_RE = re.compile(
    r"(?P<volume>\d+)\s+(?P<reporter>Fed\.\s*Reg\.|FR|Federal\s+Register)\s+"
    r"(?P<page>\d+(?:,\d{3})*|\d+)"
    r"(?:,\s*(?P<pin_cite>\d+(?:,\d{3})*(?:[-–]\d+)?))?"
    r"(?:\s+\((?P<date>[^)]+)\))?",
    re.IGNORECASE,
)

# EU Regulation regex: matches Regulation (EU|EEC) Year/Number
EU_RE = re.compile(
    r"Regulation\s+\((?P<body>EU|EEC)\)\s+(?P<year>\d{4})/(?P<num>\d+)",
    re.IGNORECASE,
)

STATUSES = ("valid_fixture", "hallucinated", "unverified", "unparsed")


class CitationASTNode:
    """Base AST node representing a structured legal citation token."""

    def __init__(
        self,
        kind: str,
        text: str,
        span: tuple[int, int],
        **attributes: Any,
    ) -> None:
        self.kind = kind
        self.text = text
        self.span = span
        self.attributes = attributes

    def to_dict(self) -> dict[str, Any]:
        """Convert AST node to plain dictionary representation."""
        data: dict[str, Any] = {
            "kind": self.kind,
            "text": self.text,
            "span": list(self.span),
        }
        data.update(self.attributes)
        return data

    def validate_bluebook(self) -> list[str]:
        """Verify strict Bluebook formatting conventions and return any violations."""
        return []

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} text={self.text!r}>"


class CaseCitationNode(CitationASTNode):
    """AST node for judicial case citations (Bluebook Rule 10)."""

    def __init__(
        self,
        text: str,
        span: tuple[int, int],
        name: str,
        volume: str,
        reporter: str,
        page: str,
        pin_cite: str | None = None,
        year: int | None = None,
        court: str | None = None,
        parenthetical: str | None = None,
    ) -> None:
        super().__init__(
            kind="case",
            text=text,
            span=span,
            name=name,
            volume=volume,
            reporter=reporter,
            page=page,
            pin_cite=pin_cite,
            year=year,
            court=court,
            parenthetical=parenthetical,
        )

    def validate_bluebook(self) -> list[str]:
        violations: list[str] = []
        if not self.attributes.get("name"):
            violations.append("missing_case_name")
        if not str(self.attributes.get("volume", "")).isdigit():
            violations.append("invalid_volume_number")
        reporter = str(self.attributes.get("reporter", ""))
        if reporter not in KNOWN_REPORTERS:
            violations.append("unrecognized_reporter")
        if not str(self.attributes.get("page", "")).isdigit():
            violations.append("invalid_first_page")
        year = self.attributes.get("year")
        if year is not None and (year < 1700 or year > 2026):
            violations.append("invalid_year")
        return violations


class USCCitationNode(CitationASTNode):
    """AST node for United States Code statutory citations (Bluebook Rule 12)."""

    def __init__(
        self,
        text: str,
        span: tuple[int, int],
        title: str,
        section: str,
        subsections: str | None = None,
        et_seq: bool = False,
    ) -> None:
        pin = subsections if subsections else None
        super().__init__(
            kind="usc",
            text=text,
            span=span,
            title=title,
            section=section,
            subsections=subsections or "",
            pin_cite=pin,
            et_seq=et_seq,
        )

    def validate_bluebook(self) -> list[str]:
        violations: list[str] = []
        try:
            title_num = int(self.attributes.get("title", 0))
            if title_num <= 0 or title_num > 54:
                violations.append("out_of_range_usc_title")
        except ValueError:
            violations.append("non_numeric_usc_title")
        if not self.attributes.get("section"):
            violations.append("missing_section_number")
        return violations


class CFRCitationNode(CitationASTNode):
    """AST node for Code of Federal Regulations citations (Bluebook Rule 14)."""

    def __init__(
        self,
        text: str,
        span: tuple[int, int],
        title: str,
        section: str,
        subsections: str | None = None,
    ) -> None:
        pin = subsections if subsections else None
        super().__init__(
            kind="cfr",
            text=text,
            span=span,
            title=title,
            section=section,
            subsections=subsections or "",
            pin_cite=pin,
        )

    def validate_bluebook(self) -> list[str]:
        violations: list[str] = []
        try:
            title_num = int(self.attributes.get("title", 0))
            if title_num <= 0 or title_num > 50:
                violations.append("out_of_range_cfr_title")
        except ValueError:
            violations.append("non_numeric_cfr_title")
        return violations


class FederalRegisterNode(CitationASTNode):
    """AST node for Federal Register notices and rules (Bluebook Rule 14)."""

    def __init__(
        self,
        text: str,
        span: tuple[int, int],
        volume: str,
        reporter: str,
        page: str,
        pin_cite: str | None = None,
        date: str | None = None,
        year: int | None = None,
    ) -> None:
        super().__init__(
            kind="federal_register",
            text=text,
            span=span,
            volume=volume,
            reporter=reporter,
            page=page,
            pin_cite=pin_cite,
            date=date,
            year=year,
        )

    def validate_bluebook(self) -> list[str]:
        violations: list[str] = []
        try:
            vol_num = int(self.attributes.get("volume", 0))
            if vol_num <= 0 or vol_num > 100:
                violations.append("out_of_range_fr_volume")
        except ValueError:
            violations.append("non_numeric_fr_volume")
        year = self.attributes.get("year")
        if year is not None and (year < 1936 or year > 2026):
            violations.append("out_of_range_fr_year")
        return violations


class EURegulationNode(CitationASTNode):
    """AST node for European Union regulations."""

    def __init__(
        self,
        text: str,
        span: tuple[int, int],
        body: str,
        year: int,
        number: str,
    ) -> None:
        super().__init__(
            kind="eu_regulation",
            text=text,
            span=span,
            body=body,
            year=year,
            number=number,
        )

    def validate_bluebook(self) -> list[str]:
        violations: list[str] = []
        year = int(self.attributes.get("year", 0))
        if year < 1958 or year > 2026:
            violations.append("invalid_eu_regulation_year")
        return violations


def advisory_envelope(payload: dict[str, Any]) -> dict[str, Any]:
    """Wrap output dictionary with the required non-legal-advice advisory stamp."""
    out = dict(payload)
    out["advisory"] = ADVISORY_STAMP
    out["not_legal_advice"] = True
    return out


def _normalize_space(text: str) -> str:
    """Collapse repeated whitespace characters into a single space."""
    return re.sub(r"\s+", " ", text).strip()


def load_suite(path: Path | None = None) -> dict[str, Any]:
    """Load JSON citation test suite from path or repository default."""
    target = path or FIXTURE_SUITE
    data = json.loads(target.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict) or "items" not in data:
        raise ValueError(f"citation suite missing items: {target}")
    return data


def parse_citations_ast(text: str) -> list[CitationASTNode]:
    """Extract citations into an AST of CitationASTNode objects with strict span tracking."""
    nodes: list[CitationASTNode] = []
    occupied: list[tuple[int, int]] = []

    def overlaps(start: int, end: int) -> bool:
        return any(start < b and end > a for a, b in occupied)

    # 1. Judicial case citations
    for match in CASE_RE.finditer(text):
        c_start = match.start("name")
        c_end = match.end()
        occupied.append((c_start, c_end))
        parenthetical = (match.group("parenthetical") or "").strip()
        year = None
        court = None
        if parenthetical:
            year_match = re.search(r"(1[7-9]\d{2}|20\d{2})", parenthetical)
            if year_match:
                year = int(year_match.group(1))
                court_part = parenthetical[: year_match.start()].strip().rstrip(",").strip()
                court = court_part if court_part else None
            else:
                court = parenthetical

        reporter = _normalize_space(match.group("reporter"))
        nodes.append(
            CaseCitationNode(
                text=_normalize_space(text[c_start:c_end]),
                span=(c_start, c_end),
                name=_normalize_space(match.group("name")),
                volume=match.group("volume"),
                reporter=reporter,
                page=match.group("page"),
                pin_cite=match.group("pin_cite"),
                year=year,
                court=court,
                parenthetical=parenthetical if parenthetical else None,
            )
        )

    # 2. U.S. Code statutory citations
    for match in USC_RE.finditer(text):
        if overlaps(match.start(), match.end()):
            continue
        occupied.append((match.start(), match.end()))
        subsections = match.group("subsections") or None
        nodes.append(
            USCCitationNode(
                text=_normalize_space(match.group(0)),
                span=(match.start(), match.end()),
                title=match.group("title"),
                section=match.group("section"),
                subsections=subsections,
                et_seq=bool(match.group("et_seq")),
            )
        )

    # 3. Code of Federal Regulations citations
    for match in CFR_RE.finditer(text):
        if overlaps(match.start(), match.end()):
            continue
        occupied.append((match.start(), match.end()))
        subsections = match.group("subsections") or None
        nodes.append(
            CFRCitationNode(
                text=_normalize_space(match.group(0)),
                span=(match.start(), match.end()),
                title=match.group("title"),
                section=match.group("section"),
                subsections=subsections,
            )
        )

    # 4. Federal Register citations
    for match in FED_REG_RE.finditer(text):
        if overlaps(match.start(), match.end()):
            continue
        occupied.append((match.start(), match.end()))
        date_str = match.group("date")
        year = None
        if date_str:
            ym = re.search(r"(19\d{2}|20\d{2})", date_str)
            if ym:
                year = int(ym.group(1))

        nodes.append(
            FederalRegisterNode(
                text=_normalize_space(match.group(0)),
                span=(match.start(), match.end()),
                volume=match.group("volume"),
                reporter=_normalize_space(match.group("reporter")),
                page=match.group("page").replace(",", ""),
                pin_cite=match.group("pin_cite"),
                date=date_str,
                year=year,
            )
        )

    # 5. EU regulations
    for match in EU_RE.finditer(text):
        if overlaps(match.start(), match.end()):
            continue
        occupied.append((match.start(), match.end()))
        nodes.append(
            EURegulationNode(
                text=_normalize_space(match.group(0)),
                span=(match.start(), match.end()),
                body=match.group("body").upper(),
                year=int(match.group("year")),
                number=match.group("num"),
            )
        )

    # Sort nodes by appearance in text
    nodes.sort(key=lambda n: n.span[0])
    return nodes


def parse_citations(text: str) -> list[dict[str, Any]]:
    """Extract case, USC, CFR, Federal Register, and EU regulation citations into dict rows."""
    ast_nodes = parse_citations_ast(text)
    return [node.to_dict() for node in ast_nodes]


def _reporter_looks_fake(reporter: str) -> bool:
    """Identify hallmark patterns of LLM hallucinated reporters."""
    lowered = reporter.lower()
    if any(marker in lowered for marker in FAKE_REPORTER_MARKERS):
        return True
    compact = reporter.replace(" ", "")
    if re.search(r"F\.\d{2,}", compact) and compact not in {"F.2d", "F.3d"}:
        return True
    return reporter not in KNOWN_REPORTERS


def classify_parsed(parsed: dict[str, Any], known_texts: set[str]) -> str:
    """Classify a parsed citation as valid_fixture, hallucinated, or unverified."""
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
    if kind == "federal_register":
        vol = int(parsed.get("volume") or 0)
        year = parsed.get("year")
        if vol <= 0 or vol > 100:
            return "hallucinated"
        if year is not None and (year < 1936 or year > 2026):
            return "hallucinated"
        return "unverified"
    if kind == "eu_regulation":
        year = int(parsed.get("year") or 0)
        if year < 1958 or year > 2026:
            return "hallucinated"
        return "unverified"
    return "unparsed"


def verify_text(text: str, *, suite: dict[str, Any] | None = None) -> dict[str, Any]:
    """Verify citations within arbitrary text against known fixture baselines."""
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
    """Run regression verification on all synthetic citation fixture items."""
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
    """Retrieve CourtListener token from environment without logging."""
    return os.environ.get(TOKEN_ENV, "").strip()


def main(argv: list[str] | None = None) -> int:
    """CLI entrypoint for citation parsing and verification."""
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--suite", type=Path, help="Citation fixture JSON")
    parser.add_argument("--text", help="Raw text containing citations")
    parser.add_argument("--file", type=Path, help="Read citations from a text file")
    parser.add_argument("--ast", action="store_true", help="Include AST validation details in output")
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
        if args.ast:
            ast_nodes = parse_citations_ast(source)
            report["ast_nodes"] = [
                {
                    "class": node.__class__.__name__,
                    "node": node.to_dict(),
                    "bluebook_violations": node.validate_bluebook(),
                }
                for node in ast_nodes
            ]
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
