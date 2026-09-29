# Chapter 10 — Chapter 10. Inform Phase: Where Are You Right Now?

> **Role:** Derived textbook source-of-truth note.  
> **Book source locator:** `OEBPS/ch10.xhtml`  
> **Source word count:** 3,569  
> **Source boundary:** Detailed derived note from the owned EPUB; chapter body text is not reproduced.

## 1. Chapter Brief

Chapter 10 explains the practical discipline of understanding the current state before trying to optimize it. Raw cost data is not enough. FinOps practitioners need business, ownership, technical, financial, and organizational context so they can ask the right questions and avoid acting on misleading signals.

The chapter emphasizes:

- data without context is weak evidence,
- stakeholder interviews are part of technical analysis,
- root cause should be understood before waste is removed,
- transparency creates a feedback loop,
- team benchmarking can help if metrics are fair,
- maturity develops gradually,
- high performers can answer complex spend/forecast questions quickly and connect them to unit economics.

## 2. Why This Chapter Matters

This chapter is effectively an RCA discipline for FinOps.

A weak response to a cost spike is:

```text
Find the biggest expensive resource and optimize it.
```

A stronger response is:

```text
What changed?
Where?
Who owns it?
Is it expected?
What business event occurred?
Is variance driven by usage or rate?
Is this actually waste?
What bottleneck or process allowed it?
```

That mindset maps directly to the user's Data Engineering RCA background and is one of the strongest transfer points into FinOps.

## 3. Source Section Map

- Chapter 10. Inform Phase: Where Are You Right Now?  `[OEBPS/ch10.xhtml]`
- Data Is Meaningless Without Context  `[OEBPS/ch10.xhtml]`
- Seek First to Understand  `[OEBPS/ch10.xhtml]`
- Organizational Work During This Phase  `[OEBPS/ch10.xhtml]`
- Transparency and the Feedback Loop  `[OEBPS/ch10.xhtml]`
- Benchmarking Team Performance  `[OEBPS/ch10.xhtml]`
- What Great Looks Like  `[OEBPS/ch10.xhtml]`
- Conclusion  `[OEBPS/ch10.xhtml]`

## 4. Core Concepts

### 4.1 Context converts data into decision evidence

A number such as `RM500,000/month` is not actionable until it is linked to:

- product/workload,
- owner,
- service/resource,
- business volume,
- budget/forecast,
- technical event,
- rate/discount state,
- SLA/business purpose.

### 4.2 Seek first to understand

The chapter explicitly advises against immediately removing discovered waste. First investigate how and why it arose. The goal is not only to reduce the current bill but to prevent recurrence.

### 4.3 Stakeholder interviews are analytical inputs

Questions to Finance, Engineering, Product/Business, and Procurement help define the correct allocation structure, reporting dimensions, and business context.

### 4.4 Transparency creates accountability

When teams can see the financial consequences of their decisions, cost becomes another operational feedback metric rather than an external Finance complaint.

### 4.5 Benchmarking needs context

Comparing teams can motivate improvement, but metrics must normalize for differences teams cannot control.

### 4.6 “Great” means speed and depth of understanding

High performers are able to:

- answer complex spend questions quickly,
- produce useful forecasts/scenarios,
- understand deployment/business impact,
- analyze unit economics,
- identify information/automation gaps,
- find optimization opportunities from granular allocation.

## 5. Detailed Explanation

### 5.1 Start with questions, not reports

Before building dashboards, determine what stakeholders need to decide.

Examples from the source's questioning approach include:

- What should we report by: product, application, cost center, business unit?
- Where does most spend come from?
- Do we need showback or chargeback?
- Which teams own major services?
- What does Finance need to forecast?
- What does Engineering consider efficient usage?

The resulting answers define the data model.

### 5.2 RCA before cleanup

If an unused resource exists, simply deleting it saves money but does not explain why it existed.

Possible root causes:

- missing TTL/expiry,
- failed deployment cleanup,
- environment lifecycle gap,
- owner left organization,
- manual test process,
- architecture requirement misunderstood,
- stale IaC state,
- backup/resilience dependency.

The corrective action depends on root cause.

### 5.3 Bottleneck thinking

Improving a non-bottleneck metric can produce little business value. The senior FinOps Engineer should identify which limitation prevents better outcomes: attribution, forecast accuracy, engineering action, commitment governance, recommendation trust, or data quality.

### 5.4 Transparency as feedback

Useful cost feedback should reach the people who control the usage while the information is still relevant. Transparency alone is not enough; the metric must include context and ownership.

### 5.5 Benchmarking without blame

A team can have a higher cloud bill because it handles more customers, stricter reliability, or a different product architecture. Better comparison can use:

- cost per business unit,
- allocation quality,
- percentage of actionable waste addressed,
- forecast accuracy,
- normalized efficiency metrics.

### 5.6 Mature Inform supports what-if analysis

The end state is not a static spend report. It is the ability to answer:

```text
What will cost become if traffic grows 30%?
What if we move region/service?
What if we change retention?
What if this deployment doubles compute?
What is cost per transaction after the change?
```

## 6. Examples

### 6.1 Orphan storage

Finding:

```text
RM20k/month unattached storage
```

Weak action:

```text
Delete volumes.
```

Senior approach:

1. Verify truly unattached/not backup dependency.
2. Identify creation source/owner.
3. Determine why cleanup did not happen.
4. Remove safely.
5. Validate billing reduction.
6. Add TTL/lifecycle/CI guardrail.

### 6.2 Cost increase after deployment

```text
Cost +25%
Transaction volume +40%
Cost per transaction -10.7%
Latency stable
```

The aggregate increase is not automatically a problem. Inform context shows efficiency actually improved.

### 6.3 Benchmarking teams

Do not rank teams only by total spend. A better comparison might include:

```text
allocation coverage
cost per request
forecast variance
realized optimization / actionable opportunity
SLA performance
```

## 7. Justification / Why the Approach Works

### SOURCE-DERIVED RATIONALE

Understanding current state and stakeholder context reduces wrong assumptions, increases trust, and reveals the actual questions an organization needs to answer.

### PROJECT ANALYSIS

This is standard root-cause engineering applied to financial telemetry. Optimizing before understanding root cause is equivalent to restarting a failed pipeline without investigating why it failed.

## 8. Senior FinOps Approach

1. Validate source data/freshness.
2. Define comparison scope and time.
3. Map ownership.
4. Interview relevant stakeholder if context missing.
5. Identify biggest variance/cost drivers.
6. Separate expected demand from unexpected change.
7. Split usage vs rate.
8. Correlate deployment/business events.
9. Evaluate unit economics.
10. Form hypothesis.
11. Validate hypothesis against evidence.
12. Only then move into Optimize.
13. Capture root cause and recurrence control.

## 9. Step-by-Step Execution

```text
QUESTION
→ DATA QUALITY
→ SCOPE / TIME
→ OWNER
→ COST DRIVER
→ USAGE VS RATE
→ BUSINESS / TECH EVENT
→ HYPOTHESIS
→ EVIDENCE TEST
→ ROOT CAUSE
→ OPTIMIZATION OPTIONS
→ ACTION
→ VALIDATION
→ PREVENT RECURRENCE
```

## 10. Decision Rules

- If ownership is unknown, fix attribution before assigning accountability.
- If current-period data is incomplete, do not compare it as final.
- If cost rises with business volume, check unit economics before declaring waste.
- If recommendation contradicts workload owner context, investigate before escalation.
- If the same issue recurs, prioritize systemic guardrail over repeated manual cleanup.

## 11. Trade-offs

| Choice | Benefit | Risk |
|---|---|---|
| Fast cleanup | quick saving | root cause persists |
| Deep investigation | recurrence prevention | delays immediate action |
| Transparent team comparison | accountability | blame/gaming if unfair |
| Detailed context | better decisions | data integration complexity |
| Simple benchmark | easy communication | hides workload differences |

A practical strategy can do low-risk containment while RCA continues.

## 12. Failure Modes / Edge Cases

- blaming the highest-spend team,
- assuming provider recommendation = root cause,
- benchmarking without workload normalization,
- deleting “unused” resources without dependency validation,
- using incomplete recent billing data,
- building allocation dimensions before asking stakeholder questions,
- fixing symptoms repeatedly without recurrence guardrail.

## 13. Data Required

- cost/usage/time,
- source completeness metadata,
- account/service/resource/SKU,
- owner/product/environment,
- utilization/performance,
- business volume/value,
- budget/forecast,
- deployment/change events,
- commitment/rate state,
- SLA/SLO,
- recommendation/action history.

## 14. SQL / Python / IaC Application

### SQL

- window-function variance,
- top-N driver decomposition,
- usage/rate split,
- cost per unit,
- orphan/unallocated resources,
- owner/team benchmarks.

### Python

- anomaly detection,
- change-point/event correlation,
- forecast/scenario,
- automated RCA evidence packs.

### IaC / CI-CD

Once root cause is known, add preventive controls such as mandatory TTL, owner tag, budget, or policy test.

## 15. Provider Implementation

Native provider cost tools can supply initial visibility, but the same Inform questions should apply across AWS, Azure, Fabric, Snowflake, and Databricks. A multicloud normalized model makes ownership/business context consistent.

## 16. Stakeholder Perspective

- Engineering supplies workload and operational context.
- Finance supplies budget/accounting/planning context.
- Business/Product supplies denominator/value context.
- Procurement supplies pricing/contract context.
- FinOps connects these into a trusted current-state model.

## 17. Validation

### Technical

Root cause should align with operational telemetry/change evidence.

### Financial

Cost-driver totals reconcile and explain material variance.

### Business

The interpretation should make sense relative to business volume/outcome.

### Organizational

Accountable owner agrees the context/action path.

## 18. KPIs

- cost-driver coverage of total variance,
- unallocated cost %,
- time-to-root-cause,
- anomaly time-to-owner,
- repeat-incident rate,
- forecast error,
- cost per unit,
- benchmark normalization coverage,
- source freshness/completeness.

## 19. Guardrails

### Preventive

ownership/TTL/tag/IaC standards.

### Detective

anomaly, unallocated spend, stale resources, forecast variance.

### Corrective

cleanup, reallocation, reforecast, policy update, automation.

## 20. Real-World Implications

The source's emphasis on blameless understanding aligns with production engineering culture: incorrect attribution or recommendations damage trust and slow future action. High-quality FinOps should make teams more willing to engage, not more defensive.

## 21. FinOps Framework 2026 Reconciliation

### Status: **CURRENT, DISTRIBUTED ACROSS MULTIPLE CAPABILITIES**

The older “Inform phase” remains a useful lifecycle concept. Current Framework work maps more specifically to Data Ingestion, Allocation, Reporting & Analytics, Anomaly Management, Forecasting, KPIs & Benchmarking, Unit Economics, and Assessment.

Use the phase to organize reasoning; use current capabilities for canonical classification.

## 22. Malaysia N=7 Market Relevance

- governance 7/7,
- forecasting 6/7,
- showback 5/7,
- allocation/cost visibility 4/7,
- anomaly management 3/7,
- cost analysis 2/7,
- unit economics 2/7.

The market expects substantial Inform capability before optimization.

## 23. Lab Mapping

Add a common RCA task to each lab:

```text
Do not reveal synthetic fault.
Learner must:
1 establish baseline
2 identify scope/owner
3 isolate driver
4 form hypothesis
5 prove root cause
6 recommend action
7 validate and guardrail
```

This supports senior transfer better than step-following labs.

## 24. Power BI Mapping

Primary Diagnose view should answer:

- what changed,
- how much,
- where,
- owner,
- usage vs rate,
- business volume,
- related event,
- data freshness.

Power BI should help formulate a hypothesis rather than immediately label something “waste.”

## 25. Interview Mapping

### 30-second answer

In the Inform stage I first make cost data trustworthy and contextual. I validate freshness and comparison periods, map ownership, identify service/resource drivers, split usage versus rate, correlate deployments and business volume, and only then form a root-cause hypothesis. I avoid jumping directly from a recommendation to remediation.

### 2-minute answer

If cloud cost increases 30%, I start by validating the comparison and data completeness. Then I isolate account/subscription, service, SKU/resource and owner; split usage and effective-rate variance; correlate deployments, seasonality and business-volume changes; and check unit economics. I involve the workload owner because low utilization or high cost may have a legitimate SLA or product reason. Once I can explain the material variance with evidence, I move into optimization options. After the change I validate technical, financial and business outcomes and add a recurrence guardrail.

### Senior follow-up

**WHAT:** current-state/context and RCA discipline.  
**WHY:** cost data alone does not explain value or root cause.  
**WHEN:** before optimization and whenever assumptions materially change.  
**HOW:** data quality → scope → owner → variance → context → hypothesis → proof.  
**TRADEOFF:** speed of action vs confidence/systemic learning.  
**VALIDATION:** variance explained and stakeholder/technical evidence agrees.  
**BUSINESS IMPACT:** fewer unsafe fixes and repeat problems.

## 26. Key Takeaways

1. Data is meaningless without context.
2. Ask stakeholder questions before designing the reporting model.
3. Seek root cause before simply removing visible waste.
4. Transparency should create a timely feedback loop to owners.
5. Benchmarking requires fair normalization.
6. High-performing Inform capability supports fast complex questions and scenarios.
7. Current capabilities classify the work more precisely than the older phase label.
8. RCA discipline is a major Data Engineering → FinOps transfer advantage.

## 27. Source Locator

- EPUB file: `OEBPS/ch10.xhtml`
- Primary sections used: context, stakeholder questions, organizational work, transparency/feedback, benchmarking, high-performance characteristics.
