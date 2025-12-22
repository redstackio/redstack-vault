---
id: proc-k8s-observe-exhaustion
tags:
  - kubernetes
  - monitoring
  - dos
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/kubectl-top-nodes]]'
  - '[[commands/kubectl-get-pods-watch]]'
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:30.555Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Observe Kubernetes Resource Exhaustion

## Summary

This procedure monitors CPU/memory usage on master nodes and control plane components to confirm DoS impact from scaling attacks.

## Description

Post-execution, watch for 100% utilization on API server/etcd processes, pod scheduling failures, and API timeouts. Even multi-master clusters (3x4vCPU/15GB) become unresponsive.

## Requirements

1. Access to master nodes (SSH or monitoring tools)
2. kubectl with metrics-server enabled
3. top/htop on nodes

## Defense

Defensive measures and detection strategies:

- Proactive: Vertical scaling of masters, etcd clustering
- Detection: Prometheus alerts on CPU>90%, API latency >5s
- Recovery: Drain nodes, restart API/etcd

## Objectives

1. Validate resource spikes
2. Confirm cluster unresponsiveness
3. Measure DoS duration

## Instructions

### Step 1: Monitor Node Resources

**Context**: Use kubectl top for overview.

**Command** ([[commands/kubectl-top-nodes]]):

```bash
kubectl top nodes
```

> Shows CPU/memory per node; expect masters at limits.

### Step 2: Watch Pod Status

**Context**: Observe API delays.

**Command** ([[commands/kubectl-get-pods-watch]]):

```bash
watch -n 1 'kubectl get pods --all-namespaces'
```

> Increasing timeouts/errors. Expected: Commands hang >30s.

### Step 3: Node-Level Monitoring

**Context**: SSH to masters for process view.

**Command** (top):

```bash
ssh master-node 'top -p $(pgrep kube-apiserver) $(pgrep etcd)'
```

> API/etcd at 100% CPU.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[OS Exhaustion Flood]] OS Exhaustion Floods

### Sub-Techniques


## Commands Used

- [[commands/kubectl-top-nodes]]
- [[commands/kubectl-get-pods-watch]]

## Tools Used

- [[tools/kubectl]]

## Tags

- kubernetes
- monitoring
- dos
