---
id: proc-uuid-002
tags:
  - logcat
  - token-extraction
  - android
type: procedure
tools:
  - '[[tools/logcat]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/logcat-grep-twitter]]'
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:24:35.244Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Extract-Leaked-OAuth-Token-from-Logcat

## Summary

This procedure captures Android device logs using logcat and filters for Twitter-related entries to identify and extract leaked temporary OAuth tokens from Fabric Twitter Kit's authentication process. It is primarily used post-login to demonstrate information disclosure in a multi-app device environment.

## Description

After performing Twitter login in a vulnerable app, the procedure uses ADB logcat to stream device logs and grep for 'twitter' keywords, revealing unsanitized OAuth tokens in the authorize URL. The target is any Android device with ADB access. Prerequisites include USB debugging enabled and the vulnerable app installed. Expected outcomes include visible token in logs, which can be used by malicious apps for unauthorized Twitter access.

## Requirements

1. ADB installed and device connected with USB debugging
2. Vulnerable app with Twitter Kit already installed and login performed
3. Basic command-line access for log monitoring

## Defense

Defensive measures and detection strategies:

- Disable verbose logging in apps and filter sensitive data before output
- Use runtime protections like app sandboxing to limit log access
- Monitor for anomalous logcat queries from other apps
- Update to non-vulnerable SDKs and audit log outputs in CI/CD

## Objectives

1. Capture real-time logs from the Android device
2. Filter and identify the leaked OAuth token
3. Validate the token for potential unauthorized use

## Instructions

### Step 1: Initiate Logcat Capture

**Context**: Start streaming logs from the device immediately after login to catch the fresh entries.

Execute [[commands/logcat-grep-twitter]] to filter for Twitter logs:

```bash
adb logcat | grep twitter
```

> This command streams all logs and filters lines containing 'twitter', displaying entries like the OAuth authorize URL with the embedded token.

### Step 2: Identify and Extract Token

**Context**: Review the filtered output for the specific leakage pattern.

Look for log entries showing the authentication URL, e.g., containing 'oauth_token=...' or similar parameters.

> Copy the token from the output; test it manually in a browser or curl against Twitter API to confirm validity (note: temporary, expires quickly).

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used

- [[commands/logcat-grep-twitter]]

## Tools Used

- [[tools/logcat]]

## Tags

- logcat
- oauth-leak
- android
