---
id: proc-uuid-002
tags:
  - oauth
  - authorization
  - facebook
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:15.865Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Authorize-App-on-Facebook

## Summary

This procedure handles the user authorization step in the OAuth flow, capturing the callback response that includes the victim's authorization code alongside the fixed state.

## Description

After initiating the request, the user (victim) authorizes the app on Facebook, triggering a redirect to the Shopify callback URL. The fixed state is preserved, allowing later CSRF. This step requires user interaction and is key to obtaining the code parameter for exploitation.

## Requirements

1. Valid Facebook account for testing/victim simulation
2. Access to the authorization URL from Step 1
3. Ability to intercept redirects (e.g., via proxy)

## Defense

Defensive measures and detection strategies:

- Enforce state validation on callback
- Use short-lived authorization codes
- Log and alert on mismatched states

## Objectives

1. Complete user authorization
2. Capture callback parameters
3. Confirm state fixation in redirect

## Instructions

### Step 1: Direct to Authorization Page

**Context**: Navigate to the OAuth URL in a browser to prompt Facebook login and app permission.

**Instructions**: Open the URL from the initiation step in a browser. Log in to Facebook and grant permissions for manage_pages and email scopes.

> Expected: Facebook authorization dialog appears, followed by redirect.

### Step 2: Capture Callback

**Context**: Intercept the redirect to extract code and state.

**Instructions**: Use browser dev tools or a proxy to monitor the redirect to https://facebookstore.shopifyapps.com/authenticated?code=VICTIM_CODE&state=c2f449f2df5ee64df6173702846bce72e3a57319.

> Expected: Parameters include auth code and fixed state. Note the code for potential reuse in testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[oauth]]
- [[authorization]]
- [[facebook]]
