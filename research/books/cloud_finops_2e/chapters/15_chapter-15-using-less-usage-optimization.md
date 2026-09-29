# Chapter 15 — Chapter 15. Using Less: Usage Optimization

> **Role:** Derived textbook source-of-truth note.  
> **Book source locator:** `OEBPS/ch15.xhtml`  
> **Source word count:** 10,797  
> **Source boundary:** Detailed derived note from the owned EPUB; chapter body text is not reproduced.

## 1. Chapter Brief

Chapter 15 is the book's deep treatment of **usage optimization**: reducing unnecessary resource consumption while preserving the workload's required business and technical outcomes. It covers removal, rightsizing, storage lifecycle, network cleanup, scaling, scheduling, architecture redesign, serverless, automation maturity, and savings tracking.

Its most important senior lesson is that utilization data is not enough by itself. A low average CPU value does not automatically mean a resource is oversized, and an apparently idle resource is not automatically waste. Recommendations need workload shape, peaks, memory/network/storage requirements, performance/SLA context, seasonality, architecture dependencies, and owner validation.

For this project, rightsizing appears in **5/7** vacancies, making Chapter 15 a P0/deep capability.

## 2. Why This Chapter Matters

The learner already has performance optimization experience. The FinOps gap is to turn performance evidence into a safe economic decision:

```text
technical utilization
+ workload/SLA context
+ resource price
+ business value
+ owner approval
→ usage optimization decision
```

A technically smaller resource that causes batch overruns or availability incidents is not a successful FinOps outcome.

## 3. Source Section Map

- Chapter 15. Using Less: Usage Optimization `[OEBPS/ch15.xhtml]`
- The Cold Reality of Cloud Consumption
- Where Does Waste Come From?
- Usage Reduction by Removing/Moving
- Usage Reduction by Resizing (Rightsizing)
- Common Rightsizing Mistakes
- Relying on Recommendations That Use Only Averages or Peaks
- Failing to Rightsize Beyond Compute
- Not Addressing Your Resource “Shape”
- Not Simulating Performance Before Rightsizing
- Hesitating Due to Reserved Instance Uncertainty
- Going Beyond Compute: Tips to Control Cloud Costs
- Block Storage
- Object Storage
- Networking
- Usage Reduction by Redesigning
- Scaling
- Scheduled Operations
- Effects on Reserved Instances
- Benefit Versus Effort
- Serverless Computing
- Not All Waste Is Waste
- Maturing Usage Optimization
- Advanced Workflow: Automated Opt-Out Rightsizing
- Tracking Savings
- Conclusion

## 4. Core Concepts

### 4.1 Waste is contextual

Waste can originate from abandoned resources, overprovisioning, poor scheduling, wrong storage tier, excess IOPS, inefficient data transfer, architecture choices, or temporary environments that became permanent.

But the absence of visible activity is not enough to prove waste. Resilience, backup, DR, test windows, compliance, or rare critical workloads may justify low utilization.

### 4.2 Rightsizing is multi-dimensional

CPU alone is insufficient. Consider:

- CPU distribution and peaks,
- memory,
- network,
- disk throughput/IOPS,
- concurrency,
- latency,
- request patterns,
- burst credits,
- resource-family shape,
- failure/resilience headroom.

### 4.3 Average and peak can both mislead

Average utilization can hide brief critical peaks. Peak alone can overstate normal requirements. Use percentiles, time distribution, seasonality, and workload-specific SLOs.

### 4.4 Optimize beyond compute

Storage and networking can be material:

- orphaned volumes,
- zero-throughput/IOPS storage,
- overprovisioned premium volumes,
- excessive retention,
- wrong object-storage tier,
- unused addresses,
- inefficient network routes/egress.

### 4.5 Remove, resize, schedule, scale, redesign

Usage optimization is broader than downsizing:

```text
remove
move/tier
resize
schedule
scale dynamically
redesign architecture
```

### 4.6 Benefit versus effort

A RM50/month saving requiring a week of engineering may be lower priority than a RM20k/month safe automation. Optimization backlog should consider materiality, effort, risk, repeatability, and strategic benefit.

### 4.7 Automation maturity

Mature organizations may move from recommendation-only to opt-in or opt-out automated rightsizing. This should happen only after recommendation quality, rollback, exceptions, and trust are strong.

## 5. Detailed Explanation

### 5.1 Idle-resource removal

The safest opportunities often have strong evidence of no required activity and clear owner confirmation. Even then, use a staged process:

```text
identify
→ owner notification
→ dependency check
→ quarantine/stop where possible
→ observation
→ delete
→ validate cost disappears
```

### 5.2 Rightsizing process

A robust rightsizing candidate includes:

- observation window,
- P50/P95/P99 utilization,
- workload schedule,
- recommended target shape,
- projected cost difference,
- SLA/performance risk,
- owner,
- rollback plan,
- confidence.

### 5.3 Resource shape matters

A workload might need high memory but little CPU. Moving to a smaller general-purpose instance can create memory pressure even though CPU appears low. Select a resource family that matches workload shape before reducing size.

### 5.4 Simulate or test performance

Before production resizing, use load tests, canaries, lower-environment tests, historical headroom analysis, or controlled change windows. The expected saving is not worth an outage.

### 5.5 Storage lifecycle

Object storage should have retention and lifecycle aligned with data value/access frequency. Block storage should be reviewed for orphaning, provisioned IOPS, size and performance tier.

### 5.6 Scheduling and scaling

Non-production resources often have predictable idle windows. Scheduling can create high-confidence savings with low architecture change. Autoscaling can better match demand but needs stable scaling signals and bounds.

### 5.7 Rightsizing can affect commitments

Reducing or changing resource families can alter RI/Savings Plan coverage/utilization. Usage optimization should normally precede major commitments, or commitment economics must be recalculated after the change.

### 5.8 Tracking realized outcomes

Do not use provider “potential savings” as realized savings. Compare an appropriate post-change period with a normalized baseline, accounting for demand/rate changes.

## 6. Examples

### 6.1 Average CPU trap

Workload A: 5% CPU most of the day, but 95% for a 20-minute settlement job with a hard deadline.

Average says downsize; SLA context says test carefully because the short peak may be critical.

### 6.2 Shape mismatch

Current resource:

```text
8 vCPU / 64 GB RAM
CPU P95 = 20%
Memory P95 = 85%
```

Dropping to a smaller balanced shape could fail. Better option may be memory-optimized family with fewer CPUs and similar RAM.

### 6.3 Dev scheduling

A development cluster needed weekdays 08:00–20:00 can be stopped nights/weekends with owner override. This is often safer than aggressive production rightsizing.

### 6.4 Storage lifecycle

Logs required hot for 30 days and retained 365 days do not need to remain in the most expensive hot tier for the entire year.

## 7. Justification / Why the Approach Works

### SOURCE-DERIVED RATIONALE

Cloud makes unused consumption financially removable. However, usage decisions are tightly coupled to workload behavior, so workload owners and performance evidence are essential.

### PROJECT ANALYSIS

This maps naturally to performance engineering: optimization should be hypothesis-driven, tested, measured, rolled back if necessary, and validated across both cost and SLA.

## 8. Senior FinOps Approach

1. Rank material cost/usage hotspots.
2. Map owner and workload criticality.
3. Collect multi-dimensional utilization.
4. Cover representative peaks/seasonality.
5. Classify remove/resize/schedule/scale/redesign options.
6. Quantify projected value and effort.
7. Evaluate SLA/reliability and commitment interactions.
8. Validate with workload owner.
9. Test/simulate where needed.
10. Implement with rollback.
11. Validate technical health.
12. Compare normalized post-change cost.
13. Record realized outcome.
14. Add recurrence automation/guardrail.

## 9. Step-by-Step Execution

```text
COST HOTSPOT
→ OWNER / WORKLOAD
→ UTILIZATION + SHAPE
→ TIME / SEASONALITY
→ SLA / RESILIENCE
→ OPTIONS
→ BENEFIT / EFFORT / RISK
→ TEST / SIMULATE
→ APPROVAL
→ CHANGE + ROLLBACK
→ TECH VALIDATION
→ FINANCIAL VALIDATION
→ BUSINESS VALIDATION
→ GUARDRAIL
```

## 10. Decision Rules

- Never rightsize from average CPU alone.
- Use multiple resource dimensions and representative windows.
- Prefer remove/schedule when evidence is high-confidence and business need absent.
- Optimize obvious waste before increasing commitments.
- Do not change production without owner/SLA validation.
- Automate only after recommendation precision and rollback are proven.
- Rank by realized-value potential relative to effort and risk.

## 11. Trade-offs

| Option | Benefit | Risk |
|---|---|---|
| Downsizing | lower cost | performance/headroom loss |
| Scheduling | strong non-prod saving | availability-window mismatch |
| Autoscaling | demand alignment | complexity/thrashing/cold-start risk |
| Storage tiering | lower retention cost | retrieval latency/fees |
| Redesign/serverless | potentially large efficiency | migration effort/vendor/runtime tradeoffs |
| Automated remediation | scale/low manual effort | bad logic scales quickly |

## 12. Failure Modes / Edge Cases

- averages/peaks used without distribution context,
- CPU-only recommendation,
- wrong resource-family shape,
- no load/performance simulation,
- commitment constraints ignored,
- orphan storage deleted without dependency check,
- lifecycle policy ignores retrieval cost,
- theoretical savings counted as realized,
- automation introduced before trust/exception workflow,
- “idle” resources needed for DR or rare events.

## 13. Data Required

- resource cost/effective rate,
- CPU/memory/network/storage metrics,
- timestamps/seasonality,
- resource family/shape,
- owner/application/environment,
- workload schedule,
- SLA/SLO,
- business-volume data,
- commitment coverage,
- recommendation/action/validation history.

## 14. SQL / Python / IaC Application

### SQL

Rank cost hotspots, join utilization, calculate percentiles, idle windows, cost-per-unit and before/after comparison.

### Python

Recommendation scoring, time-series utilization analysis, benefit/effort ranking, simulation and evidence generation.

### IaC / CI-CD

Scheduled controls, default sizing, storage lifecycle, autoscaling bounds, expiry/TTL, policy tests and safe modules.

## 15. Provider Implementation

### AWS / Azure

Use native rightsizing/optimization recommendations as candidate evidence, then validate with workload metrics and owner context.

### Fabric

Capacity/workload optimization should consider throttling, peak windows and business deadlines rather than cost alone.

### Snowflake

Warehouse sizing, auto-suspend, query/workload optimization and resource monitors are usage levers.

### Databricks

Cluster/serverless sizing, autoscaling, job schedules and workload efficiency are usage levers; validate using billing and workload telemetry.

## 16. Stakeholder Perspective

- Engineering owns operational safety and many usage changes.
- Finance validates financial effects.
- Procurement becomes relevant if usage change alters commitment strategy.
- Leadership sets risk/materiality priorities.
- FinOps enriches and prioritizes opportunities.

## 17. Validation

- **Technical:** latency, throughput, error rate, job duration, SLA/SLO.
- **Financial:** normalized comparable cost after change.
- **Business:** required workload outcome preserved.
- **Operational:** no repeated manual waste pattern.

## 18. KPIs

- idle-cost value,
- rightsizing potential,
- recommendation acceptance rate,
- realized usage reduction,
- cost per business unit,
- SLA guardrail compliance,
- repeat-waste rate,
- automated-safe action coverage.

## 19. Guardrails

### Preventive

sane defaults, TTL, schedules, autoscaling bounds, lifecycle policy.

### Detective

idle/orphan scans, utilization thresholds, stale resource reports.

### Corrective

stop/delete/resize/tier with owner, exception, rollback and validation.

## 20. Real-World Implications

ExxonMobil's published AWS OLA case is a strong project anchor for rightsizing and related optimization analysis. The source does not justify copying its undisclosed architecture; it supports the pattern of evidence-driven optimization and measured outcomes.

## 21. FinOps Framework 2026 Reconciliation

### Status: **CURRENT — Usage Optimization**

The current Framework capability is **Usage Optimization**, with related Architecting & Workload Placement, Governance Policy & Risk, and Automation concepts. The book's “using less” mental model remains directly useful.

## 22. Malaysia N=7 Market Relevance

Rightsizing = **5/7 (71.43%)**. Automation/CI-CD each appear in 3/7. This is P0 and should be one of the strongest hands-on interview proofs.

## 23. Lab Mapping

`03_rightsizing` must include:

- synthetic multi-metric utilization,
- misleading-average case,
- shape mismatch,
- seasonal peak,
- SLA metadata,
- commitment interaction,
- accept/defer/reject workflow,
- before/after validation,
- realized-savings evidence.

Extensions: `05_idle_compute`, `06_storage_lifecycle`, `07_transfer`.

## 24. Power BI Mapping

Show:

```text
cost hotspot
→ utilization evidence
→ candidate option
→ projected value
→ owner/status
→ technical validation
→ realized financial outcome
```

Do not label every recommendation as savings.

## 25. Interview Mapping

### 30-second answer

I treat rightsizing as a workload-safety decision, not a CPU-average exercise. I look at CPU, memory, network, storage, percentiles, peaks, seasonality and SLA, choose the right resource shape, validate with the owner, test if needed, implement with rollback, then compare normalized post-change billing before calling the saving realized.

### 2-minute answer

For a rightsizing opportunity I first rank material spend and map the workload owner. I use a representative window and multiple utilization dimensions because average CPU can hide short critical peaks and a workload may be memory-bound. I compare remove, resize, schedule, autoscale or redesign options, account for commitment effects, and quantify value versus effort and risk. Production changes need workload-owner/SLA validation and a rollback. After implementation I confirm latency, throughput or batch SLA and compare equivalent billing periods, separating demand/rate changes. Only then do I record realized value and add a recurrence guardrail.

### Senior follow-up

**WHAT:** reduce unnecessary technology usage safely.  
**WHY:** cloud unused consumption remains financially actionable.  
**WHEN:** after trusted Inform context.  
**HOW:** evidence → options → owner → safe change → validation.  
**TRADEOFF:** cost versus performance/reliability/effort.  
**VALIDATION:** technical + financial + business.  
**BUSINESS IMPACT:** sustainable efficiency without SLA damage.

## 26. Key Takeaways

1. Usage optimization is broader than downsizing.
2. Not all low utilization is waste.
3. CPU averages or peaks alone are unsafe recommendation inputs.
4. Resource shape and all major bottleneck dimensions matter.
5. Simulate/test performance before risky changes.
6. Storage/network/lifecycle matter alongside compute.
7. Usage optimization can change commitment economics.
8. Prioritize benefit versus effort and risk.
9. Mature automation needs trust, exceptions and rollback.
10. Potential savings become realized only after validated implementation.

## 27. Source Locator

- EPUB file: `OEBPS/ch15.xhtml`
- Primary source sections used: waste sources, removal, rightsizing mistakes, shape/performance, storage/network, redesign/scaling/scheduling, commitment interactions, effort/value, automation maturity, savings tracking.
