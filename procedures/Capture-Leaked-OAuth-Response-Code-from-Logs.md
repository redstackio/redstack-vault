---
id: proc-capture-code-001
tags:
  - oauth-leak
  - capture
  - logs
type: procedure
tools:
  - '[[tools/adb]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:24:42.164Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Capture Leaked OAuth Response Code from Logs

## Summary

This procedure involves extracting the OAuth response code leaked into Android logcat by the Coinbase app during authorization, allowing an attacker to obtain sensitive authorization data.

## Description

Following log monitoring, this procedure focuses on parsing the log output for the plain-text OAuth response code. It targets the information disclosure vulnerability where the app logs the code without sanitization. Used in scenarios with shared device access, it leads to token exchange. Expected outcome is the isolated response code ready for API use.

## Requirements

1. Active logcat session from prior monitoring
2. User completing OAuth flow in Coinbase app
3. Text editor or grep for log parsing

## Defense

Defensive measures and detection strategies:

- Implement log sanitization in apps to avoid sensitive data exposure
- Use runtime application self-protection (RASP) to detect log access
- Educate users on avoiding shared devices with untrusted apps

## Objectives

1. Identify OAuth response code in log entries
2. Extract and validate the code format
3. Prepare code for token exchange

## Instructions

### Step 1: Scan Logs During Authorization

**Context**: While the OAuth flow completes, watch for log entries containing the response code.

**Command** (Manual observation or pipe to grep):
```bash
adb logcat -s Coinbase | grep -i "response code"
```

> Pipe the log output to grep for keywords like 'response code' or 'oauth'. Expected output: Lines like "Coinbase: OAuth response code: xyz789".

### Step 2: Extract and Store the Code

**Context**: Copy the code from the log output for later use.

**Command** (No command; manual extraction):

> Isolate the alphanumeric string (e.g., 64-character code) from the log line. Validate by checking length and format.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Web Session Cookie]] Data from Local System

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/adb]]

## Tags

- oauth-leak
- android
- extraction
