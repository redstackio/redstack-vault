---
id: proc-k8s-scale-down
tags:
  - kubernetes
  - scaling
  - json
type: procedure
tools:
  - '[[tools/bash]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:30.580Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Prepare Kubernetes Scale Down JSON

## Summary

This procedure generates a JSON file to scale a deployment down to 1 replica, completing the up/down cycle for repeated resource spikes.

## Description

Similar to scale-up, this payload reduces replicas to 1, triggering cleanup and rescheduling in etcd/API, amplifying exhaustion when looped. Targets the same deployment.

## Requirements

1. Text editor or shell
2. Existing scale-up counterpart

## Defense

Defensive measures and detection strategies:

- Monitor for oscillating scale patterns in audit logs
- Enforce cooldown periods on scale operations via custom controllers

## Objectives

1. Define low-scale payload
2. Pair with up-scale for cycles
3. Maintain API compatibility

## Instructions

### Step 1: Create Scale Down JSON

**Context**: Echo the minimal spec for 1 replica.

**Command** (bash echo):

```bash
echo '{"spec":{"replicas":1}}' > scaledown.json
```

> Creates file; verify contents. Expected: Valid JSON.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/bash]]

## Tags

- kubernetes
- scaling
- json
