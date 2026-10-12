# Legal skills

Purpose: domain skills for this legal-router spoke. Local constraints: advisory-only output, attorney-in-the-loop, no WorldCC scrape, no Bluebook redistribution, no client secrets.

Attorney-in-the-loop process is in use. Cases are required to include an `attorney_review` object with `process_in_use`, `metadata`, `timestamp`, `status`, and `hash`. This is enforced by `scripts/legal/attorney_review_gate.py`.

Next hop: assigned `SKILL.md`, then [`../../../docs/standards/legal-overlay.md`](../../../docs/standards/legal-overlay.md).
