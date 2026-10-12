# Legal skills

Purpose: domain skills for this legal-router spoke. Local constraints: advisory-only output, attorney-in-the-loop, no WorldCC scrape, no Bluebook redistribution, no client secrets.

Attorney-in-the-loop is enforced by `scripts/legal/attorney_review_gate.py`: a work product ships only with an `approved` sign-off record (reviewer id, bar jurisdiction, timezone-aware review time, SHA-256 of the reviewed content). Use `hash` to compute the digest and `check` to verify; missing, rejected, or stale (edited after review) sign-offs fail closed.

Next hop: assigned `SKILL.md`, then [`../../../docs/standards/legal-overlay.md`](../../../docs/standards/legal-overlay.md).
