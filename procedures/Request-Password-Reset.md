---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - password-reset
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:58.374Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Request-Password-Reset

## Summary

This procedure initiates a password reset for a target account on the NordVPN user control panel, generating a reset token that is emailed to the associated address, setting the stage for token exploitation.

## Description

In the context of the NordVPN vulnerability, this step involves navigating to the lost password page and submitting the target's email address (e.g., main@main.com). The system generates a reset link without proper expiration or invalidation logic, which can be exploited later. This is a standard web-based authentication flow but highlights the improper handling of reset tokens during email updates.

## Requirements

1. Web browser access to https://ucp.nordvpn.com/lost-password
2. Knowledge of the target account's original email address
3. Ability to receive emails at that address

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on reset requests per IP/email
- Log all reset initiations and monitor for anomalies
- Require additional verification (e.g., CAPTCHA) for reset requests

## Objectives

1. Generate a valid password reset token
2. Receive the token via email for subsequent steps
3. Prepare for email change without token invalidation

## Instructions

### Step 1: Navigate to Lost Password Page

**Context**: Access the password recovery endpoint to start the reset process.

Open a web browser and go to https://ucp.nordvpn.com/lost-password.

> This loads the form for entering the email address.

### Step 2: Submit Target Email

**Context**: Provide the account's email to trigger the reset email.

Enter the email address (e.g., main@main.com) in the form field and submit.

> The system processes the request and sends an email containing the reset link.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-reset]]
- [[web-auth]]
