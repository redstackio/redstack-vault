---
tags:
  - xss
  - injection
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - iOS
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 7e01b50a-c6cc-40cf-8127-aacdfbff2293
created_at: '2025-12-14T03:47:12.884Z'
updated_at: '2025-12-14T03:47:12.884Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-Injected-JavaScript-on-Top-Frame

## Summary

This procedure exploits the unescaped 'version' parameter in Brave iOS's U2F response handling to inject and execute arbitrary JavaScript on the top frame, resulting in universal XSS.

## Description

In U2FExtensions.swift, the 'version' from the postMessage is directly embedded into evaluateJavaScript without escaping, allowing attacker-controlled code (e.g., alert('XSS')) to run on the top-level origin. This occurs post-FIDO interaction in the attack flow, granting access to the victim's session and data. Scenario: Follows subframe trigger and device touch; requires no additional user action. Outcomes: Full DOM access, cookie theft, or further exploits.

## Requirements

1. Completed U2F registration from prior steps
2. Malicious 'version' payload in postMessage (e.g., ';alert(1);//')
3. Brave iOS version vulnerable to unescaped evaluation

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all postMessage parameters before JS evaluation
- Implement JS injection detection in browser telemetry
- Patch U2F implementations to validate and escape inputs

## Objectives

1. Inject arbitrary code via unescaped parameter
2. Achieve code execution on top frame origin
3. Realize universal XSS for data exfiltration or persistence

## Instructions

### Step 1: Include Malicious Version Parameter

**Context**: Embed payload in the initial postMessage.

Set 'version' to '1.0; maliciousJS();' in the U2F message.

> This will be inserted as evaluateJavaScript('version: 1.0; maliciousJS();').

### Step 2: Process Response After Interaction

**Context**: Let browser handle the FIDO response.

Upon device confirmation, the evaluation occurs automatically.

> Expected: JS executes, e.g., alert pops on top frame.

### Step 3: Verify Execution

**Context**: Confirm XSS success.

Check for alert or console logs on victim origin.

> Success: Arbitrary code runs, demonstrating UXSS.

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
- [[injection]]
- [[JavaScript]]
