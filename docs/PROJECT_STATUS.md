# Project Status

## Locked / implemented

- repository architecture
- vacancy population contract
- raw/evidence separation
- vacancy ID contract
- deterministic vacancy classifier
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
STATUS: LIVE RESEARCH PASS EXECUTED / CURRENT VERIFIED SNAPSHOT N = 4
Snapshot date: 2026-09-30
Target requested: up to 50 active Malaysia exact-title FinOps Engineer vacancies
Raw candidate records: 5
Evidence records: 5
Verified active unique exact-title population: 4
Rejected/non-canonical: 1 inactive
Coverage: 4 / 50
```

The current verified active population contains four unique opportunities found in the reproducible public-web research pass: ExxonMobil, NTT DATA Services, Xsolla, and Agensi Pekerjaan JobScoper. One Net2Source posting is retained as an inactive rejection so the active-status gate remains auditable.

Obvious syndications of the same underlying vacancy are not counted as separate market demand. The snapshot represents the verified population found through the documented public-source search on 2026-09-30; it does not claim that unindexed, login-gated, private, or newly published vacancies cannot exist.

Because N = 4, one vacancy moves a percentage by 25 percentage points. Use frequency tables as observed snapshot evidence, not as a stable estimate of the entire Malaysia labour market.

## CI state

GitHub-hosted Actions on `luqmanmang/finops_engineer` are operational. Checkpoint 1 builds have executed unit tests, generated market outputs, and validated the raw/evidence contracts successfully on GitHub-hosted runners.

The canonical `.github/workflows/market-census-quality.yml` remains the repository quality gate for changes to market data, census code, and tests.

## Next gate

Checkpoint 2 may use this observed snapshot for market-to-knowledge mapping, but every conclusion must carry the N = 4 limitation. Do not silently generalize a 25%, 50%, 75%, or 100% snapshot frequency into a universal Malaysia-market claim.
