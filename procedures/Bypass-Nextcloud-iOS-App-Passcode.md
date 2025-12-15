---
tags:
  - auth-bypass
  - passcode-bypass
  - nextcloud
  - ios
  - mobile
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile App
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:42.706Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: 9d56ec97-2196-4a94-b31f-cb6917e82542
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-Nextcloud-iOS-App-Passcode

## Summary

This procedure exploits a vulnerability in the Nextcloud iOS app's passcode authentication system, allowing full bypass of the lock screen to gain unauthorized access to the application's data and features. Reported on HackerOne as a low-severity issue (CVSS 1.8), it stems from improper implementation of access controls, enabling attackers with device access to view synced files and account information without credentials.

## Description

The Nextcloud iOS app includes a passcode feature to protect user data when the device is unlocked. However, due to flawed access control logic, the app does not properly validate passcode entry, permitting users to proceed directly to the main interface upon launch. This vulnerability was discovered through manual testing and reported via HackerOne (Report #1847368). It affects app versions prior to the patch and requires only local device access, with no remote exploitation possible. Successful execution grants immediate read/write access to Nextcloud-synced content, potentially exposing sensitive files, but does not extend to device-wide compromise or server-side escalation.

## Requirements

1. iOS device with Nextcloud app installed and passcode feature enabled
2. Physical access to the unlocked device (no jailbreak required)
3. App version vulnerable to the improper access control flaw (pre-patch releases)

## Defense

Defensive measures and detection strategies:

- Update the Nextcloud iOS app to the latest version to apply access control fixes
- Enable device-level biometric authentication (e.g., Face ID or Touch ID) as an additional layer
- Monitor app logs for anomalous access patterns, such as repeated launches without passcode prompts
- Use mobile device management (MDM) tools to enforce app security policies and restrict local access

## Objectives

1. Bypass app passcode to access protected data
2. View and potentially exfiltrate Nextcloud-synced files
3. Demonstrate the impact of improper authentication controls in mobile apps

## Instructions

### Step 1: Prepare the Target Device

**Context**: Ensure the Nextcloud app is installed with passcode enabled to set up the vulnerable state.

Open the iOS Settings app, navigate to the Nextcloud app settings, and enable the passcode protection feature. Lock the app and confirm the passcode prompt appears on next launch.

**Expected Output**: Passcode screen displays when attempting to open the app.

### Step 2: Exploit the Bypass

**Context**: Launch the app to trigger the improper access control flaw, allowing entry without verification.

Simply tap the Nextcloud app icon to launch it. The vulnerability causes the passcode verification to be skipped due to inadequate checks in the authentication flow, granting direct access to the dashboard.

**Expected Output**: App opens to the main file viewer or sync status without requiring passcode input.

### Step 3: Validate Access

**Context**: Confirm unauthorized access by interacting with app features.

Browse files, access account settings, or attempt to sync new data. All functions should operate as if properly authenticated.

**Expected Output**: Full read/write access to app contents, including any synced documents or photos.

**Success Indicators**:
- No passcode prompt or automatic dismissal
- Ability to view sensitive data
- No errors in app functionality post-bypass

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- auth-bypass
- passcode-bypass
- nextcloud
- ios
- mobile
