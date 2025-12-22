---
tags:
  - logout
  - token-revocation
  - vulnerability
type: procedure
tools:
  - '[[tools/okhttp]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/revoke-shop-installation]]'
  - '[[commands/revoke-firebase-installation]]'
  - '[[commands/logout-request]]'
verified: false
platforms:
  - Android
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:45.099Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 5acdf177-2089-4f43-b6b3-de2a33b382ac
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Initiate-Logout-in-Shopify-Ping-App

## Summary

This procedure triggers the logout in the Shopify Ping app, which revokes secondary tokens but fails to invalidate the primary access_token due to a missing Logout Token Hint, exposing the vulnerability.

## Description

Logout sends three DELETE requests: revoke tokenB on myshopify.com, Firebase installation, and tokenA on accounts.shopify.com. The last fails with 400, leaving tokenA valid. This is the core vulnerability; observable via proxy. Prerequisites: active session with tokens.

## Requirements

1. Active tokens (tokenA and tokenB)
2. Installation IDs for shop and Firebase
3. Network access to all endpoints

## Defense

Defensive measures and detection strategies:

- Require Logout Token Hint in all revocation requests
- Audit logout failures and alert on 400 errors
- Clear local token storage on logout attempt

## Objectives

1. Revoke secondary tokens
2. Trigger failed primary token invalidation
3. Confirm vulnerability for persistence

## Instructions

### Step 1: Revoke Shop Installation Token

**Context**: DELETE tokenB installation.

**Command** ([[commands/revoke-shop-installation]]):
```bash
curl -X DELETE https://ravel2.myshopify.com/admin/api/ping-api/v1/client/installations/8eec631b-6b40-4718-9a25-16821434c4a5 \
  -H "Authorization: Bearer [tokenB]"
```

> Expected output: HTTP/1.1 200 OK {"status":"ok"}

### Step 2: Revoke Firebase Installation

**Context**: DELETE Firebase token.

**Command** ([[commands/revoke-firebase-installation]]):
```bash
curl -X DELETE https://firebaseinstallations.googleapis.com/v1/projects/shopify-ping/installations/eGSi2WuU9CLH8ZZYJKGsKm \
  -H "Content-Type: application/json" \
  -H "Authorization: [Firebase auth]"
```

> Expected output: HTTP/1.1 200 OK {}

### Step 3: Attempt Primary Logout

**Context**: DELETE for tokenA, which fails.

**Command** ([[commands/logout-request]]):
```bash
curl -X DELETE https://accounts.shopify.com/api/v1/logout \
  -H "Authorization: Bearer [tokenA]"
```

> Expected output: HTTP/1.1 400 Bad Request {"error":"Missing Logout Token Hint"}

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/revoke-shop-installation]]
- [[commands/revoke-firebase-installation]]
- [[commands/logout-request]]

## Tools Used

- [[tools/okhttp]]

## Tags

- logout
- token-revocation
- vulnerability
