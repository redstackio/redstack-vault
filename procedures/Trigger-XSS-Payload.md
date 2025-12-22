---
tags:
  - xss-execution
  - javascript
type: procedure
tools:
  - '[[tools/Firefox-ESR]]'
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
updated_at: '2025-12-14T03:46:31.269Z'
sub_techniques: []
id: ab1ee2d3-63ce-4076-a1ff-a7c4669daaf2
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Payload

## Summary

This procedure triggers the stored XSS by hovering over the malicious filename in the browser's directory listing, executing the injected JavaScript and confirming arbitrary code execution.

## Description

The payload uses onmouseover=alert(1) to fire when the mouse hovers over the link, running in the browser's context. This demonstrates the vulnerability's impact, such as potential phishing or keylogging in real attacks.

## Requirements

1. Directory listing loaded in browser
2. Malicious filename visible
3. Interactive browser session

## Defense

Defensive measures and detection strategies:

- Implement strict XSS filters on all outputs
- Educate users on avoiding suspicious file shares
- Use browser sandboxing and no-script extensions

## Objectives

1. Execute the JavaScript payload client-side
2. Verify XSS success with alert
3. Highlight risks like session theft

## Instructions

### Step 1: Interact with the Filename

**Context**: Hover the mouse cursor over the malicious filename in the listing to activate the event handler.

No command; perform mouse hover in [[tools/Firefox-ESR]].

> Expected output: A pop-up alert box showing "1". Console may log errors if CSP is present, but in vulnerable setup, it executes cleanly.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-ESR]]

## Tags

- xss-execution
- javascript
