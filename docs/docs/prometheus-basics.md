## Purpose
The purpose of this setup is to understand how node-level system metrics are collected, exposed, and visualized using node_exporter and Prometheus.
It demonstrates how low-level operating system statistics (CPU, memory, disk, load) are converted into time-series metrics that can be queried, analyzed, and correlated over time.

## Architecture
Prometheus follows a pull-based model.
The node_exporter runs on the VM and exposes system metrics over an HTTP endpoint (/metrics on port 9100).
Prometheus periodically scrapes this endpoint at a configured interval and stores the collected metrics in its time-series database.
Flow:
Linux Kernel → node_exporter → /metrics endpoint → Prometheus

## Key Metrics Observed
### CPU Metrics
- node_cpu_seconds_total
  - A cumulative counter representing total CPU time spent in different modes (user, system, idle, iowait, etc.).
- Key understanding:
  - CPU usage percentages are derived, not stored, by calculating the rate of change of this counter over time.
### 🧠 CPU — node_cpu_seconds_total
#### ❓ Why is this counter increasing?
. It is a counter that tracks total CPU time spent in different modes:
  - user
  - system
  - idle
  - iowait etc.
- As long as the system is running, CPU time always accumulates
- It never resets (except reboot)
- 👉 Even an idle CPU is still accumulating idle time.
#### ❓ How do tools derive CPU percentages from it?
- Prometheus calculates the rate of change over time
- CPU % is derived using:
  - rate(node_cpu_seconds_total[5m])
- The rate tells:
  - “How much CPU time was spent per second during this window”
- Percentages are then calculated by:
  - Grouping by CPU mode
  - Dividing by total CPU time
  - Converting to %
- 👉 CPU % is not stored — it is calculated

Memory Metrics
node_memory_MemAvailable_bytes
Memory that can be allocated immediately without swapping.
node_memory_MemFree_bytes
Memory that is completely unused.
Key understanding:
Low free memory is normal on Linux due to aggressive caching; available memory is the meaningful indicator.
Memory — node_memory_MemAvailable_bytes vs MemFree
❓ Why does “free” memory look scary but isn’t?
Linux aggressively uses RAM for:
Page cache
Buffers
This memory is reclaimable
So:
MemFree = memory doing literally nothing
MemAvailable = memory that can be used immediately
👉 Low MemFree is normal and healthy
What matters:
MemAvailable
Swap activity (si/so)

Disk Metrics
node_disk_io_time_seconds_total
Total time the disk spent servicing I/O requests.
node_disk_read_time_seconds_total
Time spent processing disk read operations.
Key understanding:
These metrics represent disk busy time, not throughput or latency.
🧠 Disk — node_disk_io_time_seconds_total
❓ What does “time spent doing I/O” really mean?
Measures how long the disk was busy
Not how much data was transferred
Not how fast it was
Includes time when:
Requests were queued
Disk was servicing reads/writes
High value means:
Disk is busy, not necessarily slow
👉 It reflects disk saturation, not throughput
node_disk_read_time_seconds_total
Time spent servicing read requests
High value = many reads or slow reads

### Load Metrics
- node_load1, node_load5 -
Average number of runnable or blocked processes over time windows.
- Key understanding:
  - Load reflects system demand, not just CPU usage.
- 🧠 Load — node_load1, node_load5
- ❓ Why does load exist even when CPU is idle?
- Load average counts:
Processes running
Processes waiting (blocked)
CPU idle does NOT mean:
No blocked I/O
No runnable processes waiting
So load can increase when:
Disk I/O is slow
Processes are stuck in uninterruptible sleep
👉 Load ≠ CPU usage

## What Prometheus Shows Better Than CLI Tools
### Trends
- Displays metric behavior over time rather than point-in-time snapshots.
- Makes gradual performance degradation visible.
### Correlations
- Allows comparison of multiple metrics on the same timeline.
  - Example: rising load alongside increasing disk I/O wait.
### Historical Context
- Enables investigation of past incidents.
- Supports root cause analysis using historical data.

## What Prometheus Cannot Tell Me
### Exact Root Cause
- Prometheus shows what changed, not why it changed.
- Further investigation using logs, traces, or system-level debugging is required.
### Business Impact
- Metrics reflect system behavior, not user experience or revenue impact.
- Application-level and business metrics are needed for this context.
### Intent
- Prometheus cannot distinguish between:
   - Legitimate workload
   - Misconfiguration
   - Faulty application behavior
- Human analysis and domain knowledge are required.

## Summary
This setup demonstrates how Prometheus and node_exporter provide deep visibility into system behavior through time-series metrics, while also highlighting the importance of combining monitoring data with logs, traces, and contextual knowledge for effective troubleshooting.

“Prometheus metrics are mostly counters which only goes up and resets only on restart; meaningful values like CPU percentage are derived using rates over time. Linux memory appears ‘used’ due to caching, which is healthy, and load average reflects system demand, not just CPU utilization.”
