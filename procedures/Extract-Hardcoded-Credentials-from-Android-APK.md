---
id: proc-uuid-1
tags:
  - android-apk
  - hardcoded-credentials
  - credential-access
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:10.576Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Extract-Hardcoded-Credentials-from-Android-APK

## Summary

This procedure extracts sensitive hardcoded API credentials (such as Twitter consumer key and secret) from an Android app's APK resource files, specifically strings.xml, by inspecting the publicly available APK without needing advanced decompilation.

## Description

In scenarios where developers embed API keys directly in app resources, attackers can download the APK from public sources (e.g., Google Play or APK mirrors) and use basic tools to dump string values. For the Reddit Android app (com.reddit.frontpage), this reveals Twitter OAuth credentials in Resources.arsc/res/values/strings.xml. The process requires no authentication and exploits poor secret management, leading to credential theft. Expected outcome: Plaintext credentials ready for misuse in API calls.

## Requirements

1. Downloaded APK file (e.g., com.reddit.frontpage.apk)
2. Android SDK tools installed (includes aapt)
3. Basic command-line access (Linux/macOS/Windows with aapt in PATH)

## Defense

Defensive measures and detection strategies:

- Avoid hardcoding secrets; use secure storage like Android Keystore or server-side proxies
- Obfuscate APK resources and use runtime credential fetching
- Monitor API usage for anomalous patterns from app-originated IPs

## Objectives

1. Identify and extract embedded API credentials from APK strings
2. Validate credentials for usability in external services
3. Demonstrate risk of public APK exposure

## Instructions

### Step 1: Download and Prepare APK

**Context**: Obtain the target APK for inspection. For Reddit, search for com.reddit.frontpage.apk on public repositories.

No command needed; save the file locally as reddit.apk.

### Step 2: Dump String Resources

**Context**: Use aapt to extract XML strings from the APK's Resources.arsc without full unpacking.

**Command** (aapt-dump-xmlstrings):
```bash
aapt dump xmlstrings reddit.apk res/values/strings.xml | grep -i twitter
```

> This command dumps all string resources and filters for Twitter-related entries, revealing `<string name="twitter_consumer_key">actual_key</string>` and `<string name="twitter_consumer_secret">actual_secret</string>`. Expected output: Hardcoded credential values in plaintext.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- None

## Commands Used

- None specific (uses standard aapt)

## Tools Used

- None

## Tags

- [[android-apk]]
- [[hardcoded-credentials]]
- [[credential-access]]
