---
id: proc-test-js-xss-payload
tags:
  - xss
  - javascript-execution
  - dom-injection
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
updated_at: '2025-12-13T23:52:21.037Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test-JavaScript-Execution-Payload-for-DOM-XSS

## Summary

This procedure exploits the DOM XSS by injecting a javascript: URI into the URL search parameter, leading to arbitrary code execution in the browser context.

## Description

By prepending 'javascript:' to the payload, the replace function interprets it as a script scheme, executing the code. This allows stealing cookies, session data, or performing actions, all under the informatica.com origin, amplifying the attack's stealth and impact.

## Requirements

1. Confirmed vulnerable endpoint
2. Browser allowing JS execution
3. Basic payload crafting knowledge

## Defense

Defensive measures and detection strategies:

- Parse and validate URL schemes, blocking javascript: and data:
- Implement strict CSP with 'unsafe-inline' disallowed
- Browser-side monitoring for anomalous script execution via extensions

## Objectives

1. Execute JS payload to confirm XSS
2. Demonstrate data theft potential
3. Evaluate execution context (same-origin)

## Instructions

### Step 1: Build XSS Payload

**Context**: Use a simple alert to test JS interpretation.

Form the URL: https://iqcard.informatica.com/pub/fujitsu/fm3v2/player/attach.html?javascript:alert(1)

> The substring(1) removes the ?, leaving 'javascript:alert(1)' for replace.

### Step 2: Trigger and Verify Execution

**Context**: Load the URL and check for JS alert.

Open in browser and observe.

> Expected output: Alert dialog with '1' appears, confirming execution.

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
- [[javascript-execution]]
- [[dom-injection]]
