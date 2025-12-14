---
id: proc-uuid-2
tags:
  - xss
  - user-interaction
type: procedure
tools:
  - '[[tools/Firefox]]'
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
updated_at: '2025-12-13T23:52:24.821Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Interact-with-Overlaid-Form-Elements

## Summary

This procedure simulates user interaction with decoy elements in the clickjacking PoC to populate hidden form fields on the vulnerable page with a malicious JavaScript payload, preparing for XSS execution.

## Description

By dragging visual decoys (e.g., frog images) in the PoC, the procedure maps mouse events to input values in the iframe's form fields for 'triager' and 'hacker'. The payload, such as '<script>alert("XSS")</script>', is injected without escaping. This targets browsers rendering the PoC and requires the iframe to be interactive. Prerequisites include the loaded PoC from the prior step.

## Requirements

1. Loaded clickjacking PoC in browser
2. Payload prepared in form fields via overlay mapping
3. Victim unaware of underlying form

## Defense

Defensive measures and detection strategies:

- Use pointer-events: none on sensitive elements or detect overlay attempts
- Validate input lengths and content before processing
- Browser extensions to warn of clickjacking

## Objectives

1. Populate form fields with unsanitized payload
2. Maintain user deception through visual interaction
3. Prepare for form submission

## Instructions

### Step 1: Align Decoy Elements

**Context**: Drag the frog elements to simulate input, which sets the value of hidden inputs to the payload.

No command; perform mouse drag action on the PoC.

> Dragging Frog 1 to the other frogs updates document.getElementById('triager').value and document.getElementById('hacker').value with the injected script tag.

### Step 2: Validate Input Injection

**Context**: Use dev tools to confirm payload in form fields.

Inspect the iframe's DOM to see the values set without escaping.

> Expected: Fields contain <script>alert('XSS')</script> or similar.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[user-interaction]]
