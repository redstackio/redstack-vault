---
id: uuid-2
tags:
  - xss-injection
  - payload
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
updated_at: '2025-12-14T17:27:50.059Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Contact-Form

## Summary

This procedure involves filling the Nextcloud contact form with valid data and injecting JavaScript payloads into fields like message or company to test for reflected XSS.

## Description

User-supplied data in the contact form is not sanitized before being embedded in the HTML of the confirmation email. Injecting payloads such as event-handler based scripts allows arbitrary JS execution when the email source is viewed in a browser.

## Requirements

1. Access to the contact form page
2. Valid email address for form submission
3. Knowledge of XSS payload syntax

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding
- Validate form fields server-side to reject script tags or event handlers
- Monitor for anomalous form submissions

## Objectives

1. Bypass client-side validation if any
2. Ensure payload is accepted and will reflect in email
3. Set up for email-based execution

## Instructions

### Step 1: Enter Valid Data

**Context**: Provide legitimate values in required fields to ensure form acceptance.

Manually input data.

> In the name field, enter a valid name like "Test User". In the email field, enter your test email address, e.g., "test@example.com".

### Step 2: Inject Payload

**Context**: Place the XSS payload in non-required fields to avoid detection.

Use payloads targeting onload events.

> In the message or company field, enter: `<img src="x" onload=alert(document.cookie);>` or `<svg/onload=alert(document.cookie);>`. These will execute JS to alert cookies when rendered.

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
- [[injection]]
