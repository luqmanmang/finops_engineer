# Case 02 — ExxonMobil: AWS OLA, Rightsizing, Licensing and Independent Validation

## Evidence boundary

**Primary source:** AWS Migration & Modernization — How ExxonMobil reduced cloud costs with an AWS OLA  
https://aws.amazon.com/blogs/migration-and-modernization/how-exxonmobil-reduced-cloud-costs-with-an-aws-ola/

**Evidence grade:** A.

## SOURCE FACT

- ExxonMobil operated a mix of on-premises and cloud workloads where reliability-oriented provisioning, low utilization and licensing complexity created cost pressure.
- The AWS Optimization and Licensing Assessment addressed compute/storage efficiency, licensing economics and database modernization.
- The source identifies underutilized compute, licensing misalignment, Availability Zone effects on Dedicated Host/SQL licensing, limited visibility and an approaching Exadata refresh as drivers.
- The engagement evaluated rightsized EC2/RDS mappings, Single-AZ consolidation for eligible lower-criticality workloads while preserving stronger resilience where required, and Oracle modernization options.
- After the assessment, ExxonMobil performed a rightsizing initiative on AWS workloads.
- ExxonMobil independently validated results using AWS Cost and Usage Reports. The source states that realized savings aligned closely with AWS Compute Optimizer projections.
- AWS provided Athena queries/methodology support; the intent was to leave ExxonMobil able to continue optimization independently.

## Diagnose

**Source-backed problem:** cost inefficiency was multi-dimensional: compute utilization, licensing, resilience topology, visibility and technology-refresh economics.

The source demonstrates why a senior FinOps diagnosis should avoid reducing every problem to "find idle VMs."

## Hypothesis

### OUR ANALYSIS

A structured assessment that combines utilization data, licensing constraints, architecture/resilience requirements and modernization alternatives should reveal savings that simple instance-rightsizing alone would miss.

## Finding

### SOURCE FACT

The source describes opportunities across EC2/RDS sizing, SQL Server licensing/topology, Oracle modernization and other infrastructure layers. It also states that eligible lower-criticality workloads could use different resilience choices while stricter workloads retained stronger recovery posture.

### OUR ANALYSIS

The central pattern is **optimize within workload requirements**, not optimize cost in isolation. Availability/recovery objectives are constraints in the decision model.

## Solution

### SOURCE FACT

AWS OLA plus partner analysis provided data-driven recommendations; ExxonMobil then executed further rightsizing and performed its own CUR-based validation.

### OUR REPRODUCTION LAB

Build a synthetic estate containing:

- instance type / utilization / hours / cost;
- workload criticality and recovery requirement;
- license model and core count;
- storage/database option;
- provider recommendation;
- workload-owner decision;
- projected saving;
- implementation date;
- comparable post-period cost;
- realized saving.

## Validation

### SOURCE FACT

Independent CUR analysis is the strongest evidence in this case: realized savings were checked against recommendation projections rather than accepted from the recommendation engine alone.

### OUR REPRODUCTION VALIDATION

A recommendation does not become `realized` until:

1. technical health/SLA remains acceptable;
2. comparable pre/post cost is reconciled;
3. demand/rate changes are controlled or explained;
4. workload owner signs off;
5. the result is traceable to the implemented change.

## Insight

The interview-grade lesson is not "use Compute Optimizer." It is: **combine provider recommendations with workload constraints, licensing/architecture economics and independent billing validation**.

## Interview transfer

Be ready to explain why a low-utilization system may still require capacity, why Single-AZ can be unacceptable for some workloads, how licensing changes the TCO equation, how to validate projected savings independently, and why realized savings should be separated from recommendations.

## Project mapping

- Market capabilities: governance, rightsizing, cost visibility, cost analysis, vendor/provider collaboration.
- Labs: `03_rightsizing`, `06_storage_lifecycle`, architecture/TCO extension.
- Evidence: before/after billing, SLA, owner approval, rollback, recommendation vs realized comparison.
