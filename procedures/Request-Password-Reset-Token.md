---
id: proc-001
tags:
  - broken-authentication
  - password-reset
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
updated_at: '2025-12-14T17:31:52.116Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
---

# Request-Password-Reset-Token

## Summary

This procedure initiates a password reset request on the Courier web application to obtain a reset token/code sent via email, which is left unused to test for expiration flaws.

## Description

In the context of broken authentication vulnerabilities, this step creates a reset token by simulating a forgotten password scenario. The target is https://www.trycourier.app, where users can register or log in. After logout, the reset request sends a code to the associated email. This token is critical for later reuse if not properly invalidated. Prerequisites include a registered account and email access. Expected outcome: Token received without immediate use, enabling subsequent exploitation.

## Requirements

1. Access to https://www.trycourier.app with a registered or new account
2. Valid email address for the account to receive the reset code
3. Web browser for navigation

## Defense

Defensive measures and detection strategies:

- Implement token expiration on reset requests (e.g., 15-30 minutes TTL)
- Invalidate all pending tokens upon successful password change via any method
- Monitor for multiple reset requests from the same IP/email in short periods

## Objectives

1. Generate and receive a password reset token
2. Maintain the token's validity for testing
3. Set up conditions for token reuse exploitation

## Instructions

### Step 1: Account Creation or Login

**Context**: Ensure an active account exists to request the reset from.

Navigate to https://www.trycourier.app and register a new account or log in with an existing one. Confirm email verification if prompted during registration.

### Step 2: Initiate Password Reset

**Context**: Log out and request the reset to generate the token.

Log out of the current session. On the login page, select 'Forgot Password' or similar, enter the account email, and submit the request.

**Expected Output**: An email arrives with a reset code or link containing the token.

### Step 3: Retrieve but Do Not Use Token

**Context**: Access the email to note the code without applying it.

Check the email inbox for the reset message. Copy the code but do not proceed to reset the password yet.

**Expected Output**: Reset code obtained and ready for later use.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[broken-authentication]]
- [[password-reset]]

---
