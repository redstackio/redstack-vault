---
tags:
  - android
  - malicious-apk
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1626.002]]'
updated_at: '2025-12-14T03:46:31.956Z'
sub_techniques: []
id: d90372a2-79bb-496d-95ac-aab615842e0b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1626.002]]'
---
# Install-Malicious-Attacker-App

## Summary

This procedure deploys a custom malicious APK designed to exploit the Exness app by launching intents targeting the exported SMFeedbackActivity.

## Description

The attacker app contains Java code to use getLaunchIntentForPackage and setClassName for targeting com.surveymonkey.surveymonkeyandroidsdk.SMFeedbackActivity in the Exness package, with timed delays to inject payloads after app launch. Installation can be via sideloading or phishing to gain device access.

## Requirements

1. Compiled malicious APK (built in Android Studio with exploit code)
2. Android device allowing unknown sources
3. ADB or direct file transfer for sideloading

## Defense

Defensive measures and detection strategies:

- Enable Google Play Protect to scan side-loaded APKs
- Restrict unknown source installations
- Monitor for apps with intent-launching permissions

## Objectives

1. Place the exploit vector on the device
2. Ensure compatibility with target app
3. Avoid detection during installation

## Instructions

### Step 1: Prepare and Sideload APK

**Context**: Transfer and install the custom APK containing the exploit sequence.

Use ADB: adb install malicious.apk

> Expected output: Success message, app listed in device apps.

### Step 2: Grant Permissions

**Context**: Allow necessary permissions for activity launching.

In app settings, enable any required runtime permissions.

> Expected output: Permissions granted without user prompts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1626.002]] Component with Known Vulnerability

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- android
- malicious-apk
