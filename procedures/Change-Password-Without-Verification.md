---
id: proc-change-password-no-verif-207552
tags:
  - broken-authentication
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:32:58.256Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Change-Password-Without-Verification

## Summary

This procedure demonstrates changing a user's password on Khan Academy without requiring the old password, OTP, or other verification, enabling immediate account takeover.

## Description

The vulnerability stems from the absence of security checks in the password change form on the account settings page. An attacker with session access can submit a new password directly, locking out the legitimate user. Discovered via manual testing, this affects all logged-in sessions and leads to full control without alerts. The platform's clarification on mobile usage does not mitigate the password issue.

## Requirements

1. Access to the account settings page via active session
2. Knowledge of a strong new password to set
3. No additional auth factors enabled on the account

## Defense

Defensive measures and detection strategies:

- Enforce old password or multi-factor verification for changes
- Log and alert on password modifications from new IPs/sessions
- Use CAPTCHA or rate limiting on settings submissions

## Objectives

1. Replace the account password to exclude the owner
2. Maintain session control post-change
3. Prevent legitimate user recovery without intervention

## Instructions

### Step 1: Locate Password Form

**Context**: Identify the password change section in settings.

No command required; perform UI action:

- Scroll to or find the 'Change Password' field.

> Form appears with new password input. Expected output: Empty field ready for entry.

### Step 2: Submit New Password

**Context**: Enter and save the new password without barriers.

No command required; perform UI action:

- Input new password and click 'Save' or 'Update'.

> Submission succeeds without prompts. Expected output: Confirmation of update; test login with old password fails.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-change]]
- [[no-verification]]
