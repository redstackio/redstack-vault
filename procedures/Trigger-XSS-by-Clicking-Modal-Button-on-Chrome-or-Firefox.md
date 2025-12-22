---
id: proc-paypalme-xss-chrome-firefox-trigger
tags:
  - xss-execution
  - user-interaction
  - javascript
type: procedure
tools:
  - '[[tools/Chrome]]'
  - '[[tools/Firefox]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.029Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Clicking-Modal-Button-on-Chrome-or-Firefox

## Summary

This procedure triggers the reflected XSS payload by clicking the modal's 'X' button in Chrome or Firefox, executing the injected JavaScript to demonstrate domain access and potential for authenticated actions.

## Description

Following payload delivery, the modal buttons' hrefs contain the unsanitized javascript: URLs. Clicking 'X' or 'Done' navigates to these, executing the encoded SVG onload alert(document.domain). This exploits the lack of scheme validation, allowing code in paypal.com's context. Prerequisites include the prior navigation step; outcomes include proof-of-concept execution, extensible to data theft or session hijacking with interaction.

## Requirements

1. Modal loaded from previous procedure.
2. Chrome or Firefox with the page open.
3. User interaction capability (mouse click).

## Defense

Defensive measures and detection strategies:

- Escape special characters in href attributes (e.g., via HTML entity encoding).
- Deploy browser-based XSS auditors or WAF rules to block javascript: schemes.
- Log and alert on modal interactions with suspicious URLs.
- Enforce strict referrer policies to limit impact.

## Objectives

1. Execute arbitrary JavaScript via user-triggered href.
2. Confirm access to document.domain for impact validation.
3. Enable escalation to authenticated user actions.

## Instructions

### Step 1: Interact with Modal

**Context**: Click the tainted button to follow the injected href and trigger execution.

Locate the modal on the page and click the 'X' button.

> This executes: javascript:<svg onload=alert(document.domain)>' (decoded from payload).

**Expected Output**: Browser alert displays 'paypal.com', confirming execution.

### Step 2: Validate Execution

**Context**: Observe the alert to verify successful injection and context.

No additional input; the alert serves as validation.

**Expected Output**: No further modals or errors; payload runs silently post-alert if modified.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome]]
- [[tools/Firefox]]

## Tags

- [[xss-execution]]
- [[user-interaction]]
