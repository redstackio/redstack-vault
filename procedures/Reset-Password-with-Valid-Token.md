---
id: proc-17512-reset-password
tags:
  - password-reset
  - account-compromise
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:06.440Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Reset Password with Valid Token

## Summary

This procedure uses a brute-forced valid reset token to access the password edit page and set a new password, compromising the account.

## Description

With a valid token, the endpoint loads the edit form without further auth. Submit a new password to overwrite the original, granting control. This exploits improper token protection, leading directly to takeover.

## Requirements

1. Valid reset token URL
2. Access to the edit page
3. Desired new password

## Defense

Defensive measures and detection strategies:

- Invalidate tokens after first use
- Require additional verification (e.g., email code)
- Audit password changes for anomalies

## Objectives

1. Load password edit form with token
2. Submit and confirm new password
3. Ensure change propagates

## Instructions

### Step 1: Access Edit Page

**Context**: Navigate using valid token.

Enter the full URL https://hackerone.com/users/password/edit?reset_password_token=VALIDTOKEN.

> Expect 200 response with form; success: Edit page loads.

### Step 2: Submit New Password

**Context**: Change the password.

Fill password fields with new value (e.g., attacker-controlled) and submit.

> Confirmation message; success: Password updated.

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
- [[account-compromise]]
