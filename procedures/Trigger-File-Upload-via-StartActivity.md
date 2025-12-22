---
id: proc-owncloud-trigger-upload
tags:
  - android
  - exfiltration
  - intent-trigger
type: procedure
tools:
  - '[[tools/ADB-Android-Debug-Bridge]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/adb-install-app]]'
  - '[[commands/adb-shell-am-start]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1429]]'
  - '[[T1631]]'
updated_at: '2025-12-14T17:24:41.900Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[T1429]]'
  - '[[T1631]]'
---
# Trigger File Upload via StartActivity

## Summary

This procedure launches the crafted malicious intent to invoke the ownCloud app's vulnerable activity, causing it to read and upload protected files to the server, resulting in data theft without user awareness.

## Description

Calling startActivity() on the malicious intent executes it in the ownCloud app's context, where the activity processes the STREAM extra as a file URI, reads the content (e.g., database file), and uploads it to the configured ownCloud server. This exploits the absence of validation, leading to exposure of user data like file history and credentials. The attack requires the malicious app to be installed and run, with ADB facilitating testing; outcomes include remote access to sensitive app internals.

## Requirements

1. Crafted malicious intent from prior procedure
2. Malicious APK built and ready for installation
3. Device with ownCloud app and server connectivity

## Defense

Defensive measures and detection strategies:

- Add user consent prompts for unexpected intents in exported activities
- Restrict uploads to validated URIs using ContentResolver and permission checks
- Detect anomalous uploads via server-side logging or app analytics for unusual file sources

## Objectives

1. Force the target app to process the malicious intent non-interactively
2. Achieve exfiltration of protected data to the remote server
3. Validate successful theft by checking server contents

## Instructions

### Step 1: Install Malicious App

**Context**: Deploy the app containing the intent to the target device.

**Command** ([[commands/adb-install-app]]):
```bash
adb install path/to/malicious_app.apk
```

> Expected output: Success message; app now installed as com.malicious or similar.

### Step 2: Launch Malicious App to Trigger Intent

**Context**: Start the malicious app's activity, which dispatches the intent to ownCloud.

**Command** ([[commands/adb-shell-am-start]]):
```bash
adb shell am start -n com.malicious/.MainActivity
```

> This runs the app; inside MainActivity.onCreate(), call startActivity(maliciousIntent) to invoke ownCloud. The target activity processes the URI, reads /data/data/com.owncloud.android/databases/filelist, and uploads it.

### Step 3: Verify Exfiltration

**Context**: Check the ownCloud server for the uploaded file to confirm success.

**Instructions**: Log into the ownCloud web interface or use the app to view recent uploads; the database file should appear as a new entry.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[T1429]] Component with Known Vulnerability
- [[T1631]] Access Permission to Specific Component

### Sub-Techniques


## Commands Used

- [[commands/adb-install-app]]
- [[commands/adb-shell-am-start]]

## Tools Used

- [[tools/ADB-Android-Debug-Bridge]]

## Tags

- [[android]]
- [[Exfiltration]]
- [[intent-trigger]]
