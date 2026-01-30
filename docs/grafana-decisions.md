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
-Load rising with low idle → CPU contention
