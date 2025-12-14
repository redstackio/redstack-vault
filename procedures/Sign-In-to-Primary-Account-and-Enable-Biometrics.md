---
tags:
  - bitwarden
  - android
  - biometric
  - authentication
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:42.458Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 1075ad9e-a6fb-4d8f-bdef-2af362259d2e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Sign-In-to-Primary-Account-and-Enable-Biometrics

## Summary

This procedure logs into the Bitwarden Android app using a primary account and enables biometric unlock, establishing the baseline for exploiting the biometric integrity bypass vulnerability.

## Description

In the context of the Bitwarden vulnerability (HackerOne #1929915), this step authenticates the primary account normally and activates fingerprint-based unlock. It requires physical device access and sets up the app state before invalidating the integrity check. Expected outcome: Primary vault accessible with biometrics enabled, preparing for fingerprint change to trigger the flaw in BiometricIntegrityValid flag enforcement.

## Requirements

1. Android device with Bitwarden app installed and fingerprint sensor
2. Primary Bitwarden account credentials (email and master password)
3. Device unlocked for app access

## Defense

Defensive measures and detection strategies:

- Enforce app updates to patch the vulnerability (check Bitwarden releases for GH-1026 fixes)
- Disable biometrics or require master password periodically
- Monitor device for unauthorized app access via mobile device management (MDM) tools

## Objectives

1. Authenticate primary account to access vault
2. Enable biometrics for subsequent bypass setup
3. Confirm app state is ready for integrity invalidation

## Instructions

### Step 1: Launch and Authenticate

**Context**: Open the app and sign in to establish the primary session.

Navigate to the Bitwarden app icon and launch it. Enter the primary account email and master password in the login fields, then tap 'Log In'.

> Successful login grants access to the primary vault.

### Step 2: Enable Biometric Unlock

**Context**: Activate fingerprint authentication for quick unlock.

Go to Settings (gear icon) > Security > Unlock with Biometrics. Toggle the option on and confirm with device biometrics if prompted.

> Biometrics are now enabled; the app uses the current fingerprint for unlocks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[bitwarden]]
- [[android]]
- [[biometric]]
