---
tags:
  - password-reset
  - uber
  - web
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:15:47.286Z'
sub_techniques: []
id: 4a89c68e-69e4-404c-bfb0-cea44bbcc925
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Uber-Password-Reset-Page

## Summary

This procedure opens the Uber password reset form using the link received via email, providing access to the vulnerable input fields for payload injection.

## Description

Following the password reset request, this step involves clicking the emailed URL to load the reset form in the browser. The form includes fields for entering a new password and a 'show password' toggle. This is crucial for the self-XSS attack as it exposes the unsanitized password display. The target is the Uber partners portal, and the outcome is a loaded form ready for manipulation. No authentication is needed beyond the reset token in the URL.

## Requirements

1. Valid password reset email with clickable URL
2. Web browser
3. Internet access

## Defense

Defensive measures and detection strategies:

- Token expiration and one-time use for reset links
- Logging of reset page accesses
- CAPTCHA on repeated failed resets

## Objectives

1. Load the password reset form
2. Verify form elements are present
3. Set up for payload entry

## Instructions

### Step 1: Open Reset Email

**Context**: Locate and access the reset link.

Check the email inbox for the Uber reset notification.

> The email contains a secure URL valid for a short time (e.g., 15 minutes).

### Step 2: Click and Load Form

**Context**: Navigate to the reset page.

Click the provided URL to open the password reset form.

> The browser loads the form with new password input and confirmation fields, plus the 'show password' option.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-reset]]
- [[uber]]
- [[web]]
