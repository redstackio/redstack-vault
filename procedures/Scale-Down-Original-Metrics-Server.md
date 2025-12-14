---
tags:
  - kubernetes
  - deployment
  - scale
type: procedure
tools:
  - '[[tools/kubectl]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/run-reproduction-script]]'
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data Destruction]]'
updated_at: '2025-12-14T17:32:38.972Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: a2ce4644-e790-4481-9984-13c579ddcd58
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Data Destruction]]'
---
# Scale-Down-Original-Metrics-Server

## Summary

Scales down the legitimate metrics-server deployment to force traffic to the malicious pod, completing the hijack for SSRF exploitation.

## Description

In Kubernetes, services select pods by labels; scaling the original deployment to zero replicas ensures the malicious pod handles all requests. This uses a script to identify and scale the deployment, adapted for AKS/GKE. Requires deployment access; outcome is seamless traffic takeover.

## Requirements

1. Admin access to deployments in kube-system
2. Reproduction script (run.sh) for automation
3. Cluster-specific flags (e.g., USE_GKE=1)

## Defense

Defensive measures and detection strategies:

- Monitor deployment replica changes
- Implement RBAC to limit scaling in system namespaces
- Alert on zero-replica critical services

## Objectives

1. Redirect traffic to malicious pod
2. Maintain hijack without downtime alerts
3. Prepare for redirect observation

## Instructions

### Step 1: Identify Deployment

**Context**: Locate the metrics-server deployment using kubectl.

**Command** ([[tools/kubectl]]):

```bash
kubectl get deployment -n kube-system | grep metrics-server
```

> Lists deployment name; expected output: metrics-server   1/1     1            1           5m.

### Step 2: Scale Down Using Script

**Context**: Run the script to automate scaling to 0.

**Command** ([[commands/run-reproduction-script]]):

```bash
USE_GKE=1 ./run.sh
```

> Scales down; expected output: Scaled to 0 replicas.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Data Destruction]]

### Sub-Techniques


## Commands Used

- [[commands/run-reproduction-script]]

## Tools Used

- [[tools/kubectl]]

## Tags

- kubernetes
- deployment
- scale
