## Purpose
This document explains core Linux system metrics from an SRE perspective.
The goal is not to list commands, but to understand:
- What subsystem a metric represents
- What normal behavior looks like
- What kind of failures it can indicate
- What it cannot tell us

## CPU Metrics
### Key Commands
- uptime
- top
- vmstat
- sar -u
### CPU States (from /proc/stat)
- user: Time spent running user-space processes
- system: Time spent in kernel space
- idle: CPU doing nothing
- iowait: CPU waiting for I/O completion
- steal: Time taken by hypervisor (virtualized environments)
### How to Interpret
High CPU usage alone is NOT a problem.
Examples:
- High user + low system → CPU-heavy application
- High system → Kernel or driver overhead
- High iowait → Disk or network bottleneck, NOT CPU
- High steal → Host-level contention (cloud issue)
### Common Misconceptions
- High load ≠ high CPU usage
- iowait is not CPU pressure
- Adding more CPU does not fix I/O bottlenecks

## Load Average
### What Load Average Means
Load average represents the number of:
- Running processes
- Runnable processes
- Processes waiting for uninterruptible I/O
It is NOT a measure of CPU usage.
### How to Read Load Correctly
Rule of thumb:
Load ≈ number of CPU cores → system is busy but OK
Load >> number of cores → saturation or blocking
Example:
- 12-core system
- Load average: 24
Likely indicates blocked I/O or excessive runnable processes

## Memory Metrics
### Key Commands
- free -m
- vmstat
- sar -r
### Important Concepts
- Used memory includes cache
- Cache is reclaimable
- Free memory being low is NOT a problem
### What Actually Matters
- Available memory
- Swap usage
- Swap activity (si/so in vmstat)
### Red Flags
- Increasing swap usage
- High swap in/out rates
- OOM killer messages in logs

## Disk & I/O Metrics
### Key Commands
- iostat
- sar -d
- vmstat
### Key Metrics Explained
- await: Average I/O latency
- util: Percentage of time disk is busy
- iowait: CPU waiting on disk I/O
### How to Think About Disk Problems
- High disk usage ≠ problem.
- High disk latency = problem.
- A disk at 90% utilization with low latency can be fine.
- A disk at 30% utilization with high latency is a serious issue.

## Process Metrics
### Key Commands
- ps aux
- top
- htop
### What to Look For
- CPU spikes from single processes
- Memory growth over time (leaks)
- Zombie or stuck processes
### Important Insight
Top shows a snapshot.
Trends matter more than snapshots.

## Logs vs Metrics
Metrics tell you:
- Something is wrong
Logs tell you:
- Why it might be wrong
Neither is sufficient alone.
### Example
High iowait in metrics +
Disk timeout errors in logs
→ Confirms I/O bottleneck

## Limitations of Metrics
Metrics cannot:
- Explain business impact
- Tell you intent
- Always identify root cause
Metrics provide signals, not answers.

## My Observations
- High CPU is often a symptom, not the cause
- I/O wait is one of the most misleading metrics
- Linux aggressively uses memory for cache
- Load average must always be read with CPU core count

## Observation on my VM
- CPU usage mostly idle (~95–99%)
- Load average well below number of available CPU cores
- Memory shows high cache usage with minimal swap activity
- No iowait observed, indicating no disk bottlenecks
- Run queue remains low, indicating no CPU contention
- No steal time, confirming no hypervisor CPU pressure
- System remains stable and responsive under idle conditions

### CPU Stress Experiment — sar Observations
- CPU user time increased after starting yes > /dev/null &
- System CPU usage increased significantly due to frequent kernel syscalls
- Idle CPU dropped from ~98% to ~49%, indicating sustained CPU load
- No iowait observed, confirming workload was CPU-bound
- No steal time recorded, indicating no hypervisor CPU throttling
- After stopping the process, CPU utilization returned to baseline
- CPU load affected only part of total capacity (single process on 2 vCPUs)

### CPU Stress Experiment — vmstat Observations
- Run queue (r) increased, showing higher CPU demand
- CPU idle (id) dropped immediately, reflecting real-time stress
- User and system CPU time increased, confirming active processing
- No I/O wait (wa) observed, ruling out disk bottlenecks
- No swap activity (si/so), indicating sufficient memory
- Steal time (st) remained zero, confirming no cloud CPU contention
- CPU metrics returned to normal instantly after terminating the process





