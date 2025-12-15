---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
name: Extract-Hardcoded-Credentials-from-APK
tags:
  - hardcoded-credentials
  - information-disclosure
  - reverse-engineering
type: procedure
tools:
  - '[[tools/jadx]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/grep-search-strings]]'
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:24:42.520Z'
sub_techniques:
  - '[[Credentials In Files]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
  - '[[Credentials In Files]]'
---
# Extract-Hardcoded-Credentials-from-APK

## Summary

This procedure searches decompiled Android APK files for hardcoded credentials, such as those embedded in URLs to third-party APIs, allowing attackers to disclose and potentially misuse sensitive authentication data.

## Description

Hardcoded credentials in mobile apps like 8x8 represent a common misconfiguration where API keys or usernames/passwords are directly included in code or resources. This procedure targets strings in smali, XML, or Java files post-decompilation. In the 8x8 case, credentials were found in a URL to a bug capture API. Outcomes include exfiltration of creds for unauthorized access, with prerequisites being a decompiled APK.

## Requirements

1. Decompiled APK directory from prior steps
2. Basic command-line tools like grep
3. Knowledge of common credential patterns (e.g., API keys, base64-encoded strings)

## Defense

Defensive measures and detection strategies:

- Use secure credential storage like Android Keystore or encrypted configs
- Perform static analysis scans with tools like MobSF during development
- Detect via runtime monitoring for credential usage anomalies in app telemetry

## Objectives

1. Locate embedded credentials in app code
2. Validate their relation to third-party services
3. Document for potential exploitation

## Instructions

### Step 1: Search for Credential Patterns

**Context**: Scan decompiled files for keywords indicating hardcoded secrets.

**Command** ([[commands/grep-search-strings]]):
```bash
grep -r -i "api\|key\|token\|password\|https://bug" decompiled_app/ > creds.txt
```

> Searches recursively for patterns, outputting matches to creds.txt. Review for URLs like the bug capture API endpoint with embedded auth.

### Step 2: Refine Search in Specific Files

**Context**: Focus on likely locations like strings.xml or network config files.

**Command** ([[commands/grep-specific-files]]):
```bash
grep -i "credential" decompiled_app/res/values/strings.xml
```

> Targets resource files. Expected output: Lines with potential secrets, e.g., hardcoded user/pass in API URLs.

### Step 3: Decode and Verify

**Context**: Check for encoded credentials and test validity.

**Command** ([[commands/base64-decode]]):
```bash
echo "encoded_string" | base64 -d
```

> Decodes any base64 strings found. Manually verify by noting the API endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials
- [[Credentials In Files]] Embedded Credentials

### Sub-Techniques

- [[Credentials In Files]] Embedded Credentials

## Commands Used

- [[commands/grep-search-strings]]
- [[commands/grep-specific-files]]
- [[commands/base64-decode]]

## Tools Used

- [[tools/jadx]]

## Tags

- hardcoded-credentials
- extraction
- android
