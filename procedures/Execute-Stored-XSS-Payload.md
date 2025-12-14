---
tags:
  - xss
  - execution
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:37.414Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: a8d912f8-ec99-4126-b0ad-8088d819f6bb
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-Stored-XSS-Payload

## Summary

This procedure executes the injected JavaScript payload to achieve arbitrary code execution in the browser context of users viewing the restaurant page, demonstrating potential for data exfiltration or manipulation.

## Description

With the payload triggered, the onmouseover event fires, running the prompt function to display the document domain, proving control. In production attacks, this could extend to document.cookie theft, keylogging, or phishing overlays. The execution occurs client-side, impacting any authenticated user on the page without server involvement.

## Requirements

1. Triggered payload from edit or view action
2. Browser with JS enabled
3. Victim interaction (e.g., mouse hover) for event-based payload

## Defense

Defensive measures and detection strategies:

- Deploy strict CSP headers blocking unsafe-inline
- Sanitize all user-generated content on output
- Use browser security features like XSS Auditor

## Objectives

1. Run JS to interact with DOM and session data
2. Collect evidence of execution (e.g., alert)
3. Enable escalation to session hijacking

## Instructions

### Step 1: Interact with Injected Element

**Context**: Perform the action that fires the event handler in the payload.

In the rendered review or edit form, hover the mouse over the area where the img tag is injected.

### Step 2: Observe Execution

**Context**: Verify JS runs by checking for the prompt or console output.

The payload `prompt(document.domain)` should display an alert with the domain (e.g., 'www.zomato.com').

> Success indicates full XSS control; replace prompt with `fetch('/steal?cookie=' + document.cookie)` for real impact.

**Expected Output**: Browser alert box appears with domain name.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[javascript-execution]]
