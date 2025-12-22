---
id: uuid-inject-payload
tags:
  - xss
  - injection
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
updated_at: '2025-12-14T03:15:35.830Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Owners-Name

## Summary

This procedure injects a JavaScript payload into the direct debit owner's name field, exploiting the lack of input sanitization to store malicious code.

## Description

The owner's name field in the mandate form allows arbitrary input, including HTML and script tags, without escaping. The payload `asdf'><script>alert(document.cookie)</script>` breaks out of the string context and executes JavaScript when reflected. This is a classic stored XSS setup targeting user-facing pages.

## Requirements

1. Access to the direct debit form (from previous procedure)
2. Knowledge of XSS payloads
3. Browser developer tools to verify input

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding
- Use Content Security Policy (CSP) to block inline scripts
- Log and alert on suspicious input patterns like <script>

## Objectives

1. Insert executable JavaScript into the name field
2. Ensure payload evades basic validation
3. Set up for storage and reflection

## Instructions

### Step 1: Enter Payload

**Context**: Locate and fill the owner's name field with the crafted payload.

**Instructions**: In the form, type or paste `asdf'><script>alert(document.cookie)</script>` into the owner's name input field.

> The field should accept the input without truncation or errors. Use browser dev tools to inspect if needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- injection
