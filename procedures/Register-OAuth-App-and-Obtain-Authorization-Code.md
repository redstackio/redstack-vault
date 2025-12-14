---
id: proc-oauth-register-code-001
tags:
  - oauth
  - app-registration
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/open-authorize-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:32:38.837Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Register-OAuth-App-and-Obtain-Authorization-Code

## Summary

This procedure registers a malicious OAuth 2.0 application with the target provider and obtains a single-use authorization code by simulating the authorization flow, setting the stage for token exploitation.

## Description

In OAuth 2.0, applications must be registered to receive client_id and client_secret. The attacker then crafts an authorization URL, opens it in a browser (potentially as the victim), logs in, grants access, and extracts the code from the redirect URI. This code is intended for one-time use per RFC 6749 but is vulnerable to race conditions in many implementations. Prerequisites include access to the provider's developer portal and victim credentials.

## Requirements

1. Access to the OAuth provider's app registration portal.
2. Victim's login credentials for the provider.
3. A registered redirect URI (e.g., https://attacker.com/callback).

## Defense

Defensive measures and detection strategies:

- Enforce strict app registration with manual review.
- Monitor for unusual authorization requests from unknown IPs.
- Implement rate limiting on /oauth/authorize endpoints.

## Objectives

1. Obtain client credentials for token exchanges.
2. Acquire a valid authorization code.
3. Prepare for concurrent exploitation.

## Instructions

### Step 1: Register the Application

**Context**: Create a new app in the provider's developer console to get client_id and client_secret.

**Command** ([[commands/register-app]]):
No specific command; perform via web interface.

> Register the app, noting the client_id (e.g., APPLICATION_ID) and client_secret (e.g., APPLICATION_SECRET), and set redirect_uri to your controlled domain.

### Step 2: Initiate Authorization Flow

**Context**: Construct and open the authorize URL to obtain the code.

**Command** ([[commands/open-authorize-url]]):
```bash
# Manually open in browser: https://OAUTH_PROVIDER_DOMAIN/oauth/authorize?client_id=APPLICATION_ID&redirect_uri=https://APPLICATION_REDIRECT_URI&response_type=code
```

> Log in as victim, grant access; code appears in callback like https://APPLICATION_REDIRECT_URI?code=AUTHORIZATION_CODE_VALUE.

### Step 3: Extract the Code

**Context**: Capture the code from the redirect.

No command; parse URL manually or via script.

> Expected: AUTHORIZATION_CODE_VALUE ready for exchange.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques

-

## Commands Used

- [[commands/open-authorize-url]]

## Tools Used

- [[tools/curl]]

## Tags

- [[oauth]]
- [[app-registration]]
