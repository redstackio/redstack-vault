---
id: proc-zaption-inject-xss-payload
tags:
  - xss
  - payload
  - injection
  - javascript
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
updated_at: '2025-12-14T03:16:14.316Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Quick-Question-Field

## Summary

This procedure describes injecting a crafted XSS payload into the Zaption 'Quick question' input field, exploiting poor HTML sanitization to enable JavaScript execution when rendered.

## Description

The vulnerability stems from the question text being inserted into HTML without proper escaping, allowing attribute breakout and event handler injection. The payload `asdf"><img src=x onerror=prompt(1)>` uses a benign string to pad, closes the attribute with `">`, and injects an `<img>` tag with an `onerror` event that fires due to the invalid `src=x`, executing `prompt(1)`. This executes in the DOM context of the presentation page for all viewers.

## Requirements

1. Access to the Quick question input field in an active presentation
2. Knowledge of basic HTML/JavaScript for payload crafting
3. Multi-browser setup to test propagation

## Defense

Defensive measures and detection strategies:

- Enforce strict input validation and HTML escaping on all user-supplied content
- Use libraries like DOMPurify for sanitization in client-side rendering
- Scan for event handler patterns (e.g., onerror) in logged inputs

## Objectives

1. Deliver a payload that evades basic filtering and breaks HTML context
2. Ensure the injection renders in the presentation view
3. Prepare for cross-user execution confirmation

## Instructions

### Step 1: Enter the Payload

**Context**: Input the malicious string directly into the question field to exploit the reflection.

Type or paste `asdf"><img src=x onerror=prompt(1)>` into the question text box and submit or proceed.

### Step 2: Submit and Render

**Context**: Trigger the rendering of the question in the session to activate the payload.

Click to display the question in the presentation; observe how the input is reflected without sanitization.

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
- [[payload]]
- [[injection]]
- [[JavaScript]]
