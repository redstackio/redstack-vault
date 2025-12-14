---
tags:
  - oauth
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: f383883b-cdc4-4e22-90cc-f12a00faf248
created_at: '2025-12-14T17:24:38.899Z'
updated_at: '2025-12-14T17:24:38.899Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Initiate-OAuth-Flow-from-Scoped-Website

## Summary

This procedure initiates the standard OAuth authorization flow from a legitimate scoped website like xbox.dayz.com, triggering a request to the authorization server at accounts.bistudio.com to observe the default parameters and prepare for exploitation.

## Description

In the context of exploiting an open redirect vulnerability in the OAuth flow, this step establishes the baseline OAuth request. The scoped website (e.g., DayZ Xbox integration) redirects users to the authorization endpoint for login or token grant. The server validates the redirect_uri by checking only if it starts with 'https://xbox.dayz.com/', which is key for the subsequent bypass. Prerequisites include access to the internet and a web browser; no special credentials are needed initially.

## Requirements

1. Web browser with developer tools enabled for inspecting network requests
2. Access to the scoped website (e.g., https://xbox.dayz.com)
3. Understanding of OAuth 2.0 parameters (client_id, redirect_uri, state, scope)

## Defense

Defensive measures and detection strategies:

- Monitor OAuth initiation logs for unusual patterns or high-volume requests from scoped sites
- Implement client-side validation of OAuth URLs before redirection
- Use web application firewalls (WAF) to flag anomalous redirect_uri values

## Objectives

1. Trigger and observe the OAuth authorization request
2. Identify the default redirect_uri format for tampering
3. Confirm the flow without errors to ensure exploit feasibility

## Instructions

### Step 1: Access the Login Page

**Context**: Navigate to the target scoped website's login or authorization endpoint to start the OAuth process.

Open a web browser and go to https://xbox.dayz.com (or similar login page). Click the login button to initiate the flow.

> This redirects to https://accounts.bistudio.com/api/auth with query parameters. Use browser dev tools (F12 > Network tab) to inspect the request.

### Step 2: Inspect OAuth Parameters

**Context**: Analyze the authorization URL to note the structure, especially the redirect_uri.

In the browser address bar or network logs, observe the full URL, e.g., https://accounts.bistudio.com/api/auth?client_id=...&redirect_uri=https://xbox.dayz.com/api/auth/callback&state=...&response_type=code.

> Expected output: Confirmation that redirect_uri starts with the allowed prefix. No code execution needed; this is observational.

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
- [[web]]
- [[Reconnaissance]]
