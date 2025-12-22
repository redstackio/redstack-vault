---
tags:
  - token-generation
  - shopify-api
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/post-shopify-xauth-login]]'
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 1d32d0e9-caaf-4240-856e-87aff53ed5aa
created_at: '2025-12-14T17:29:57.279Z'
updated_at: '2025-12-14T17:29:57.279Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Obtain-Low-Priv-Access-Token

## Summary

This procedure generates a Shopify Ping access token for a low-privileged user via the /admin/api/xauth login endpoint, enabling use in the IDOR exploit.

## Description

Using low-priv credentials, send a POST to Shopify's xauth API to obtain an access_token. This token is valid for Ping but misused for KITCRM. Target: Shopify API. Prerequisites: Low-priv account. Outcome: Token for escalation.

## Requirements

1. Low-privileged user credentials (email/password)
2. Target shop domain (e.g., alwayzhack.myshopify.com)
3. HTTP client like curl or Burp

## Defense

Defensive measures and detection strategies:

- Rate-limit login API calls
- Log token issuances and validate user permissions

## Objectives

1. Authenticate low-priv user
2. Retrieve access_token
3. Validate token usability

## Instructions

### Step 1: Send Login Request

**Context**: POST credentials to xauth endpoint.

**Command** ([[commands/post-shopify-xauth-login]]):
```bash
curl -X POST https://alwayzhack.myshopify.com/admin/api/xauth \
  -H "Content-Type: application/json" \
  -d '{"email":"lowpriv@example.com","password":"password"}'
```

> This authenticates and returns JSON with access_token. Expected output: {"access_token": "TOKEN"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/post-shopify-xauth-login]]

## Tools Used


## Tags

- [[token-generation]]
- [[shopify-api]]
