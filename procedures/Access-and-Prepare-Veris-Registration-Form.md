---
id: 71ef7e32-6061-42a5-b276-1a3ba658f342
name: Access-and-Prepare-Veris-Registration-Form
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:23.395Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - csrf
  - web
  - recon
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Access-and-Prepare-Veris-Registration-Form

## Summary

This procedure involves navigating to the Veris registration page, filling out the form, and solving any CAPTCHA to prepare for intercepting the submission and testing CSRF token handling.

## Description

In the context of testing CSRF protections on unauthenticated endpoints like Veris's registration page (https://sandbox.veris.in/portal/register/), this step sets up the environment by accessing the page and completing the form. It targets Django-based applications where CSRF tokens are typically generated client-side but verified server-side. The expected outcome is a ready-to-submit form that can be intercepted to demonstrate weak token validation, where the server only checks token length (up to 32 characters) without cryptographic verification.

## Requirements

1. Direct internet access to https://sandbox.veris.in/portal/register/
2. A web browser configured to use a proxy like Burp Suite for traffic interception
3. Ability to solve CAPTCHA challenges manually

## Defense

Defensive measures and detection strategies:

- Implement strict CSRF token generation and validation using cryptographically secure tokens (e.g., Django's built-in CSRF middleware with proper secret key usage)
- Monitor for unusual proxy traffic or repeated form submissions from testing tools
- Enable logging of failed CSRF validations to detect bypass attempts

## Objectives

1. Gain access to the unauthenticated registration endpoint
2. Prepare form data for manipulation during submission
3. Identify any client-side CSRF token generation

## Instructions

### Step 1: Navigate to Registration Page

**Context**: Load the target endpoint to inspect the page and confirm CSRF token presence in the form.

No specific command; use browser to visit https://sandbox.veris.in/portal/register/ and observe the form fields including csrfmiddlewaretoken.

> The page should load with a registration form containing fields for user details and a hidden csrfmiddlewaretoken input.

### Step 2: Fill Form and Solve CAPTCHA

**Context**: Complete the form to simulate a legitimate submission, enabling interception of the full request.

Manually enter details like username, email, password, and solve the CAPTCHA.

> Form submission is paused at the proxy for the next procedure; success is indicated by no client-side errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[web]]
- [[recon]]
