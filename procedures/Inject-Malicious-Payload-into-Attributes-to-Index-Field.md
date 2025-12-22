---
tags:
  - xss
  - payload-injection
  - javascript
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
updated_at: '2025-12-13T23:52:39.113Z'
sub_techniques: []
id: 75cd311b-bc68-4409-9132-5dab0b68d91b
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Attributes-to-Index-Field

## Summary

This procedure involves entering a malicious JavaScript payload into the 'Attributes to index' field of Algolia's ranking tab to exploit the Stored XSS vulnerability, bypassing any client-side validation.

## Description

The 'Attributes to index' field accepts user input without proper HTML escaping, allowing injection of script tags or event handlers. The payload used is `"><img src=x onerror=prompt('XSS');>`, which closes the attribute and injects an img tag with an onerror event that executes JavaScript. This step targets the web interface directly via browser interaction, with the outcome being the payload staged for storage and later execution on page loads.

## Requirements

1. Active session in the Algolia explorer ranking tab
2. Web browser developer tools (optional, for inspection)
3. Knowledge of basic JavaScript payloads

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding
- Implement Content Security Policy (CSP) to block inline scripts
- Log and alert on suspicious input patterns like <script> or onerror

## Objectives

1. Successfully input the payload without rejection
2. Confirm the field accepts HTML/JavaScript constructs
3. Set up for persistence in the next save step

## Instructions

### Step 1: Locate the Vulnerable Field

**Context**: Identify the input field susceptible to injection within the ranking tab.

**Action**:

Scroll to or click on the 'Attributes to index' input field in the ranking configuration section.

> The field should be a text input or textarea allowing multi-line or special character entry.

### Step 2: Enter the Payload

**Context**: Type the exact payload to exploit the lack of sanitization.

**Action**:

Paste or type `"><img src=x onerror=prompt('XSS');>` into the field and press Enter or Tab to submit.

> This injects the payload by breaking out of the attribute context; inspect the DOM if needed to verify injection.

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
- [[payload-injection]]
- [[JavaScript]]
