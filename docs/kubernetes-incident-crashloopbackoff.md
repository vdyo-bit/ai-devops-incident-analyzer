# Kubernetes Incident — CrashLoopBackOff

## Objective

Generate a controlled application failure and observe Kubernetes restart behavior.

---

## Failure Injection

Deployment created:

kubectl create deployment crash-demo --image=busybox -- /bin/sh -c "exit 1"

The container was configured to terminate immediately with exit code 1.

---

## Observed Behavior

Pod entered:

CrashLoopBackOff

Kubernetes repeatedly restarted the container.

---

## Evidence

Container State:

* Waiting
* Reason: CrashLoopBackOff

Last State:

* Terminated
* Reason: Error
* Exit Code: 1

Additional Evidence:

* Restart Count: 6
* Back-off restarting failed container

---

## Root Cause

The container started successfully but the application exited immediately with a non-zero exit code.

Kubernetes attempted automatic recovery by restarting the container multiple times.

After repeated failures, Kubernetes entered CrashLoopBackOff state.

---

## Learning

CrashLoopBackOff differs from ImagePullBackOff:

ImagePullBackOff:

* Container never starts
* Image retrieval problem

CrashLoopBackOff:

* Container starts successfully
* Application crashes after startup

Useful troubleshooting commands:

kubectl describe pod

kubectl logs

kubectl logs --previous

---

## Takeaway

CrashLoopBackOff usually indicates application startup problems rather than Kubernetes infrastructure issues.

Container lifecycle information and restart counts are often the fastest indicators of root cause.

