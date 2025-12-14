---
id: proc-deploy-hijacker-pod-001
tags:
  - ssrf
  - kubernetes
  - pod-hijack
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:08.950Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Deploy-Malicious-Pod-to-Hijack-Metrics-Server

## Summary

Deploys a malicious pod in the kube-system namespace using the same label selector as metrics-server (k8s-app=metrics-server) to intercept and hijack API requests, enabling SSRF redirects.

## Description

Aggregated API servers in Kubernetes select pods based on labels; by deploying a pod with matching labels, the malicious one can be prioritized or replace the legitimate metrics-server. This causes clients like kube-controller-manager to send requests to the hijacker, which redirects them externally. Scale down the original deployment if replicas conflict. Requires kubectl access to kube-system.

## Requirements

1. kubectl configured with cluster-admin RBAC
2. Malicious image available (e.g., docker.io/weinong/go-redirect)
3. go-redirect.yaml manifest defining pod with matching labels

## Defense

Defensive measures and detection strategies:

- Use admission controllers to block unauthorized deployments in kube-system
- Implement label validation and pod security policies
- Audit deployments for label overlaps with critical services

## Objectives

1. Intercept requests to metrics-server API endpoints
2. Position hijacker for SSRF exploitation
3. Minimize detection by mimicking legitimate pod

## Instructions

### Step 1: Scale Down Original Metrics-Server

**Context**: Prevent conflicts by reducing replicas of the legitimate deployment.

Use [[tools/kubectl]]:

```bash
kubectl scale deployment metrics-server --replicas=0 -n kube-system
```

> Scales down; verify with `kubectl get deployments -n kube-system` showing replicas=0.

### Step 2: Apply Malicious Deployment

**Context**: Deploy the hijacker using go-redirect.yaml with labels k8s-app=metrics-server.

```bash
kubectl apply -f go-redirect.yaml -n kube-system
```

> Deploys pod; check status with `kubectl get pods -n kube-system -l k8s-app=metrics-server`.

### Step 3: Verify Hijack

**Context**: Confirm the malicious pod is selected by API aggregations.

```bash
kubectl get endpoints -n kube-system metrics-server
```

> Shows malicious pod IP as endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/kubectl]]

## Tags

- ssrf
- kubernetes
- pod-hijack
