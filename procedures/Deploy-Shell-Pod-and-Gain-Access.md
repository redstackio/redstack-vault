---
id: proc-1
name: Deploy-Shell-Pod-and-Gain-Access
tags:
  - kubernetes
  - pod-access
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/kubectl-apply-shell-yaml]]'
  - '[[commands/kubectl-exec-ash]]'
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:18.581Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Deploy-Shell-Pod-and-Gain-Access

## Summary

Deploys a simple pod with shell access to simulate initial compromise in a Kubernetes cluster, providing a foothold for further escalation.

## Description

In a kOps-managed Kubernetes cluster on GCP, this procedure assumes or creates pod shell access, which is the starting point for exploiting node service accounts. It uses a basic Alpine manifest to run a pod, then execs into it for interactive shell. This targets environments where workloads allow shell execution or via misconfigured RBAC.

## Requirements

1. kubectl configured with cluster access
2. Permissions to create pods in default namespace
3. shell.yaml manifest (Alpine image with ash shell)

## Defense

- Implement Pod Security Standards to restrict shell images
- Use RBAC to deny pod creation/exec for non-admins
- Monitor for unusual pod deployments via audit logs

## Objectives

1. Gain executable shell in a running pod
2. Establish initial access for metadata retrieval
3. Prepare for host-level escalation

## Instructions

### Step 1: Deploy the Shell Pod

**Context**: Apply a Kubernetes manifest to create an Alpine pod for shell access.

**Command** ([[commands/kubectl-apply-shell-yaml]]):
```bash
k apply -f shell.yaml
```

> Deploys the pod named 'shell'. Expected output: 'pod/shell created'.

### Step 2: Exec into the Pod

**Context**: Gain interactive shell in the deployed pod.

**Command** ([[commands/kubectl-exec-ash]]):
```bash
k exec -it shell-5d64dd647c-8l8s6 -- ash
```

> Provides ash shell. Expected output: Pod shell prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/kubectl-apply-shell-yaml]]
- [[commands/kubectl-exec-ash]]

## Tools Used

- [[tools/kubectl]]

## Tags

- kubernetes
- pod-access
