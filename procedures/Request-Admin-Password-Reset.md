---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: Request-Admin-Password-Reset
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:28:36.697Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Account Manipulation]]'
sub_techniques: []
tags:
  - password-reset
  - account-manipulation
  - phabricator
commands: []
platforms:
  - Web
tools: []
skill_level: low
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---

# Request-Admin-Password-Reset

## Summary

This procedure submits a password reset request for the Phabricator admin account from an authenticated normal user session, generating a sensitive reset link that fails to email due to prior disruption.

## Description

Phabricator allows users to request resets for other accounts via the interface, especially if email enumeration is possible. During mail disruption, the generated token/link is not sent but logged in daemon logs. This step leverages the authenticated session to target the admin email, exploiting the lack of strict access controls on reset requests.

## Requirements

1. Active normal user session in Phabricator
2. Knowledge of the admin's email address (e.g., via user directory or enumeration)
3. Ongoing mail service disruption

## Defense

Defensive measures and detection strategies:

- Restrict password reset requests to the account owner only (e.g., via CAPTCHA or verification)
- Rate-limit reset requests per IP or user to prevent abuse
- Log and alert on reset requests for admin accounts

## Objectives

1. Generate a time-sensitive password reset token for the admin
2. Ensure the token is logged due to delivery failure
3. Avoid triggering email delivery

## Instructions

### Step 1: Access Reset Interface

**Context**: Locate the password reset functionality within Phabricator.

No command required; from the dashboard, navigate to Account > Password or use the global forgot password link.

> Select or enter the admin's email address in the reset form. Expected output: Form submission prompt.

### Step 2: Submit Request

**Context**: Initiate the reset to create the logged token.

No command required; submit the form with the admin email.

> UI shows 'Reset link sent' message, but no actual email due to disruption. Success: Request processed without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[password-reset]]
- [[account-manipulation]]
- [[phabricator]]
