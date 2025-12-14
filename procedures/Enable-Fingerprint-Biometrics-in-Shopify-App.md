---
id: p-enable-shopify-biometrics
tags:
  - setup
  - biometrics
  - android
type: procedure
tools:
  - '[[tools/ADB]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:36.404Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Enable-Fingerprint-Biometrics-in-Shopify-App

## Summary

This procedure activates fingerprint biometrics in the Shopify Android app settings, establishing the authentication baseline that subsequent steps will bypass via deeplink exploitation.

## Description

In the context of testing the Shopify Android app (com.shopify.mobile), enabling biometrics simulates a secure user environment. The app's DeepLinkActivity vulnerability allows bypassing this check when intents are triggered, leading to unauthorized access. This step requires manual interaction on the device and assumes the app is installed with a logged-in session.

## Requirements

1. Android device with fingerprint sensor and Shopify app installed
2. ADB access for device interaction (optional for this step)
3. Existing app login to access settings

## Defense

Defensive measures and detection strategies:

- Enforce app-level policies requiring re-auth for all external intents
- Monitor ADB usage on production devices
- Implement biometric re-prompt on any activity launch

## Objectives

1. Activate biometrics to enable bypass testing
2. Verify app prompts for fingerprint on launch
3. Prepare session for deeplink exploitation

## Instructions

### Step 1: Access App Settings

**Context**: Open the Shopify app and navigate to settings to toggle biometrics.

No command required; manual steps:

1. Launch the app.
2. Go to Profile > Settings > Security.
3. Enable 'Use Fingerprint' option.
4. Confirm with device fingerprint.

> This sets up the auth mechanism. Expected: App locks on next launch.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ADB]]

## Tags

- setup
- biometrics
