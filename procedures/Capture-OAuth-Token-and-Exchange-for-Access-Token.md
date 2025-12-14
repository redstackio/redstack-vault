---
id: uuid-5
tags:
  - token-exchange
  - account-takeover
  - periscope-api
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:33:34.357Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Capture-OAuth-Token-and-Exchange-for-Access-Token

## Summary

Intercept the OAuth token from the redirect fragment and exchange it for a permanent access token to authenticate and takeover the victim's Periscope account.

## Description

Parse the URL fragment on the attacker site to get token and verifier, then complete OAuth by requesting access token. Use it to call Periscope API for takeover actions. Targets post-redirect; requires signing. Outcome: Full account control.

## Requirements

1. Captured request token, secret, verifier.
2. Consumer credentials.
3. Access to Periscope API endpoints.

## Defense

Defensive measures and detection strategies:

- Short-lived tokens and verifier validation.
- Monitor API for anomalous access token uses.
- Account alerts for unauthorized changes.

## Objectives

1. Extract token from fragment.
2. Exchange for access token.
3. Perform takeover (e.g., rename).

## Instructions

### Step 1: Parse Redirect Fragment

**Context**: On attacker site, read URL hash.

Use JavaScript: `location.hash` to get `#&oauth_token=...&oauth_verifier=...`.

> Store securely; avoid logging to prevent exposure.

### Step 2: Exchange for Access Token

**Context**: Sign request to access_token endpoint.

POST to `https://api.twitter.com/oauth/access_token` with request token, verifier, consumer creds.

> Response: `oauth_token=access&oauth_token_secret=secret&user_id=...&screen_name=...`.

### Step 3: Authenticate to Periscope

**Context**: Use access token for API calls.

Sign Periscope requests (e.g., PUT /account/rename) with access token.

> Success: Account renamed; confirm via GET user info.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[token-exchange]]
- [[account-takeover]]
