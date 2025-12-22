---
id: proc-shopify-view-logs-001
tags:
  - android
  - log-analysis
  - data-leakage
type: procedure
tools:
  - '[[tools/ADB-Android-Debug-Bridge]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/adb-logcat-shopifyhack]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:32:10.988Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# View-Leaked-Data-in-Android-Logs

## Summary

This procedure uses ADB logcat to filter and display the POC's logs, revealing the intercepted sensitive data from Shopify broadcasts for verification and further use.

## Description

After interception, the POC logs data with a specific tag. This step retrieves those logs via ADB, confirming leakage of items like access_tokens and cookies, which can then be used for account takeover.

## Requirements

1. ADB connected to the Android device
2. POC APK installed and broadcast triggered
3. USB debugging enabled

## Defense

Defensive measures and detection strategies:

- Disable USB debugging in production
- Monitor logcat outputs for sensitive tags
- Use app sandboxing to prevent log access

## Objectives

1. Retrieve and inspect leaked credentials
2. Validate the full extent of data exposure
3. Prepare data for exfiltration or exploitation

## Instructions

### Step 1: Connect Device via ADB

**Context**: Establish connection to pull logs.

```bash
adb devices
```

> Ensure device is listed and authorized.

### Step 2: Filter and View Logs

**Context**: Execute the logcat command to display verbose logs for the POC tag.

Execute [[commands/adb-logcat-shopifyhack]]:

```bash
adb logcat -s SHOPIFYHACK:V
```

> This filters logs tagged 'SHOPIFYHACK' at verbose level, showing extras like response headers and body.

### Step 3: Analyze Output

**Context**: Identify sensitive data in the logs.

Look for lines containing 'admin_cookie' or 'access_token'.

> Expected: Dumped JSON/XML with tokens, enabling takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used

- [[commands/adb-logcat-shopifyhack]]

## Tools Used

- [[tools/ADB-Android-Debug-Bridge]]

## Tags

- android
- log-analysis
- data-leakage
