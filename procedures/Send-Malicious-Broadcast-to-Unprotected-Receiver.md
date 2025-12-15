---
tags:
  - broadcast-receiver
  - android
  - exploitation
  - adb
type: procedure
tools:
  - '[[tools/Android-Debug-Bridge]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/adb-send-broadcast]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:24:42.606Z'
sub_techniques: []
id: 9338ff4a-ab11-498e-896e-7e88e3ff9b68
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Send-Malicious-Broadcast-to-Unprotected-Receiver

## Summary

This procedure exploits an unprotected broadcast receiver in the Nextcloud Talk Android app by sending unauthorized broadcasts via ADB, demonstrating interference with call starts and audio/Bluetooth setup due to the missing broadcastPermission.

## Description

The vulnerability allows any app (or external tool like ADB) to send intents to the receiver without checks, potentially causing denial of service or data manipulation during calls. Target an installed Nextcloud Talk app on an ADB-enabled device. Outcomes include observed disruptions, validating the access control flaw. Requires developer mode enabled on the device.

## Requirements

1. ADB installed and device connected via USB with debugging enabled
2. Nextcloud Talk app installed and vulnerable version confirmed
3. Knowledge of the broadcast action (e.g., from manifest or static analysis)

## Defense

Defensive measures and detection strategies:

- Add explicit broadcastPermission to registerReceiver calls in app code
- Monitor device logs for unexpected am broadcast commands via ADB
- Implement runtime permission checks for sensitive broadcast actions

## Objectives

1. Gain unauthorized access to the app's broadcast receiver
2. Disrupt core functionality like call initiation or audio routing
3. Validate the vulnerability's exploitability for reporting or mitigation

## Instructions

### Step 1: Identify Broadcast Action

**Context**: Determine the intent action for the receiver (e.g., via APK decompilation or logs).

**Command** ([[commands/adb-logcat-filter]]):
```bash
adb logcat | grep NextcloudTalk
```

> Filter logs while starting a call to capture broadcast actions. Expected output: Intent actions like "com.nextcloud.talk.CALL_START".

### Step 2: Send Malicious Broadcast

**Context**: Simulate a malicious app by broadcasting an intent to interfere.

**Command** ([[commands/adb-send-broadcast]]):
```bash
adb shell am broadcast -a com.nextcloud.talk.CALL_START --es interference_flag "disrupt"
```

> This sends the broadcast with extras to trigger interference. Expected output: No error; app reacts by failing call setup or altering audio.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used

- [[commands/adb-logcat-filter]]
- [[commands/adb-send-broadcast]]

## Tools Used

- [[tools/Android-Debug-Bridge]]

## Tags

- [[app-exploitation]]
- [[broadcast-abuse]]
