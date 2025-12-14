---
id: uuid-proc-3
tags:
  - token-theft
  - ato
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:24.602Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
  - '[[Valid Accounts]]'
---
# Exfiltrate-Access-Token-via-Injected-Element

## Summary

This procedure uses the injected HTML element to capture the access token from the OIDC form and transmit it to an attacker, enabling account takeover with the stolen credentials.

## Description

Following injection, the malicious button's onclick event extracts the access token (included in the form for submission) and sends it via HTTP request to the attacker. In World ID, this allows impersonation for ATO. The attack requires one click but has high impact; CSP may block full XSS but not basic fetches in this case.

## Requirements

1. Successfully injected interactive HTML from previous step
2. Active listener on attacker endpoint to capture token
3. Valid OIDC session with access token present in form

## Defense

Defensive measures and detection strategies:

- Avoid including sensitive tokens in client-side forms; use server-side handling
- Monitor for unexpected outbound requests from auth pages
- Rotate tokens immediately on detection of anomalies and implement rate limiting

## Objectives

1. Extract and exfiltrate the access token
2. Validate token usability for account actions
3. Achieve full account takeover

## Instructions

### Step 1: Trigger Interaction

**Context**: Simulate or induce user click on the injected button.

Load the response page; click the malicious button to execute the exfiltration script.

> Script runs: fetches token value and sends to attacker.com.

### Step 2: Capture Exfiltrated Data

**Context**: Receive and log the token on the attacker side.

Monitor the endpoint (e.g., using ngrok or a server) for incoming requests containing the token query param.

> Expected: GET /steal?token=eyJ... with valid JWT.

### Step 3: Utilize Token for ATO

**Context**: Test the stolen token against target APIs.

Use the token in Authorization header for API calls, e.g., to fetch user profile or perform actions.

> Success if API responds with user data, confirming takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Unsecured Credentials]]
- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[token-theft]]
- [[ato]]
- [[Exfiltration]]
