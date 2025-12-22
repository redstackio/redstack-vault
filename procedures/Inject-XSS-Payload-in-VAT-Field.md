---
tags:
  - xss-injection
  - payload
  - self-xss
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
updated_at: '2025-12-14T03:15:26.677Z'
sub_techniques: []
id: a0f594d7-bc00-4f24-85d0-6bcdf4331b50
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-VAT-Field

## Summary

This procedure involves entering a crafted XSS payload into the VAT number input field of the Uber Partners Profile page to test for stored self-XSS vulnerability.

## Description

The VAT number field lacks proper sanitization, allowing HTML and JavaScript injection. The payload `'><img src=x onerror=alert(0)> "><img src=x onerror=alert(0)> <script>alert(0)</script>` breaks out of the input context and injects executable code. This is a self-XSS as it only affects the injecting user's session when viewing the profile. Prerequisites: Access to the edit page.

## Requirements

1. Profile edit page loaded
2. VAT number field visible and editable
3. Knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Sanitize inputs with HTML entity encoding on output
- Use Content Security Policy (CSP) to block inline scripts
- Validate VAT numbers against expected format (e.g., regex for numeric/alpha patterns)

## Objectives

1. Insert executable JavaScript without rejection
2. Break out of input context using HTML attributes
3. Prepare payload for storage and later execution

## Instructions

### Step 1: Locate VAT Number Field

**Context**: Identify the target input field on the profile edit form.

No command required; scroll to or search for the 'VAT Number' label and focus on its input box.

> The field should be a text input type.

### Step 2: Enter the Payload

**Context**: Type the XSS payload to inject script execution.

No command required; paste or type: `'><img src=x onerror=alert(0)> "><img src=x onerror=alert(0)> <script>alert(0)</script>` into the field.

> The payload should display in the field without truncation or auto-escape.

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
- payload
