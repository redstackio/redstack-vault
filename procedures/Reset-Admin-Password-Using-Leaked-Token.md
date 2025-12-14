---
tags:
  - account-takeover
  - password-reset
type: procedure
tools:
  - '[[tools/Python3]]'
  - '[[tools/requests]]'
  - '[[tools/post_auth_nosqli.py]]'
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/python3-post-auth-nosqli]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Domain Accounts]]'
updated_at: '2025-12-14T03:46:14.822Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 162c7625-a39b-442f-ab7b-38c8d0355eec
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Domain Accounts]]'
---
# Reset-Admin-Password-Using-Leaked-Token

## Summary

This procedure uses the leaked reset token (and 2FA secrets if applicable) to change the admin's password, achieving account takeover.

## Description

A POST to /api/v1/users.resetPassword with the token, new password, and optional 2FA code bypasses normal auth. Requires leaked token and 2FA data. Outcome: Control of admin account for further privilege escalation.

## Requirements

1. Leaked reset token
2. Optional 2FA bypass data
3. New password to set

## Defense

Defensive measures and detection strategies:

- Invalidate tokens after single use
- Require 2FA for all resets
- Alert on successful resets from unusual IPs
- Audit password change logs

## Objectives

1. Gain admin session
2. Enable privileged actions
3. Proceed to RCE setup

## Instructions

### Step 1: Submit Password Reset

**Context**: Use token to set new password, bypassing 2FA with leaked secrets.

**Command** ([[commands/python3-post-auth-nosqli]]):
```bash
python3 post_auth_nosqli.py -u attacker -p attacker 'http://localhost:3000'
```

> Script submits the reset payload. Expected output: Success message; login with new creds works.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Domain Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/python3-post-auth-nosqli]]

## Tools Used

- [[tools/Python3]]
- [[tools/requests]]
- [[tools/post_auth_nosqli.py]]

## Tags

- account-takeover
- password-reset
