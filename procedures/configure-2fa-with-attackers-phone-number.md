---
tags:
  - 2fa-hijack
  - account-lockout
  - phone-verification
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: db92a53d-6bb7-4c8d-9300-21fb6bd71a75
created_at: '2025-12-14T17:24:47.700Z'
updated_at: '2025-12-14T17:24:47.700Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Valid Accounts]]'
---
# Configure 2FA with Attacker's Phone Number

## Summary

This final procedure uses the brute-forced verification code to complete 2FA setup, linking the attacker's phone for OTP delivery and locking the victim out of the account.

## Description

With email verification bypassed, the attacker proceeds through Evernote's 2FA configuration to add their phone number. The system sends an OTP to this number for confirmation, securing the account under attacker control. The victim, lacking OTP access, cannot log in, reset passwords, or recover the account, achieving permanent denial of service and pre-takeover. This step requires no additional tools beyond the web interface.

## Requirements

1. Valid verification code from prior brute-force
2. Attacker's phone number ready for SMS receipt
3. Access to the verified account session

## Defense

Defensive measures and detection strategies:

- Require additional verification (e.g., existing password) before 2FA changes
- Alert users via email/SMS on 2FA setup attempts
- Implement account recovery flows that bypass hijacked 2FA with support tickets
- Monitor for rapid 2FA configurations post-signup

## Objectives

1. Link attacker's phone to the victim's account for 2FA
2. Enable OTP control, denying victim access
3. Achieve full account lockout and takeover potential

## Instructions

### Step 1: Submit Verification Code

**Context**: Verify email ownership to unlock 2FA setup.

Return to the verification form or Repeater.

> Enter the correct 6-digit code and submit; expect success response confirming verification.

### Step 2: Enter Phone Number

**Context**: Proceed to phone-based 2FA configuration.

Follow the UI prompt after verification.

> Input attacker's phone number (e.g., +1-555-123-4567) and request OTP via SMS.

### Step 3: Confirm with OTP

**Context**: Complete setup using received OTP.

Receive SMS on attacker's phone.

> Enter the OTP code to finalize 2FA; account is now protected by attacker's phone.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Brute Force]]
- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa-hijack]]
- [[account-lockout]]
