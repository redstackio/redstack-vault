---
id: proc-inject-payload-registration
tags:
  - xss-injection
  - payload
  - registration-exploit
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
updated_at: '2025-12-14T03:15:41.664Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-in-Registration

## Summary

This procedure details creating a user account while injecting a stored XSS payload into the name and last name fields of a web application's registration form, exploiting lack of input sanitization to store malicious JavaScript.

## Description

Targeted at CGI-based web apps like the DoD application, this step involves submitting a form with a payload such as an onerror image tag that executes JavaScript on render. The payload is stored in the backend database and later rendered unsanitized on profile pages (e.g., myaccount.cgi). Prerequisites include access to the registration form. Outcomes: Payload persistence, setting up for execution on victim views.

## Requirements

1. Valid email or other registration details (excluding name fields)
2. Knowledge of simple XSS payloads (e.g., no advanced evasion needed here)
3. Browser session from previous access step

## Defense

Defensive measures and detection strategies:

- Sanitize and HTML-escape all user inputs before storage (e.g., use libraries like DOMPurify)
- Validate input lengths and characters on server-side for name fields
- Scan registration logs for suspicious strings like <script> or onerror

## Objectives

1. Store unsanitized JavaScript in user profile data
2. Bypass any client-side validation
3. Enable execution for any authenticated user viewing the profile

## Instructions

### Step 1: Fill Registration Form

**Context**: Enter legitimate details but replace name/last name with payload to test storage.

No command; manual form submission:

In the name field, input: `<IMG SRC=X ONERROR=ALERT(1)>`

Complete other fields (email, password) and submit the form.

> Submission succeeds if no server-side blocks; payload is now stored.

### Step 2: Confirm Account Creation

**Context**: Verify the account is active post-submission.

Check for success message or email confirmation.

> If redirected to login, the injection phase is complete.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-injection]]
- [[payload]]
- [[registration-exploit]]
