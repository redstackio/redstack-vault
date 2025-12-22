---
id: 00000000-0000-0000-0000-000000000003
tags:
  - xss-injection
  - payload-delivery
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
updated_at: '2025-12-14T00:11:09.564Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Stored-XSS-Payload-in-Full-Name

## Summary

This procedure details the injection of a malicious JavaScript payload into the full name field of the 8x8 registration form, exploiting lack of input sanitization to store executable code in the backend database.

## Description

The 8x8 web application at https://www.easycontactnow.com/ fails to sanitize or escape user input in the full name field during registration, allowing HTML and JavaScript to be persisted. This procedure uses a simple alert payload to demonstrate, but in real attacks, it could be escalated to steal sessions or data. Prerequisites include access to the registration form from the previous procedure. The outcome is the payload stored and ready for execution on dashboard load.

## Requirements

1. Access to the registration form
2. Valid details for other fields (email, password)
3. Knowledge of basic JavaScript payloads

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding (e.g., &lt; for <)
- Use Content Security Policy (CSP) to restrict script execution
- Validate input server-side to reject script tags
- Log and monitor anomalous input patterns like <script>

## Objectives

1. Deliver persistent JavaScript via unsanitized field
2. Store payload in backend without detection
3. Set up for execution in authenticated contexts

## Instructions

### Step 1: Prepare Payload

**Context**: Craft the XSS payload to break out of the input context and inject script.

Use the payload: `'><script>alert(1)</script>`

> This closes any open attributes/tags and injects a script tag.

### Step 2: Input Payload

**Context**: Submit the malicious input during registration.

Enter the payload in the full name field, complete other fields, and submit.

> Form submission succeeds, triggering email confirmation.

### Step 3: Validate Storage

**Context**: Ensure the payload is stored by proceeding to login (detailed in next procedure).

No immediate visual confirmation; storage is backend-only.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-injection
- payload-delivery
