---
tags:
  - account-takeover
  - password-reset
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 96e3753c-f161-4f0d-83e9-47f3a2067ced
created_at: '2025-12-14T17:33:34.472Z'
updated_at: '2025-12-14T17:33:34.472Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Execute-Account-Takeover-via-Password-Reset

## Summary

Use the now-associated attacker's phone number to initiate a password reset on the target site, gaining full control of the victim's account.

## Description

With the phone linked, the site's Digits integration treats the account as owned by the attacker. Requesting a reset sends the code to the attacker's phone, allowing password change and access to victim data.

## Requirements

1. Phone association completed
2. Access to attacker's Digits phone
3. Target site supports phone-based resets

## Defense

Defensive measures and detection strategies:

- Multi-factor for resets (e.g., email + phone)
- Rate limiting on reset requests
- Anomaly detection on sudden phone changes

## Objectives

1. Trigger reset using associated phone
2. Receive and use verification code
3. Access and control the account

## Instructions

### Step 1: Initiate Reset

**Context**: Go to the site's forgot password flow.

**Instructions**: Enter the victim's email/username; select phone reset option.

### Step 2: Receive Code

**Context**: Get the SMS code on attacker's phone.

**Instructions**: Input code to proceed.

### Step 3: Set New Password

**Context**: Change password and login.

**Instructions**: Set strong password; access account dashboard to confirm takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[takeover]]
- [[reset-abuse]]
