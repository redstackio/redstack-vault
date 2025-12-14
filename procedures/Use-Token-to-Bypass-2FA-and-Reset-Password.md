---
tags:
  - 2fa-bypass
  - password-reset
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2b99f863-7618-4e78-b2c9-f61e12cab7fc
created_at: '2025-12-14T17:24:45.491Z'
updated_at: '2025-12-14T17:24:45.491Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Account Manipulation]]'
  - '[[Exploit Public-Facing Application]]'
---
# Use-Token-to-Bypass-2FA-and-Reset-Password

## Summary

This procedure exploits the non-expiring confirmation token to directly access the password entry page in login.gov, bypassing 2FA and allowing password reset for account takeover.

## Description

By navigating to the enter_password endpoint with the token (e.g., https://idp.staging.login.gov/sign_up/enter_password?confirmation_token=1wzjBaAyfcVnS5iWgmxq&request_id=), the attacker reaches the password form without 2FA verification. After setting a new password, they can log in directly. This works in the staging environment due to missing expiration enforcement. Prerequisites: Valid token from email. Expected outcome: Control over the account without phone-based 2FA.

## Requirements

1. Valid confirmation token
2. HTTP client or browser for GET request
3. New password meeting complexity requirements

## Defense

Defensive measures and detection strategies:

- Enforce token expiration and single-use policy
- Require 2FA even in confirmation flows
- Monitor for anomalous password resets from unverified sessions

## Objectives

1. Access password reset form via token
2. Set new password without 2FA
3. Achieve login post-reset

## Instructions

### Step 1: Access Token Endpoint

**Context**: Use the token to reach the password entry page.

**Instructions**: Open the URL https://idp.staging.login.gov/sign_up/enter_password?confirmation_token=<TOKEN>&request_id= in a browser, replacing <TOKEN> with the extracted value.

> Expected output: Password form loads without 2FA prompt.

### Step 2: Submit New Password

**Context**: Complete the reset to activate the account.

**Instructions**: Enter a new password (e.g., test_?123+) and submit the form.

> Expected output: Confirmation of password update; immediate login capability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Account Manipulation]] Account Manipulation
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[2fa-bypass]]
- [[password-reset]]
- [[account-takeover]]
