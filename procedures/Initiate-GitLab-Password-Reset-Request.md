---
id: proc-001
tags:
  - password-reset
  - web
  - gitlab
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:34.526Z'
skill_level: beginner
impact_level: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-GitLab-Password-Reset-Request

## Summary

This procedure initiates the password reset process on a GitLab instance by submitting the victim's email address, setting up the request for interception and modification in subsequent steps of an account takeover attack.

## Description

In the context of exploiting GitLab's password reset vulnerability, this step accesses the forgot password functionality and submits the target's email. The request is typically form-encoded but will be intercepted for conversion. This requires no authentication and targets the public-facing web application. Expected outcome: Generation of a resettable request that can be manipulated to send links to unauthorized emails.

## Requirements

1. Access to the GitLab login page via web browser
2. Knowledge of the victim's email address
3. Burp Suite or similar proxy configured in the browser

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on password reset requests per IP
- Validate email inputs to accept only single strings, not arrays
- Monitor for unusual proxy traffic patterns to the reset endpoint

## Objectives

1. Trigger the password reset workflow for the victim's account
2. Generate an interceptable HTTP POST request
3. Prepare for payload manipulation without alerting the user

## Instructions

### Step 1: Access Password Reset Page

**Context**: Navigate to the GitLab instance and locate the reset functionality to begin the process.

No command required; use browser to visit https://target-gitlab.com/users/password/new (or equivalent) and click 'Forgot Your Password?'.

> Enter the victim's email (e.g., victim@gmail.com) and submit the form. The browser sends a POST to /users/password with the email parameter.

### Step 2: Submit the Request

**Context**: Complete the submission while ensuring it's intercepted by the proxy.

No command; submit the form.

> Expected: Request held in Burp Suite intercept if enabled.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

None

## Commands Used

None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[password-reset]]
- [[web]]
- [[gitlab]]
