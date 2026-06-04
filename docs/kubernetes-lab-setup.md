# Kubernetes Lab Setup

## Environment

* Ubuntu 22.04 VM
* Docker Desktop
* Kind
* kubectl

## Cluster Creation

```bash
kind create cluster --name ai-analyzer
```

## Verify Cluster

```bash
kubectl get nodes
```

Expected:

```text
ai-analyzer-control-plane   Ready
```

## First Deployment

```bash
kubectl create deployment nginx --image=nginx
```

## Verify Deployment

```bash
kubectl get deployments
kubectl get pods
```

## Useful Commands

### View Pods

```bash
kubectl get pods
```

### Describe Pod

```bash
kubectl describe pod <pod-name>
```

### View Logs

```bash
kubectl logs <pod-name>
```

## Learning Outcome

Successfully created a local Kubernetes cluster and deployed the first workload.

This environment will be used to generate Kubernetes incidents for the AI DevOps Incident Analyzer project.

## First Failure Scenario

Created a deployment with an invalid image.

Observed:

- ErrImagePull
- ImagePullBackOff

Used:

kubectl get pods
kubectl describe pod

This demonstrated how Kubernetes surfaces container image failures through pod status and events.
