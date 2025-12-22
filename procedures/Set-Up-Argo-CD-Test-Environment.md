---
id: uuid1
tags:
  - setup
  - kubernetes
  - argocd
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:50.238Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Set-Up-Argo-CD-Test-Environment

## Summary

This procedure sets up a vulnerable Argo CD instance in a Kubernetes cluster to test CSRF exploitation, simulating a production environment with version 2.8.2.

## Description

Argo CD is a declarative GitOps tool for Kubernetes. Vulnerable versions lack Content-Type validation, allowing CSRF attacks. This setup involves deploying Argo CD via Helm or manifests in a local or cloud Kubernetes cluster, ensuring internal exposure and default cookie policies. Prerequisites include kubectl access and a running Kubernetes cluster.

## Requirements

1. Kubernetes cluster (e.g., Minikube or EKS) with admin access
2. Helm installed for Argo CD deployment
3. Domain control for subdomains (for later steps)

## Defense

Defensive measures and detection strategies:

- Upgrade Argo CD to patched versions (2.10-rc2+)
- Enable strict Content-Type validation in API servers
- Monitor for anomalous application creations in Argo CD logs

## Objectives

1. Deploy vulnerable Argo CD for testing
2. Verify API accessibility
3. Prepare for subdomain-based attacks

## Instructions

### Step 1: Install Argo CD

**Context**: Use Helm to deploy Argo CD v2.8.2.

**Command** (helm-install-argocd):
```bash
helm repo add argo https://argoproj.github.io/argo-helm
helm install argocd argo/argo-cd --version 2.8.2 -n argocd --create-namespace
```

> This deploys Argo CD pods. Expected output: Pods in Running state via `kubectl get pods -n argocd`.

### Step 2: Expose Argo CD Server

**Context**: Port-forward or use Ingress for internal access.

**Command** (kubectl-port-forward):
```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

> Access at https://localhost:8080. Expected output: Argo CD login page.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- setup
- kubernetes
