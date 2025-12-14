---
id: proc-002
tags:
  - kubernetes
  - ingress
  - nginx
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/kubectl-apply-ingress-deployment]]'
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:49.949Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Deploy-NGINX-Ingress-Controller

## Summary

This procedure deploys the official NGINX Ingress Controller to a Kind Kubernetes cluster, setting up the vulnerable component for path injection exploitation.

## Description

The NGINX Ingress Controller handles incoming traffic and processes Ingress resources. In this vulnerable version, the path field lacks proper sanitization, allowing directive injection. Deployment uses the Kind-specific YAML which includes necessary RBAC, services, and deployments. Post-deployment, the controller pod runs with a default service account.

## Requirements

1. Running Kind cluster from previous procedure.
2. kubectl configured to access the cluster.
3. Internet access to fetch the YAML from GitHub.
4. No special privileges beyond cluster-admin (default in Kind).

## Defense

Defensive measures and detection strategies:

- Pin ingress-nginx versions to patched releases (post-CVE fix).
- Enable NGINX config validation with strict sanitizers.
- Monitor pod deployments in ingress-nginx namespace for anomalies.
- Use network policies to restrict ingress traffic.

## Objectives

1. Install the ingress controller pod and services.
2. Expose ports for testing malicious Ingress.
3. Verify controller readiness.
4. Prepare for Ingress resource creation.

## Instructions

### Step 1: Apply Deployment YAML

**Context**: Fetch and apply the official Kind deployment manifest, which creates namespace, RBAC, configmap, service, and deployment.

**Command** ([[commands/kubectl-apply-ingress-deployment]]):

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
```

> Expected output: Resources created in ingress-nginx namespace, e.g., "namespace/ingress-nginx created", "deployment.apps/ingress-nginx-controller created".

### Step 2: Verify Deployment

**Context**: Check that the controller pod is running and ready.

**Command** (kubectl get pods):

```bash
kubectl get pods -n ingress-nginx
```

> Expected output: ingress-nginx-controller-xxx pod in Running state with 1/1 ready containers.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/kubectl-apply-ingress-deployment]]

## Tools Used

- [[tools/kubectl]]

## Tags

- kubernetes
- ingress
- nginx
