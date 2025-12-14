---
tags:
  - account-creation
  - initial-access
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:38.179Z'
sub_techniques: []
id: 0ac55bff-c136-45d8-afb4-20ed51a4a642
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Temporary-Account-on-Informatica-Registration

## Summary

This procedure establishes initial access by registering a new temporary account on the Informatica Cloud platform, setting the stage for injecting a stored XSS payload without requiring existing credentials.

## Description

The Informatica account registration form at https://accounts.informatica.com/registration.html allows public sign-ups with minimal validation. By creating an account, an attacker can store user-supplied input, such as in the Company field, which is later displayed unsanitized in the admin panel. This procedure focuses on the registration step, using arbitrary details to avoid detection while ensuring the account is created successfully. Expected outcomes include a new user ID that can be targeted by admins during routine reviews.

## Requirements

1. Web browser with internet access
2. Valid email address for registration (can be temporary)
3. No prior authentication needed

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or rate limiting on registration forms
- Monitor for anomalous registrations (e.g., suspicious company names)
- Log all new account creations with IP tracking

## Objectives

1. Create a persistent user record for payload storage
2. Avoid triggering any immediate validation errors
3. Position the account for admin visibility

## Instructions

### Step 1: Navigate to Registration Page

**Context**: Access the public registration endpoint to begin the process.

No command required; use a browser to visit https://accounts.informatica.com/registration.html.

> Fill in basic fields: Name, Email, Password. Leave Company field for next step.

### Step 2: Submit Registration Form

**Context**: Complete the form submission to generate the user record.

No command required; click 'Register' after entering details.

> Expected output: Success message and email verification link (optional; proceed without if possible).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[initial-access]]
