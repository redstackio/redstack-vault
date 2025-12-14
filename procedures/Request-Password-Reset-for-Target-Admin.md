---
tags:
  - password-reset
  - credential-access
type: procedure
tools:
  - '[[tools/post-auth-nosqli-py]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:32:20.451Z'
sub_techniques: []
id: e132c02a-fa4a-4205-a918-706c88f46a08
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Request-Password-Reset-for-Target-Admin

## Summary

This procedure triggers a password reset for the leaked admin email, generating a temporary reset token stored in the user's services.password.reset field in MongoDB, setting up for leakage.

## Description

Using the exfiltrated email, the attacker submits a reset request via Rocket.Chat's forgot password feature. This updates the database with a token, which can then be blindly injected and extracted, bypassing normal auth flows.

## Requirements

1. Leaked admin email
2. Access to reset endpoint (/api/v1/login-token)
3. No 2FA interference at this stage

## Defense

- Require CAPTCHA or additional verification for resets
- Expire tokens quickly and log reset attempts
- Restrict resets to verified emails

## Objectives

1. Generate exploitable reset token
2. Store token in injectable DB field
3. Bridge to token leakage

## Instructions

### Step 1: Submit Reset Request

**Context**: Use email to initiate reset.

**Instructions**: POST to reset endpoint with {"user": {"email": "leaked@email.com"}} or use UI.

> Expected: Token generated, possibly emailed (but we target DB).

### Step 2: Confirm Token Creation

**Context**: Verify via preliminary injection if needed.

**Instructions**: Quick $where check for non-null reset.token.

> Expected: Oracle confirms token exists.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Account Manipulation]] Account Manipulation (reset)

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/post-auth-nosqli-py]]

## Tags

- reset-token
