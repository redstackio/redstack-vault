---
id: proc-request-reset-concretecms
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
updated_at: '2025-12-14T17:31:11.158Z'
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
# Request-Password-Reset-Without-Using

## Summary

This procedure generates a password reset token in Concrete CMS by initiating the reset process but deferring its use to test token persistence.

## Description

Password reset in Concrete CMS sends a time-limited token via email. This step creates the token without consumption, setting up for later exploitation of invalidation flaws. The target environment is a web-accessible CMS with email delivery enabled.

## Requirements

1. Registered account with accessible email
2. Web access to the login/reset page
3. Ability to receive emails promptly

## Defense

Defensive measures and detection strategies:

- Limit reset requests per IP/email (e.g., rate limiting)
- Log all reset attempts for anomaly detection
- Use short token expiration (e.g., 15 minutes)

## Objectives

1. Obtain a valid reset token
2. Preserve token for staleness testing
3. Verify email delivery mechanism

## Instructions

### Step 1: Initiate Reset

**Context**: Trigger the reset workflow from the login interface.

**Instructions**: On the Concrete CMS login page, click 'Forgot Password' or similar, enter the registered email, and submit.

> An email with a reset link (containing the token) will be sent.

### Step 2: Capture and Store Link

**Context**: Secure the token without activating it.

**Instructions**: Open your email client, locate the reset message, copy the full URL/link, but do not click it.

> Store the link in a secure note or file for later use.

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
