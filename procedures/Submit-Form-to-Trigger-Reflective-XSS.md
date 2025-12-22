---
tags:
  - xss
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.438Z'
sub_techniques: []
id: 04714388-0e50-4d1f-9f7f-4de7c1a0e50a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Submit-Form-to-Trigger-Reflective-XSS

## Summary

This procedure covers submitting the form with the injected payload, causing the server to reflect it unsanitized and execute the JavaScript in the browser context.

## Description

Upon submission, the form handler echoes the company field back in the response without escaping, rendering the SVG element and firing the onload event. This executes `confirm(document.domain)`, proving arbitrary code execution. The absence of CSRF tokens amplifies risk for crafted attacks.

## Requirements

1. Form populated with payload from previous step
2. No additional tools beyond browser
3. Understanding of response inspection

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens to prevent unauthorized submissions
- Output encoding (e.g., HTML entity encoding) for reflected fields
- Monitor for XSS payloads in form submissions via logging

## Objectives

1. Trigger reflection and execution
2. Confirm vulnerability impact
3. Demonstrate potential for broader attacks

## Instructions

### Step 1: Submit the Form

**Context**: Initiate the POST request to the server to reflect the payload.

No command required; click the 'Get your copy now' submit button on the form.

> The response loads, reflecting the payload, and a confirmation alert displays the domain, indicating successful XSS execution.

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
- execution
