---
id: proc-multiple-password-changes
tags:
  - password-change
  - session-invalidation
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
updated_at: '2025-12-14T17:31:11.154Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Log-In-and-Change-Password-Multiple-Times

## Summary

This procedure involves logging into a Concrete CMS account and repeatedly changing the password to invalidate sessions while testing token persistence.

## Description

By performing multiple password updates (up to 10), this step simulates legitimate user activity that should invalidate prior tokens but fails in vulnerable Concrete CMS versions. Each change forces logout, destroying sessions, but the reset token remains active, enabling later bypass.

## Requirements

1. Valid login credentials for the test account
2. Access to account settings page
3. Patience for repeated logins (due to logouts)

## Defense

Defensive measures and detection strategies:

- Invalidate all prior tokens/sessions on any password change
- Alert on rapid successive password changes
- Implement change limits (e.g., once per hour)

## Objectives

1. Invalidate active sessions through changes
2. Demonstrate token non-invalidation
3. Prepare for stale token exploitation

## Instructions

### Step 1: Initial Login

**Context**: Gain access to the account dashboard.

**Instructions**: Enter credentials on the login page and authenticate.

> Successful login redirects to the dashboard.

### Step 2: Perform Multiple Changes

**Context**: Navigate to settings and update password repeatedly.

**Instructions**: Go to 'My Account' > 'Settings' > 'Change Password'. Enter old password, new password (vary slightly each time), confirm, and submit. Repeat 5-10 times, re-logging in after each logout.

> Each submission logs you out; confirm change via re-login attempt.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-change]]
- [[session-invalidation]]
