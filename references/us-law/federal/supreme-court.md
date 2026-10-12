---
doc_kind: reference
canonical_id: us-law-federal-supreme-court
purpose: [reference]
topics: [us-law, federal]
rag_keywords: [supreme-court, slip-opinion, preliminary-print, united-states-reports, october-term, orders]
version: "captured-2026-10-07"
publication: United States Reports
captured_at_utc: "2026-10-07T18:00:00Z"
upstream_url: https://www.supremecourt.gov/opinions/opinions.aspx
advisory_only: true
---

# Supreme Court of the United States

This capture is a point-in-time locator and structural summary for attorney review, not legal advice and not a filing.

## Purpose

Opinions of the Supreme Court are published officially in the United States Reports. The Court’s site posts them first as slip opinions, then replaces those files as the Reporter of Decisions edits them into the Reports’ publication style. This page maps that sequence. It does not summarize any case.

## Source ranking

| Rank | Source | What it is |
| --- | --- | --- |
| official-primary | [Opinions index](https://www.supremecourt.gov/opinions/opinions.aspx) | Stable index. Defines slip opinions, argued opinions, per curiam opinions, in-chambers opinions, and opinions relating to orders. |
| official-primary | [Slip opinions by term](https://www.supremecourt.gov/opinions/slipopinion/26) | Current pattern. `/25` is the prior term. |
| official-primary | [U.S. Reports](https://www.supremecourt.gov/opinions/USReports.aspx) | Preliminary prints and bound volumes. The page cites 28 U.S.C. § 411 for official publication in the Reports. |
| official-primary | [Table definitions](https://www.supremecourt.gov/opinions/definitions.aspx) | What the citation column means before pagination is final. |
| official-primary | [Orders of the Court](https://www.supremecourt.gov/orders/ordersofthecourt.aspx) | Resolves to the current term-year orders path. |
| official-primary | [GovInfo U.S. Reports collection](https://www.govinfo.gov/app/collection/usreports) | GPO collection URL. It resolved. The Court’s own page is where the print sequence is explained. |

## Structural summary

### Three stages of an opinion

The opinions index says opinions are posted on release in slip opinion format and stay in that form until they are replaced with versions edited to the usual style of the United States Reports. Updated PDFs are posted as that process continues, including preliminary prints and bound volumes.

The U.S. Reports page adds the middle and last stages. Before the bound volume, the Court releases soft-cover preliminary prints with the same materials as the Reports. Two or three preliminary prints are later combined into one bound volume. Each preliminary print has a volume number and a part number, for example Volume 577, Part 1. The Reporter of Decisions compiles the Reports. Page proofs prepared by the Court are reproduced, printed, and bound with the Government Publishing Office. Bound volumes on the Court’s site are therefore the GPO-coordinated print, in preliminary-print PDF and bound-volume PDF.

The citation column on a slip table is the permanent citation in the forthcoming preliminary print and bound volume. If the paginated opinion is not up yet, the column is the Reports volume and the preliminary-print part where the case will appear. From the 2021 Term, the Reporter’s note on a revised slip says the revised pagination makes the official Reports citation available before the book is published, and that the syllabus is prepared by the Reporter and is not part of the opinion.

### Slip-opinion URL pattern

`https://www.supremecourt.gov/opinions/slipopinion/25` is titled “Opinions of the Court - 2025.” The page says those opinions were issued during October Term 2025, October 5, 2025, through October 4, 2026, and that they are posted in slip opinion format until replaced with Reports pagination. The path segment `25` is that term year. It is not an opinion number. The segment `slipopinion` is the slip-opinion collection the paragraph describes.

`https://www.supremecourt.gov/opinions/slipopinion/26` uses the same pattern for October Term 2026, October 5, 2026, through October 3, 2027. On the capture date, October 7, 2026, that is the term in progress. The prior-term URL remains the locator for October Term 2025.

The stable index is `/opinions/opinions.aspx`, not a term number. It also separates opinions relating to orders (for example a dissent from a denial of certiorari), in-chambers opinions on applications for interim relief, and per curiam opinions.

### Orders

`https://www.supremecourt.gov/orders/ordersofthecourt.aspx` returned HTTP 200 and resolved to `/orders/ordersofthecourt/26`. That page is titled “Orders of the Court: Term Year 2026,” so the numeric segment is again the term year. `/orders/ordersofthecourt/25` also returned HTTP 200. Orders are not slip opinions. The opinions index treats writing about an order as its own category.

## Matter map

| Class | Where this corpus fits |
| --- | --- |
| Constitutional | Review of federal and, within the Court’s jurisdiction, state judgments. |
| Criminal | Final federal criminal review, and opinions relating to criminal orders. |
| Civil | Same court, civil docket. Procedure below is Title 28 and the civil rules. |
| Administrative | Review of some agency action, often after a court of appeals. |

## What is stored locally vs what still needs a live fetch

Stored here: the slip, preliminary-print, and bound-volume sequence, and the term-year URL pattern confirmed for 2025 and 2026. Not stored: any opinion, syllabus, or order. A Reports citation that is only a volume-and-part placeholder is not yet the paginated pin cite.

## Capture notes

Captured 2026-10-07. Slip paths `/25` and `/26`, the opinions index, the definitions page, the U.S. Reports page, and both orders term paths returned HTTP 200. No opinion text was copied.
