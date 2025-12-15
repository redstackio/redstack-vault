---
tags:
  - account-takeover
  - password-reset
type: procedure
tools:
  - '[[tools/post-auth-nosqli-py]]'
  - '[[tools/bcrypt]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:20.439Z'
sub_techniques: []
id: 3e65c1df-8b8c-4574-bd71-8fea9df1cdf3
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
  - '[[Valid Accounts]]'
---
# Reset-Admin-Password-Using-Leaked-Data

## Summary

This procedure uses the leaked reset token and 2FA secrets to submit a password change request, taking over the admin account.

## Description

With token and 2FA bypassed, POST to the reset endpoint with new password. Bcrypt may be used if hashing is involved, but primarily API submission. Post-reset, login as admin.

## Requirements

1. Full reset token
2. 2FA bypass data if applicable
3. New strong password

## Defense

- Validate tokens server-side with IP/session checks
- Require 2FA re-enrollment post-reset
- Alert on admin resets

## Objectives

1. Change admin password
2. Gain admin login
3. Escalate privileges

## Instructions

### Step 1: Prepare Reset Payload

**Context**: Include token and new pass.

**Instructions**: {"token": "leaked_token", "password": "DEbCf2b0A2BE79bBcDf1"}

> Expected: Password updated.

### Step 2: Login as Admin

**Context**: Test takeover.

**Instructions**: Auth with new credentials via API/UI.

> Expected: Admin session with elevated roles.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Account Manipulation]] Account Manipulation
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/bcrypt]]

## Tags

- takeover
