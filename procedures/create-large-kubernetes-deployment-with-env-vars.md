---
id: proc-k8s-large-deploy
tags:
  - kubernetes
  - deployment
  - env-vars
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/kubectl-apply-deployment]]'
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:30.600Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Create Large Kubernetes Deployment with Env Vars

## Summary

This procedure creates a Kubernetes deployment bloated with a large number of environment variables to force excessive processing in the API server and etcd during creation and management, setting the stage for DoS via scaling.

## Description

In vulnerable Kubernetes setups without limits on deployment size (e.g., env var count or YAML size), an authenticated user can submit a deployment YAML exceeding 1MB with dummy env vars using a low-resource image like nginx. This inflates etcd storage and API processing without consuming pod resources, enabling subsequent scaling attacks. Targets clusters with default admission controls; assumes default namespace access.

## Requirements

1. Authenticated kubeconfig with create deployment permissions
2. Local kubectl installed and configured
3. Access to a text editor for YAML creation
4. Kubernetes cluster without ResourceQuota or custom limits on env vars

## Defense

Defensive measures and detection strategies:

- Implement admission webhooks (e.g., LimitRanger) to cap env var count per container (<100)
- Enable ResourceQuota in namespaces to limit deployment object size
- Monitor API server logs for large YAML submissions and etcd write spikes
- Use PodSecurityPolicies or OPA Gatekeeper to restrict oversized configs

## Objectives

1. Deploy an oversized configuration to bloat control plane storage
2. Ensure minimal pod resource use for scalability
3. Prepare for rapid replica changes without scheduler overload

## Instructions

### Step 1: Prepare Deployment YAML

**Context**: Generate a YAML file with ~10,000 env vars (e.g., ENV1=value1, etc.) to approach max YAML size, using nginx:alpine image for low footprint.

**Command** ([[commands/kubectl-apply-deployment]]):
No direct command; use editor to create large-nginx-deployment.yaml:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        env:
        # Add thousands of env vars here, e.g., - name: VAR1 value: "dummy1"
        resources:
          requests:
            cpu: 10m
            memory: 32Mi
```

> Fill env section programmatically (e.g., via script) to maximize size. Expected: Valid YAML file ~1MB.

### Step 2: Apply the Deployment

**Context**: Submit the YAML to the cluster API, triggering initial processing overhead.

**Command** ([[commands/kubectl-apply-deployment]]):

```bash
kubectl apply -f large-nginx-deployment.yaml
```

> Applies the deployment; expect "deployment.apps/nginx created" if successful. Initial etcd write may cause minor spike.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[OS Exhaustion Flood]] OS Exhaustion Floods

### Sub-Techniques


## Commands Used

- [[commands/kubectl-apply-deployment]]

## Tools Used

- [[tools/kubectl]]

## Tags

- kubernetes
- deployment
- env-vars
