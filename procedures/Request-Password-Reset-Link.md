---
id: proc-17512-request-reset
tags:
  - password-reset
  - token-generation
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
updated_at: '2025-12-14T17:33:06.452Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Request Password Reset Link

## Summary

This procedure triggers a password reset for a target email, generating a URL with a reset token that can be intercepted or observed for brute forcing.

## Description

Web platforms like HackerOne allow password resets via email, producing a token-laden URL. This step submits the request to obtain the initial token format, exploiting the system's response to valid emails. Prerequisites include a valid email; outcomes yield a URL like https://hackerone.com/users/password/edit?reset_password_token=...

## Requirements

1. Valid target email from enumeration
2. Access to the password reset form
3. Ability to submit POST requests (browser or tool)

## Defense

Defensive measures and detection strategies:

- Require CAPTCHA on reset requests
- Log and rate limit reset attempts per IP/email
- Use short-lived, high-entropy tokens

## Objectives

1. Generate a reset token for the target account
2. Observe the token structure in the URL
3. Enable subsequent brute force without full token knowledge

## Instructions

### Step 1: Access Reset Form

**Context**: Navigate to the password reset page.

Use browser to go to /users/password/new and enter the target email.

> Submit the form; expect 200 OK if email valid.

### Step 2: Capture Reset URL

**Context**: Intercept the generated link.

The system emails or redirects with a URL containing the token parameter.

> Extract partial token for brute force basing; success: URL format confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-reset]]
- [[token-generation]]
