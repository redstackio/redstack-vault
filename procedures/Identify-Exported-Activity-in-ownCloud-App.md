---
tags:
  - android
  - recon
  - app-analysis
type: procedure
tools:
  - '[[tools/ADB-Android-Debug-Bridge]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:24:45.285Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 0e51bfd2-ec35-4637-86e6-b1ea8cdf6133
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify Exported Activity in ownCloud App

## Summary

This procedure involves analyzing the ownCloud Android app to identify the exported ReceiveExternalFilesActivity, which handles incoming file intents without proper validation, setting the stage for exploitation.

## Description

By inspecting the app's AndroidManifest.xml or decompiling the APK, attackers can discover that com.owncloud.android.ui.activity.ReceiveExternalFilesActivity is exported and processes android.intent.action.SEND intents with android.intent.extra.STREAM URIs. This lack of export restrictions allows any app or external tool to target it. The procedure requires tools like APK decompilers (e.g., JADX) or ADB for runtime inspection on a device with the app installed.

## Requirements

1. Android device or emulator with ownCloud app (v2.8.0 or below) installed
2. ADB access for pulling the APK or inspecting runtime
3. APK analysis tools like APKTool or JADX

## Defense

Defensive measures and detection strategies:

- Use app shielding tools to detect exported activities
- Monitor inter-app intent traffic with runtime security apps like AppSealing
- Regularly audit app manifests for exported components

## Objectives

1. Locate vulnerable exported activities in target apps
2. Understand intent handling for exploitation planning
3. Confirm no path validation on file URIs

## Instructions

### Step 1: Pull and Decompile APK

**Context**: Extract the app's APK for static analysis to find exported activities.

**Command** ([[commands/adb-pull-apk]]):
```bash
adb pull /data/app/com.owncloud.android-*/base.apk owncloud.apk
```

> This pulls the APK from the device. Then use JADX or similar to open owncloud.apk and search for ReceiveExternalFilesActivity in AndroidManifest.xml to confirm <activity android:exported="true">.

### Step 2: Inspect Activity Code

**Context**: Review the activity's code to verify URI processing without validation.

No specific command; manually inspect the decompiled Java code for onCreate or onReceive handling of getParcelableExtra("android.intent.extra.STREAM").

> Expected: Code that opens and processes the URI without checking if it's external or safe.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ADB-Android-Debug-Bridge]]

## Tags

- android
- app-analysis
