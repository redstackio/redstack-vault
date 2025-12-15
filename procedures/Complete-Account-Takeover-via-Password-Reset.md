---
id: p5e6f7g8-i9j0-1234-efgh-567890123456
tags:
  - account-takeover
  - password-reset
  - web
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
updated_at: '2025-12-14T17:32:58.360Z'
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
# Complete-Account-Takeover-via-Password-Reset

## Summary

This final procedure allows the attacker to reset the password on the email-hijacked account, achieving full takeover of the victim's IntenseDebate account.

## Description

Post-CSRF, the account email is now the attacker's. Using the forgot password feature, the attacker requests a reset link via their email, sets a new password, and verifies to gain exclusive control. This completes the takeover, as the victim is locked out without further access.

## Requirements

1. Email changed to attacker's via CSRF
2. Access to attacker's email inbox
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Require secondary verification (e.g., 2FA) for resets
- Audit logs for rapid email/password changes
- User notifications for all account modifications

## Objectives

1. Reset password on reclaimed account
2. Verify and login as attacker
3. Achieve persistent access

## Instructions

### Step 1: Request Password Reset

**Context**: Initiate reset with attacker's email.

No command; visit https://intensedebate.com/, click forgot password, enter attacker's email.

> Expected: Reset email sent.

### Step 2: Set and Verify New Password

**Context**: Complete reset to login.

No command; click link in email, set new password, verify if prompted.

> Expected: Full account access.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[password-reset]]
- [[web]]
