---
tags:
  - totp-generation
  - 2fa-leak
type: procedure
tools:
  - '[[tools/Google-Authenticator]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
  - Android
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:25:18.049Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 888a7ee5-0f0c-4870-9815-18bde8e8f504
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Import-Secret-into-TOTP-App

## Summary

This procedure imports the leaked gauth_secret into a TOTP application like Google Authenticator to begin generating valid 6-digit codes that mimic legitimate 2FA authentication.

## Description

With the 2FA secret extracted, the attacker adds it as a new account in the TOTP app, which uses the HMAC-based algorithm to produce time-synced codes. This bypasses the need for the original device. Prerequisites: Mobile app installed and secret value. Outcomes: Functional TOTP generator for use in account actions, leading to authentication bypass.

## Requirements

1. Google Authenticator app installed on Android/iOS device
2. Extracted gauth_secret value
3. Device time synchronized (for accurate TOTP generation)

## Defense

Defensive measures and detection strategies:

- Rotate 2FA secrets periodically and invalidate old ones on renewal
- Detect multiple TOTP validations from unusual IP/device fingerprints
- Require device binding or hardware keys (e.g., YubiKey) alongside TOTP

## Objectives

1. Successfully add the secret to the TOTP app
2. Verify code generation aligns with server expectations
3. Prepare codes for immediate use in protected actions

## Instructions

### Step 1: Open App and Add Account

**Context**: Initiate manual entry for the custom secret.

No specific command; Launch Google Authenticator and tap the '+' icon to add a new account. Select 'Enter a setup key'.

> Interface prompts for account name, key type (Time-based), and secret entry.

### Step 2: Enter Secret Details

**Context**: Input the leaked secret to configure the generator.

No specific command; Name the account (e.g., 'Algolia Compromise'), select 'Time based', and paste the gauth_secret into the key field. Tap 'Add'.

> App validates the secret format and creates the entry.

### Step 3: Verify Code Generation

**Context**: Confirm the app produces valid codes.

No specific command; Observe the 6-digit code displayed, which should refresh every 30 seconds.

> Compare with any known valid code if available; otherwise, proceed to test in Step 4 of the chain.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unprotected Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Authenticator]]

## Tags

- totp-generation
- 2fa-leak
