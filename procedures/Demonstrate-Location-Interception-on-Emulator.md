---
tags:
  - android
  - emulator
  - poc-demonstration
  - location-tracking
type: procedure
tools:
  - '[[tools/Android-Emulator]]'
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Android
techniques:
  - '[[T1429]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 67a11377-6564-4fcb-a3ff-008a41cbbb55
created_at: '2025-12-14T17:24:42.749Z'
updated_at: '2025-12-14T17:24:42.749Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[T1429]]'
---
# Demonstrate-Location-Interception-on-Emulator

## Summary

This procedure tests the POC app on an Android emulator to demonstrate real-time interception of Twitter's location broadcasts, recording the process for proof.

## Description

Targeting an emulated Android environment, this simulates a malicious app scenario where location data from Twitter is captured without permissions. It requires the Twitter app and POC installed, with location enabled. Outcomes include visual confirmation of data leakage via logs or UI, and a video PoC showing the vulnerability in action.

## Requirements

1. Android Emulator set up via Android Studio
2. Twitter APK and POC APK ready for installation
3. Emulator with location simulation enabled
4. Screen recording tool for documentation

## Defense

Defensive measures and detection strategies:

- Educate users on app permissions and broadcast risks
- Use emulator detection in apps to prevent testing
- Monitor for anomalous location data access on devices

## Objectives

1. Install and run both apps on emulator
2. Trigger and intercept location broadcasts
3. Record evidence of unauthorized surveillance

## Instructions

### Step 1: Set Up Emulator and Install Apps

**Context**: Prepare the testing environment.

Launch Android Emulator from Android Studio, create a virtual device (e.g., Pixel 3, API 28).

Install APKs via ADB:

```bash
adb install twitter.apk
adb install poc.apk
```

> Expected output: Both apps listed in emulator's app drawer.

### Step 2: Enable Location in Twitter

**Context**: Trigger the broadcast by activating location services.

Open Twitter app, navigate to settings, enable location services.

In emulator, use extended controls to set a mock location (e.g., latitude 37.7749, longitude -122.4194).

> This simulates user movement, sending the broadcast.

### Step 3: Observe and Record Interception

**Context**: Capture the POC receiving data.

Open POC app; check logs via Logcat in Android Studio or display in app UI.

Start screen recording to show Twitter location enablement and POC logging coordinates.

> Expected output: POC shows 'Intercepted Location: 37.7749, -122.4194' without requesting permissions.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[T1429]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Android-Emulator]]

## Tags

- [[android]]
- [[emulator]]
- [[poc-demonstration]]
