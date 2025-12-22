---
tags:
  - script-execution
  - js-payload
  - data-exfil
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:20.326Z'
sub_techniques: []
id: f8021f0d-47d2-4bea-b9c2-8d1166720579
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-Malicious-Script-in-Victims-Browser

## Summary

This procedure executes the JavaScript payload downloaded from the attacker's server, running in the victim's browser context on secnews.gr, allowing arbitrary code like alerts, cookie theft, or further attacks.

## Description

After colorbox inserts the response, the <script> tag executes immediately. The proof-of-concept alerts document.domain to confirm context, but in practice, it could hijack sessions, steal data, or perform actions. The vulnerability's out-of-scope status for bounty highlights its potential despite mitigations like WAF.

## Requirements

1. Previous steps completed (injection and trigger)
2. No CSP blocking script execution
3. Victim's browser supports JavaScript

## Defense

Defensive measures and detection strategies:

- Deploy strict CSP with script-src 'self'
- Use X-XSS-Protection: 1; mode=block header
- Monitor browser console for unauthorized script loads

## Objectives

1. Run JS in target domain context
2. Demonstrate impact (e.g., alert or exfil)
3. Enable follow-on attacks like session hijacking

## Instructions

### Step 1: Deliver and Execute Payload

**Context**: The server response handles delivery; execution is passive.

**Command**:
```bash
# Server-side: Ensure response is <script>alert(document.domain)</script>
# Client-side: Automatic upon insertion
```

> No direct command; observe alert in victim's browser.

### Step 2: Validate Execution

**Context**: Check for signs of success post-interaction.

**Command**:
```bash
# Use browser dev tools or proxy to inspect
```

> Success: Alert fires, or custom payload (e.g., fetch to attacker server with cookies) logs data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- execution
- javascript
- impact
