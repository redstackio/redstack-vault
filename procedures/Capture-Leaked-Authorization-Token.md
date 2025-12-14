---
tags:
  - token-capture
  - exfiltration
  - javascript
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
  - '[[Steal Application Access Token]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:35.019Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: d2ee558c-d630-46af-a38c-d17ddcdc2ebf
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Application Access Token]]'
  - '[[JavaScript]]'
---
# Capture-Leaked-Authorization-Token

## Summary

This procedure sets up an event listener on the malicious page to receive the authorization token via postMessage from the PSN response window, displaying it for exfiltration and use in impersonation attacks.

## Description

Due to the wildcard targetOrigin, the PSN response.html sends the token to any origin via window.opener.postMessage. The onmessage handler captures this, allowing the attacker to view and extract the token for API abuse, such as accessing friends lists or posting. Targets browsers post-exploitation of the OAuth misconfig.

## Requirements

1. Popup window triggered and granting access
2. onmessage listener active on parent page
3. DOM element for token display (e.g., div id='token-plate')

## Defense

Defensive measures and detection strategies:

- Implement strict CSP to restrict postMessage origins
- Log and alert on wildcard postMessage usage
- Monitor for anomalous token usage in PSN APIs

## Objectives

1. Intercept token from postMessage event
2. Display and exfiltrate for further attacks
3. Validate token for impersonation

## Instructions

### Step 1: Set Up Event Listener

**Context**: Initialize onmessage on the malicious page before opening popup.

JavaScript: window.onmessage = function(event) { if (event.data.access_token) { document.getElementById('token-plate').innerText = event.data.access_token; } };

> Expected output: Listener ready; no immediate output.

### Step 2: Receive and Display Token

**Context**: After popup closes or messages, capture and show token.

Navigate back to malicious page if needed.

> Expected output: Token string in div, e.g., 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9...'

### Step 3: Validate Token Usage

**Context**: Test token with PSN API (e.g., fetch friends).

Use token in Authorization: Bearer header for API calls.

> Expected output: Successful API response with victim data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Steal Application Access Token]] Steal Application Access Token
- [[JavaScript]] Command and Scripting Interpreter: JavaScript

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[token-capture]]
- [[Exfiltration]]
- [[JavaScript]]
