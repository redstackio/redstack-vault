---
id: ac-grammarly-log-leak
tags:
  - information-exposure
  - android
  - logging
  - mobile
type: attack_chain
tools: []
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Android
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Extract-User-Input-from-Grammarly-Logs]]'
step_count: 1
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:24:45.309Z'
description: >-
  Demonstrates the leakage of non-sensitive user input from the Grammarly
  Keyboard Android app (versions <4.1) into device logs on older Android
  devices, enabling local information exposure.
skill_level: beginner
impact_level: low
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Information Exposure via Debug Logs in Grammarly Keyboard Android App

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[App Installation and Input] --> B[Log Extraction and Analysis]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Android Debug Bridge (ADB)

### Target Environment

- Android device running version <5.0
- Grammarly Keyboard app version <4.1 installed
- USB debugging enabled on device

### Initial Access Requirements

- Physical or USB access to the Android device
- ADB installed on host machine

## Detailed Attack Procedures

### Step 1: Log Extraction for Input Leakage
procedure: [[procedures/Extract-User-Input-from-Grammarly-Logs]]

**Objective**: Capture and analyze device logs to expose non-sensitive user input entered via the Grammarly Keyboard app.

**Instructions**: Enable USB debugging on the target Android device, connect it to a host machine via USB, and use ADB to monitor logs while interacting with the app. Install the vulnerable Grammarly Keyboard app if not present, set it as the default keyboard, enter non-sensitive text in another app, then extract and filter logs for leaked input.

**Expected Output**: Log entries containing the entered user text, confirming the leakage.

**Success Indicators**:
- Logs show user-entered text from Grammarly Keyboard
- No leakage observed for sensitive fields (e.g., passwords)

## Attack Chain Summary

### Key Achievements

1. Successful capture of leaked user input from app logs
2. Verification of vulnerability on older Android versions
3. Assessment of low-impact information exposure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Data from Local System]]

### MITRE ATT&CK Tactics

- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
