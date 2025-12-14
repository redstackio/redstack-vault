---
id: proc-uuid-001
tags:
  - android
  - app-install
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
  - '[[T1566.001]]'
updated_at: '2025-12-14T17:33:06.358Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Install-Exness-Social-Trading-App

## Summary

This procedure installs the vulnerable Exness Social Trading Android app, setting up the target environment for exploitation of the SMFeedbackActivity vulnerability.

## Description

The Exness Social Trading app (com.exness.investments, version 2.45.8-release) integrates the SurveyMonkey SDK with an exported SMFeedbackActivity, allowing intent-based attacks. Installation from the official source ensures the app is in its default vulnerable state, with WebViews using shared cookie storage for sites like my.exness.asia. Prerequisites include an Android device; no login is needed initially, but exploitation assumes a logged-in session for cookie theft.

## Requirements

1. Android device or emulator (API 21+ recommended)
2. Google Play Store access
3. Sideloading enabled for subsequent attacker app

## Defense

Defensive measures and detection strategies:

- Review AndroidManifest.xml for exported activities during app development
- Use app shielding tools like DexGuard to restrict intent handling
- Monitor for anomalous app launches via device logs (adb logcat)

## Objectives

1. Establish the vulnerable target app on the device
2. Verify app integrity and version
3. Prepare for parallel installation of attacker components

## Instructions

### Step 1: Download from Play Store

**Context**: Obtain the official APK to avoid tampering flags.

Search for "Exness Social Trading" in Google Play Store and install version 2.45.8-release.

**Expected Output**: Installation prompt succeeds; app appears in app drawer.

### Step 2: Verify Installation

**Context**: Confirm the app is ready and vulnerable.

Launch the app briefly, then check version in settings > about.

**Expected Output**: Version 2.45.8-release displayed; app closes normally.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.001]] Phishing: Spearphishing Attachment (app installation as entry point)

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-Attacker-App]]

## Tags

- android
- app-install
