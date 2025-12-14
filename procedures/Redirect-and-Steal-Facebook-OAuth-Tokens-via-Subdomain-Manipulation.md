---
id: proc-oauth-redirect-theft
tags:
  - oauth
  - redirect
  - token-theft
  - csrf
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Application Access Token]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:35.558Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
  - '[[Exploit Public-Facing Application]]'
---
# Redirect and Steal Facebook OAuth Tokens via Subdomain Manipulation

## Summary

This procedure exploits an OAuth redirect misconfiguration in Rockstar's SocialClub Facebook integration, allowing redirection of authorization codes or tokens to attacker-controlled subdomains for theft.

## Description

The Facebook OAuth flow on socialclub.rockstargames.com and www.rockstargames.com permits redirects to any *.rockstargames.com subdomain without proper validation. With domain control from prior steps, the attacker modifies the redirect_uri parameter to point to a malicious endpoint (e.g., evil.rockstargames.com). Upon user approval, Facebook sends the token there, enabling exfiltration. This also ties into CSRF weaknesses lacking state validation.

## Requirements

1. Control over the rockstargames.com domain context from SSO propagation.
2. Ability to register or spoof a *.rockstargames.com subdomain (via DNS or proxy).
3. Active Facebook app integration on the target site.
4. User interaction to initiate OAuth login.

## Defense

Defensive measures and detection strategies:

- Whitelist exact redirect URIs in OAuth client configuration on Facebook.
- Implement state parameters with CSRF protection in OAuth flows.
- Monitor for anomalous redirects to subdomains via proxy logs.
- Use short-lived tokens and validate origins server-side.

## Objectives

1. Intercept and redirect the OAuth callback to attacker control.
2. Capture the issued Facebook access token.
3. Exfiltrate the token for further abuse, like API access.

## Instructions

### Step 1: Intercept OAuth Initiation

**Context**: From the main domain payload, hook into the Facebook login button or flow.

Inject JS to modify the OAuth request, altering redirect_uri to 'https://attacker-sub.rockstargames.com/callback'.

**Expected Output**: Modified auth request sent to Facebook.

### Step 2: Handle Redirect and Capture

**Context**: Set up the attacker subdomain to receive the callback.

Host a server on the controlled subdomain to log GET parameters containing the code or token.

**Expected Output**: Token received in query string, e.g., ?code=ABC123.

### Step 3: Validate and Exfiltrate

**Context**: Confirm token usability and send to attacker C2.

Use the token to call Facebook Graph API, e.g., /me, and beacon the data.

**Expected Output**: Successful API response with user data; token exfiltrated.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access
- [[Execution]] Execution

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- [[T1528.001]] Steal Application Access Token: Application Access Token

## Commands Used


## Tools Used


## Tags

- [[oauth]]
- [[redirect]]
- [[token-theft]]
- [[csrf]]
