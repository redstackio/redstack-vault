---
tags:
  - xss
  - self-xss
  - web
  - uber
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.274Z'
sub_techniques: []
id: b7bb57b4-af94-48f2-ae33-5569418350c4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Showing-Password

## Summary

This procedure triggers the self-XSS by clicking 'Show password', causing the app to render the injected script and execute JavaScript in the browser.

## Description

Post-submission, the 'Show password' feature displays the stored password in an unsafe context (e.g., innerHTML), parsing and running the script. Limited to self-XSS as it affects only the current session. Requires successful injection. Outcome: Alert or console execution confirming vuln.

## Requirements

1. Password set with payload
2. Access to show password UI element
3. Browser with JS enabled

## Defense

Defensive measures and detection strategies:

- Escape output when displaying passwords (use textContent instead of innerHTML)
- Avoid rendering user input as HTML in UI components

## Objectives

1. Execute the injected JavaScript
2. Verify XSS impact
3. Demonstrate vulnerability proof-of-concept

## Instructions

### Step 1: Activate Show Password

**Context**: Interact with the UI to reveal and execute the payload.

No command; UI click:

```plaintext
Click: Show password button
```

> Alert pops up with domain. Check dev tools for execution.

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
- [[self-xss]]
- [[web]]
- [[uber]]
