---
tags:
  - 2fa
  - account-takeover
  - authentication-modification
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Modify Authentication Process]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Reversible Encryption]]'
id: 0932ac00-f8a7-49d3-ad4c-c39db3acff16
created_at: '2025-12-14T17:24:48.425Z'
updated_at: '2025-12-14T17:24:48.425Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Modify Authentication Process]]'
---
# Enable-2FA-Without-Verification

## Summary

This procedure enables two-factor authentication on an unverified account, binding it to the attacker's device and preventing victim access.

## Description

The 2FA setup feature lacks checks for email verification, allowing attackers to configure it immediately after login. Verification codes are then sent to the attacker's authenticator app, rendering password resets ineffective for the victim and achieving takeover or DoS.

## Requirements

1. Active session from unverified account login
2. Authenticator app on attacker's device (e.g., Google Authenticator)
3. Access to account security settings

## Defense

Defensive measures and detection strategies:

- Mandate email verification before 2FA configuration
- Require re-verification for sensitive changes like 2FA
- Audit logs for 2FA enables on unverified accounts

## Objectives

1. Bind 2FA to attacker's control
2. Lock out the legitimate user
3. Secure persistent access to the account

## Instructions

### Step 1: Access Security Settings

**Context**: Navigate to 2FA enablement.

From the account dashboard, go to settings > security or two-factor authentication section.

### Step 2: Configure 2FA

**Context**: Set up 2FA without additional checks.

Scan the provided QR code with your authenticator app or enter the secret key manually. Enter the generated code to verify and enable 2FA.

**Expected Output**: Confirmation of 2FA activation; logout and test login requiring the app code.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Modify Authentication Process]]

### Sub-Techniques

- [[Reversible Encryption]]

## Commands Used


## Tools Used


## Tags

- [[2fa]]
- [[account-takeover]]
- [[authentication-modification]]
