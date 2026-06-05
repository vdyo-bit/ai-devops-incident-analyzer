# Kubernetes Incident — OOMKilled

## Objective

Generate a controlled memory exhaustion scenario and observe Kubernetes resource enforcement.

---

## Failure Injection

A deployment was created using the stress utility.

Container configuration:

- Memory Request: 32Mi
- Memory Limit: 64Mi

Workload configuration:

stress --vm 1 --vm-bytes 128M --vm-hang 1

The application intentionally attempted to allocate more memory than allowed.

---

## Observed Behavior

The pod repeatedly terminated and restarted.

Observed states:

- OOMKilled
- Restarting
- Back-off restarting failed container

---

## Evidence

Container State:

- Terminated
- Reason: OOMKilled
- Exit Code: 137

Additional Evidence:

- Restart Count: 5
- Back-off restarting failed container

Resource Configuration:

- Request: 32Mi
- Limit: 64Mi

Application Demand:

- 128M allocation

---

## Root Cause

The application attempted to consume more memory than the container limit.

Kubernetes enforced the memory boundary and terminated the process.

---

## Learning

OOMKilled is different from CrashLoopBackOff.

CrashLoopBackOff:
- Application exits on its own

OOMKilled:
- Kubernetes terminates the application

Exit Code 137 is a common indicator of memory-related termination.

---

## Takeaway

Resource limits protect cluster stability but can terminate workloads when configured too aggressively.

Memory requests and limits should reflect actual application requirements.
