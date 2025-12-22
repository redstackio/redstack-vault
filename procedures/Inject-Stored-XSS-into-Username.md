---
id: proc-uuid-2
tags:
  - xss
  - stored-xss
  - client-side-bypass
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
updated_at: '2025-12-14T17:27:42.625Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-into-Username

## Summary

This procedure bypasses client-side validation on the username change form to inject and store an XSS payload that executes when profiles are viewed.

## Description

The vulnerability stems from client-side only checks limiting usernames to 8-20 alphanumeric characters. Using browser dev tools, the maxlength is altered to inject HTML/JS like `"><img src onerror=confirm(document.cookie)>`. The payload stores in the database without sanitization and triggers on profile views.

## Requirements

1. Authenticated session
2. Browser with developer console (e.g., Chrome DevTools)
3. Access to username change form

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and sanitization (e.g., escape HTML)
- Use Content Security Policy (CSP) to block inline scripts
- Log and monitor unusual username changes

## Objectives

1. Store malicious payload in username
2. Ensure payload evades client-side checks
3. Enable execution on profile view

## Instructions

### Step 1: Access Username Change Form

**Context**: Navigate to the profile settings.

Click on 'Change username' button after logging in.

> Expected: Form with new username and confirm fields appears.

### Step 2: Bypass Validation with DevTools

**Context**: Modify input attributes to allow longer payloads.

Right-click input fields, inspect element, change `maxlength="20"` to `maxlength="100"` in the HTML.

> Expected: Input now accepts longer text without restriction.

### Step 3: Enter and Submit Payload

**Context**: Inject the XSS payload.

Enter `"><img src onerror=confirm(document.cookie)>` in both new and confirm fields, then submit.

> Expected: Form submits successfully, username updated.

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
- [[stored-xss]]
