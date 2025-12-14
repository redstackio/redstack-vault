---
tags:
  - password-reset
  - credential-abuse
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
updated_at: '2025-12-14T03:46:14.827Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7821dcb7-5d28-4290-95c5-4c429b90fd42
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Domain Accounts]]'
---
# Request-Password-Reset-for-Admin

## Summary

This procedure requests a password reset for the leaked admin email, generating a reset token stored in the MongoDB users collection for subsequent extraction.

## Description

Using the leaked email, a POST request to the password reset API (e.g., /api/v1/users.forgotPassword) triggers token generation. The token is saved in this.services.password.reset.token. This step assumes prior email leakage and authenticated access. Outcome: Token ready for blind injection leakage, paving way for takeover.

## Requirements

1. Leaked admin email
2. Access to reset API endpoint
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Require CAPTCHA or additional verification for reset requests
- Rate limit reset attempts per email/IP
- Log and monitor reset requests for suspicious patterns
- Expire tokens quickly and invalidate on use

## Objectives

1. Generate exploitable reset token
2. Position for token leakage
3. Facilitate account compromise

## Instructions

### Step 1: Trigger Password Reset

**Context**: Send reset request with admin email to create token.

**Command** ([[commands/python3-post-auth-nosqli]]):
```bash
python3 post_auth_nosqli.py -u attacker -p attacker 'http://localhost:3000'
```

> Script calls the API with the email payload. Expected output: Confirmation of reset sent, token generated internally.

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

- password-reset
- credential-abuse
