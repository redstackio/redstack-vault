---
id: fd57ed68-33b0-4085-af59-b6e277836739
name: Initiate-Bitbucket-OAuth-Authorization-Flow
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.352Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - csrf
  - oauth
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Initiate-Bitbucket-OAuth-Authorization-Flow

## Summary

This procedure starts the OAuth authorization flow with Bitbucket for Gratipay integration, exploiting the lack of a state parameter to generate a reusable oauth_token.

## Description

In the context of Gratipay's vulnerable OAuth setup, the attacker accesses the Bitbucket authorization endpoint without CSRF protection. This generates an oauth_token that can be intercepted and reused, as there's no session-binding state parameter. The target environment is a web browser interacting with public OAuth endpoints.

## Requirements

1. Attacker's Bitbucket account credentials
2. Web browser access to https://bitbucket.org
3. Knowledge of Gratipay's OAuth callback URL structure

## Defense

Defensive measures and detection strategies:

- Implement state parameters in all OAuth requests to bind to user sessions
- Monitor for unusual OAuth token generations from single IPs
- Use web application firewalls to detect missing state in OAuth flows

## Objectives

1. Generate a temporary oauth_token for later reuse
2. Confirm absence of CSRF protection in the flow
3. Prepare for token preservation in subsequent steps

## Instructions

### Step 1: Access OAuth Endpoint

**Context**: Begin the authorization request to Bitbucket without a state parameter.

Navigate to the Bitbucket OAuth authorize URL, such as https://bitbucket.org/site/oauth1/authorize?oauth_token= (the token will be auto-generated upon initiation).

> This step leverages the public-facing OAuth endpoint, which lacks validation.

### Step 2: Observe Token Generation

**Context**: Capture the oauth_token from the redirect URL.

After initiation, the browser redirects to a URL containing the oauth_token (e.g., ZmCHb7dnyYVYKTYRNt). Copy this token manually.

> Expected output: Token visible in address bar; no errors if flow starts successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[csrf]]
- [[oauth]]
