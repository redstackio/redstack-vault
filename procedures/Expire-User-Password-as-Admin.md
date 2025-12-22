---
id: proc-uuid-3
tags:
  - gitlab
  - admin
  - password-expiration
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
updated_at: '2025-12-14T17:32:29.251Z'
skill_level: intermediate
impact_level: low
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Expire-User-Password-as-Admin

## Summary

This procedure uses administrator privileges to expire a user's password in GitLab, simulating a lockout that should block access but fails to invalidate tokens due to the vulnerability.

## Description

Log in as an admin and edit the target user's account to change the password, setting 'password expired at' to the current time. This triggers the expiration check but does not affect token validity, rooted in a flawed patch for LDAP integration.

## Requirements

1. Administrator credentials for GitLab
2. Access to admin users panel at https://gitlab.domain.com/admin/users
3. Target user account (e.g., 'user01')

## Defense

Defensive measures and detection strategies:

- Enable automatic token revocation on password changes
- Monitor admin actions in audit logs
- Use multi-factor authentication for admins

## Objectives

1. Set user password to expired state
2. Verify UI login is blocked
3. Confirm tokens remain unaffected

## Instructions

### Step 1: Log In as Admin

**Context**: Gain admin access to user management.

Navigate to https://gitlab.domain.com/users/sign_in and log in with admin credentials.

> Dashboard loads with admin menu visible.

### Step 2: Edit User and Expire Password

**Context**: Modify the user to trigger expiration.

Go to https://gitlab.domain.com/admin/users/user01/edit, change the password to a new value, and save. This sets 'password expired at' to now.

> Save succeeds; check user details to confirm expiration timestamp.

### Step 3: Test UI Login Failure

**Context**: Validate the expiration locks UI access.

Attempt login as 'user01' with old password (fails) or new (prompts for update, but do not complete).

> Login fails or prompts, confirming expired state.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- admin-access
- expiration
