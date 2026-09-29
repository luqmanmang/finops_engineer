# Final Five FinOps Case Studies

## Selection contract

The Source of Truth requires:

1. Financial Services
2. Oil & Gas / Energy
3. Semiconductor
4. Market-selected case
5. Market-selected case

Selection uses evidence quality, technical diversity, relevance to the N=7 vacancy snapshot, reproducibility and resume-gap coverage. A market-selected case is chosen to cover recurring market capabilities and engineering patterns; it does not imply the case company's industry appeared in the vacancy census.

## Final selection

| Slot | Company | Industry | Primary evidence | Why selected | Main capabilities |
|---|---|---|---|---|---|
| Financial Services | RSA | Insurance / Financial Services | Microsoft Customer Story | Named financial-services case connecting procurement, commitment, allocation, ownership, renewal and forecasting | forecasting, allocation, procurement, vendor management, commitments |
| Oil & Gas / Energy | ExxonMobil | Energy | AWS OLA case | Primary interview-driver industry; unusually strong independent CUR validation after optimization | rightsizing, cost visibility, licensing/TCO, validation, governance |
| Semiconductor | Arm | Semiconductor | AWS Customer Story | Strong workload-aware Spot/rate-optimization case with technical integrity constraints | pricing model, Spot, commitments, unit economics, workload reliability |
| Market-selected 1 | Carlsberg | Consumer goods / manufacturing | Microsoft Customer Story | Broadest published match to recurring market capabilities | governance, budgeting, forecasting, rightsizing, tagging, commitments, showback |
| Market-selected 2 | BMW Group | Automotive | AWS/BMW engineering case | Deepest data-engineering/automation transfer into FinOps anomaly/RCA at scale | anomaly management, forecasting baseline, cost data, owner routing, automation, RCA |

## Why these five work together

The set avoids five near-identical cost-cutting stories.

- **RSA** proves the commercial/financial side of FinOps.
- **ExxonMobil** proves optimization plus independent financial validation.
- **Arm** proves that cost optimization is constrained by workload behavior and reliability.
- **Carlsberg** proves a broad recurring operating model rather than a one-off optimization.
- **BMW** proves FinOps as a data/automation engineering system with scale, filtering, ownership and feedback.

Together they cover the largest resume gaps identified in `docs/MARKET_INTERPRETATION.md` while also leveraging existing Data Engineering strengths.

## Integrity rules

Every case file must contain:

```text
SOURCE FACT
OUR ANALYSIS
OUR REPRODUCTION LAB
Diagnose
Hypothesis
Finding
Solution
Validation
Insight
Interview transfer
```

Rules:

1. No invented company architecture or KPI.
2. If the source does not disclose a detail, say so.
3. Company results are not copied into our lab as if we reproduced them.
4. Our lab validates the underlying mechanism on synthetic/trial data.
5. Published percentages remain source facts; they are not expected lab outcomes.
6. Potential/projected savings remain separate from realized savings.
7. A provider recommendation is not implementation approval.

## Checkpoint status

- **Checkpoint 5 — Final Cases: COMPLETE.**
- **Checkpoint 6 — Case Dissection: COMPLETE for the five selected cases.**

Case files:

- `case_studies/01_financial_services/CASE.md`
- `case_studies/02_oil_gas_energy/CASE.md`
- `case_studies/03_semiconductor/CASE.md`
- `case_studies/04_market_selected/CASE.md`
- `case_studies/05_market_selected/CASE.md`

The next gate is to turn these patterns into reproducible labs and evidence artifacts, not to add more case prose.
