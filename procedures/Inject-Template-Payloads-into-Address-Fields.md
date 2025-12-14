---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - template-injection
  - angularjs
  - xss
type: procedure
tools:
  - '[[tools/PortSwigger-Web-Security-Research]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - WordPress
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.715Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-Template-Payloads-into-Address-Fields

## Summary

This procedure injects simple AngularJS template expressions into billing and shipping address fields during account editing, exploiting lack of sanitization to enable client-side evaluation.

## Description

User-controlled address fields in /my-account/edit-address/ are rendered via AngularJS templates on checkout without proper escaping, allowing {{ }} expressions to execute. Start with benign payloads like {{1+1}} to confirm injection without alerting defenses. This targets the root cause of unsanitized output in dynamic rendering.

## Requirements

1. Authenticated session with editable addresses
2. Knowledge of AngularJS syntax for templates
3. Access to /my-account/edit-address/

## Defense

Defensive measures and detection strategies:

- Sanitize inputs to remove {{ }} patterns before storage
- Use AngularJS's $sce service for strict contextual escaping on output
- Implement Content Security Policy (CSP) to block inline JS

## Objectives

1. Store injectable payloads in address fields
2. Confirm no server-side validation blocks expressions
3. Prepare for evaluation testing on checkout

## Instructions

### Step 1: Navigate to Address Edit

**Context**: Access the form for billing and shipping details.

Go to https://mercantile.wordpress.org/my-account/edit-address/ and select billing or shipping tab.

> Clear existing fields if needed.

### Step 2: Inject Payloads

**Context**: Enter template expressions in all relevant fields except zip code.

For billing: Enter '{{1+1}}' in address line 1, city, state, etc. For shipping: Enter '{{1==1}}' similarly. Leave zip as numeric.

> Click save changes.

### Step 3: Verify Save

**Context**: Ensure payloads are stored without modification.

Reload the edit page to check if inputs persist.

> Expected: Payloads visible in form fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/PortSwigger-Web-Security-Research]]

## Tags

- [[template-injection]]
- [[angularjs]]
- [[xss]]
