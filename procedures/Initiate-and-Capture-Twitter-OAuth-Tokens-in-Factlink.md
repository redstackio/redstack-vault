---
tags:
  - oauth
  - token-capture
  - csrf-prep
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.257Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7b78ab65-98f6-4ca1-8b0b-9b1c3dbbd22b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-and-Capture-Twitter-OAuth-Tokens-in-Factlink

## Summary

This procedure outlines starting the Twitter OAuth 1.0A flow in Factlink to obtain oauth_token and oauth_verifier, which are then captured and prevented from being consumed, setting up a subsequent CSRF attack.

## Description

In the context of Factlink's vulnerable Twitter integration, the attacker begins the authentication process to generate temporary credentials. Due to the absence of a state parameter, these tokens can be reused to force another user's login. This step requires manual browser interaction and token extraction, typically via developer tools or a proxy like Burp Suite.

## Requirements

1. Access to a Twitter account controlled by the attacker
2. Web browser with developer console or intercepting proxy
3. Factlink application accessible

## Defense

Defensive measures and detection strategies:

- Implement OAuth state parameters to bind requests to sessions
- Monitor for unusual OAuth token reuse or rapid authentications
- Use Content Security Policy (CSP) to restrict callback origins

## Objectives

1. Generate and capture OAuth tokens without completing the flow
2. Prevent token consumption to enable reuse
3. Prepare for CSRF injection

## Instructions

### Step 1: Start OAuth Flow

**Context**: Navigate to the Twitter login endpoint in Factlink to initiate the request token phase.

**Instructions**: Open a browser and visit Factlink's Twitter auth URL, e.g., `https://factlink.com/auth/login/twitter:twitter.com/`. This redirects to Twitter for authorization.

> The flow begins with a GET request lacking state, generating oauth_token.

### Step 2: Authorize and Intercept Callback

**Context**: Grant permissions on Twitter's side and capture the callback parameters.

**Instructions**: On Twitter's authorization page, click "Authorize app". The callback to Factlink will include `oauth_token` and `oauth_verifier`. Use browser dev tools (Network tab) or a proxy to copy these values and block the final redirect.

> Expected: Parameters like `oauth_token=ABC123&oauth_verifier=XYZ789` visible in the URL or request.

### Step 3: Store Tokens Securely

**Context**: Save the tokens for URL crafting.

**Instructions**: Note down the token and verifier values. Do not proceed to Factlink login to keep tokens valid.

> Success: Tokens extracted and flow aborted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oauth
- token-capture
