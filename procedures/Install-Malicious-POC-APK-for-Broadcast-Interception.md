---
id: proc-shopify-install-poc-001
tags:
  - android
  - malicious-app
  - broadcast-interception
type: procedure
tools:
  - '[[tools/Custom-POC-APK-shopifyhack]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[T1475]]'
updated_at: '2025-12-14T17:32:11.009Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1475]]'
---
# Install-Malicious-POC-APK-for-Broadcast-Interception

## Summary

This procedure installs a custom proof-of-concept APK that registers a broadcast receiver to monitor the Shopify app's unprotected 'com.shopify.service.requestComplete' action, enabling interception of sensitive API data without any special permissions.

## Description

The Shopify Android client uses implicit broadcasts to communicate API request completions, which any app can receive due to lack of permission protection. This procedure deploys a malicious POC APK that silently registers a receiver in the background, setting up for data leakage during user interactions like login. The attack requires sideloading the APK on the target device, exploiting Android's inter-app communication model.

## Requirements

1. Android device with USB debugging enabled and developer options active
2. Shopify Android client installed from official sources
3. Access to the POC APK file (shopifyhack.apk)
4. ADB tools for installation if not manual

## Defense

Defensive measures and detection strategies:

- Enforce app installation from trusted sources only (e.g., Google Play)
- Use mobile device management (MDM) to restrict sideloading
- Monitor for unusual apps or log broadcast registrations via app analysis tools
- Apply signature-level permissions to broadcasts in app development

## Objectives

1. Establish persistent monitoring for Shopify broadcasts
2. Avoid detection by running in background without UI
3. Prepare for interception of API responses containing credentials

## Instructions

### Step 1: Download and Prepare POC APK

**Context**: Obtain the POC APK that includes the HackBroadcastReceiver and manifest intent-filter for the target action.

No command required; download from provided URL and transfer to device via ADB or file manager.

> Ensure the APK is signed and compatible with the device's Android version.

### Step 2: Install POC APK and Shopify App

**Context**: Install both apps to enable the receiver to monitor broadcasts from Shopify.

Use ADB for installation:

```bash
adb install shopifyhack.apk
adb install shopify-app.apk  # If not already installed
```

> This installs the POC without permissions, registering the receiver automatically on boot or launch.

### Step 3: Verify Installation

**Context**: Confirm the receiver is active without triggering alerts.

Check installed packages:

```bash
adb shell pm list packages | grep shopify
```

> Expected output includes both Shopify and the POC package names.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1475]] Install Malicious Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-POC-APK-shopifyhack]]

## Tags

- android
- malicious-app
- broadcast-interception
