# Kubernetes Basics — Local Lab Observations

## Purpose

This document captures foundational observations from running a local Kubernetes lab.  
The focus is understanding how Kubernetes reports system resources and how node-level behavior differs from pod-level behavior.

This is not a theoretical guide — it reflects practical learning from experimentation.

---

## Node Metrics vs Pod Metrics

### Node Metrics

Node metrics describe the overall resource usage of a Kubernetes node (the machine hosting workloads).

Examples include:

- Total CPU utilization
- Total memory usage
- Disk pressure
- Network activity

These metrics represent **system-wide capacity and health**.

Node metrics answer questions like:

- Is the node under resource pressure?
- Is CPU or memory saturated?
- Is the system stable enough to schedule more pods?

They reflect the combined impact of:

- Kubernetes components
- Running pods
- System services

---

### Pod Metrics

Pod metrics describe the resource consumption of individual workloads.

Examples include:

- CPU usage per pod
- Memory usage per container
- Restart counts

These metrics answer:

- Which workload is consuming resources?
- Is a specific pod misbehaving?
- Is a container nearing limits?

Pod metrics are **workload-focused**, not system-wide.

---

### Key Difference

Node metrics show **capacity and system pressure**.

Pod metrics show **application behavior**.

Understanding both is essential because:

- A node can appear healthy while a pod misbehaves
- A pod may look normal while node saturation affects scheduling

Effective troubleshooting requires correlating both views.

---

## Resource Reporting Behavior

Kubernetes resource reporting is based on:

- Scheduler awareness
- Container runtime statistics
- Metrics server aggregation

Important behaviors observed:

### Requests vs Limits

Pods define:

- **Requests** → minimum guaranteed resources
- **Limits** → maximum allowed usage

Scheduler decisions are based on **requests**, not real-time usage.

This means:

- A node may appear lightly loaded
- Yet Kubernetes refuses to schedule more pods

because allocation decisions follow declared resource reservations.

---

### Metrics Lag

Resource metrics are not perfectly real-time.

Short spikes may not immediately appear in:
kubectl top nodes
kubectl top pods

This reinforces:

- Metrics are observational
- They are not exact real-time telemetry

---

### Resource Isolation

Containers cannot exceed defined limits without throttling or eviction.

Observed effects include:

- CPU throttling under heavy load
- Memory eviction when limits are reached

This demonstrates Kubernetes enforcing workload boundaries.

---

## What Surprised Me

Several behaviors were unexpected during experimentation:

### Scheduler ≠ Real Usage

Kubernetes schedules based on declared requests, not instantaneous usage.

This creates scenarios where:

- Nodes appear idle
- Scheduling is still restricted

This highlights Kubernetes’ preference for predictability over dynamic packing.

---

### Metrics Are Aggregated Views

Metrics are simplified summaries, not raw kernel telemetry.

They provide operational guidance but may hide transient spikes.

Understanding this prevents over-trusting single metric snapshots.

---

### Pod Isolation Is Strict

Resource limits are actively enforced.

Even in a local lab:

- Containers experienced throttling
- Memory pressure triggered eviction behavior

This mirrors production resource control.

---

### Observability Requires Context

Looking at only pod metrics or only node metrics is misleading.

Correlation is necessary to understand system behavior.

---

## Practical Takeaways

- Node health does not guarantee workload health
- Pod metrics reveal application-level pressure
- Scheduler decisions rely on declared resource intent
- Metrics are guides, not ground truth
- Resource isolation is enforced even in lab environments

---

## Summary

This lab reinforced that Kubernetes operates on:

- Predictable scheduling rules
- Resource isolation
- Aggregated observability

Understanding how node and pod metrics interact is essential for diagnosing performance issues and designing stable deployments.

Hands-on experimentation revealed behaviors that are not obvious from documentation alone.


