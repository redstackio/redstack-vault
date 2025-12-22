---
tags:
  - xss
  - trigger
  - stored-xss
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
updated_at: '2025-12-14T03:16:14.505Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 025f05ba-abd4-414c-b08b-e27607a90a11
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-on-Fuel-Cards-Enrollment-Page

## Summary

This procedure navigates to the fuel cards enrollment page where the stored address from the user profile is reflected without sanitization, causing the injected XSS payload to execute in the browser.

## Description

The vulnerability stems from insufficient output encoding on https://partners.uber.com/fuel_cards/enroll, which renders the user's stored address directly into the HTML. When visited post-injection, this leads to arbitrary JS execution in the context of the authenticated session, enabling further exploitation.

## Requirements

1. Previously injected payload in profile
2. Active browser session
3. Access to the enrollment URL

## Defense

Defensive measures and detection strategies:

- Encode user inputs on output (e.g., htmlspecialchars in PHP)
- Audit reflected fields for user-controlled content
- Implement XSS auditors in web proxies

## Objectives

1. Load the page to reflect the stored payload
2. Achieve JS execution context
3. Confirm vulnerability for chaining

## Instructions

### Step 1: Navigate to Enrollment Page

**Context**: Visit the specific URL to trigger reflection of the address field.

**Command** ([[No Command]]):

Directly access https://partners.uber.com/fuel_cards/enroll in the browser.

> Expected: Page loads, and address content (with payload) appears in the DOM, inspectable via DevTools.

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
- trigger
