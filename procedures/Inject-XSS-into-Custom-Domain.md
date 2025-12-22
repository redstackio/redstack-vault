---
tags:
  - xss
  - stored-xss
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/javascript-alert-domain]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.667Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c1188d6c-b89b-413e-9202-78f361a4f5b5
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-into-Custom-Domain

## Summary

This procedure injects a javascript: payload into the Custom Domain field of the Federalist site settings, exploiting lack of sanitization to store XSS that executes in the admin context upon interaction.

## Description

The Custom Domain field in Federalist (/sites/<siteid>/settings) accepts user input without validating against javascript: protocols. By entering a payload like 'javascript:alert(document.domain)', an attacker stores malicious code that triggers when an admin clicks 'View Website', executing JS in the high-privilege admin domain. This can lead to session theft or further attacks on other users.

## Requirements

1. Authenticated admin session from prior login.
2. Access to site settings page.
3. Knowledge of target site ID.

## Defense

Defensive measures and detection strategies:

- Sanitize all input fields to strip or escape javascript: protocols and other XSS vectors.
- Implement Content Security Policy (CSP) to restrict script execution from user-controlled sources.
- Log and monitor unusual inputs in admin fields for javascript: patterns.

## Objectives

1. Store XSS payload in Custom Domain without detection.
2. Ensure payload executes on 'View Website' interaction.
3. Enable arbitrary JS for data theft or CSRF bypass.

## Instructions

### Step 1: Locate Custom Domain Field

**Context**: Identify the input field in the site settings form.

Navigate to http://localhost:1337/sites/<siteid>/settings and find the Custom Domain input.

> Expected output: Empty or existing domain field ready for input.

### Step 2: Enter XSS Payload

**Context**: Inject the javascript: payload to test execution.

**Command** ([[commands/javascript-alert-domain]]):
```javascript
javascript:alert(document.domain)
```

> Paste this into the Custom Domain field. Expected output: Payload accepted without validation error; no immediate execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/javascript-alert-domain]]

## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[JavaScript]]
