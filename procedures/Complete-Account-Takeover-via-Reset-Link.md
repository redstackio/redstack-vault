---
id: proc-005
tags:
  - account-takeover
  - password-reset
  - email-link
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:34.520Z'
skill_level: beginner
impact_level: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Complete-Account-Takeover-via-Reset-Link

## Summary

This procedure uses the unauthorized password reset link received by the attacker to change the victim's GitLab password and log in, achieving full account control without any victim interaction.

## Description

Upon receiving the email, the link leads to a reset form valid for the victim's account. Submitting a new password updates the credentials server-side. No tools needed beyond a browser; outcome: Attacker gains persistent access.

## Requirements

1. Password reset email received in attacker's inbox
2. Valid reset link (typically expires in 1 hour)
3. Access to email client

## Defense

Defensive measures and detection strategies:

- Shorten reset link expiration times (e.g., 5 minutes)
- Require additional verification (e.g., security questions) for resets
- Notify users via alternate channels (e.g., app push) on reset attempts

## Objectives

1. Access the reset form via the link
2. Set a new password for the victim
3. Verify takeover by logging in

## Instructions

### Step 1: Open Reset Link

**Context**: Click the link in the received email to access the reset page.

Use email client to open the message from GitLab.

> Link format: https://target-gitlab.com/users/password/edit?reset_token=TOKEN.

### Step 2: Change Password and Login

**Context**: Submit new credentials and authenticate.

Enter new password twice and submit.

> Then, go to login page, use victim's email and new password to access account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

None

## Commands Used

None

## Tools Used

None

## Tags

- [[account-takeover]]
- [[password-reset]]
- [[email-link]]
