# Malaysia FinOps Engineer Census Search Notes

## Snapshot

- Research date: **2026-09-30**
- Requested target: **up to 50**
- Inclusion rule: currently active Malaysia vacancy whose observed title contains the contiguous phrase `FinOps Engineer` (case-insensitive).
- Raw candidate records retained: **9**
- Evidence records retained: **9**
- Current verified active unique canonical population: **7**
- Rejected/non-canonical records: **2** — one active duplicate syndication and one inactive posting.
- Coverage: **7 / 50**

The target is an upper bound, not a quota to pad. Under the locked Source-of-Truth rule, the census stops at the source-verifiable `N` when fewer than 50 unique active qualifying vacancies can be verified.

## Research approach

Discovery used repeated broad public-web searches and direct verification against accessible employer and job-platform pages. Search patterns covered the exact phrase `FinOps Engineer`, `Senior FinOps Engineer`, `Lead FinOps Engineer`, `Cloud FinOps Engineer`, and other titles containing the same contiguous phrase, combined with Malaysia, Kuala Lumpur, Selangor, Cyberjaya, Penang and Johor.

The search pass covered official employer career pages plus indexed sources including LinkedIn, Indeed, JobStreet, Jora, Maukerja, Ricebowl and other regional job indexes. Company/recruiter-specific searches were also used after candidate discovery. Results were reconciled by employer, requisition/job ID, title, location and materially matching role content so mirrors were not counted as independent demand.

A dedicated cross-source recheck was then run for **JobStreet Malaysia, Indeed Malaysia, Google Careers and Google-indexed public-web results**. Its evidence matrix is stored in `market/SOURCE_CROSSCHECK_2026-09-30.md`. This pass confirmed that platform absence is not equivalent to vacancy inactivity and that different FinOps requisitions from the same employer must not be silently conflated.

Every canonical vacancy requires a matching record under `market/evidence/` confirming active state, title and Malaysia scope at the collection snapshot.

## Included active unique opportunities

| ID | Company | Observed title | Primary verification source |
|---|---|---|---|
| MY-FE-0001 | ExxonMobil | FinOps Engineer | ExxonMobil Careers — Kuala Lumpur |
| MY-FE-0002 | NTT DATA Services | FinOps Engineer | NTT DATA Careers / JobStreet — Kuala Lumpur |
| MY-FE-0003 | Xsolla | FinOps engineer | Xsolla Lever Careers — Kuala Lumpur among hiring locations |
| MY-FE-0006 | International SOS | FinOps Engineer | LinkedIn direct-employer posting — Kuala Lumpur; public employer-careers visibility conflict documented |
| MY-FE-0007 | Coforge | FinOps Engineer | Direct LinkedIn job ID 4445718197 — Kuala Lumpur; Indeed has a separate FinOps Analyst requisition |
| MY-FE-0008 | Encora | Cloud Project Manager – FinOps engineer | Current regional job-board listing — Kuala Lumpur |
| MY-FE-0009 | Softenger | FinOps Engineer | Current regional listing + Softenger recruiter signal — Kuala Lumpur |

## Rejected / non-canonical records

| ID | Company | State | Reason |
|---|---|---|---|
| MY-FE-0004 | Agensi Pekerjaan JobScoper Sdn. Bhd. | Active | Duplicate/syndicated representation of the International SOS underlying vacancy; retained for audit but excluded from market frequencies |
| MY-FE-0005 | Net2Source Inc. | Inactive | Posting explicitly showed that it was no longer accepting applications at verification time |

## De-duplication decisions

- **International SOS / JobScoper:** the agency post explicitly describes a global medical and travel security services client and materially matches the direct International SOS role. International SOS is canonical; JobScoper is retained as `duplicate_of = MY-FE-0006`. The dedicated recheck found that International SOS's public careers list did not surface the role while LinkedIn still surfaced the exact-title requisition, so this source-visibility conflict is recorded rather than hidden.
- **ExxonMobil:** MyPetroCareer and other indexed copies were treated as mirrors of the official ExxonMobil vacancy, not extra demand. JobStreet and Indeed independently corroborated the exact-title Kuala Lumpur role.
- **Xsolla:** aggregators were reconciled to the active Xsolla Lever posting. Indeed also surfaced the FinOps engineer opening. A separate Xsolla FinOps posting scoped to CIS/Baku/Serbia is not a Malaysia vacancy and is not counted.
- **Coforge:** direct LinkedIn job ID `4445718197` remained live with the exact title `FinOps Engineer`. Indeed currently surfaces a separate `FinOps Analyst (Hybrid Infrastructure)` role; the two are separate requisitions, so the Analyst role does not invalidate or replace the Engineer requisition.
- **Net2Source:** multiple recruiter postings with materially identical requirements were not multiplied; the verified listings were inactive.
- **NTT DATA:** JobStreet showed duplicate employer-name renderings with materially identical role text. Those are treated as one underlying requisition.
- **NTT DATA / Softenger:** the roles have overlapping insurance-sector AWS/OCI FinOps requirements, but separate employers and no confirmed shared requisition or explicit syndication relationship were found, so each remains a separate canonical vacancy.

## Dedicated JobStreet / Indeed / Google result

The dedicated major-source pass did **not** reveal a hidden population approaching 50 unique qualifying roles. It primarily:

- corroborated ExxonMobil and NTT DATA on JobStreet;
- corroborated ExxonMobil and Xsolla on Indeed;
- exposed the separate Coforge `FinOps Analyst` and `FinOps Engineer` requisitions;
- confirmed that Google Careers is Google's own employer portal, not a universal job-board population source;
- used Google-indexed public-web discovery only as supporting discovery, never as a reason to duplicate a requisition.

See `market/SOURCE_CROSSCHECK_2026-09-30.md` for the per-vacancy matrix.

## Search saturation result

After the broad title/location/job-board pass, dedicated JobStreet/Indeed/Google pass, title-variant pass, company/recruiter follow-up, and duplicate reconciliation, newly surfaced results repeatedly resolved to the same known requisitions, inactive Net2Source posts, adjacent-title roles, or mirrors of canonical vacancies. No additional unique active Malaysia vacancy satisfying the locked contiguous-title rule could be source-verified in the accessible public snapshot.

Therefore **Checkpoint 1 closes at verified `N = 7`, not 50**. This is intentionally different from inventing, padding, counting mirrors, counting inactive roles, or relaxing the title rule simply to reach the requested target.

This is not a claim that no unindexed, private, login-gated, newly published or otherwise inaccessible qualifying vacancy exists. It is the reproducible verified public snapshot for **2026-09-30**.

## Evidence and copyright handling

The public repository stores structured source facts, named technologies, qualifications and concise verification evidence. Long vacancy descriptions are paraphrased rather than copied verbatim. Source URLs remain attached to each raw/evidence pair for traceability.

## Interpretation guardrail

With `N = 7`, one vacancy equals approximately **14.29 percentage points**. Frequency outputs describe this observed snapshot only and must not be presented as precise estimates of the entire Malaysia labour market.

## Reproducibility rule

Future rechecks should preserve stable vacancy IDs and source history. New unique active vacancies receive new IDs; expired or duplicate records are not recycled or silently deleted. Re-run `make market-build` after source-backed changes and require the canonical GitHub Actions quality workflow to pass before merge.
