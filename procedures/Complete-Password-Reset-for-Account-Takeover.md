---
id: proc-uuid-004
name: Complete-Password-Reset-for-Account-Takeover
tags:
  - account-takeover
  - password-reset
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:33:06.511Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Complete-Password-Reset-for-Account-Takeover

## Summary

This final procedure submits the brute-forced verification code to access the password change form, sets a new password, and logs in to achieve full control over the victim's account.

## Description

Using the correct code from the brute-force, the attacker resubmits the POST request or follows the UI flow to reach the new password input. Setting a known password allows immediate login, granting unauthorized access to sensitive data or functions in the DoD application.

## Requirements

1. Correct verification code obtained from prior brute-force
2. Access to the verification submission form
3. Desired new password meeting app policies

## Defense

Defensive measures and detection strategies:

- Require email confirmation for password changes
- Notify users of reset attempts via alternate channels
- Audit logs for successful resets from unusual IPs

## Objectives

1. Submit valid code to unlock password form
2. Set new controllable password
3. Gain persistent account access

## Instructions

### Step 1: Submit Valid Code

**Context**: Use the discovered code to authenticate the reset session.

In the browser or Repeater, modify the POST with the correct code (e.g., code=1234) and submit.

> Expected Output: Redirect to /set-new-password or success message.

### Step 2: Set New Password

**Context**: Enter and confirm a new password to complete the reset.

Fill the form with a strong but known password (e.g., NewPass123!), submit.

> Expected Output: Confirmation page; attempt login with email and new password to verify takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Account Manipulation]] Account Manipulation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[password-reset]]
