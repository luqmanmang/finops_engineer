# Malaysia FinOps Engineer Census Search Notes

## Snapshot

- Research date: **2026-09-30**
- Requested target: **up to 50**
- Inclusion rule: currently active Malaysia vacancy whose observed title contains the contiguous phrase `FinOps Engineer` (case-insensitive).
- Current verified active unique population: **4**
- Rejected candidate records retained for audit: **1 inactive**

## Research approach

Discovery used broad public-web searches and direct verification against accessible employer or job-platform pages. Search patterns included the exact phrase `FinOps Engineer` together with Malaysia, Kuala Lumpur, Cyberjaya and common seniority/title variants. Discovery covered official employer career pages and indexed job platforms including LinkedIn and regional job-board results.

Every included vacancy required a matching record under `market/evidence/` confirming active state, title and Malaysia scope at the collection snapshot.

## Included active unique opportunities

| ID | Company | Observed title | Malaysia evidence source |
|---|---|---|---|
| MY-FE-0001 | ExxonMobil | FinOps Engineer | ExxonMobil Careers — Kuala Lumpur |
| MY-FE-0002 | NTT DATA Services | FinOps Engineer | NTT DATA Careers — Kuala Lumpur |
| MY-FE-0003 | Xsolla | FinOps engineer | Xsolla Lever Careers — Kuala Lumpur listed among hiring locations |
| MY-FE-0004 | Agensi Pekerjaan JobScoper Sdn. Bhd. | Cloud FinOps Engineer | LinkedIn — Kuala Lumpur |

## Rejected candidate

| ID | Company | Reason |
|---|---|---|
| MY-FE-0005 | Net2Source Inc. | Posting explicitly no longer accepting applications at verification time |

## De-duplication decisions

- Multiple JobScoper syndications with materially identical role content were treated as one underlying vacancy rather than separate market demand.
- Near-identical Net2Source syndications were not multiplied; one inactive candidate record is retained to show the exclusion reason.
- NTT DATA and Net2Source contain substantially similar FinOps requirements, but they are separate employer postings. NTT DATA was independently verified active through its official careers site; Net2Source was independently verified inactive.

## Evidence and copyright handling

The public repository stores structured source facts, named technologies, qualifications and concise verification evidence. Long vacancy descriptions are paraphrased rather than copied verbatim. Source URLs remain attached to each raw/evidence pair for traceability.

## Limitations

This is the verified population found in the documented public-source research pass on 2026-09-30. It is not a claim that no unindexed, private, login-gated, newly published or otherwise inaccessible vacancy exists.

With `N = 4`, one vacancy equals **25 percentage points**. Frequency outputs therefore describe this snapshot only and should not be presented as precise estimates of the entire Malaysia labour market.

## Reproducibility rule

Future rechecks should preserve stable vacancy IDs and source history. New unique active vacancies receive new IDs; expired records are not recycled or silently deleted. Re-run `make market-build` after source-backed changes and require the canonical GitHub Actions quality workflow to pass before merge.
