---
tags:
  - account-takeover
  - password-reset
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:33:12.476Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 114b7e3e-e42c-4803-ba7d-f47de3089f83
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Use-Token-to-Reset-Password

## Summary

This procedure submits the captured reset token to the legitimate endpoint to change the victim's password, resulting in account takeover.

## Description

With the token, the attacker accesses the reset form on Mars.com and sets a new password. This bypasses authentication entirely. Requires the token to be unexpired. Outcome is full control of the account.

## Requirements

1. Captured valid reset token
2. Access to the reset submission endpoint
3. New password for the account

## Defense

Defensive measures and detection strategies:

- Shorten token expiration times (e.g., 5 minutes)
- Require additional verification (e.g., email code) post-reset
- Alert users on successful resets and monitor for rapid changes

## Objectives

1. Validate and use the token for password change
2. Confirm access to the account
3. Secure the session post-takeover

## Instructions

### Step 1: Access Reset Endpoint

**Context**: Navigate to the password reset form with the token.

Construct or visit the reset URL with the token, e.g., `https://mars.com/reset?token=abc123`, and enter a new password.

> The form should accept the token without further auth.

### Step 2: Submit and Verify

**Context**: Complete the reset and test access.

Submit the form with the new password. Then, login using the victim's email and new password.

> Success if login succeeds and account contents are accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[password-reset]]
