---
id: proc-uuid-3
name: Manipulate-OAuth-Redirect-to-Steal-Facebook-Tokens
tags:
  - oauth
  - token-theft
  - redirect
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
  - '[[Application Access Token]]'
updated_at: '2025-12-14T03:47:12.610Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Application Access Token]]'
---
# Manipulate-OAuth-Redirect-to-Steal-Facebook-Tokens

## Summary

This procedure exploits an OAuth redirect URI validation flaw in Rockstar SocialClub's Facebook integration, allowing redirection of authorization codes or tokens to arbitrary subdomains like socialclub.rockstargames.com, enabling theft of sensitive authentication material.

## Description

Due to lack of strict redirect URI validation, the OAuth flow accepts attacker-specified subdomains under rockstargames.com. With an escalated session from prior steps, the attacker initiates Facebook login and alters the redirect parameter to an evil subdomain under attacker control. The token is then sent there, compromising user accounts. This targets web OAuth implementations and requires an authenticated session to trigger the flow.

## Requirements

1. Authenticated session on rockstargames.com via SSO
2. Control over a subdomain mimicking rockstargames.com (e.g., via DNS or wildcard)
3. Facebook app configured for SocialClub with loose redirect validation

## Defense

Defensive measures and detection strategies:

- Enforce exact-match redirect URI validation in OAuth client config
- Use state parameters and PKCE to prevent manipulation
- Monitor OAuth logs for anomalous redirect domains

## Objectives

1. Intercept Facebook OAuth tokens during redirect
2. Exfiltrate tokens to attacker server
3. Enable unauthorized access to linked Facebook-SocialClub accounts

## Instructions

### Step 1: Initiate OAuth Flow with Altered Redirect

**Context**: From the authenticated session, start Facebook login and modify the redirect_uri parameter.

Construct a URL like `https://www.rockstargames.com/oauth/facebook?redirect_uri=https://evil.socialclub.rockstargames.com/callback` and load it in the victim's context.

### Step 2: Capture Token on Attacker Endpoint

**Context**: Host a receiver on the fake subdomain to log incoming tokens.

Set up a simple server (e.g., using Node.js or Python) to capture POST/GET parameters containing the OAuth code or token.

### Step 3: Validate Token Usage

**Context**: Test the stolen token against SocialClub or Facebook APIs.

Use the token to perform actions like accessing user profile or linking accounts, confirming theft success.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Application Access Token]] Use Alternate Authentication Material: Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[oauth]]
- [[token-theft]]
