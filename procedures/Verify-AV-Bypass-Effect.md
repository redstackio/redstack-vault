---
id: proc-bypass-verify-001
tags:
  - av-bypass
  - logs
  - verification
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T17:29:10.007Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Verify-AV-Bypass-Effect

## Summary

Check system logs to confirm the AV function disable and observe the impact, such as bypassed read-only volume scans, validating the full AV bypass.

## Description

Post-injection, the com.kaspersky.kav.sysext process logs 'FileMonitor: disabling read-only volume scan' upon method invocation. This indicates successful control, with potential UI desync bugs. Test by attempting scans on read-only volumes to confirm bypass, leading to evasion of protections and enabling malware persistence or escalation.

## Requirements

1. Console.app or log command-line access
2. KIS running with exploited extension

## Defense

Defensive measures and detection strategies:

- Log all AV configuration changes and alert on disables
- Use tamper protection in AV to prevent unauthorized method calls
- Monitor for log entries indicating disabled scans

## Objectives

1. Confirm disable via logs
2. Validate protection bypass
3. Assess overall impact

## Instructions

### Step 1: Monitor System Logs

**Context**: Search for confirmation from the SEXT process.

Use Console.app or:

```bash
log show --predicate 'process == "com.kaspersky.kav.sysext"' --last 5m
```

> Expected output: Entry 'FileMonitor: disabling read-only volume scan'.

### Step 2: Test Bypass

**Context**: Verify functional impact.

Attempt a scan on a read-only volume (e.g., via KIS UI or API); observe failure or skip.

> Expected output: Scan disabled, no protection applied; note any UI desync.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Disable or Modify Tools]] Disable or Modify Tools (AV disable)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- verification
- logs
- bypass
