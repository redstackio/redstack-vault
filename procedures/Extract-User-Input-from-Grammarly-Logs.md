---
id: proc-grammarly-log-extract
tags:
  - information-exposure
  - android
  - logging
  - adb
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/adb-logcat-capture]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:24:45.306Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Extract-User-Input-from-Grammarly-Logs

## Summary

This procedure demonstrates how to exploit the debug logging vulnerability in the Grammarly Keyboard Android app (versions <4.1) by extracting device logs to reveal non-sensitive user-entered text. It targets older Android devices (<5.0) where the app fails to sanitize input in logs, allowing local access to potentially useful information.

## Description

The Grammarly Keyboard app logs user input for debugging purposes without proper restrictions on older Android platforms, leading to information exposure. An attacker with device access can use tools like ADB to capture these logs while the user interacts with the keyboard. Sensitive fields (e.g., passwords) are excluded from logging, limiting the impact to non-sensitive data. This is useful in physical access scenarios or for post-compromise analysis on rooted/jailbroken devices. Prerequisites include USB debugging enabled and the vulnerable app installed.

## Requirements

1. Android device with version <5.0 and USB debugging enabled
2. Grammarly Keyboard app version <4.1 installed and set as default keyboard
3. Host machine with ADB installed and USB connection to device
4. Basic knowledge of Android log analysis

## Defense

Defensive measures and detection strategies:

- Update the Grammarly Keyboard app to version 4.1 or later to fix logging sanitization
- Disable USB debugging on production devices and restrict physical access
- Monitor device logs for unauthorized ADB connections or log extractions
- Use app sandboxing and review permissions for keyboard apps

## Objectives

1. Capture leaked user input from app logs to demonstrate information exposure
2. Verify that only non-sensitive text is leaked, assessing low severity
3. Identify vulnerable app versions and platforms for remediation

## Instructions

### Step 1: Setup Device Connection

**Context**: Connect the target Android device to the host machine and verify ADB access to enable log monitoring.

**Command** ([[commands/adb-logcat-capture]]):
```bash
adb devices
```

> This lists connected devices. Expected output: Device listed as 'device' status. If authorized, proceed; otherwise, enable USB debugging in device settings.

### Step 2: Install and Configure Vulnerable App

**Context**: Ensure the Grammarly Keyboard app is installed and active to trigger logging during input.

Install via ADB if needed:
```bash
adb install grammarly-keyboard.apk
```

> Replace with the APK path for version <4.1. Then, in device settings, set Grammarly as default keyboard and open a text input app (e.g., Notes).

### Step 3: Capture Logs During Input

**Context**: Monitor logs in real-time while entering non-sensitive text to capture the leakage.

**Command** ([[commands/adb-logcat-capture]]):
```bash
adb logcat | grep -i grammarly
```

> Enter text like 'test input for vulnerability' in an app using the Grammarly keyboard. Expected output: Log lines containing the entered text, e.g., 'User input: test input for vulnerability'. Test sensitive fields (e.g., password) to confirm no leakage.

### Step 4: Analyze Extracted Logs

**Context**: Filter and review logs offline to confirm exposure.

Save logs:
```bash
adb logcat > device_logs.txt
```

> Search the file for Grammarly-related entries: `grep -i 'input' device_logs.txt`. Expected output: Confirmation of leaked text in debug logs.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]

### Sub-Techniques


## Commands Used

- [[commands/adb-logcat-capture]]

## Tools Used


## Tags

- information-exposure
- android
- logging
- adb
