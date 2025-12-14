---
tags:
  - takeover-verification
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
updated_at: '2025-12-14T17:33:11.916Z'
sub_techniques: []
id: ddd77bce-b6f9-4d7c-91a1-7f0c0df05292
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Email-Change-and-Account-Takeover

## Summary

This procedure confirms the email update by attempting login with the new email and initiating a password reset to demonstrate full account control.

## Description

Post-IDOR, the original email loses access, while the new one gains it. This exploits the app's reliance on email for resets, enabling takeover without interaction.

## Requirements

1. Updated email address
2. Original password (if known or guessed)
3. Access to password reset flow

## Defense

Defensive measures and detection strategies:

- Email change notifications to original address
- Secondary verification for email updates
- Monitor reset requests from new domains

## Objectives

1. Validate hijack
2. Gain unauthorized access
3. Assess impact

## Instructions

### Step 1: Login with New Email

**Context**: Test access with hijacked email.

Use browser login form with new email and original password.

> Expected: Successful login; original email fails.

### Step 2: Initiate Password Reset

**Context**: Request reset to control account fully.

Submit reset form with new email.

> Expected: Reset link emailed to attacker.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[takeover-verification]]
