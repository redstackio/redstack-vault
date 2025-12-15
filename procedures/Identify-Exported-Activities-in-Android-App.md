---
id: proc-identify-exported-activities
tags:
  - android
  - reconnaissance
  - apk-analysis
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:28:44.597Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify-Exported-Activities-in-Android-App

## Summary

This procedure involves analyzing an Android APK to identify exported activities that lack permission attributes, enabling potential exploitation by external apps. It is primarily used in mobile app security assessments to uncover improper component exports in apps like Nextcloud.

## Description

In the context of the Nextcloud Android app vulnerability, exported activities such as FileDisplayActivity allow external apps to launch them without authentication. By decompiling the APK and inspecting the AndroidManifest.xml, attackers can find activities with android:exported="true" but no android:permission, leading to unauthorized access. Prerequisites include an Android development environment and the target APK file.

## Requirements

1. Android APK file of the target app (e.g., Nextcloud from Google Play or sideloaded)
2. APK decompilation tool like APKTool or Jadx GUI
3. Basic knowledge of Android manifest structure

## Defense

Defensive measures and detection strategies:

- Set android:exported="false" for sensitive activities or add custom permissions
- Use mobile security scanners like MobSF to detect exported components during app reviews
- Monitor for anomalous app launches via device logs

## Objectives

1. Discover vulnerable exported activities in the target app
2. Document activities without permission checks
3. Prepare for intent-based exploitation

## Instructions

### Step 1: Obtain and Decompile the APK

**Context**: Acquire the Nextcloud APK and decompile it to access the manifest file.

Download the APK using a tool like APK Downloader or extract from an installed app via ADB. Then decompile:

- Use APKTool: `apktool d nextcloud.apk`

This extracts resources including AndroidManifest.xml.

### Step 2: Inspect the AndroidManifest.xml

**Context**: Search for activity declarations with exported=true but no permission.

Open AndroidManifest.xml in a text editor or XML viewer. Look for lines like:

```xml
<activity android:name="com.owncloud.android.ui.activity.FileDisplayActivity" android:exported="true" />
```

Identify the four vulnerable activities: FileDisplayActivity, ReceiveExternalFilesActivity, AuthenticatorActivity, ShareActivity.

### Step 3: Verify Export Status

**Context**: Confirm the activities can be targeted by external intents.

Use ADB or an emulator to test intent resolution without installing a malicious app:

- `adb shell am start -n com.owncloud.android/.ui.activity.FileDisplayActivity`

If it launches without errors, the activity is exploitable.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[android]]
- [[Reconnaissance]]
- [[apk-analysis]]
