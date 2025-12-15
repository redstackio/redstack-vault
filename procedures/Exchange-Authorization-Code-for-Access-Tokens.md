---
tags:
  - oauth
  - token-exchange
  - pkce
type: procedure
tools:
  - '[[tools/okhttp]]'
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/oauth-code-exchange]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Application Access Token]]'
updated_at: '2025-12-14T17:24:45.105Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 76cf97e2-f0a2-42a9-bbc1-25a443d4a3ad
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Application Access Token]]'
---
# Exchange-Authorization-Code-for-Access-Tokens

## Summary

This procedure exchanges the OAuth authorization code obtained from the Shopify login redirect for access_token (tokenA), refresh_token, and id_token using the PKCE flow on accounts.shopify.com.

## Description

Following the browser redirect, the app sends a POST to /oauth/token with the code, grant_type=authorization_code, redirect_uri, code_verifier, and client_id. This acquires the primary access_token used throughout the session. In a vulnerability context, this token becomes the target for persistence exploitation. Prerequisites include the code from login; outcomes include usable tokens for API calls.

## Requirements

1. Valid authorization code from callback
2. PKCE code_verifier stored in app
3. Client ID: 8bb79a45-2d69-4890-9006-ab6ca705d708
4. Network access to accounts.shopify.com

## Defense

Defensive measures and detection strategies:

- Validate code_verifier strictly in PKCE flows
- Shorten token lifetimes and enforce rotation
- Log token issuance for anomaly detection

## Objectives

1. Acquire primary access_token
2. Enable authenticated API interactions
3. Set up for logout persistence test

## Instructions

### Step 1: Prepare Token Exchange Request

**Context**: Construct the POST body with code and verifier.

**Command** ([[commands/oauth-code-exchange]]):
```bash
curl -X POST https://accounts.shopify.com/oauth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "code=ABCDEFG&grant_type=authorization_code&redirect_uri=com.shopify.ping%3A%2F%2Fauth%2Fcallback&code_verifier=Uiz7J0nHRPvKDpX8ETGYaV9YEW0fx_drl7W4Mmiy-ZOMkwY0mb-5mvNmsDcg3IqBIXQ5XtYrS-wHh1xa6IbEkA&client_id=8bb79a45-2d69-4890-9006-ab6ca705d708"
```

> Expected output: {"access_token":"atkn_0......","refresh_token":"atkn_9.....","id_token":"eyJ0eXA....."}

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Application Access Token]] Application Access Token

### Sub-Techniques


## Commands Used

- [[commands/oauth-code-exchange]]

## Tools Used

- [[tools/okhttp]]

## Tags

- oauth
- token-exchange
- pkce
