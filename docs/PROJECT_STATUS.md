# Project Status

## Locked / implemented

- repository architecture
- vacancy population contract
- raw/evidence separation
- vacancy ID contract
- deterministic vacancy classifier
- active/inactive and duplicate-underlying-vacancy gates
- canonical dataset builder
- derived frequency outputs
- certification-demand frequency output
- quality report contract
- unit-test suite
- GitHub Actions workflow definition
- practitioner-signal artifacts
- recommendation quality gate
- RACI working model
- operating cadence working model
- research questions

## Current execution state

```text
Checkpoint 1 — Vacancy Census
STATUS: CURRENT VERIFIED PUBLIC SNAPSHOT COMPLETE / SEARCH SATURATED AT N = 7
Snapshot date: 2026-09-30
Target requested: up to 50 active Malaysia exact-title FinOps Engineer vacancies
Raw candidate records: 9
Evidence records: 9
Verified active unique exact-title population: 7
Rejected/non-canonical: 2
  - 1 active duplicate/syndication
  - 1 inactive posting
Coverage: 7 / 50
```

The seven canonical opportunities are ExxonMobil, NTT DATA Services, Xsolla, International SOS, Coforge, Encora and Softenger.

The requested 50 is an upper target, not a quota. The locked population rule requires the project to stop at the source-verifiable `N` when fewer than 50 unique active qualifying vacancies are found. Broad public-web discovery, title/location variants, job-board searches, employer/recruiter follow-up and duplicate reconciliation repeatedly converged on the same requisitions. The project therefore does **not** pad the census with mirrors, inactive roles, adjacent titles, non-Malaysia roles or fabricated records.

The JobScoper record remains active evidence but is excluded from canonical frequencies because it maps to the same underlying International SOS vacancy. Net2Source is retained as an inactive rejection. Full search and de-duplication rationale is recorded in `market/CENSUS_SEARCH_NOTES.md`.

This snapshot does not claim that unindexed, private, login-gated, newly published or otherwise inaccessible vacancies cannot exist.

Because N = 7, one vacancy moves a frequency by approximately 14.29 percentage points. Use frequency tables as observed snapshot evidence, not as a precise estimate of the entire Malaysia labour market.

## CI state

GitHub-hosted Actions on `luqmanmang/finops_engineer` are operational. Checkpoint 1 builds have executed unit tests, generated market outputs, validated raw/evidence contracts and tested duplicate-vacancy handling successfully on GitHub-hosted runners.

The canonical `.github/workflows/market-census-quality.yml` remains the repository quality gate for changes to market data, census code and tests.

## Next gate

Checkpoint 2 may use the observed N = 7 snapshot for market-to-knowledge mapping. Every market-weighted conclusion must preserve the N = 7 limitation and source lineage. Do not silently generalize snapshot percentages into universal Malaysia-market claims.
