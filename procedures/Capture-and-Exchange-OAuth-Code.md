---
id: proc-uuid-5
name: Capture and Exchange OAuth Code
tags:
  - oauth-code
  - token-exchange
  - credential-access
type: procedure
tools:
  - '[[tools/Webhook-Site]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Use Alternate Authentication Material]]'
updated_at: '2025-12-14T17:30:18.740Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Use Alternate Authentication Material]]'
---
# Capture and Exchange OAuth Code

## Summary

This procedure intercepts the authorization code from the redirect and exchanges it for an access token, granting the attacker access to the victim's WakaTime resources based on scopes.

## Description

After authorization, the OAuth page redirects to the attacker's redirect_uri with ?code=CODE. Using webhook.site, the code is captured. The attacker then POSTs to WakaTime's token endpoint with the code, client_id, client_secret, and grant_type=authorization_code to obtain the token, enabling API calls like reading/writing organizations.

## Requirements

1. Captured code from redirect
2. Client_secret from app registration
3. Access to WakaTime API docs

## Defense

Defensive measures and detection strategies:

- Short-lived authorization codes
- Monitor token exchanges for anomalies
- Revoke tokens on suspicious activity

## Objectives

1. Intercept and store the code
2. Exchange for long-term access token
3. Verify access to victim data

## Instructions

### Step 1: Monitor Redirect for Code

**Context**: Capture the code from the OAuth redirect.

No command; use webhook.site at https://webhook.site/15495620-7c98-4643-a6df-9e7864c0dead to log the GET request with ?code=CODE.

> Expected: Code parameter visible in webhook logs, e.g., code=abc123.

### Step 2: Exchange Code for Token

**Context**: Use the code to request an access token via API.

No command; send POST request to https://wakatime.com/api/v1/oauth/token with form data: client_id=joUNHCTnWqQ9hsmrWS5CTokR, client_secret=your_secret, code=abc123, grant_type=authorization_code, redirect_uri=https://webhook.site/15495620-7c98-4643-a6df-9e7864c0dead.

> Expected: JSON response with access_token, usable for API access.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Use Alternate Authentication Material]] Use Alternate Authentication Material

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Webhook-Site]]

## Tags

- [[oauth-code]]
- [[token-exchange]]
- [[credential-access]]
