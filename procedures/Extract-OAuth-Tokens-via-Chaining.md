---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - oauth-disclosure
  - token-theft
  - chaining
  - facebook
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:24:39.033Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Credentials In Files]]'
---
# Extract-OAuth-Tokens-via-Chaining

## Summary

This procedure chains an image injection vulnerability with an OAuth information disclosure flaw to steal Facebook authentication tokens from a victim's session, enabling potential account takeover.

## Description

Building on the image injection in the Screenshot Viewer, this step exploits weaknesses in the Facebook OAuth integration where tokens are exposed in the session during authentication flows. The injected image acts as a vector to capture and exfiltrate these tokens to an attacker-controlled endpoint. This targets web applications with third-party OAuth logins and requires the victim to be authenticated with Facebook.

## Requirements

1. Successful image injection from prior procedure
2. Active Facebook OAuth session in the victim's browser
3. Attacker server configured to capture and parse leaked data
4. Knowledge of the OAuth endpoint in the target application

## Defense

Defensive measures and detection strategies:

- Secure OAuth token storage using short-lived tokens and secure cookies (HttpOnly, Secure flags)
- Validate and sanitize all chained inputs across features
- Implement rate limiting on OAuth flows and monitor for token exfiltration attempts
- Use token binding to prevent reuse outside the intended context

## Objectives

1. Trigger the OAuth flow in the compromised session
2. Capture exposed tokens via the injection vector
3. Exfiltrate and validate the stolen tokens

## Instructions

### Step 1: Prepare Chained Environment

**Context**: Ensure the image injection is active and navigate to OAuth integration.

With the malicious image injected in the Screenshot Viewer, keep the tab open and switch to the Facebook login or integration page without refreshing the session.

### Step 2: Trigger OAuth Flow

**Context**: Initiate the authentication process to expose tokens.

Click the Facebook login button or perform an action that invokes the OAuth redirect. The chained vulnerability allows the injected image to load during this process, embedding session tokens in the request.

Monitor the browser's network activity for requests to the injected URL containing token data.

**Expected Output**: Attacker server receives a request with OAuth token parameters (e.g., access_token=xyz).

### Step 3: Capture and Validate Tokens

**Context**: Log and test the exfiltrated data.

Review server logs for the token and attempt to use it in a separate Facebook API call or session hijack test (e.g., via Graph API explorer).

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Credentials In Files]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oauth-theft
- information-disclosure
- session-hijacking
