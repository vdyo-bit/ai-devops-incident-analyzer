
## What to Observe?
### What changed first
- CPU Idle % dropped sharply to ~0%
- This happened before load average peaked
- Indicates CPU capacity was exhausted immediately
#### CPU was the first bottleneck, not disk or memory.

### What lagged?
- Load Average (1m) continued to rise even after CPU was saturated
- After CPU load stopped, load average decayed slowly
- Memory available recovered more gradually
#### Load is an averaged signal, not instantaneous.

### What looked scary but wasn’t?
- Load average exceeded CPU core count (~2–3)
- Memory Available dipped sharply
- Disk I/O Time showed spikes
#### All of these were secondary effects, not root causes.

### What did NOT change(key signal)?
- Node Exporter stayed UP (constant 1)
- Disk I/O Time remained low relative to saturation
- No swap activity
- System did not crash
#### The absence of change ruled out disk, memory exhaustion, and monitoring failure.

## Incident Summary
A controlled CPU saturation test was executed on a single VM by generating sustained CPU-bound workloads. The system experienced reduced responsiveness due to full CPU utilization. Monitoring services remained healthy, and the system recovered immediately after load removal.

## Initial Symptoms
- CPU Idle % panel dropped to near zero
- Load Average (1m) rose rapidly to ~3
- Shell responsiveness degraded
- Grafana panels updated normally throughout the event

## Metrics Observed (Panel-by-Panel)
### CPU Idle %
- Dropped from ~95% to 0%
- Confirmed complete CPU saturation
- Recovered immediately once load stopped

### Load Average (1m)
- Increased rapidly during CPU stress
- Peaked above CPU core count
- Decayed slowly after stress ended
#### Indicates scheduling pressure, not direct CPU usage.

### Memory Available
- Gradual decline during CPU load
- Sharp dip during peak stress
- Recovered after load ended
#### Memory pressure was secondary, not causal.

### Disk I/O Time
- Small spikes observed
- No sustained elevation
- No correlation with CPU idle collapse
#### Disk activity was incidental, not a bottleneck.

### Node Exporter Up
- Remained at 1 throughout the incident
- No monitoring gaps or exporter failures
#### Confirms observability continuity.

## Logs Observed
#### Commands reviewed:
journalctl -u node_exporter  
journalctl -u prometheus

#### Observations:
- No warnings or errors
- Services remained stable
- No kernel or system-level alerts

## False Leads
- High load average initially suggested broader system stress
- Memory available drop appeared alarming
- Disk I/O spikes looked suspicious
All were ruled out after correlating CPU Idle % with other panels.

## Root Cause
The root cause was intentional CPU saturation caused by running multiple CPU-bound background processes (yes > /dev/null) equal to the number of available CPU cores.

## Resolution
- CPU stress processes were terminated
- CPU Idle % immediately returned to baseline
- Load average decayed naturally
- No service restarts were required

## Lessons Learned
- CPU saturation is visible in metrics before users feel slowness
- Load average reflects demand, not usage
- Memory dips during CPU stress are often normal
- Disk metrics are essential to eliminate false assumptions
- Observing what does not change is often the fastest diagnostic shortcut

## Final Review: What an Engineer Could Misread  
|Misleading Conclusion|Why It’s Wrong|
| :--- | :--- |
| “Disk caused the issue”  |   Disk I/O remained low   |
| “Memory leak exists”     |   Memory recovered post-load | 
| “System was unstable”    |   Exporter stayed UP  |
| “Load = CPU usage”       |   Load includes waiting tasks |

## Final Takeaway
This dashboard correctly identified CPU saturation as the sole bottleneck while preventing misdiagnosis by correlating CPU, load, memory, disk, and exporter health.  
This incident demonstrates how correlating multiple node-level metrics prevents false root cause attribution during CPU saturation events.
