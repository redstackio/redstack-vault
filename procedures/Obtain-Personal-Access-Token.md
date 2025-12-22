---
tags:
  - authentication
  - api-access
  - token-generation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 41e164bb-7d77-4a11-97af-75e1e2b1f5fd
created_at: '2025-12-14T03:47:13.130Z'
updated_at: '2025-12-14T03:47:13.130Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Obtain-Personal-Access-Token

## Summary

This procedure generates or acquires a Personal Access Token in Rocket.Chat for authenticated API interactions, enabling subsequent message posting and exploitation.

## Description

In Rocket.Chat, Personal Access Tokens provide API authentication without full session cookies. This step is prerequisite for REST API calls like chat.postMessage. It targets user settings or admin panels, assuming an existing account. Outcomes include token retrieval for header-based auth, setting up for XSS injection.

## Requirements

1. Valid Rocket.Chat user account with login access
2. Web browser or API client for token generation
3. Network connectivity to the Rocket.Chat server

## Defense

Defensive measures and detection strategies:

- Enable token expiration and scoping to limit API permissions
- Monitor API token creation logs for anomalous activity
- Use multi-factor authentication (MFA) for token-enabled accounts

## Objectives

1. Secure authenticated access to Rocket.Chat API endpoints
2. Prepare for payload delivery without direct session exposure
3. Minimize detection by using legitimate token mechanisms

## Instructions

### Step 1: Access User Settings

**Context**: Log in to Rocket.Chat and navigate to token generation.

No command required; use the web interface:

1. Log in to your Rocket.Chat account.
2. Go to User Menu > My Account > Personal Access Tokens.
3. Click 'Add' to create a new token with necessary scopes (e.g., chat:write).

> Token generated as a string, e.g., 'abc123-def456-ghi789'. Copy and store securely.

### Step 2: Verify Token

**Context**: Test the token with a simple API call to confirm validity.

Use a basic curl test (not linked to specific command here):

```bash
curl -H "X-Auth-Token: <Token>" -H "X-User-Id: <user Id>" https://<server>/api/v1/me
```

> Expected output: JSON with user details if valid.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[api-access]]
- [[token-generation]]
