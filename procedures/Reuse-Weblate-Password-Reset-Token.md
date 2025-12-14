---
tags:
  - token-reuse
  - unauthorized-change
  - account-takeover
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:19.677Z'
skill_level: low
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 23266d14-9dc3-413b-a12f-e5ace348137a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
  - '[[Exploit Public-Facing Application]]'
---
# Reuse-Weblate-Password-Reset-Token

## Summary

This procedure exploits the vulnerability by using the original password reset token after a settings-based password change, successfully modifying the password again and confirming the token's invalidation failure.

## Description

With the reset token from the earlier request in hand, this step accesses the link post-password update to demonstrate persistence. The Weblate implementation (Python/Django) fails to revoke the token, allowing a second unauthorized change. This could enable account takeover in scenarios where tokens are phished or intercepted. The outcome is a confirmed exploit, highlighting risks to session management best practices.

## Requirements

1. Saved reset token URL from prior step
2. Web browser
3. Updated password knowledge (for verification)

## Defense

Defensive measures and detection strategies:

- Enforce one-time-use for reset tokens with immediate invalidation on any password activity
- Use short expiration times (e.g., 15 minutes) and hash-based tokens
- Detect and block reuse attempts via logging and anomaly detection

## Objectives

1. Reuse the stale token for password change
2. Confirm vulnerability exploitation
3. Assess impact on account security

## Instructions

### Step 1: Access the Reset Link

**Context**: Attempt to use the token despite the prior change.

Paste the copied reset URL into the browser (e.g., `https://demo.weblate.org/accounts/password/reset/key/.../`).

> The form should load without expiration errors.

### Step 2: Submit New Password

**Context**: Complete the reset to alter the account again.

Enter a new password (different from the settings change) twice and submit.

> Success indicates the token was still valid; log in with the latest password to verify.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Account Manipulation]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- token-reuse
- unauthorized-change
- account-takeover
- weblate
