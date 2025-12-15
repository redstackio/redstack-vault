---
id: proc-736522-forward-verify
tags:
  - impersonation
  - verification
  - exploit
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:31:10.849Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Forward-Modified-Request-and-Verify-Impersonation

## Summary

This procedure submits the tampered token refresh request and validates that the server issues a new signed access token with the forged user identity, confirming the authentication bypass.

## Description

By forwarding the modified request to POST /token, the vulnerable endpoint processes the tampered access token without proper validation, signs a new token based on the altered payload, and returns it. This enables full impersonation, as the new token authenticates as the modified user (e.g., changed email). The root cause is in core.js's checkRefreshToken, which skips jwt.verify on the access token.

## Requirements

1. Intercepted and modified request in Burp Suite
2. Active proxy session
3. Target app running

## Defense

Defensive measures and detection strategies:

- Enforce strict JWT validation on all tokens in reissuance flows
- Audit token payloads for tampering indicators (e.g., mismatched user IDs)
- Use token blacklisting or rotation on anomalies
- Deploy WAF rules to detect modified JWT structures

## Objectives

1. Submit forged request
2. Receive new impersonated token
3. Confirm unauthorized access

## Instructions

### Step 1: Forward the Request

**Context**: Release the intercepted request to the server.

**Instructions**: In Burp Proxy > Intercept, click 'Forward' on the modified POST /token request.

No command; UI action.

> Expected output: 200 OK response with new 'token' and 'refreshToken'.

### Step 2: Verify Impersonation

**Context**: Check that the new token reflects the forged identity.

**Instructions**: Inspect the response JSON; decode the new access token (e.g., via jwt.io or JWT4B) to confirm the 'u' field matches the modification (e.g., 'admin@target.com'). Test the token in the app if applicable.

No command; inspection action.

> Expected output: New token payload shows impersonated user; app accepts it as valid.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- impersonation
- verification
- exploit
