---
tags:
  - dos
  - disk-exhaustion
  - verification
type: procedure
tools:
  - '[[tools/df]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/df-check-kubelet]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:56.628Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: e7536fb9-30a6-46c9-9306-db704a86e577
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Confirm-Host-Disk-Exhaustion

## Summary

This procedure monitors the host's /var/lib/kubelet filesystem usage to verify disk exhaustion caused by pod writes, confirming the DoS impact.

## Description

After repeated writes, df shows decreasing available space on the kubelet volume, potentially filling it to 100% and causing node panic or unavailability, especially in cloud environments.

## Requirements

1. Host access for monitoring
2. df utility
3. Prior exploitation steps completed

## Defense

Defensive measures and detection strategies:

- Set node-level disk quotas
- Alert on high disk usage thresholds
- Use Kubernetes taints to isolate affected nodes

## Objectives

1. Validate DoS achievement
2. Observe node degradation
3. Assess cluster-wide effects

## Instructions

### Step 1: Monitor Disk Usage

**Context**: Check space before and after writes.

**Command** ([[commands/df-check-kubelet]]):
```bash
df -h /var/lib/kubelet
```

> Initial: ample space; post-exploit: 0% available, e.g., "100G 100G 0 100% /var/lib/kubelet".

### Step 2: Check Node Status

**Context**: Verify operational impact.

**Command** (kubectl get nodes):
```bash
kubectl get nodes
```

> Look for NotReady status.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[OS Exhaustion Flood]]

### Sub-Techniques


## Commands Used

- [[commands/df-check-kubelet]]

## Tools Used

- [[tools/df]]

## Tags

- [[dos]]
- [[disk-exhaustion]]
