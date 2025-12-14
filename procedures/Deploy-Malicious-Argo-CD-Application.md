---
id: uuid5
tags:
  - argocd
  - deployment
  - yaml
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:50.223Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Deploy-Malicious-Argo-CD-Application

## Summary

The CSRF-created Argo CD Application syncs a malicious GitHub repo, deploying Kubernetes resources including a privileged pod, ServiceAccount, ClusterRole, and ClusterRoleBinding for cluster-admin access.

## Description

Argo CD automatically syncs the repo on creation due to syncPolicy. The repo https://github.com/califio/argotest1 contains YAML manifests that escalate privileges and deploy the RCE payload.

## Requirements

1. CSRF successful, application created
2. Repo with malicious YAML accessible
3. Argo CD sync enabled

## Defense

Defensive measures and detection strategies:

- Review application creations manually
- Restrict repo sources in Argo CD projects
- Audit RBAC bindings

## Objectives

1. Sync malicious repo
2. Deploy privileged resources
3. Gain admin pod

## Instructions

### Step 1: Confirm Application Creation

**Context**: Check Argo CD UI or API.

**Command** (kubectl-get-applications):
```bash
kubectl get applications -n argocd
```

> Expected output: test-app1 listed.

### Step 2: Trigger Sync

**Context**: Argo CD auto-syncs; monitor deployment.

**Command** (kubectl-get-pods):
```bash
kubectl get pods -n default
```

> Expected output: Malicious pod running.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- deployment
