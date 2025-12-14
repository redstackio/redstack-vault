---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
tags:
  - token-exchange
  - code-intercept
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:24:35.619Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Intercept-and-Exchange-OAuth-Authorization-Code

## Summary

This procedure captures the leaked authorization code from the redirect and exchanges it for an access token, allowing SSO login as the victim on admin.8x8.vc.

## Description

After the victim authenticates, the code is appended to the attacker's URL. This step involves logging it and posting to the token endpoint to obtain the access token, exploiting the lack of redirect validation. Web-based, requires server to handle GET requests. Outcome: Full account access.

## Requirements

1. Server logging redirects (e.g., simple HTTP listener)
2. Knowledge of OAuth client details (client_id from URL)
3. Access to token endpoint (Google OAuth)

## Defense

Defensive measures and detection strategies:

- Short-lived authorization codes
- Validate redirect URIs on token exchange
- Audit token issuances for anomalous IPs

## Objectives

1. Extract code from query string
2. Perform token exchange
3. Access victim SSO account

## Instructions

### Step 1: Capture the Redirect

**Context**: Log the incoming request on the controlled domain.

Set up a server endpoint at /callback to log GET parameters. When victim redirects, capture ?code=AUTH_CODE&state=xyz.

> Store the code securely for immediate use.

### Step 2: Exchange Code for Token

**Context**: POST to OAuth token endpoint with the code.

Use a tool like curl (or browser) to send: POST https://oauth2.googleapis.com/token with body: client_id=..., redirect_uri=https://attacker.com/callback, grant_type=authorization_code, code=AUTH_CODE.

> Response includes access_token; use it in Authorization: Bearer header for admin.8x8.vc API or login.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-code]]
- [[sso-takeover]]
