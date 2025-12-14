---
tags:
  - android
  - installation
type: procedure
tools:
  - '[[tools/SurveyMonkey-Android-SDK]]'
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
updated_at: '2025-12-14T03:46:31.970Z'
sub_techniques: []
id: ef10da8e-f98f-4c63-a2d0-44df30bdcbfb
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1626.002]]'
---
# Install-Exness-Social-Trading-App

## Summary

This procedure installs the vulnerable Exness Social Trading Android app, ensuring the target environment is set up for exploitation of the SurveyMonkey SDK vulnerability.

## Description

The Exness Social Trading app (version 2.45.8-release) integrates the SurveyMonkey SDK with an exported SMFeedbackActivity, allowing external apps to launch it and inject malicious payloads into a JavaScript-enabled WebView. This step prepares the device by installing the app from the Google Play Store, where static analysis reveals the improper export in AndroidManifest.xml and direct passing of Intent Extras to loadDataWithBaseURL.

## Requirements

1. Android device with Google Play Store access
2. No prior app installation conflicts
3. Sufficient storage for APK (~50MB)

## Defense

Defensive measures and detection strategies:

- Review app permissions and SDK integrations during development
- Set android:exported='false' for sensitive activities
- Monitor for side-loaded apps launching external intents

## Objectives

1. Establish the vulnerable app on the target device
2. Verify app version and login functionality
3. Prepare for malicious app deployment

## Instructions

### Step 1: Download and Install App

**Context**: Locate and install the official app to confirm vulnerability presence.

No specific command; use Google Play Store to search for "Exness Social Trading" and install com.exness.investments version 2.45.8-release.

> Expected output: Installation complete, app icon appears on home screen.

### Step 2: Verify Installation

**Context**: Launch app to ensure it runs and supports WebView logins.

Open the app and attempt login to my.exness.asia to populate WebView cookies.

> Expected output: Successful login, positions and portfolio visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1626.002]] Component with Known Vulnerability

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/SurveyMonkey-Android-SDK]]

## Tags

- android
- installation
