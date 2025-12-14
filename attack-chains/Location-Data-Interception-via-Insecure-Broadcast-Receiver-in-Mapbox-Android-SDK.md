---
tags:
  - android
  - information-disclosure
  - broadcast-receiver
  - location-leak
  - mapbox-sdk
type: attack_chain
tools:
  - '[[tools/JADX]]'
  - '[[tools/Android-Debug-Bridge]]'
tactics:
  - '[[Collection]]'
  - '[[Initial Access]]'
commands:
  - '[[commands/adb-install-apk]]'
platforms:
  - Android
complexity: low
procedures:
  - '[[procedures/Analyze-Android-SDK-for-Broadcast-Vulnerabilities]]'
  - '[[procedures/Implement-Malicious-Broadcast-Receiver-for-Interception]]'
step_count: 2
techniques:
  - '[[Adversary-in-the-Middle]]'
description: >-
  Demonstrates the interception of sensitive location data exposed by the Mapbox
  Android SDK's use of global Broadcast Receivers, allowing malicious apps to
  capture broadcasts outside the app's process.
skill_level: intermediate
impact_level: low
id: b7e125ac-50e9-4d1a-b03c-5d34b78f780e
created_at: '2025-12-14T17:24:42.127Z'
updated_at: '2025-12-14T17:24:42.127Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Location Data Interception via Insecure Broadcast Receiver in Mapbox Android SDK

Multi-stage attack chain demonstrating how a malicious Android app can exploit the Mapbox SDK's improper use of global Broadcast Receivers to intercept sensitive location data. The vulnerability stems from broadcasting location services requests without process isolation, enabling any app on the device to listen in. This was discovered through code analysis and can lead to unauthorized access to user location information.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Analyze SDK Code] --> B[Implement Malicious Receiver]
    B --> C[Install and Intercept Data]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/JADX]]
- [[tools/Android-Debug-Bridge]]

### Target Environment

- Android device or emulator (API level compatible with Mapbox SDK v4.0-4.2.0)
- Installed app using vulnerable Mapbox Android SDK
- USB debugging enabled on device

### Initial Access Requirements

- ADB access to the target Android device
- Android development environment (e.g., Android Studio)
- Knowledge of the specific broadcast intent action used by Mapbox (determined via analysis)

## Detailed Attack Procedures

### Step 1: Analyze Mapbox Android SDK
procedure: [[procedures/Analyze-Android-SDK-for-Broadcast-Vulnerabilities]]

**Objective**: Perform static code analysis to identify the use of global Broadcast Receivers for location data, confirming the lack of LocalBroadcastManager.

**Instructions**: Obtain the Mapbox SDK JAR or APK, then use [[tools/JADX]] to decompile and search for BroadcastReceiver implementations in the location services module. Look for calls to `sendBroadcast()` without `LocalBroadcastManager.getInstance(context).sendBroadcast()` and note the intent actions (e.g., location update intents).

**Expected Output**: Decompiled Java code showing vulnerable broadcast patterns, such as explicit or implicit intents for location data without process restrictions.

**Success Indicators**:
- Identification of BroadcastReceiver class handling location services
- Confirmation of global broadcast scope allowing cross-app reception

### Step 2: Implement and Install Malicious Receiver
procedure: [[procedures/Implement-Malicious-Broadcast-Receiver-for-Interception]]

**Objective**: Develop and deploy a malicious Android app that registers a BroadcastReceiver to capture the vulnerable location broadcasts from the Mapbox SDK.

**Instructions**: In Android Studio, create a new project and add a BroadcastReceiver in the AndroidManifest.xml for the identified intent action. Implement the receiver to log or exfiltrate extras from the intent (e.g., latitude/longitude). Build the APK, then install it on the target device using [[commands/adb-install-apk]]:

```bash
adb install ./malicious-receiver.apk
```

Trigger location services in the target Mapbox app and monitor logs (via `adb logcat`) for intercepted data.

**Expected Output**: APK installed successfully; log entries showing received intents with location data when the Mapbox app broadcasts.

**Success Indicators**:
- Malicious app receives broadcast intents from Mapbox app
- Location data (e.g., coordinates) captured in app logs

## Attack Chain Summary

### Key Achievements

1. Static analysis reveals insecure broadcast usage in Mapbox SDK location module
2. Successful interception of sensitive location data by a co-located malicious app
3. Demonstration of information disclosure risk without requiring root or elevated privileges

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Adversary-in-the-Middle]]

### MITRE ATT&CK Tactics

- [[Collection]]
- [[Initial Access]]

---
*Last updated: 2024-10-01T00:00:00Z*
