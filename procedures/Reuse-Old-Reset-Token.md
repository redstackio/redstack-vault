---
tags:
  - token-reuse
  - auth-bypass
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
updated_at: '2025-12-14T17:31:19.240Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: e40392e7-c34a-4dd5-bf47-15bdb72b97bf
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Reuse-Old-Reset-Token

## Summary

This procedure leverages the uninvalidated reset token from the old email to access the password change form post-email update.

## Description

With the account logged out and email changed, accessing the old token link bypasses normal authentication, exploiting the core flaw. This manual step via email link leads directly to the vulnerable reset interface, assuming control of the old email.

## Requirements

1. Access to old email (a@x.com) with the reset link
2. Logged-out state
3. Token still valid (typically within expiration window)

## Defense

Defensive measures and detection strategies:

- Expire and invalidate tokens on email changes
- Tie tokens to current email and validate on use
- Detect token usage from mismatched emails

## Objectives

1. Access reset form without new email verification
2. Bypass post-change protections
3. Prepare for password modification

## Instructions

### Step 1: Log Out

**Context**: Ensure no active session interferes.

**Instructions**: If logged in, log out from the dashboard.

> Session ends, redirecting to login.

### Step 2: Access Old Link

**Context**: Use the stored token to initiate reset.

**Instructions**: Open the email in a@x.com, click the reset link (e.g., https://hackerone.com/reset?token=abc123).

> Form loads for password entry without additional checks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[token-reuse]]
- [[auth-bypass]]
