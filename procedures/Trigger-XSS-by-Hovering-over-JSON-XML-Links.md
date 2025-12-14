---
tags:
  - xss
  - execution-trigger
  - onmouseover
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 6429b940-9b47-46e9-84a8-d89f741fced3
created_at: '2025-12-14T03:15:35.914Z'
updated_at: '2025-12-14T03:15:35.914Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Hovering-over-JSON-XML-Links

## Summary

This procedure triggers the XSS payload by hovering over affected elements on the simulated Gravatar page, executing arbitrary JavaScript and demonstrating the vulnerability's exploitability.

## Description

With the page loaded, user interaction via mouse hover on elements like 'JSON' or 'XML' links fires the onmouseover event, executing the injected script (e.g., alert with '916137'). This PoC, as in http://grabilla.com/04318-ff2c5eea-0491-4841-977a-a4b7b1fafc9e.html, shows how attackers can steal data in real scenarios. The technique exploits poor encoding, affecting multiple Gravatar instances with high impact on browser security.

## Requirements

1. Loaded HTML page from previous procedure
2. Mouse-enabled interaction in browser
3. Firefox with JS enabled

## Defense

Defensive measures and detection strategies:

- Encode all attributes to prevent event handler injection
- Monitor for unexpected alerts or JS pops in user sessions
- Use WAF rules to detect onmouseover patterns in inputs

## Objectives

1. Execute injected JS via hover
2. Confirm arbitrary code run
3. Highlight session theft potential

## Instructions

### Step 1: Interact with Elements

**Context**: Hover to activate the payload.

Move the mouse cursor over the 'JSON' or 'XML' link on the page.

> Alert box appears with '916137'; script executes in context.

### Step 2: Validate Execution

**Context**: Check for success and implications.

Observe the alert and inspect console for full execution log.

> Expected: No errors; demonstrates potential for cookie access via document.cookie.

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
- [[trigger-execution]]
