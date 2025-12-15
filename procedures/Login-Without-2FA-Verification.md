---
id: proc-uuid-3
tags:
  - 2fa-bypass
  - unauthorized-login
  - account-takeover
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
updated_at: '2025-12-14T17:31:30.813Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-Without-2FA-Verification

## Summary

This procedure logs into a deactivated HackerOne account using the newly reset password, bypassing 2FA due to the platform's failure to enforce it post-deactivation.

## Description

After password reset, the attacker attempts login with the new credentials. The logical vulnerability causes the system to skip the 2FA prompt for deactivated accounts during recovery login, granting full access. This completes the account takeover. Prerequisites include the new password; expected outcome is dashboard access without 2FA.

## Requirements

1. New password from the reset procedure
2. Web browser access to HackerOne
3. No additional credentials needed beyond the reset password

## Defense

Defensive measures and detection strategies:

- Always require 2FA reactivation before allowing login on recovered accounts
- Implement session monitoring to detect logins from unusual IPs post-recovery
- Use behavioral analytics to flag logins without 2FA on accounts that previously had it enabled

## Objectives

1. Access the account dashboard without 2FA interruption
2. Verify the bypass success by performing account actions
3. Achieve complete unauthorized control

## Instructions

### Step 1: Attempt Login with New Password

**Context**: Use the updated credentials to log in, observing the absence of 2FA.

Navigate to the HackerOne login page, enter the email and new password, and submit. The system processes the login without requesting a 2FA code.

> Expected output: Direct redirection to the account dashboard.

### Step 2: Validate Access

**Context**: Confirm full functionality to ensure takeover is complete.

Once logged in, navigate to reports, settings, or other features. Attempt actions like viewing sensitive data to verify unrestricted access.

> Success is indicated by normal platform usage without security halts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[2fa-bypass]]
- [[unauthorized-login]]
- [[account-takeover]]
