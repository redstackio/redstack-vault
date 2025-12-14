---
tags:
  - oauth
  - authorization
  - app-binding
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 1ad6a1e5-6082-4580-8aa9-6aa1b87e9cc3
created_at: '2025-12-14T17:30:35.371Z'
updated_at: '2025-12-14T17:30:35.371Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Complete Unauthorized App Binding on LinkedIn

## Summary

This procedure finalizes the OAuth authorization by leveraging the user's space key interaction to bind the malicious third-party app to their LinkedIn account, granting limited access scopes without explicit consent.

## Description

Once the user holds the space key on the manipulated OAuth page, the client-side JavaScript processes the event as a button activation due to the URL hash positioning. This submits the authorization request to LinkedIn's endpoint, exchanging the code for an access token. The app then gains read access to basic profile data. The vulnerability stems from insufficient validation of input methods in the OAuth UI. Outcomes include app binding visible in the user's connected apps list.

## Requirements

1. Active phishing link with user interaction completed
2. Registered OAuth app with redirect URI configured
3. Ability to handle OAuth callback for token exchange

## Defense

Defensive measures and detection strategies:

- Require explicit click-based consent in OAuth UIs, ignoring keyboard-only triggers
- Audit and notify users of new app bindings
- Scope OAuth apps minimally and review third-party permissions regularly

## Objectives

1. Trigger the OAuth submission via simulated press
2. Receive and store the authorization code/token
3. Verify app access to user data

## Instructions

### Step 1: Await OAuth Submission

**Context**: The space hold event submits the form to the authorization endpoint.

Monitor the app's callback endpoint for the incoming authorization code from LinkedIn's redirect.

### Step 2: Exchange Code for Token

**Context**: Use the code to obtain an access token via LinkedIn's token endpoint.

POST to https://www.linkedin.com/oauth/v2/accessToken with client_id, client_secret, grant_type=authorization_code, and code. This binds the app and returns the token.

### Step 3: Validate Binding

**Context**: Confirm the app has access and test scopes.

Use the token to query a scoped endpoint (e.g., /v2/me) and retrieve limited user data, verifying successful unauthorized binding.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[oauth]]
- [[authorization]]
- [[app-binding]]
