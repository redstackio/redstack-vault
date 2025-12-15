---
id: proc-initiate-oauth-flow
tags:
  - oauth
  - initial-access
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
updated_at: '2025-12-14T17:27:03.732Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Initiate Attacker's Google OAuth Flow

## Summary

This procedure starts the Google OAuth authorization flow for the ThisData application under the attacker's Google account, generating the necessary state parameter for later reuse in the CSRF attack.

## Description

In the context of exploiting Login CSRF, the attacker begins the standard OAuth 2.0 flow by requesting authorization from Google. This involves redirecting to Google's endpoint with the client's parameters, including a state token. The lack of server-side validation on ThisData allows this state to be captured and reused. Prerequisites include a valid Google account and access to the ThisData login page. Expected outcome is the initiation of the flow without completion, setting up for parameter capture.

## Requirements

1. Valid Google account for the attacker
2. Browser access to ThisData's login endpoint
3. No special permissions beyond standard user access

## Defense

Defensive measures and detection strategies:

- Implement proper state parameter generation and validation on OAuth callbacks
- Use short-lived or single-use state tokens
- Monitor for unusual OAuth initiations from attacker IPs

## Objectives

1. Generate attacker-controlled OAuth state and prepare for code exchange
2. Avoid completing the flow to preserve tokens
3. Set stage for victim deception

## Instructions

### Step 1: Access ThisData Login

**Context**: Begin the authentication process to trigger the OAuth redirect.

Navigate to the ThisData login page and click the "Sign in with Google" button. This sends a GET request to Google's authorization URL with parameters like `client_id`, `redirect_uri=https://thisdata.com/oauth/redirect`, and a generated `state`.

### Step 2: Observe Redirect to Google

**Context**: Confirm the flow starts and note the state parameter if visible in the URL.

The browser redirects to `https://accounts.google.com/o/oauth2/auth?...&state=abc123`. No command execution needed; use browser inspection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[oauth]]
- [[initial-access]]
