---
tags:
  - password-change
  - auth-bypass
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Reversible Encryption]]'
updated_at: '2025-12-14T17:31:11.345Z'
sub_techniques: []
id: 06d6d17a-9e77-4f54-8f50-3b63386586b2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Reversible Encryption]]'
---
# Change-User-Password

## Summary

This procedure updates the user's password in the web application, exploiting the lack of session invalidation to maintain access on other devices, which can lead to account misuse if sessions linger on shared computers.

## Description

The vulnerability stems from incomplete implementation in the password change endpoint at https://bridge.cspr.ng/my/account, where the feature to invalidate sessions exists in the codebase (Airship CMS, PHP-based) but is not enabled on the infrastructure. Changing the password updates the hash but does not revoke active session tokens, allowing continued access without re-authentication.

## Requirements

1. Active authenticated session in the browser
2. Knowledge of current password
3. New password that meets application policy

## Defense

Defensive measures and detection strategies:

- Enforce session termination on all devices via token revocation upon password reset
- Log password changes and notify users of concurrent sessions
- Implement client-side checks for session expiry post-auth changes

## Objectives

1. Modify account credentials without disrupting existing sessions
2. Confirm the change succeeds without logout
3. Highlight the risk of unauthorized persistence

## Instructions

### Step 1: Navigate to Account Settings

**Context**: Access the password change interface from an active session.

In the browser, go to `https://bridge.cspr.ng/my/account`.

> Loads the account management page; verify logged-in state.

### Step 2: Submit New Password

**Context**: Enter and confirm the new password to trigger the update.

Fill in current password, new password, and confirmation; submit the form.

> Expected: Success message; session cookie remains valid. No automatic logout occurs.

### Step 3: Verify Change on Same Browser

**Context**: Ensure the password update took effect without session disruption.

Attempt a logout and re-login with new password to confirm.

> Session stays active; re-login succeeds with new credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Reversible Encryption]] Multi-Factor Authentication Instrument (MFA) - but adapted for session mod

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- password-change
- auth-bypass
