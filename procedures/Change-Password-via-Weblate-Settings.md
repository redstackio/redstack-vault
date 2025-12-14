---
tags:
  - password-change
  - account-settings
  - weblate
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
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:31:19.715Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: 7af66144-3713-479c-9a2a-686444a018d4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Change-Password-via-Weblate-Settings

## Summary

This procedure logs into the Weblate account and changes the password through the profile settings, intended to invalidate any pending reset tokens but failing due to the vulnerability.

## Description

After normal login to the Django-powered Weblate application, this step accesses the user profile to update credentials. The root cause of the vulnerability lies here: the system does not revoke or expire the previously generated reset token. This simulates a legitimate user action that should secure the account but leaves it exposed. Expected results include a new password in effect, with the account requiring updated credentials for future logins.

## Requirements

1. Active Weblate session or credentials
2. Web browser
3. Knowledge of current password

## Defense

Defensive measures and detection strategies:

- Automatically invalidate all pending reset tokens upon any password change
- Implement session invalidation across all active tokens
- Audit logs for password changes followed by reset attempts

## Objectives

1. Modify account password legitimately
2. Test for token invalidation (which fails)
3. Simulate user behavior exposing the flaw

## Instructions

### Step 1: Log In to Account

**Context**: Gain access to the settings using existing credentials.

Go to `https://demo.weblate.org/accounts/login/` and enter the username/email and current password.

> Successful login redirects to the dashboard.

### Step 2: Update Password in Settings

**Context**: Change the password to trigger potential token cleanup.

Navigate to `https://demo.weblate.org/accounts/profile/`, locate the password change section, enter the old password, new password (twice), and submit.

> Confirm the change; log out and test login with the new password to verify.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- password-change
- account-settings
- weblate
