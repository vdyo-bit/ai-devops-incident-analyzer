# Kubernetes Incident — ImagePullBackOff

## Objective

Generate a controlled Kubernetes failure and observe how the platform reports deployment issues.

---

## Failure Injection

A deployment was created using nginx.

The image was intentionally replaced with a non-existent repository:

kubectl set image deployment/broken-nginx nginx=doesnotexist123/nginx:latest

---

## Observed Behavior

Pod status changed to:

ImagePullBackOff

The container never started successfully.

---

## Evidence Collected

kubectl describe pod revealed:

* Failed to pull image
* Pull access denied
* Repository does not exist
* ErrImagePull
* ImagePullBackOff
* Back-off pulling image

---

## Root Cause

The deployment referenced an invalid container image.

Kubernetes repeatedly attempted to download the image and failed because the repository could not be found.

---

## Learning

ImagePullBackOff is often caused by:

* Incorrect image names
* Missing image tags
* Private registry authentication failures
* Deleted repositories

The pod itself was healthy enough to schedule onto a node, but container startup failed because the image could not be retrieved.

---

## Takeaway

Kubernetes surfaces image-related failures through pod events rather than application logs.

kubectl describe pod is often the fastest way to identify ImagePullBackOff root causes.

