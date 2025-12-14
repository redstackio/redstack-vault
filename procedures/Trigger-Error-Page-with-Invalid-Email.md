---
tags:
  - error-trigger
  - input-validation
  - xss-setup
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:15:53.206Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 55b44e90-1796-4a51-9eb3-d5d7d5ce60b7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trigger-Error-Page-with-Invalid-Email

## Summary

This procedure demonstrates how to input an invalid email address during the RelateIQ MS Exchange connection to elicit an error page that reflects user input, revealing the lack of sanitization and priming for XSS payload injection.

## Description

Targeting the email connection form in the registration flow, this step uses a fabricated email to force an authentication or validation failure. The application's error handling echoes the input without proper escaping, creating an opportunity for reflected XSS. This is performed in a standard browser session on the web platform, with outcomes including the display of additional form fields like 'Override Endpoint Address'.

## Requirements

1. Active session on the email connection form from prior steps
2. Knowledge of basic email format to craft invalid inputs
3. Browser developer tools for inspection (optional)

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs in error messages
- Use parameterized queries or validation libraries to handle form submissions
- Log and alert on repeated failed connection attempts

## Objectives

1. Generate a reflected error response to identify the vulnerability
2. Expose additional input fields for payload placement
3. Confirm the reflection mechanism without triggering defenses

## Instructions

### Step 1: Input Invalid Email

**Context**: Use the email field to submit data that will fail validation and trigger reflection.

Enter a random invalid email, such as 'invalid@example.com', and click 'Connect email'.

> The form submits, and an error page loads reflecting the input. Expected output: Error message with echoed email and new fields.

### Step 2: Verify Reflection

**Context**: Inspect the error page to ensure input is unsanitized.

View the source or rendered page to confirm the email value appears in HTML without encoding.

> This validates the vulnerability. Expected output: Raw input visible in the DOM.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- error-trigger
- input-validation
- xss-setup
