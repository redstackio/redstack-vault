---
id: proc-owncloud-identify-exported
tags:
  - android
  - recon
  - exported-component
type: procedure
tools:
  - '[[tools/ADB-Android-Debug-Bridge]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/adb-dumpsys-package]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1631]]'
updated_at: '2025-12-14T17:24:41.910Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1631]]'
---
# Identify Vulnerable Exported Activity

## Summary

This procedure involves inspecting the Android app's manifest to identify exported activities that handle intents like SEND_MULTIPLE without proper validation, specifically targeting the ownCloud app's ReceiveExternalFilesActivity to enable subsequent file theft.

## Description

In Android apps, exported components can be invoked by other apps via intents. The ownCloud Android app (com.owncloud.android) exports com.owncloud.android.ui.activity.ReceiveExternalFilesActivity with an intent filter for android.intent.action.SEND_MULTIPLE, allowing it to receive file URIs for upload. Unlike the single SEND filter, this lacks protections against accessing protected directories (/data/data/com.owncloud.android/), making it vulnerable to intent injection from malicious apps. This step uses static analysis via ADB to confirm the vulnerability, setting up for crafting malicious intents to steal sensitive data like databases and cache.

## Requirements

1. ADB installed and device connected (USB debugging enabled)
2. ownCloud app installed on the target Android device
3. Basic knowledge of Android manifest structure

## Defense

Defensive measures and detection strategies:

- Use android:exported="false" in manifests for sensitive activities
- Validate URI permissions and paths in intent handlers (e.g., check if URI is from external sources only)
- Monitor for unexpected intent invocations via app logs or Android's StrictMode

## Objectives

1. Confirm the presence of an exported activity vulnerable to arbitrary URI handling
2. Identify the exact component and intent filter for exploitation
3. Gather technical details for crafting targeted intents

## Instructions

### Step 1: Connect Device and List Package

**Context**: Ensure ADB access and pull package information for the ownCloud app to locate exported components.

**Command** ([[commands/adb-shell]]):
```bash
adb shell
```

> This opens a shell on the device. Then run [[commands/adb-dumpsys-package]] to inspect:

**Command** ([[commands/adb-dumpsys-package]]):
```bash
dumpsys package com.owncloud.android
```

> Expected output includes activity details; grep for "ReceiveExternalFilesActivity" to see export=true and intent filters like <action android:name="android.intent.action.SEND_MULTIPLE" />.

### Step 2: Analyze Intent Filters

**Context**: Verify the activity accepts file URIs without restrictions, confirming vulnerability to protected path access.

**Command** ([[commands/adb-dumpsys-package-grep]]):
```bash
adb shell dumpsys package com.owncloud.android | grep -A 20 -B 5 "SEND_MULTIPLE"
```

> This filters output to show the intent filter, revealing acceptance of * /* types and STREAM extras without path validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[T1631]] Access Permission to Specific Component

### Sub-Techniques


## Commands Used

- [[commands/adb-dumpsys-package]]
- [[commands/adb-shell]]

## Tools Used

- [[tools/ADB-Android-Debug-Bridge]]

## Tags

- [[android]]
- [[recon]]
- [[exported-component]]
