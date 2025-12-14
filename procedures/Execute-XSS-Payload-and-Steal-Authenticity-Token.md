---
id: proc-twitter-xss-execute-steal-token
tags:
  - xss-execution
  - token-theft
  - csrf
  - csp-bypass
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-csrf-favorite-tweet]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Cloud Instance Metadata API]]'
updated_at: '2025-12-14T17:24:35.699Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Cloud Instance Metadata API]]'
---
# Execute-XSS-Payload-and-Steal-Authenticity-Token

## Summary

This procedure triggers the XSS payload on the OAuth redirect page, executes JavaScript to steal the authenticity_token, and uses it for CSRF attacks like unauthorized tweet favoriting, bypassing CSP with dangling markup.

## Description

Post-authorization, the unsanitized oauth_callback renders as HTML, executing the JS (e.g., alert). For impact, steal the form's authenticity_token via JS and exfiltrate it. Advanced PoC uses dangling markup (e.g., incomplete <img> tag) to bypass CSP, then CSRF to /i/tweet/favorite. Targets twitter.com; requires victim context.

## Requirements

1. Successful victim authorization
2. Access to a PoC server for exfiltration (e.g., innerht.ml)
3. Stolen token for CSRF submission

## Defense

Defensive measures and detection strategies:

- Validate and escape all redirect parameters
- Enforce strict CSP without unsafe-inline
- Detect anomalous JS execution or token usage in sessions

## Objectives

1. Execute arbitrary JS in victim browser
2. Extract and exfiltrate authenticity_token
3. Perform unauthorized actions via CSRF

## Instructions

### Step 1: Trigger Payload Execution

**Context**: Payload auto-executes on redirect; monitor for JS run.

No command; in PoC, JS like: document.querySelector('input[name=authenticity_token]').value sent to attacker server.

> Basic: Alert pops; advanced: Token exfiltrated via fetch/XMLHttpRequest.

### Step 2: Perform CSRF with Stolen Token

**Context**: Use exfiltrated token to submit unauthorized request.

**Command** ([[commands/curl-csrf-favorite-tweet]]):
```bash
curl -X POST 'https://twitter.com/i/tweet/favorite' \
  -d 'authenticity_token=STOLEN_AUTHENTICITY_TOKEN' \
  -d 'id=1234567890' \
  -H 'X-CSRF-Token: STOLEN_TOKEN' \
  -H 'Cookie: ct0=VICTIM_SESSION_COOKIE; auth_token=VICTIM_AUTH_TOKEN'
```

> Submits favorite for tweet ID; expected: 200 OK or redirect, confirming action.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Cloud Instance Metadata API]]

### Sub-Techniques


## Commands Used

- [[commands/curl-csrf-favorite-tweet]]

## Tools Used


## Tags

- [[xss-execution]]
- [[csrf]]
