---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - csrf
  - qr-code
  - deeplink
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:57.407Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Malicious-QR-Code-for-Periscope-Deeplink-CSRF

## Summary

This procedure generates a QR code that encodes a malicious deeplink for the Periscope iOS app, exploiting CSRF in the follow action to force unauthorized profile follows without user confirmation.

## Description

The Periscope iOS app handles deeplinks via the `pscp://` URI scheme. By encoding `pscp://user/periscopeco/follow` (or similar for any user ID) into a QR code, an attacker can trick a logged-in user into scanning it, causing the app to automatically execute the follow action. This bypasses any confirmation dialogs due to lack of CSRF protection in deeplink handling. The attack requires the app to be installed and the user logged in; it's effective for spam or unwanted subscriptions.

## Requirements

1. Access to a QR code generation tool or library (e.g., online generator or qrencode CLI)
2. Knowledge of the target user ID for the follow action
3. iOS device with Periscope app for testing

## Defense

Defensive measures and detection strategies:

- Implement user confirmation for all deeplink-triggered sensitive actions in the app
- Disable automatic URI scheme handling or add CSRF tokens to deeplinks
- Educate users on risks of scanning unknown QR codes
- Monitor app logs for unexpected follow actions

## Objectives

1. Create a scannable QR code payload that triggers CSRF in Periscope
2. Force unauthorized follow of a specified profile
3. Demonstrate impact on user subscriptions without consent

## Instructions

### Step 1: Generate the Deeplink URL

**Context**: Construct the exact deeplink URL targeting the follow action for a specific user.

Use the format `pscp://user/<user-id>/follow`, replacing `<user-id>` with the target (e.g., `periscopeco`).

**Expected Output**: A string like `pscp://user/periscopeco/follow`.

### Step 2: Encode into QR Code

**Context**: Use a QR code generator to create an image from the deeplink URL.

Visit an online QR code generator (e.g., qr-code-generator.com) or use a command-line tool like qrencode if available:

```bash
qrencode -o csrf-qr.png "pscp://user/periscopeco/follow"
```

> This command generates a PNG image file `csrf-qr.png` encoding the deeplink. If qrencode is not installed, use an online tool to input the URL and download the QR image.

**Expected Output**: QR code image file ready for distribution.

### Step 3: Test the Payload

**Context**: Verify the QR code triggers the CSRF on a test iOS device.

Scan the QR with an iOS device running Periscope (logged in). The app should open and follow the user without prompts.

**Expected Output**: App launches, follow action completes silently.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[qr-code]]
- [[deeplink]]
