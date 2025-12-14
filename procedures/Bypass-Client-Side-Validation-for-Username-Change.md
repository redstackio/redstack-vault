---
id: proc-uuid-2
name: Bypass-Client-Side-Validation-for-Username-Change
tags:
  - client-side-bypass
  - validation-bypass
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
updated_at: '2025-12-14T00:11:09.579Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass-Client-Side-Validation-for-Username-Change

## Summary

This procedure overrides browser-enforced input length validation on a username change form using developer tools, allowing injection of longer malicious payloads like XSS scripts.

## Description

Many web apps rely on client-side JavaScript for input validation (e.g., 8-20 characters), which can be bypassed by modifying DOM attributes. This targets forms without server-side checks, enabling storage of HTML/JS payloads that execute on profile views.

## Requirements

1. Authenticated session
2. Browser with developer tools (e.g., Chrome DevTools)
3. Access to username change page

## Defense

Defensive measures and detection strategies:

- Implement server-side validation and sanitization
- Use Content Security Policy (CSP) to block inline scripts
- Log and monitor unusual input lengths or patterns

## Objectives

1. Remove length restrictions on input fields
2. Enable payload injection
3. Store unsanitized data

## Instructions

### Step 1: Navigate to Username Change

**Context**: Access the form to be manipulated.

Click 'Change Username' in profile settings.

> Form loads with input fields for new and confirm username.

### Step 2: Modify Input Attributes

**Context**: Bypass max length via DOM inspection.

Open Inspect Element, find the input element (e.g., <input type="text" max="20">), change max to 100, and save.

> Input now accepts longer text; test by typing >20 chars.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- client-side-bypass
- validation-bypass
