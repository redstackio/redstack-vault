---
id: proc-002
tags:
  - xss-injection
  - payload-testing
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:27:15.888Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject XSS Payload in First Name Field

## Summary

This procedure tests for self-XSS by manually injecting a JavaScript payload into the 'first_name' form field, exploiting insufficient sanitization to allow script execution upon reflection.

## Description

The attack targets the 'first_name' parameter in the web form, where inputs are not properly escaped. By entering a payload that breaks out of string context and injects a script tag, the procedure confirms vulnerability. This is performed manually in the browser, with outcomes visible on form submission.

## Requirements

1. Access to the loaded form page from the previous procedure
2. Browser allowing direct input manipulation
3. Knowledge of basic XSS payloads

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all user inputs (e.g., using HTML entity encoding)
- Implement Content Security Policy (CSP) to block inline scripts
- Log and alert on suspicious input patterns in form fields

## Objectives

1. Insert executable JavaScript without rejection
2. Break out of input context for reflection
3. Set up for self-XSS confirmation

## Instructions

### Step 1: Locate Input Field

**Context**: Focus on the vulnerable 'first_name' field.

Click into the 'First Name' input box on the form.

> Ensure no auto-complete or validation interferes.

### Step 2: Enter Payload

**Context**: Inject the self-XSS payload to test execution.

Type or paste `test"; <script>alert(document.cookie)</script>` into the field.

> The payload uses a semicolon to close any string and injects a script tag; observe if it's accepted verbatim.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-injection]]
- [[payload-testing]]
