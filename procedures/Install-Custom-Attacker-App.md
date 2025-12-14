---
id: proc-uuid-002
tags:
  - android
  - apk-install
  - malware
type: procedure
tools:
  - '[[tools/Custom-Attacker-App]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:33:06.356Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Install-Custom-Attacker-App

## Summary

This procedure deploys a custom malicious Android APK designed to exploit the Exness app by launching intents to the vulnerable SMFeedbackActivity.

## Description

The attacker app uses Android APIs like getLaunchIntentForPackage and startActivity to target the Exness app. It injects Intent Extras (smSPageURL and smSPageHTML) without validation, exploiting the lack of restrictions on the exported activity. This setup enables payload delivery in a controlled manner with built-in delays for sequencing.

## Requirements

1. Android device with unknown sources enabled (Settings > Security)
2. Access to the malicious APK file
3. ADB optional for installation (adb install malicious.apk)

## Defense

Defensive measures and detection strategies:

- Enforce APK signature verification and restrict sideloading
- Use mobile threat defense (MTD) solutions to scan for malicious intents
- Log intent broadcasts for anomalies (e.g., via Android Debug Bridge)

## Objectives

1. Install the exploit delivery mechanism
2. Ensure compatibility with target app
3. Avoid detection during installation

## Instructions

### Step 1: Enable Sideloading

**Context**: Allow installation of non-Play Store APKs.

Go to Settings > Apps > Special access > Install unknown apps, enable for file manager.

**Expected Output**: Permission granted; no errors.

### Step 2: Install APK

**Context**: Deploy the custom app.

Transfer the APK to device and install via file manager or `adb install com.attacker.apk`.

**Expected Output**: Installation complete; app icon added.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer (APK deployment)

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-Attacker-App]]

## Tags

- android
- apk-install
- malware
