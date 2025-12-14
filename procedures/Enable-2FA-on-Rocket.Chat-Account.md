---
tags:
  - 2fa-setup
  - rocket-chat
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 5abea897-10ea-4c50-a540-60e2641eb4ae
created_at: '2025-12-14T17:24:47.910Z'
updated_at: '2025-12-14T17:24:47.910Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Enable-2FA-on-Rocket.Chat-Account

## Summary

This procedure activates two-factor authentication on a Rocket.Chat account, setting up the security layer that can be bypassed via email verification flaws.

## Description

After logging in, users navigate to account settings to enable 2FA using a time-based one-time password (TOTP) app. This generates a QR code for scanning. The procedure assumes a logged-in session and tests the 2FA enforcement. In the attack scenario, this step confirms the protection is active before exploiting the bypass.

## Requirements

1. Active Rocket.Chat account session
2. Authenticator app (e.g., Google Authenticator) installed on a mobile device
3. Web browser access to settings

## Defense

Defensive measures and detection strategies:

- Ensure 2FA is mandatory for all users
- Log 2FA enable/disable events for auditing
- Use hardware keys (e.g., YubiKey) for stronger protection

## Objectives

1. Activate 2FA to simulate protected account
2. Verify 2FA prompts on login
3. Prepare for bypass testing

## Instructions

### Step 1: Access Account Settings

**Context**: Log in and locate the 2FA configuration.

Navigate to My Account > Security > Two-Factor Authentication.

> Enable the feature and scan the QR code with your authenticator app.

### Step 2: Verify 2FA Setup

**Context**: Confirm functionality by testing a login.

Log out and log back in; enter the OTP from the app.

> Expected output: Successful login with 2FA code accepted; status shows enabled.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa-setup]]
- [[rocket-chat]]
