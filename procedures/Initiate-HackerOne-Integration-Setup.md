---
tags:
  - csrf
  - oauth
  - setup
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
updated_at: '2025-12-14T17:27:57.861Z'
sub_techniques: []
id: bc40a9c7-c6e8-4231-b132-39ab0b7ccff9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Initiate-HackerOne-Integration-Setup

## Summary

This procedure initiates the OAuth integration setup in HackerOne for services like GitHub, generating necessary session and CSRF tokens required for subsequent CSRF exploitation in the authentication flow.

## Description

In the context of exploiting CSRF in HackerOne's Tray.io-based integrations, the attacker starts by creating a program and beginning the integration authentication process. This involves logging into HackerOne, selecting an integration (e.g., GitHub), and clicking 'New Authentication' to trigger the OAuth flow. A POST request to /session obtains session and CSRF tokens, which the frontend uses to construct a GET to the vulnerable /oauth2/auth endpoint. This step sets up the authentication ID and parameters without completing the flow legitimately.

## Requirements

1. Valid HackerOne account with permission to create programs and integrations
2. Browser access to HackerOne dashboard
3. Internet connectivity for API calls

## Defense

Defensive measures and detection strategies:

- Implement strict CSRF token validation on all state-changing endpoints
- Monitor for anomalous integration setups from new programs
- Use rate limiting on authentication flows

## Objectives

1. Obtain session, CSRF tokens, and authentication ID
2. Prepare for URL crafting in CSRF attack
3. Ensure flow initiation without premature completion

## Instructions

### Step 1: Log In and Navigate to Integrations

**Context**: Access the HackerOne dashboard to start the integration process.

Log into your HackerOne account and navigate to the 'Integrations' section.

### Step 2: Select Integration and Initiate Authentication

**Context**: Choose the target service (e.g., GitHub) to begin OAuth flow.

Select GitHub (or similar service like Jira), then click 'New Authentication'. This triggers a POST to /session:

```bash
# Simulated via browser or curl equivalent
curl -X POST https://hackerone.com/session \
  -H "Content-Type: application/json" \
  -d '{"csrf_token": "<generated>"}'
```

> This returns session and CSRF tokens. The frontend then prepares the GET request.

### Step 3: Observe Generated Parameters

**Context**: Note the authentication ID and parameters for crafting.

Intercept the subsequent GET request in dev tools to capture https://hackerone.integration-authentication.com/oauth2/auth/:authentication_id?csrf=<csrf>&scope=read:org%20repo&session=<session>.

**Expected Output**: Tokens and ID ready for next steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[oauth]]
- [[setup]]
