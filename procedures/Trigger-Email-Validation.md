---
id: proc-trigger-email-validation
tags:
  - email-validation
  - xss-trigger
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
updated_at: '2025-12-13T23:55:20.751Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Email-Validation

## Summary

This procedure activates the email validation process on the target site's account page, sending a request to the controlled SMTP server and causing the XSS payload to be injected via the rejection error message.

## Description

After account creation, accessing the /account/email route and clicking the validation link prompts the site to send an email to the invalid address. The Postfix server rejects it, returning the error with the embedded XSS payload, which the site stores and later renders unsanitized on the page.

## Requirements

1. Logged-in account with invalid email
2. Access to /account/email page
3. Running SMTP server configured for rejection

## Defense

Defensive measures and detection strategies:

- Sanitize SMTP bounce/error messages before storage or display
- Implement email verification timeouts or blacklisting for repeated failures
- Audit validation endpoints for injection risks

## Objectives

1. Primary objective: Deliver XSS payload through SMTP interaction
2. Secondary objective: Store payload in site's bounce history
3. Expected outcome: Payload processed but not immediately executed

## Instructions

### Step 1: Access Email Management Page

**Context**: Log in and navigate to email settings.

**Instructions**: Go to /account/email after login.

**Expected Output**: Page shows unvalidated email with validation button.

### Step 2: Initiate Validation

**Context**: Trigger the email send to invoke SMTP rejection.

**Instructions**: Click 'Please click Here to validate it'.

**Expected Output**: Request sent; page may show temporary message, but no alert yet.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- email-validation
- xss-trigger
