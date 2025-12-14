---
tags:
  - oauth
  - token-capture
  - csrf
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
updated_at: '2025-12-14T17:27:35.883Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: a251f6d4-2878-44d5-a423-0bc3c35780b0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-Twitter-OAuth-and-Capture-Tokens

## Summary

This procedure outlines initiating the Twitter OAuth 1.0A flow in Phabricator, authorizing the app, and intercepting the callback to capture oauth_token and oauth_verifier without completing the authentication, enabling token reuse for CSRF attacks.

## Description

In Phabricator's Twitter OAuth implementation, the lack of a state parameter allows tokens generated during the attacker's flow to be reused. The attacker starts the login process, authorizes on Twitter, captures the parameters from the callback URL, and aborts the redirection to keep the tokens valid. This sets up the tokens for forcing a victim to authenticate as the attacker. Prerequisites include an attacker-controlled Phabricator account linked to Twitter and a web browser for manual steps. Expected outcome: Reusable tokens ready for malicious URL crafting.

## Requirements

1. Attacker's Phabricator account with Twitter integration enabled
2. Access to Twitter account for authorization
3. Browser with developer tools or proxy (e.g., Burp Suite) for interception
4. Victim must be logged out of Phabricator

## Defense

Defensive measures and detection strategies:

- Implement state parameters or nonce in OAuth callbacks to validate session binding
- Monitor for unusual OAuth token usage or multiple authentications from single tokens
- Rate-limit OAuth endpoints and log callback parameters for anomalies

## Objectives

1. Generate and capture valid OAuth tokens without consumption
2. Prevent legitimate completion of attacker's flow
3. Prepare tokens for victim-targeted CSRF

## Instructions

### Step 1: Start OAuth Flow

**Context**: Begin the authentication process to trigger token generation.

Navigate to the Phabricator Twitter login endpoint: https://target-phabricator.com/auth/login/twitter:twitter.com/.

This initiates a redirect to Twitter's authorization page.

> Expected: Redirect to twitter.com/oauth/authorize with Phabricator as the requesting app.

### Step 2: Authorize the Application

**Context**: Grant permissions to receive the callback with tokens.

On Twitter's page, approve access for the Phabricator application.

> Expected: After approval, Twitter redirects back to Phabricator's callback URL containing oauth_token and oauth_verifier query parameters.

### Step 3: Intercept Callback

**Context**: Extract tokens and abort to preserve them.

Use browser dev tools (F12 > Network tab) or a proxy to inspect the redirect URL from Twitter, e.g., https://target-phabricator.com/auth/login/twitter:twitter.com/callback?oauth_token=ABC123&oauth_verifier=XYZ789. Copy the values, then close the tab or block the request to Phabricator.

> Expected: Tokens recorded; no login occurs for attacker, keeping tokens fresh.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oauth
- token-capture
- csrf
