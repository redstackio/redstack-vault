---
id: proc-create-account
tags:
  - account-creation
  - authentication
  - readme-io
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
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:29:57.375Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Create-and-Verify-ReadMe-io-Account

## Summary

This procedure creates a standard user account on ReadMe.io, verifies it via email, and logs in to obtain necessary session artifacts like cookies and XSRF tokens for authenticated API interactions.

## Description

To interact with ReadMe.io's dashboard and API, an authenticated session is required. Sign up using a valid email, complete verification, and login. This establishes a legitimate user context that can be leveraged for the invite bypass. The target environment is the web-based ReadMe.io platform. Prerequisites include a disposable email service. Expected outcomes: Active session with tokens for subsequent requests.

## Requirements

1. Valid email address for verification
2. Web browser for signup and login
3. Access to ReadMe.io signup page (https://readme.io)

## Defense

Defensive measures and detection strategies:

- Rate-limit account creations and verifications
- Monitor for bulk signup patterns
- Require CAPTCHA on registration

## Objectives

1. Obtain authenticated access to ReadMe.io dashboard
2. Capture session cookies and CSRF tokens
3. Prepare for API exploitation under a valid user context

## Instructions

### Step 1: Sign Up for Account

**Context**: Create a new user account to initiate authentication.

No command; browser-based:

1. Visit https://readme.io and click 'Sign Up'
2. Provide email, password, and complete registration form

> Registration success redirects to verification prompt.

### Step 2: Verify Email and Login

**Context**: Confirm account ownership and establish session.

No command; email and browser:

1. Check email for verification link and click it
2. Return to ReadMe.io and log in with credentials
3. Use DevTools (Network tab) to capture Cookie and X-XSRF-TOKEN from login response

> Successful login grants dashboard access; tokens are set in browser storage.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[External Remote Services]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[web]]

