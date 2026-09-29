# Case 03 — Arm Semiconductor: Spot Economics Without Sacrificing Long-Running EDA Workloads

## Evidence boundary

**Primary source:** AWS Customer Story — Reducing Costs by 40% Using Amazon EC2 Spot Instances and Exostellar's Infrastructure Optimizer with Arm  
https://aws.amazon.com/solutions/case-studies/arm-ec2/

**Evidence grade:** A.

## SOURCE FACT

- Arm uses large-scale electronic-design-automation workloads on AWS.
- Frontend verification workloads were short-running and could use Spot broadly; backend EDA workloads were compute-intensive, stateful and could run longer than a week.
- Interruption of long-running backend jobs could force expensive reruns and create delays.
- Arm initially relied on On-Demand capacity for those backend workloads.
- In 2024 Arm implemented Exostellar Infrastructure Optimizer, which can migrate stateful workloads between Spot and On-Demand capacity while maintaining job continuity.
- The source says the solution reached production within three months.
- About 65% of backend workload runtime moved to Spot, and Arm reports about 40% lower cost for those backend EDA workloads.
- Arm was already using Savings Plans for On-Demand usage.

## Diagnose

The cost problem was constrained by workload behavior: a cheap but interruptible pricing model is not automatically suitable for stateful week-long jobs.

## Hypothesis

### OUR ANALYSIS

If interruption risk can be absorbed by an orchestration layer that preserves workload integrity, then more of a stateful workload can use lower-cost interruptible capacity without accepting the full restart risk.

## Finding

### SOURCE FACT

The published solution dynamically moves work between Spot and On-Demand capacity, allowing Arm to retain workload continuity while increasing Spot use.

### OUR ANALYSIS

This is a **workload-aware pricing-model** case. Rate optimization is valuable only when the architecture can safely tolerate the pricing model's operational characteristics.

## Solution

### SOURCE FACT

Arm used a workload orchestration/optimization product to manage Spot/On-Demand placement while continuing to use Savings Plans for applicable On-Demand consumption.

### OUR REPRODUCTION LAB

Create a synthetic batch-workload portfolio with:

- job duration and checkpointability;
- interruption tolerance;
- deadline/SLA;
- On-Demand rate;
- Spot rate distribution;
- restart penalty;
- Savings Plans effective rate;
- percentage of runtime eligible for Spot;
- failure/retry cost;
- total expected cost and completion risk.

Compare all-On-Demand, naive-Spot, mixed Spot/On-Demand and commitment-supported scenarios.

## Validation

### SOURCE FACT

Arm reports 65% of backend workload runtime on Spot and about 40% lower backend EDA cost while continuing to run the same jobs.

### OUR REPRODUCTION VALIDATION

The lab must validate both:

1. **financial:** expected/actualized simulated cost reduction;
2. **technical:** completion rate, deadline adherence and restart penalty.

A scenario that saves more money but violates job-completion requirements fails.

## Insight

The senior lesson is that pricing-model optimization and architecture are coupled. The cheapest rate is not the best choice if interruption creates greater business cost than the infrastructure saving.

## Interview transfer

Explain Spot suitability by workload, why a long-running stateful job differs from short batch work, how restart cost changes the equation, how commitment discounts coexist with Spot, and which technical/business metrics must be validated alongside savings.

## Project mapping

- Market capabilities: rate optimization, commitments, governance, unit economics.
- Labs: `08_commitments`, architecture cost tradeoff extension.
- KPIs: cost/job, successful completion %, deadline misses, Spot share, retry cost, projected vs realized simulated saving.
