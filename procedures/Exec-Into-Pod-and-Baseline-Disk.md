---
tags:
  - kubernetes
  - pod-exec
  - disk-baseline
type: procedure
tools:
  - '[[tools/kubectl]]'
  - '[[tools/df]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/kubectl-exec-pod]]'
  - '[[commands/df-check-usage]]'
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:26:56.639Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: afa7b900-5eda-4702-9d47-833fd9c4396e
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Exec-Into-Pod-and-Baseline-Disk

## Summary

This procedure accesses the shell of a running Kubernetes pod and checks initial disk usage to baseline the filesystem before exploitation, confirming available space on bind-mounted paths.

## Description

Once a pod is deployed, exec into it to run commands interactively. The df command reveals mount points like /etc/hosts backed by host storage (/var/lib/docker/overlay2), showing initial free space (e.g., 59G) that can be targeted for exhaustion.

## Requirements

1. Running pod (e.g., from previous procedure)
2. kubectl access
3. Pod must have shell (busybox provides sh)

## Defense

Defensive measures and detection strategies:

- Disable exec access via PodSecurityPolicy
- Audit exec events in Kubernetes API server logs
- Limit container privileges to non-root

## Objectives

1. Gain interactive shell in pod
2. Assess initial disk availability
3. Identify exploitable mounts

## Instructions

### Step 1: Exec into Pod

**Context**: Enter the pod's shell for command execution.

**Command** ([[commands/kubectl-exec-pod]]):
```bash
kubectl exec -it rate-c848c5c8b-5b8vm sh
```

> Drops into pod shell; warning about deprecated syntax may appear.

### Step 2: Check Disk Usage

**Context**: Baseline filesystem space on bind-mounts.

**Command** ([[commands/df-check-usage]]):
```bash
df -h
```

> Shows output like "/dev/sdb 100.0G 40.9G 59.1G 41% /etc/hosts".

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/kubectl-exec-pod]]
- [[commands/df-check-usage]]

## Tools Used

- [[tools/kubectl]]
- [[tools/df]]

## Tags

- [[kubernetes]]
- [[pod-exec]]
- [[disk-baseline]]
