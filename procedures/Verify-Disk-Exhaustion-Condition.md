---
tags:
  - dos
  - verification
  - disk-full
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
platforms:
  - Embedded Linux
techniques:
  - '[[OS Exhaustion Flood]]'
skill_level: basic
impact_level: high
detection_risk: low
sub_techniques: []
id: 7469dd72-f3af-4631-ae39-773c3b6ad2c2
created_at: '2025-12-14T05:32:10.007Z'
updated_at: '2025-12-14T05:32:10.007Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Verify-Disk-Exhaustion-Condition

## Summary

This procedure confirms the DoS impact by observing full disk usage on /var and /tmp partitions after mass uploads, checking for service disruptions like radiod failures.

## Description

Post-exploitation, the shared filesystem on Ubiquiti AirFibre 3.2 shows exhaustion via tools like `df`. Screenshots or logs indicate 100% usage, preventing new writes and crashing processes. This validates the attack without needing new commands, assuming console access or monitoring.

## Requirements

1. Completed mass upload procedure
2. Access to device console or remote monitoring
3. `df` command availability on target

## Defense

Defensive measures and detection strategies:

- Implement filesystem quotas and auto-cleanup for /tmp
- Monitor disk I/O and alert on rapid space consumption
- Use intrusion detection for upload patterns

## Objectives

1. Confirm partition fullness
2. Observe service impacts
3. Validate DoS success

## Instructions

### Step 1: Check Disk Usage

**Context**: Run `df -h` to inspect /tmp and /var usage.

**Command**:
```bash
df -h /tmp /var
```

> Expected output: 100% usage on partitions; e.g., /dev/root 100% full.

### Step 2: Inspect Impacted Files

**Context**: Look for errors in /tmp files like radiod.

**Command**:
```bash
ls -la /tmp | grep radiod
```

> Expected output: Incomplete or failed files due to space issues; service logs show errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[OS Exhaustion Flood]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dos]]
- [[disk-full]]
