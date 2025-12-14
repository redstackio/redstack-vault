---
id: proc-monitor-logs-001
tags:
  - android
  - logcat
  - monitoring
type: procedure
tools:
  - '[[tools/adb]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/adb-logcat-filter-coinbase]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:24:42.174Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Monitor Android Logs for Coinbase OAuth Activity

## Summary

This procedure sets up monitoring of Android device logs using ADB to capture activity from the Coinbase app during OAuth authorization, enabling the detection of leaked sensitive information.

## Description

In the context of exploiting the Coinbase Android app vulnerability, this procedure involves connecting to an Android device via ADB and filtering logcat output for 'Coinbase' tags. It is typically used when a malicious app or attacker with device access needs to intercept OAuth flows. Prerequisites include USB debugging enabled and ADB installed. Expected outcome is real-time log capture revealing app internals.

## Requirements

1. Android device with USB debugging enabled and Coinbase app installed
2. ADB tool installed on the host machine
3. Physical or emulated device access

## Defense

Defensive measures and detection strategies:

- Disable USB debugging on production devices
- Use app shielding to restrict log access
- Monitor for ADB connections via device management tools

## Objectives

1. Establish log monitoring for Coinbase app events
2. Capture authorization flow logs in real-time
3. Identify potential data leaks during OAuth

## Instructions

### Step 1: Connect Device and Start Log Monitoring

**Context**: Establish ADB connection and filter logs to focus on Coinbase activity, preparing to capture OAuth-related entries.

**Command** ([[commands/adb-logcat-filter-coinbase]]):
```bash
adb logcat -s Coinbase
```

> This command connects to the Android device and streams logs tagged 'Coinbase'. Expected output includes verbose app logs; initiate OAuth in the app to trigger relevant entries.

### Step 2: Trigger OAuth and Observe Logs

**Context**: Perform or wait for user-initiated OAuth authorization in the Coinbase app to generate log entries.

**Command** (No specific command; observe output):

> No new command; continue monitoring the existing logcat session. Look for entries related to authorization responses.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery (adapted for logs)

### Sub-Techniques


## Commands Used

- [[commands/adb-logcat-filter-coinbase]]

## Tools Used

- [[tools/adb]]

## Tags

- android
- logcat
- oauth
