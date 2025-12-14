---
id: p3b2c3d4-e5f6-7890-abcd-ef1234567890
name: Perform-Account-Takeover-via-Password-Reset
tags:
  - account-takeover
  - password-reset
  - credential-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:43.039Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Perform-Account-Takeover-via-Password-Reset

## Summary

After binding the attacker's email to the victim's VK.com account via CSRF, this procedure uses the email to request and complete a password reset, achieving full account control.

## Description

VK.com's password reset feature sends a link to the bound email. The attacker intercepts this, follows the link, and sets a new password. This completes the takeover chain. Applies to web platform.

## Requirements

1. Bound email access
2. Victim's username
3. Valid reset token from email

## Defense

Defensive measures and detection strategies:

- Require additional verification (e.g., SMS) for email changes
- Rate-limit password resets
- Alert users on email modifications
- Log and monitor reset attempts

## Objectives

1. Initiate password reset to bound email
2. Set new password using reset link
3. Access and control victim's account

## Instructions

### Step 1: Request Password Reset

**Context**: Trigger the reset process.

Go to https://vk.com/restore, enter victim's username, and submit. Check attacker's email for the reset link.

### Step 2: Follow Reset Link

**Context**: Use the token to change password.

Click the link in the email, enter a new password, and confirm.

### Step 3: Verify Takeover

**Context**: Confirm access.

Login with new password and victim's username. Access private data.

**Expected Output**: Successful login and account control.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[password-reset]]
- [[credential-access]]
