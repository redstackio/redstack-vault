---
id: proc-uuid-003
tags:
  - verification
  - password-change
  - web
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
updated_at: '2025-12-14T17:27:03.227Z'
skill_level: basic
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Password-Change-Success

## Summary

This procedure confirms the success of a password change operation, particularly after bypassing CSRF validation, by checking server response and testing the new credentials.

## Description

Post-submission of the modified request, the server returns a success indicator despite the missing token. In Veris View's Django backend, this manifests as a 'Password changed Successfully' message. To fully verify, log out and re-authenticate with the new password. This step validates the vulnerability's exploitability, showing how an attacker could force changes via CSRF on authenticated users.

## Requirements

1. Completed password change request (with or without token)
2. Knowledge of the new password used
3. Access to login endpoint for re-testing

## Defense

Defensive measures and detection strategies:

- Audit logs for password changes, correlating with CSRF token presence
- Require additional verification (e.g., email confirmation) for password updates
- Rate-limit password change attempts per session

## Objectives

1. Confirm the bypass led to actual password update
2. Assess impact, noting old password requirement as partial mitigator
3. Document evidence for reporting the vulnerability

## Instructions

### Step 1: Check Server Response

**Context**: Observe the immediate feedback from the endpoint.

No command; review the response body after forwarding.

> Look for 'Password changed Successfully' in HTML or JSON. Expected output: Success message without errors.

### Step 2: Test New Password

**Context**: Validate functionality by logging in with updated credentials.

Log out via /logout/, then log in with old username and new password.

> Expected output: Successful login, confirming the change persisted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[password-change]]
- [[web]]
