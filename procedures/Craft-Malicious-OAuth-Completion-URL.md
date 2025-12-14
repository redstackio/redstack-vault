---
tags:
  - csrf
  - url-crafting
  - phishing-prep
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:29.252Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 8affe155-40bf-4261-980a-bb6acb1a2d1e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-Malicious-OAuth-Completion-URL

## Summary

This procedure involves constructing a deceptive URL that embeds the attacker's OAuth tokens, tricking the victim into completing the authentication flow on their behalf when visited.

## Description

Exploiting the stateless nature of Factlink's OAuth callback, the attacker builds a URL mimicking the legitimate completion endpoint. When the victim accesses it, their browser submits the tokens, binding their session to the attacker's identity without additional checks.

## Requirements

1. Captured oauth_token and oauth_verifier from prior step
2. Knowledge of Factlink's callback path
3. Method to distribute the URL (e.g., email client)

## Defense

Defensive measures and detection strategies:

- Enforce state/nonce in OAuth callbacks
- Validate referrer or origin headers
- Log and alert on anomalous token submissions

## Objectives

1. Create a functional malicious URL
2. Ensure tokens are injectable via GET parameters
3. Prepare for victim delivery

## Instructions

### Step 1: Format the URL

**Context**: Use the exact callback structure from Factlink's OAuth flow.

**Instructions**: Construct the URL as `https://factlink.com/auth/login/twitter:twitter.com/?oauth_token={your_oauth_token}&oauth_verifier={your_oauth_verifier}`. Replace placeholders with captured values.

> Example: If token is ABC123 and verifier XYZ789, URL becomes `/auth/login/twitter:twitter.com/?oauth_token=ABC123&oauth_verifier=XYZ789`.

### Step 2: Test URL Integrity

**Context**: Verify the URL doesn't auto-consume tokens prematurely.

**Instructions**: In an incognito browser (not completing login), visit the URL and inspect if parameters are passed correctly without errors.

> Expected: Endpoint accepts parameters; no state mismatch error.

### Step 3: Obfuscate for Delivery

**Context**: Make the link appear legitimate to avoid detection.

**Instructions**: Shorten the URL using a service like bit.ly or embed in a phishing page.

> Success: URL ready for sending to victim.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf
- url-crafting
