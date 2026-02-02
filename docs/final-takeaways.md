## What I Learned About Linux
- CPU idle does not mean the system is healthy; processes can be blocked or contending for resources.
- Memory usage on Linux is intentionally aggressive due to caching, making “free memory” a misleading metric.
- Load average reflects system demand, not CPU utilization.
- Disk “busy time” indicates saturation, not latency or throughput.
- Many system behaviors that look alarming are normal once their semantics are understood.

## What I Learned About Observability
- Metrics answer what is happening, not why it is happening.
- Dashboards provide situational awareness but cannot replace investigation.
- Counters require rate calculations to become meaningful signals.
- Correlating multiple metrics is more important than interpreting any single panel.
- Logs, metrics, and dashboards serve different purposes and must be used together.

## What I Learned About Incident Response
- Identifying the bottleneck is not the same as identifying the root cause.
- Observing what does not change is often as valuable as observing what does.
- Fast recovery does not automatically imply a benign incident.
- Clear articulation of uncertainty is a strength, not a weakness.
- Avoiding premature conclusions prevents misdiagnosis.

## Where AI Helped
- Quickly identified known system behavior patterns.
- Acted as a second opinion to validate or challenge initial conclusions.
- Helped surface missing data and blind spots in analysis.
- Assisted in structuring post-incident documentation clearly and consistently.
- Reduced cognitive load during analysis without replacing judgment.

## Where AI Failed or Needed Guardrails
- Tended to overconfidently label symptoms as root causes early on.
- Occasionally inferred intent or causality without sufficient evidence.
- Did not always account for system-specific context or constraints.
- Required explicit instructions to avoid speculation.
- Needed human oversight to prevent oversimplified conclusions.

## How I Would Use AI in Production
- Use AI for hypothesis generation, not root cause declaration.
- Treat AI outputs as suggestions that require verification.
- Require explicit evidence mapping before accepting conclusions.
- Use AI to highlight unknowns rather than fill them in.
- Maintain clear accountability with human operators for final decisions.
