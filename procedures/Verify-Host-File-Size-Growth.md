---
tags:
  - verification
  - file-size
  - host-inspection
type: procedure
tools:
  - '[[tools/ls]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/ls-check-file-size]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:56.632Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: 71fbe621-05bb-41cf-85bf-fc988bdffe0e
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Verify-Host-File-Size-Growth

## Summary

This procedure inspects the host's Docker overlay filesystem to confirm the size increase of the bind-mounted file after pod writes, validating the exploitation.

## Description

Post-dd execution, the host's /var/lib/docker/overlay2/<container-hash>/etc-hosts file grows proportionally to the written data, demonstrating the bind-mount propagation and disk impact.

## Requirements

1. Host access (for verification; attack doesn't require it)
2. Knowledge of pod's overlay directory hash
3. ls utility available

## Defense

Defensive measures and detection strategies:

- Regularly audit overlay2 file sizes
- Use filesystem quotas on /var/lib/docker
- Integrate with SIEM for anomalous file growth alerts

## Objectives

1. Confirm write propagation to host
2. Measure exploitation effectiveness
3. Identify affected storage paths

## Instructions

### Step 1: Locate Overlay Directory

**Context**: Find the pod's storage layer on host.

Navigate to /var/lib/docker/overlay2/ and identify the hash for the pod.

### Step 2: Check File Size

**Context**: Inspect the grown file.

**Command** ([[commands/ls-check-file-size]]):
```bash
ls -al etc-hosts
```

> Output shows size like "-rw-r--r-- 1 root root 104857600 Oct 1 12:00 etc-hosts" (from 270 bytes).

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/ls-check-file-size]]

## Tools Used

- [[tools/ls]]

## Tags

- [[verification]]
- [[file-size]]
