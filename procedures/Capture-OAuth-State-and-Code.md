---
id: proc-capture-oauth-params
tags:
  - csrf
  - oauth
  - parameter-capture
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:27:03.728Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Capture OAuth State and Code Parameters

## Summary

This procedure involves authorizing the OAuth request and intercepting the callback URL's state and code parameters from the Google redirect, preventing the final login to keep the tokens reusable for the CSRF exploit.

## Description

After initiating the flow, the attacker grants permissions on Google's consent screen, triggering a redirect back to ThisData's `/oauth/redirect` endpoint with `state` and `code`. Using browser tools, the attacker copies these values and aborts the redirect. This exploits the vulnerability where the server does not validate state uniqueness or binding. Target environment is any OAuth-integrated web app like ThisData. Outcomes include preserved tokens for victim use.

## Requirements

1. Active OAuth flow from previous step
2. Browser with developer tools enabled (e.g., Chrome DevTools)
3. Attacker's Google permissions granted to ThisData

## Defense

Defensive measures and detection strategies:

- Bind state to session cookies or user agents
- Log and alert on code reuse attempts
- Enforce one-time use for authorization codes

## Objectives

1. Extract state and code without token consumption
2. Prepare parameters for malicious URL construction
3. Maintain token validity for reuse

## Instructions

### Step 1: Grant Permissions

**Context**: Complete the consent to receive the code.

On the Google consent screen, click "Allow" to grant ThisData access to the attacker's profile. This generates the authorization code.

### Step 2: Intercept Callback

**Context**: Capture the redirect before it processes.

In the browser's Network tab, locate the request to `/oauth/redirect?state=abc123&code=def456`. Copy the full URL parameters, then refresh or close the tab to drop the redirect and avoid exchanging the code.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[oauth]]
- [[parameter-capture]]
