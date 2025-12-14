---
id: proc-53098-step3
name: Trigger-XSS-via-Mouseover-Event
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:15:53.440Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - event-trigger
  - javascript-execution
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Trigger-XSS-via-Mouseover-Event

## Summary

This procedure executes the injected JavaScript payload by triggering the onmouseover event on the reflected link element, demonstrating arbitrary code execution in the victim's browser context.

## Description

After interaction, hovering over the vulnerable 'continue' element or reflected link fires the onmouseover event, running the injected alert(1) script. This exploits the lack of attribute sanitization in the reflected 'unsafe_link' parameter. Impacts include potential session hijacking or data theft, limited to Internet Explorer due to CSP in other browsers. Prerequisites: Rendered page with active payload.

## Requirements

1. Interactive DOM with injected onmouseover attribute
2. Internet Explorer
3. Mouse input capability

## Defense

Defensive measures and detection strategies:

- Sanitize HTML attributes to prevent event handler injection
- Enforce CSP nonces or hashes for scripts
- Detect anomalous JavaScript events in browser logs or WAF

## Objectives

1. Execute arbitrary JavaScript in browser context
2. Confirm XSS success with alert
3. Enable follow-on attacks like data exfiltration

## Instructions

### Step 1: Perform Mouseover on Vulnerable Element

**Context**: Trigger the event to execute the payload.

No specific command; manual hover.

Move the mouse cursor over the 'continue' button or reflected link.

> Expected output: Alert(1) dialog appears, confirming execution. In a real attack, replace with malicious code like document.cookie theft.

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
- [[event-trigger]]
- [[javascript-execution]]
