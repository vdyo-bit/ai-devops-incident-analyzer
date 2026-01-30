## Purpose
The dashboard provides a high-level health view of a single Linux VM by visualizing core node-level signals: CPU availability, memory pressure, disk activity, system load, and exporter availability.  
Its goal is situational awareness, not deep root-cause analysis.

## Purpose of Each Panel
### Node Exporter Up
#### Why it exists:
- Confirms that monitoring itself is functioning
- Distinguishes between “system is healthy” and “monitoring is broken”
#### What it tells me:
- 1 → exporter reachable
- 0 → data gap, not necessarily system failure

### CPU Idle %
#### Why it exists:
- Shows how much CPU capacity is available
- Helps identify sustained CPU pressure vs idle headroom
#### What it tells me:
-High idle → CPU not a bottleneck
-Sudden drops → CPU-bound workload or contention

### Memory Available
#### Why it exists:
- Indicates real memory pressure
- Avoids misleading “free memory” interpretation
#### What it tells me:
- Gradual decline → cache growth or workload increase
- Sharp drops → possible memory spikes or leaks

### Disk I/O Time
#### Why it exists:
- Shows when the disk is busy, not just when data is transferred
- Useful for correlating load spikes with I/O activity
#### What it tells me:
- Spikes → disk saturation periods
- Near-zero → disk not a bottleneck

### Load Average (1m)
#### Why it exists:
- Represents system demand
- Captures runnable and blocked processes
#### What it tells me:
- Load rising with CPU idle → I/O wait or blocking
- Load rising with low idle → CPU contention

## Dashboard Design Choices
#### Why these panels were chosen
- They represent orthogonal system resources:
  - CPU
  - Memory
  - Disk
  - Scheduling pressure
- Each panel answers a different “is this a bottleneck?” question
- Minimal set avoids noise and overfitting
#### Why other panels were intentionally excluded
- No per-process metrics → avoids early complexity
- No network panels → not required for initial node health
- No alerts → focus on understanding behavior, not reacting

## Common Misinterpretations (Very Important)
❌ “CPU is healthy because idle is high”  
- High CPU idle does not mean the system is fast  
- Workloads may be blocked on disk or locks

❌ “Low memory available means we’re about to crash”  
- Linux aggressively uses memory for cache  
- Low available memory alone is not an emergency

❌ “Disk I/O time spike means disk is slow”  
- It only shows the disk was busy  
- Does not indicate latency or throughput

❌ “Load is low, so system is fine”  
- Load average hides per-process pain  
- A single critical process may still be stalled

## What This Dashboard Cannot Show (Blind Spots)
❌ Exact Root Cause  
- Cannot tell which process caused CPU or memory pressure  
- Requires logs, tracing, or per-process metrics

❌ User or Business Impact  
- No application-level latency or error rates  
- No correlation to real user experience

❌ Intent  
Cannot distinguish:  
- Expected batch job
- Misconfiguration
- Runaway process

❌ Short-lived spikes
- Scrape intervals may miss very brief events
- High-resolution debugging requires other tools

## Review: Potentially Misleading Conclusions an Engineer Could Make
#### Assuming CPU is the bottleneck because load increased
- Load may be driven by I/O wait, not CPU usage
#### Blaming disk for performance issues due to I/O time spikes
- Could be normal background activity (e.g., journaling)
#### Treating memory drops as leaks
- Cache growth often looks like memory pressure
#### Assuming monitoring gaps mean system downtime
- Exporter or Prometheus restarts can cause false gaps

## Summary
This dashboard is intentionally simple and conservative.  
It answers the question:  
  “Is this node generally healthy, and which resource deserves deeper investigation?”  
It is a starting point, not a diagnostic endpoint.  
#### This dashboard provides a minimal but effective node health overview while explicitly acknowledging its limitations and the need for deeper investigation tools.
