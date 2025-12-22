---
id: proc-uuid-002
tags:
  - account-creation
  - verification
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
updated_at: '2025-12-13T23:52:33.890Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Register-and-Verify-Account-on-ReadMe-io

## Summary

This procedure creates a new user account on the ReadMe.io platform and verifies it via email, establishing a legitimate authenticated session for further exploitation.

## Description

ReadMe.io allows self-registration for free accounts, which can then be used to interact with its API. After registration, an email verification step is required to activate the account. This provides the necessary session for logged-in requests, such as dashboard access and API calls. In the context of this attack, it enables the subsequent invite exploitation without raising immediate suspicion.

## Requirements

1. Valid email address for verification
2. Web browser for registration form
3. Access to email inbox

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on registrations.
- Require CAPTCHA on signup to prevent automated abuse.
- Monitor for bulk registrations from suspicious IPs.

## Objectives

1. Gain a verified user account.
2. Prepare for authenticated API interactions.
3. Establish session for privilege escalation.

## Instructions

### Step 1: Complete Registration

**Context**: Fill out the signup form to create the account.

No command; browser-based:

1. Navigate to https://readme.io/register.
2. Enter username, email, password, and submit.

> Form submission sends a verification email; check spam if not received.

### Step 2: Verify Email

**Context**: Activate the account to enable login.

1. Open the verification email from ReadMe.io.
2. Click the verification link.

> Account is now active; login is possible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[account-creation]]
- [[web]]
