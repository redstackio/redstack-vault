---
tags:
  - csrf
  - forced-authentication
  - account-takeover
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:27:35.881Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 01173c9e-3a10-42f3-ae44-7c6d6152d394
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Deliver-Captured-Tokens-to-Victim

## Summary

This procedure involves crafting a malicious URL with captured OAuth tokens and tricking a victim into visiting it, exploiting Phabricator's lack of state validation to log them in as the attacker.

## Description

With oauth_token and oauth_verifier captured, the attacker constructs a login URL and delivers it to a logged-out victim via social engineering. Phabricator processes the tokens without verifying session state, completing the OAuth flow and authenticating the victim to the attacker's account. This enables account takeover, data access, or further attacks. Target: Phabricator web app with Twitter OAuth. Prerequisites: Captured tokens and victim contact method. Expected outcome: Victim gains attacker's session.

## Requirements

1. Captured oauth_token and oauth_verifier from prior procedure
2. Social engineering vector (email, link in chat)
3. Victim logged out of Phabricator
4. Phabricator instance vulnerable to OAuth 1.0A CSRF

## Defense

Defensive measures and detection strategies:

- Add CSRF tokens or state parameters to OAuth endpoints
- Require user confirmation for OAuth logins or detect cross-origin requests
- Log and alert on OAuth completions from unexpected IPs or user agents

## Objectives

1. Force victim to process attacker's tokens
2. Achieve unauthorized login to attacker's account
3. Enable post-exploitation from victim's browser

## Instructions

### Step 1: Craft Malicious URL

**Context**: Build the login endpoint with embedded tokens.

Construct: https://target-phabricator.com/auth/login/twitter:twitter.com/?oauth_token={oauth_token}&oauth_verifier={oauth_verifier}.

Replace placeholders with captured values, e.g., ?oauth_token=ABC123&oauth_verifier=XYZ789.

> Expected: Valid URL that mimics a legitimate OAuth callback.

### Step 2: Deliver to Victim

**Context**: Use phishing or other means to get victim to visit.

Send the URL via email, messaging, or embed in a webpage, e.g., "Click here to log in to Phabricator: [malicious URL]".

> Expected: Victim clicks and loads the endpoint, triggering OAuth processing.

### Step 3: Verify Authentication

**Context**: Confirm the forced login succeeds.

Monitor or ask victim to check their Phabricator session; they should see attacker's dashboard.

> Expected: Successful login without Twitter re-authorization; victim now has attacker's privileges.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf
- forced-authentication
- account-takeover
