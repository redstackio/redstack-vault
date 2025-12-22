---
tags:
  - xss
  - injection
  - payload
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 318ceb13-b59f-4b80-915a-96666211fc36
created_at: '2025-12-14T03:15:35.903Z'
updated_at: '2025-12-14T03:15:35.903Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Address-Fields

## Summary

This procedure involves manually entering a JavaScript payload into multiple address fields of the ExpressionEngine billing form to bypass sanitization and enable stored XSS execution upon later viewing.

## Description

Targeting the billing form at https://store.ellislab.com/billing, this step exploits insufficient input validation by injecting HTML-breaking payloads like `'><img src=x onerror=prompt(0);>` into fields such as First Name, Last Name, Street Address, Apt/Suite/#, and City. The payload closes any enclosing tags and injects an onerror handler that executes JavaScript. Using invalid CVV can trigger error displays to test reflection. Prerequisites include access to the form from the prior checkout step; outcomes confirm payload acceptance for storage.

## Requirements

1. Active billing form session from cart checkout
2. Knowledge of basic XSS payloads
3. Web browser developer tools for inspection (optional)

## Defense

Defensive measures and detection strategies:

- Enforce strict input sanitization using HTML entity encoding on all form fields
- Implement Content Security Policy (CSP) to block inline script execution
- Log and WAF-block suspicious inputs containing script tags or event handlers

## Objectives

1. Inject payload to break out of HTML context
2. Ensure multi-field injection for higher success rate
3. Validate payload acceptance without form rejection

## Instructions

### Step 1: Enter Payload in Name and Address Fields

**Context**: Populate vulnerable fields to store the malicious script.

In First Name, Last Name, Street Address, Apt/Suite/#, and City fields, input: `'><img src=x onerror=prompt(0);>`.

> This payload uses an invalid image source to trigger onerror, executing prompt(0) as a proof-of-concept alert.

### Step 2: Provide Partial Card Details

**Context**: Use invalid details to potentially reflect fields on error.

Enter valid card number and expiration but invalid CVV to submit and check for immediate reflection.

> If error page displays fields, inspect for unsanitized output confirming vulnerability.

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
