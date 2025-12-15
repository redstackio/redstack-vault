---
id: proc-uuid-001
tags:
  - oauth
  - csrf
  - shopify
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-oauth-initiate]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:15.876Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-OAuth-Authorization-Request

## Summary

This procedure initiates the OAuth authorization flow for Shopify's Facebook Store app, revealing the fixed 'state' parameter that enables CSRF token fixation attacks.

## Description

In the OAuth flow, the app sends a GET request to Facebook's Graph API with a static state value. This procedure simulates that request to inspect and confirm the fixation, allowing attackers to predict the state for later exploitation. It targets web-based e-commerce integrations and requires no authentication for initiation but benefits from session inspection tools.

## Requirements

1. Network access to Facebook Graph API and Shopify apps
2. Browser or curl for sending requests
3. Knowledge of the app's client_id (410312912374011)

## Defense

Defensive measures and detection strategies:

- Regenerate state parameters per request using secure random generation
- Implement CSRF tokens unique to each session
- Monitor for repeated state values in OAuth logs

## Objectives

1. Trigger the OAuth authorization endpoint
2. Capture the fixed state for reuse
3. Validate lack of state rotation

## Instructions

### Step 1: Send Authorization Request

**Context**: Construct and send the GET request to the Facebook OAuth endpoint with the app's parameters to observe the state.

**Command** ([[commands/curl-oauth-initiate]]):
```bash
curl -X GET "https://graph.facebook.com/oauth/authorize?client_id=410312912374011&display=popup&redirect_uri=https%3A%2F%2Ffacebookstore.shopifyapps.com%2Fauthenticated&response_type=code&scope=manage_pages+email&state=c2f449f2df5ee64df6173702846bce72e3a57319"
```

> This command initiates the flow and returns the authorization page or redirect. Inspect the URL for the fixed state 'c2f449f2df5ee64df6173702846bce72e3a57319'. Repeat the request to confirm no change.

### Step 2: Inspect Response

**Context**: Analyze the response to extract parameters for further steps.

**Command** ([[commands/curl-oauth-inspect]]):
```bash
curl -v -X GET "https://graph.facebook.com/oauth/authorize?client_id=410312912374011&display=popup&redirect_uri=https%3A%2F%2Ffacebookstore.shopifyapps.com%2Fauthenticated&response_type=code&scope=manage_pages+email&state=c2f449f2df5ee64df6173702846bce72e3a57319" > response.html
```

> Save and open response.html to verify the state persistence. Expected: Static state across invocations.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/curl-oauth-initiate]]
- [[commands/curl-oauth-inspect]]

## Tools Used


## Tags

- [[oauth]]
- [[csrf]]
- [[shopify]]
