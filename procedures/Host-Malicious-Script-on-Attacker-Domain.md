---
tags:
  - xss
  - javascript-execution
type: procedure
tools:
  - '[[tools/Browser-DevTools]]'
  - '[[tools/Apache-Web-Server]]'
tactics:
  - '[[procedures/Trigger-and-Verify-XSS-Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: c5f374af-b34b-45ee-9540-eaa31f3446ee
created_at: '2025-12-11T03:47:56.309Z'
updated_at: '2025-12-11T03:47:56.309Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Host Malicious Script on Attacker Domain

## Summary

This procedure hosts a malicious JavaScript file on an attacker-controlled domain to be loaded via redirected script imports in the XSS exploit.

## Description

By matching the path of failed script imports observed in DevTools, the attacker hosts JS that executes in the context of gitlab.com, such as alerting the domain to prove execution. This is part of the CSP bypass chain.

## Requirements

1. Control over a domain (e.g., joaxcar.com)
2. Web server like Apache
3. Knowledge of failed script paths from target

## Defense

Defensive measures and detection strategies:

- Monitor for anomalous script loads
- Use strict CSP with nonce or hash

## Objectives

1. Provide malicious payload for redirection
2. Execute arbitrary JS on target domain
3. Verify XSS success

## Instructions

### Step 1: Identify Failed Import Path

**Context**: Use DevTools to find the path of failing scripts.

Reload the page and inspect network requests for paths like assets/webpack/hello.4948f350.chunk.js.

### Step 2: Create and Host Script

**Context**: Host the script at the matching path.

Create a file with [[commands/javascript-alert-domain]]:

```javascript
alert(document.domain)
```

Upload to the server using [[tools/Apache-Web-Server]].

## MITRE ATT&CK Mapping

### Tactics

- [[procedures/Trigger-and-Verify-XSS-Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

## Commands Used

- [[commands/javascript-alert-domain]]

## Tools Used

- [[tools/Apache-Web-Server]]

## Tags

- xss
- javascript-execution
