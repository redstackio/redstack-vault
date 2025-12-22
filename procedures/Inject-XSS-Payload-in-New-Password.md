---
tags:
  - xss
  - self-xss
  - payload-injection
  - uber
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 845b9594-6d05-4080-ba56-3518c1505906
created_at: '2025-12-14T03:15:26.595Z'
updated_at: '2025-12-14T03:15:26.596Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-New-Password

## Summary

This procedure details how to inject a JavaScript XSS payload into the new password field during Uber's password reset process, exploiting insufficient sanitization to reflect the payload back for execution.

## Description

Targeted at the https://partners.uber.com/reset-password page, this step involves entering a crafted payload like "><img src=x onerror=prompt(document.domain)>" into the new password input. The lack of proper escaping allows the payload to break out of the input context and execute JavaScript upon form submission. This is a classic reflected Self-XSS, affecting only the submitter's session. Prerequisites include completing the password reset initiation.

## Requirements

1. Access to the password reset form from the previous procedure
2. Knowledge of basic XSS payloads
3. Web browser developer tools for inspection (optional)

## Defense

Defensive measures and detection strategies:

- Sanitize and escape all user inputs, especially in password fields, using HTML entity encoding
- Implement Content Security Policy (CSP) to restrict inline script execution
- Log and monitor form submissions for suspicious input patterns like script tags

## Objectives

1. Deliver the XSS payload to the server via the form
2. Ensure the payload is reflected without alteration
3. Set up for immediate execution on submission

## Instructions

### Step 1: Locate Input Field

**Context**: Identify the vulnerable new password field on the form.

Inspect the reset password page to find the input element for the new password (typically an HTML <input type="password">).

> Use browser dev tools (F12) to confirm the field name, e.g., 'newPassword'.

### Step 2: Enter Payload

**Context**: Craft and input the XSS payload to exploit reflection.

Type the following payload into the new password field: "><img src=x onerror=prompt(document.domain)>"

> This payload closes the input tag, injects an img element, and uses onerror to execute JS. Adjust if a confirm password field exists by entering a matching value.

### Step 3: Submit Form

**Context**: Trigger the reflection by submitting the payload to the server.

Click the submit or reset button on the form.

> The server echoes the input back in the response, potentially without sanitization, leading to execution.

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
- self-xss
- payload-injection
