# Resume-to-Market Gap Analysis

## Scope and privacy boundary

This artifact compares the verified 2026-09-30 Malaysia `FinOps Engineer` snapshot against a privately reviewed, versioned `MASTER_RESUME_Raja_Luqman.md` baseline.

The public repository intentionally stores only capability-level conclusions. It does **not** copy personal contact details or private resume text.

Market limitation: **N = 7** active unique exact-title vacancies. One vacancy changes frequency by approximately **14.29 percentage points**.

## Current transfer strengths

The resume already provides strong technical foundations for a technical FinOps Engineer path:

- Python, PySpark/Pandas, SQL and Bash.
- AWS and Azure engineering.
- Terraform and GitHub Actions CI/CD.
- Power BI, DAX, Power Query and governed BI delivery.
- ETL/ELT, dimensional modelling, reconciliation and data quality.
- Production RCA and monitoring patterns.
- Snowflake, Databricks and Microsoft Fabric.
- Workload/performance optimization patterns such as partition pruning, Z-Ordering, Delta compaction and Snowflake auto-suspend / credit controls.

These are **transfer assets**, not evidence of FinOps mastery.

## Gap matrix

| Market capability | Demand | Resume state | Gap to close | Proof artifact |
|---|---:|---|---|---|
| Governance | 7/7 | Partial | Technology-spend policy, risk thresholds, exception paths, commitment policy, governance cadence | `10_cicd_guardrail`, guardrail catalogue, RACI, compliance KPI |
| Forecasting | 6/7 | Gap | Cost forecast model, business-driver forecast, variance threshold, reforecast cadence | `09_forecast`, SQL/Python forecast evidence, Power BI forecast vs actual |
| Budgeting | 5/7 | Gap | Budget ownership, thresholds, forecast-vs-budget, escalation and action path | `02_budget_alert`, operating cadence |
| Chargeback | 5/7 | Gap | Invoice reconciliation, shared-cost rules, internal billing/accounting workflow | Gold allocation model + Power BI chargeback view |
| Rightsizing | 5/7 | Partial | Utilization decision rules, owner approval, SLA guardrail, rollback, realized savings validation | `03_rightsizing` |
| Showback | 5/7 | Partial | Cloud-cost ownership model and action-oriented reporting | Gold model + Power BI persona views |
| Allocation | 4/7 | Partial | Account/subscription/tag hierarchy, shared-cost allocation, allocation coverage KPI | `01_tagging`, Gold model |
| Cost visibility | 4/7 | Partial | Provider billing grain, effective/amortized cost, freshness and reconciliation | FinOps data pipeline |
| Reserved Instances | 4/7 | Gap | Coverage/utilization, break-even, term risk, expiry and approval controls | `08_commitments` |
| Tagging | 4/7 | Partial | Cost-allocation tag policy, inheritance, enforcement and exceptions | `01_tagging`, `10_cicd_guardrail` |
| Anomaly management | 3/7 | Partial | Cost-specific baselines, materiality thresholds, owner routing and financial validation | anomaly/RCA extension |
| Savings Plans | 3/7 | Gap | Stable-usage model, lookback sensitivity, coverage/utilization, lock-in risk | `08_commitments` |
| Cost analysis | 2/7 | Strong | Provider billing semantics and FinOps KPI vocabulary | SQL/Python + Power BI |
| Procurement | 2/7 | Gap | Commercial options, contract/commitment risk and approval ownership | recommendation quality gate + commitment lab |
| Unit economics | 2/7 | Partial | Cost per product/transaction/outcome tied to business drivers | Gold KPI model + Power BI |
| Vendor management | 2/7 | Gap | Renewal/obligation tracking, pricing alternatives and realized-value review | recommendation quality gate |

## Highest-priority build order

1. **Forecasting** — high demand and no direct resume proof.
2. **Budgeting** — high demand and no direct technology-budget operating proof.
3. **Chargeback / shared-cost allocation** — high demand and major finance-facing gap.
4. **FinOps governance** — highest market frequency; technical governance must be translated into spend governance.
5. **Rightsizing with SLA validation** — strong technical transfer, but needs cost/owner/business validation.
6. **Commitment strategy** — RIs/Savings Plans, coverage/utilization and commercial risk.
7. **Showback / ownership reporting** — leverage existing Power BI strength.
8. **Anomaly RCA and realized savings validation** — transfer monitoring/RCA into cost-specific operating evidence.

## What does not need to be relearned from zero

- SQL and Python fundamentals.
- ETL/ELT architecture.
- dimensional modelling.
- CI/CD fundamentals.
- Terraform fundamentals.
- Power BI fundamentals.
- general RCA and data-quality methodology.

The learning path should instead apply those existing skills to cloud cost and usage data, financial semantics, owner/accountability models and post-change validation.

## Certification interpretation

The N=7 snapshot shows FinOps Practitioner certification language in 5/7 vacancies. Certification is therefore useful for vocabulary and screening, but the project priority remains:

```text
job competence
> hands-on proof
> interview readiness
> certification
```

## Completion criterion

This gap analysis is considered closed only when the high-priority gaps have reproducible repo evidence and can be explained using:

`WHAT → WHY → WHEN → HOW → TRADEOFF → VALIDATION → BUSINESS IMPACT`.
