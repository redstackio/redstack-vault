---
id: proc-736522-intercept-modify
tags:
  - jwt-modification
  - burp-suite
  - interception
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/JSON-Web-Tokens-JWT4B]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:31:10.852Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Credentials In Files]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Unsecured Credentials]]'
---
# Intercept-and-Modify-JWT-Token-Refresh-Request

## Summary

This procedure uses Burp Suite to intercept the POST /token refresh request and modifies the access token's JWT payload to forge the user identity, exploiting the lack of validation in authmagic-timerange-stateless-core's checkRefreshToken function.

## Description

During token reissuance, the vulnerable module (core.js L11) verifies only the refresh token with jwt.verify but decodes the access token without full verification, comparing only signatures post-decoding. This allows tampering with the payload (e.g., 'u' field for user email) while keeping the signature intact, leading to a new signed token for the impersonated user. Burp Suite proxies the request, and the JWT4B plugin facilitates easy editing.

## Requirements

1. Burp Suite running with proxy (default 127.0.0.1:8080)
2. Browser proxy configured to Burp
3. Active user session with tokens
4. JWT4B extension installed in Burp

## Defense

Defensive measures and detection strategies:

- Validate both access and refresh tokens with jwt.verify (full signature and payload checks)
- Use short-lived access tokens and secure refresh token storage
- Monitor for anomalous token payloads (e.g., unexpected user fields) via logging
- Implement request signing or additional auth headers

## Objectives

1. Capture refresh request
2. Tamper with access token payload
3. Prepare forged request for submission

## Instructions

### Step 1: Trigger and Intercept Request

**Context**: Initiate refresh to capture tokens in transit.

**Instructions**: In the app, click 'Refresh token'. In Burp's Proxy > Intercept tab, ensure interception is on for POST /token.

No command; UI action.

> Expected output: Intercepted request body with 'token' and 'refreshToken' fields.

### Step 2: Modify JWT Payload

**Context**: Edit the access token to change user identity.

**Instructions**: In Burp Repeater or Inspector, select the 'token' field. Use JWT4B extension: right-click > Send to JWT Editor, change 'u' to a target email (e.g., 'admin@target.com'), and re-sign if needed (but signature remains valid due to vuln).

No command; tool action.

> Expected output: Updated JWT with modified payload, visible in editor.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- [[Credentials In Files]] Credentials In Files (JWT as credential)

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]
- [[tools/JSON-Web-Tokens-JWT4B]]

## Tags

- jwt-modification
- burp-suite
- interception
