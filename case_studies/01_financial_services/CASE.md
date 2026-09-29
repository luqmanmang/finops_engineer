# Case 01 — RSA Financial Services: Procurement, Commitments, Forecasting and Allocation

## Evidence boundary

**Primary source:** Microsoft Customer Story — RSA maximizes cloud efficiency and cost savings with Microsoft commercial marketplace  
https://www.microsoft.com/en/customers/story/20026-royal-sun-alliance-ireland-azure-marketplace

**Evidence grade:** A for published production practices/outcomes explicitly stated by the named customer/provider story.

Anything not disclosed by the source is marked as such. The reproduction design below is ours and is not presented as RSA's architecture.

## SOURCE FACT

- RSA identified traditional procurement processes as a barrier to faster technology delivery.
- RSA entered a three-year Microsoft Azure Consumption Commitment (MACC), receiving an overall Azure infrastructure discount and increased visibility/control over cloud spending during the contract period.
- Legacy subscriptions and SaaS purchases were fragmented across multiple portals and spreadsheets, making budget management and visibility difficult.
- Using Microsoft commercial marketplace consolidated purchases into Azure, giving RSA a unified view of assets and a single monthly invoice.
- The source states that RSA can identify responsible owners, allocate costs to cost centers, and manage license agreements and renewals.
- The consolidated invoice improves RSA's ability to predict monthly, quarterly and annual forecasts.
- The source describes faster procurement and strategic vendor collaboration; it does not disclose a specific realized dollar-savings figure attributable solely to the FinOps controls.

## Diagnose

**Source-backed problem:** fragmented procurement/billing and slow purchasing reduced visibility, budget control and speed to market.

**Not disclosed by source:** exact original number of portals, exact allocation schema, forecast algorithm, budget variance thresholds, MACC discount percentage, internal accounting entries, or implementation architecture.

## Hypothesis

### OUR ANALYSIS

If vendor purchases, ownership metadata, commitments and billing are consolidated into a governed purchasing/billing path, then cost attribution should become more reliable, forecasting should become more stable because recurring obligations are visible, procurement cycle time may fall, commitment consumption can be managed against business demand, and Finance/Procurement/Engineering can reason from one cost view instead of reconciling disconnected sources.

This is an analytical interpretation of the source facts, not a claim that RSA used this exact causal model.

## Finding

### SOURCE FACT

The source reports that the marketplace gave RSA a unified view of purchases, owner/cost-center attribution, license/renewal management, and a consolidated monthly invoice that improved forecast predictability.

### OUR ANALYSIS

The deeper pattern is **commercial FinOps + allocation + forecasting**, not simply "buy through a marketplace." The system of record and ownership metadata matter because they reduce financial ambiguity and create a stable planning baseline.

## Solution

### SOURCE FACT

RSA used Microsoft commercial marketplace and its Azure commitment relationship to centralize technology purchasing and cloud investment management.

### OUR REPRODUCTION LAB

Build a synthetic vendor/commitment decision model with vendor/product owner, cost center, monthly committed spend, eligible spend, renewal date, realized consumption, forecast consumption, unused commitment risk, alternative purchase paths, approval owner and allocation status.

No real contract or commitment purchase is required.

## Validation

### SOURCE FACT

The customer story reports improved visibility, owner attribution, forecasting control and faster procurement outcomes. It does **not** disclose enough numeric billing data to independently recompute realized monetary savings.

### OUR REPRODUCTION VALIDATION

The lab must prove that every purchase has an owner or explicit unowned state, allocated cost reconciles to the source invoice total, commitment consumption/remaining obligation reconcile by month, forecast variance is calculated separately from commitment utilization, and no modeled saving is labeled `realized_savings` without comparable post-period evidence.

## Insight

A senior FinOps Engineer must connect procurement and vendor management to cost visibility, allocation, commitments and forecasting. Commercial optimization is not independent from data quality: fragmented purchasing creates fragmented cost data, which then weakens budgets, forecasts and accountability.

## Interview transfer

Explain how to evaluate a commitment without blindly maximizing coverage; why owner/cost-center metadata matters before chargeback; how a consolidated invoice improves forecasting without guaranteeing accuracy; where Finance/Procurement approvals fit; and how negotiated discount, projected saving and realized saving differ.

## Project mapping

- Market capabilities: forecasting, budgeting, allocation, procurement, vendor management, commitment/rate optimization.
- Labs: `08_commitments`, `09_forecast`, allocation/Gold model.
- Dashboard: commitment exposure, owner allocation, forecast variance, renewal/expiry timeline.
