---
id: proc-002
tags:
  - account-creation
  - unverified-email
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:48.246Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register Account with Victim's Email

## Summary

This procedure exploits the absence of email verification during signup on XVideos to create an account tied to the victim's email, enabling further account manipulation.

## Description

By submitting a registration form with the victim's email without any verification step, the attacker gains control over an account associated with that email. This sets up the DoS by preventing the victim from using their email for legitimate registration or recovery.

## Requirements

1. Victim's email address
2. Web browser
3. Basic form-filling knowledge

## Defense

Defensive measures and detection strategies:

- Enforce email verification via OTP or link during registration
- Log and alert on multiple registrations per email

## Objectives

1. Create account without ownership proof
2. Obtain login access to the fake account
3. Associate account with victim's email for lockout

## Instructions

### Step 1: Locate and Fill Registration Form

**Context**: From the homepage, access the signup area and input details using the victim's email.

No command; interact with the web form: Enter username, password, and victim's email, then submit.

> Registration succeeds immediately, providing login details. No email confirmation is sent or required.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[registration]]
- [[email-spoof]]
