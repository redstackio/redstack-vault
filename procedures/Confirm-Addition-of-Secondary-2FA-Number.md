---
id: proc-slack-confirm-2fa
tags:
  - 2fa
  - confirmation
  - account-mod
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:27:29.554Z'
skill_level: basic
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Confirm-Addition-of-Secondary-2FA-Number

## Summary

This procedure validates the successful addition of the secondary phone number to the victim's Slack account for 2FA purposes.

## Description

Post-verification, the endpoint response confirms the phone is now an optional 2FA receiver. If the victim had no prior 2FA, this forces it on; otherwise, it allows code diversion. The attacker can now receive codes during login attempts.

## Requirements

1. Successful verification from prior step
2. Access to victim's account settings (via session or later login)
3. No additional inputs needed

## Defense

Defensive measures and detection strategies:

- Notify users via email/Slack for 2FA changes
- Limit secondary numbers per account
- Require re-auth for sensitive settings changes
- Periodic 2FA audits

## Objectives

1. Ensure secondary number is active
2. Enable SMS routing to attacker
3. Set stage for DoS or takeover

## Instructions

### Step 1: Monitor Verification Response

**Context**: Check the POST response for success indicators.

Expected: 200 OK with updated settings; no error on confirmation_code.

> Confirms addition.

### Step 2: Test 2FA Option

**Context**: If possible, inspect victim's settings.

Login and view /account/settings/2fa_sms; secondary number listed.

> Success: Option available for code delivery.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa]]
- [[confirmation]]
