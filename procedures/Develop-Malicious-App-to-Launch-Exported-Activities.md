---
id: proc-develop-malicious-app-launch
tags:
  - android
  - malicious-apk
  - intent-exploitation
type: procedure
tools:
  - '[[tools/Android-Studio]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:44.593Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Develop-Malicious-App-to-Launch-Exported-Activities

## Summary

This procedure details creating a simple malicious Android app that sends intents to launch exported activities in the Nextcloud app, bypassing permission checks. It is used in proof-of-concept exploits for Android component vulnerabilities.

## Description

Targeting the Nextcloud app's exported activities, this involves building an APK with code to create and fire explicit intents to classes like com.owncloud.android.ui.activity.FileDisplayActivity. The malicious app installs on the same device and triggers the activity without authentication, exploiting the lack of android:permission. Requires Android Studio and a development setup.

## Requirements

1. Android Studio installed for app development
2. Target device or emulator with Nextcloud app installed
3. Knowledge of Android Intents API

## Defense

Defensive measures and detection strategies:

- Implement signature-based permissions for activities
- Scan for sideloaded malicious APKs using antivirus like Google Play Protect
- Log and alert on cross-app intent invocations

## Objectives

1. Build an APK capable of launching Nextcloud activities
2. Test intent resolution without authentication
3. Enable data access via exploited components

## Instructions

### Step 1: Set Up Android Studio Project

**Context**: Create a new Android project for the malicious app.

Launch Android Studio, create a new Empty Activity project named MaliciousLauncher. Set minimum SDK to match Nextcloud's (API 21+).

### Step 2: Implement Intent Code

**Context**: Add code to send an intent to a vulnerable activity.

In MainActivity.java, add:

```java
import android.content.Intent;

Intent intent = new Intent();
intent.setClassName("com.owncloud.android", "com.owncloud.android.ui.activity.FileDisplayActivity");
startActivity(intent);
```

Place this in onCreate() triggered by a button click.

### Step 3: Build and Install the APK

**Context**: Compile the app and deploy to the device.

Build the APK via Build > Build Bundle/APK. Install using ADB: `adb install malicious.apk`. Launch the app and trigger the intent to verify it starts the Nextcloud activity.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript (adapted for Java in Android)

### Sub-Techniques


## Commands Used


## Tools Used

- [[Android Studio]]

## Tags

- [[android]]
- [[malicious-apk]]
- [[intent-exploitation]]
