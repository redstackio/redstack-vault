---
tags:
  - xss
  - trigger
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/javascript-alert-domain]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.661Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: aedf8b18-6898-43d9-b571-f5d07874d557
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Settings-and-Trigger-Custom-XSS

## Summary

This procedure saves the injected payloads in site settings and triggers the stored XSS from the Custom Domain by interacting with the 'View Website' button, executing JavaScript in the admin context.

## Description

After injection, submitting the form persists the malicious javascript: URI. Clicking 'View Website' interprets it as a navigation target, executing the payload. This runs in the admin domain, allowing theft of session cookies or CSRF token bypass for requests to attacker-controlled hosts.

## Requirements

1. Payloads injected in both domain fields.
2. Active admin session.
3. No client-side validation blocking save.

## Defense

Defensive measures and detection strategies:

- Server-side validation to reject javascript: URIs before storage.
- Escape outputs in links/buttons to prevent execution.
- Detect JS alerts or errors in admin logs.

## Objectives

1. Persist XSS for repeated execution.
2. Trigger arbitrary JS on interaction.
3. Demonstrate impact like domain alerting.

## Instructions

### Step 1: Submit Settings Form

**Context**: Save the configuration to store payloads.

Click the 'Save' button on the settings form.

> Expected output: Success message; settings updated in backend.

### Step 2: Trigger via View Website

**Context**: Interact to execute the stored payload.

**Command** ([[commands/javascript-alert-domain]]):
```javascript
javascript:alert(document.domain)
```

Click 'View Website'; it executes the payload.

> Expected output: Alert showing 'localhost' or admin domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/javascript-alert-domain]]

## Tools Used


## Tags

- [[xss]]
- [[trigger]]
- [[Execution]]
