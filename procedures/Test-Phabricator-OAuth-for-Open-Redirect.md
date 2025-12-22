---
id: proc-test-phab-oauth-redirect-3930
tags:
  - oauth
  - open-redirect
  - phabricator
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
updated_at: '2025-12-14T17:24:35.424Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test Phabricator OAuth for Open Redirect

## Summary

This procedure tests the Phabricator OAuth endpoint for an open redirect vulnerability by supplying an invalid scope parameter, causing an automatic redirect to a specified URI without user interaction or login requirements.

## Description

In the attack scenario, an attacker accesses the Phabricator OAuth server endpoint (/oauthserver/auth/) with malformed parameters. The lack of validation on the scope parameter allows the server to redirect immediately to the redirect_uri, bypassing normal OAuth flows. This is tested on public instances like secure.phabricator.com and enables chaining with other OAuth providers. Prerequisites include a web browser and access to the endpoint; no authentication is needed due to the bypass.

## Requirements

1. Web browser with developer tools for URL manipulation
2. Publicly accessible Phabricator instance
3. Attacker-controlled domain for redirect testing

## Defense

Defensive measures and detection strategies:

- Validate all redirect_uris against a whitelist in OAuth implementations
- Log and monitor anomalous redirects from OAuth endpoints
- Require user confirmation for any redirect in OAuth flows

## Objectives

1. Confirm open redirect vulnerability in Phabricator OAuth
2. Verify bypass of login and interaction requirements
3. Prepare for chaining with external providers

## Instructions

### Step 1: Access OAuth Endpoint with Malformed Parameters

**Context**: Navigate to the Phabricator OAuth authorization endpoint and append query parameters to test for automatic redirection.

No specific command; use browser URL bar or curl equivalent:

```bash
curl "https://secure.phabricator.com/oauthserver/auth/?redirect_uri=http://attacker-site.com&response_type=code&client_id=PHID-OASC-oyfqtnanxsukiw5lsnce&scope=ggg" -v
```

> This sends a GET request to the endpoint with an invalid scope ('ggg'). Expected output: HTTP 302 redirect to http://attacker-site.com without authentication challenges.

### Step 2: Observe Redirect Behavior

**Context**: Follow the redirect in the browser to confirm no prompts appear.

Use browser dev tools to inspect the response and location header.

**Expected Output**: Direct browser navigation to the redirect_uri; no Phabricator login or scope confirmation page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oauth
- open-redirect
- phabricator
