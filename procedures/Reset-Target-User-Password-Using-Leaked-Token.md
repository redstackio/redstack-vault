---
id: proc-rocket-password-reset
tags:
  - account-takeover
  - credential-access
type: procedure
tools:
  - '[[tools/Python3]]'
  - '[[tools/requests]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-password-reset-submit]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:46:19.927Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Reset-Target-User-Password-Using-Leaked-Token

## Summary

This procedure uses the leaked reset token to submit a new attacker-controlled password via the Rocket.Chat reset endpoint, resulting in full account takeover.

## Description

After obtaining the token through injection, POST it along with a new password to /api/v1/users.resetPassword. This works only if the target has no email verification or TOTP 2FA enabled. The account is immediately controllable, allowing login and privilege escalation if admin.

## Requirements

1. Leaked reset token from prior step
2. Target Rocket.Chat URL
3. New password (strong enough to pass policy)
4. No 2FA on target account

## Defense

Defensive measures and detection strategies:

- Mandate TOTP 2FA for all users, especially admins
- Shorten token expiration times (e.g., 5 minutes)
- Log and alert on reset completions
- Require email confirmation for resets

## Objectives

1. Gain control of target account
2. Access user privileges and data
3. Escalate if admin

## Instructions

### Step 1: Submit Reset Request with Token

**Context**: Use the token to authenticate the reset and set a new password.

**Command** ([[commands/curl-password-reset-submit]]):
```bash
curl -X POST 'http://target:3000/api/v1/users.resetPassword' -H 'Content-Type: application/json' -d '{"token":"leaked_token_here","user":{"password":"NewAttackerPass123!"}}'
```

> Expect {"success": true}; now login with the new password.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/curl-password-reset-submit]]

## Tools Used

- [[tools/Python3]]
- [[tools/requests]]

## Tags

- account-takeover
- credential-access
