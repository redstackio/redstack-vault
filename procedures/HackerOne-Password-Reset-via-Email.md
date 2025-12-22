---
id: 123e4567-e89b-12d3-a456-426614174002
name: HackerOne-Password-Reset-via-Email
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:42.825Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - password-reset
  - email-access
  - hackerone
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# HackerOne-Password-Reset-via-Email

## Summary

This procedure details using email access to perform a password reset on a deactivated HackerOne account, exploiting the lack of 2FA enforcement to set a new password controlled by the attacker.

## Description

Targeting the HackerOne platform's 'Forgot Password' feature, this step assumes the account is deactivated with 2FA enabled. The attacker accesses the victim's email to intercept the reset link, completing the process without OTP. This leads to account takeover in the web-based SaaS environment.

## Requirements

1. Access to the victim's email account
2. Knowledge of the victim's HackerOne email address
3. Web browser for interacting with the platform

## Defense

Defensive measures and detection strategies:

- Require 2FA for all reset actions, even on deactivated accounts
- Send alerts for password reset attempts on inactive accounts
- Implement rate limiting on reset requests per email

## Objectives

1. Initiate password reset without 2FA prompt
2. Set a new attacker-controlled password
3. Regain access pathway to the account

## Instructions

### Step 1: Initiate Reset

**Context**: Start the password recovery process on the login page.

Visit https://hackerone.com/login, click 'Forgot your password?', enter the victim's email, and submit.

> A reset email is sent to the inbox; no 2FA is required due to deactivation.

### Step 2: Complete Reset

**Context**: Use the email link to change the password.

Open the received email, click the reset link, enter a new strong password, and confirm.

> Success: Password updated confirmation, account remains deactivated but password is reset.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-reset]]
- [[email-access]]
- [[hackerone]]
