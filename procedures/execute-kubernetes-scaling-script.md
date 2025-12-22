---
id: proc-k8s-execute-script
tags:
  - kubernetes
  - execution
  - dos
type: procedure
tools:
  - '[[tools/bash]]'
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/run-scaling-script]]'
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:30.559Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Execute Kubernetes Scaling Script

## Summary

This procedure runs the scaling script multiple times, possibly in background, to perform concurrent API requests causing resource exhaustion.

## Description

Executing run.sh repeatedly sends bursts of scale operations, overwhelming the API server's mutating request queue and etcd's write throughput, leading to unresponsiveness.

## Requirements

1. run.sh prepared and executable
2. kubectl proxy running
3. scale JSON files present

## Defense

Defensive measures and detection strategies:

- Circuit breakers in API server for high load
- Alert on concurrent scale requests >10/min
- Isolate namespaces with quotas

## Objectives

1. Initiate concurrent scaling floods
2. Amplify DoS effect
3. Observe escalating failures

## Instructions

### Step 1: Run Script Instances

**Context**: Launch 3+ instances for concurrency.

**Command** ([[commands/run-scaling-script]]):

```bash
./run.sh &
./run.sh &
./run.sh
```

> Background runs (&) for parallelism. Expected: Curl outputs with initial successes, then timeouts.

### Step 2: Monitor Execution

**Context**: Check process count.

**Command** (ps):

```bash
ps aux | grep run.sh
```

> Lists running scripts.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/run-scaling-script]]

## Tools Used

- [[tools/bash]]
- [[tools/curl]]

## Tags

- kubernetes
- execution
- dos
