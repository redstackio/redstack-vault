---
id: proc-ubiquiti-verify-001
tags:
  - dos
  - verification
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/df-disk-usage]]'
verified: false
platforms:
  - Embedded Linux
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:31:10.953Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Verify-Disk-Exhaustion-Impact

## Summary

This procedure checks the filesystem usage on the target Ubiquiti AirFibre device after bulk uploads to confirm disk exhaustion and resulting DoS impact on services.

## Description

Using the 'df' command on the Embedded Linux shell, this verifies that the /dev/root partition (shared by /tmp and /var) is at 100% capacity. It also observes indirect effects like changes in service files (e.g., radiod) to validate disruption. Access to the device shell is assumed post-exploitation or via physical/debug access.

## Requirements

1. Shell access to the target device (e.g., via SSH or console)
2. Prior execution of upload procedures to induce exhaustion
3. Basic Linux command familiarity

## Defense

Defensive measures and detection strategies:

- Set up automated alerts for disk usage exceeding 90%
- Regularly audit /tmp for unexpected files
- Implement filesystem quotas on embedded partitions

## Objectives

1. Confirm partition fullness
2. Identify service disruptions
3. Validate overall DoS success

## Instructions

### Step 1: Check Filesystem Usage

**Context**: Run 'df' to display disk usage statistics, focusing on /tmp and /var mounts.

**Command** ([[commands/df-disk-usage]]):

```bash
df
```

> This command reports disk space usage. Expected output shows /dev/root at 100% used, e.g., '/dev/root  100% /tmp' and similar for /var, indicating exhaustion.

### Step 2: Observe Service Impact

**Context**: Monitor device logs or files for errors caused by space issues.

**Instructions**: Check radiod process or logs for anomalies, such as failed writes.

**Expected Output**: Errors in logs or stalled services due to no space left.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/df-disk-usage]]

## Tools Used


## Tags

- dos
- verification
