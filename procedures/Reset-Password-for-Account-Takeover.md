---
id: p3c4d5e6-f7g8-9012-cdef-3456789012
name: Reset-Password-for-Account-Takeover
tags:
  - password-reset
  - account-takeover
  - web
  - credential-access
type: procedure
tools: []
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
updated_at: '2025-12-14T17:33:24.338Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques:
  - '[[Default Accounts]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Reset-Password-for-Account-Takeover

## Summary

This procedure uses the forgot password feature on the hijacked email to reset the victim's password, achieving full account takeover without further interaction.

## Description

After email hijacking via IDOR, the attacker submits a password reset request using the victim's new email. The reset link is sent to the attacker's inbox, allowing password change and login. This exploits the trust in email-based recovery, common in web apps like Atavist.

## Requirements

1. Control over the victim's updated email address
2. Access to https://magazine.atavist.com/forgot
3. No additional tools needed beyond browser

## Defense

Defensive measures and detection strategies:

- Require secondary verification (e.g., SMS or security questions) for resets
- Alert on rapid email changes followed by reset requests

## Objectives

1. Initiate password recovery flow
2. Set new password via reset link
3. Gain persistent access to victim account

## Instructions

### Step 1: Submit Reset Request

**Context**: Trigger the forgot password process using the hijacked email.

Navigate to https://magazine.atavist.com/forgot and enter the victim's email.

> Reset request submitted; email with link sent to attacker's inbox.

### Step 2: Complete Reset and Login

**Context**: Use the link to change password and access the account.

Click the link in the email, set a new password, and login at https://magazine.atavist.com/login.

> Successful login to victim's account with full privileges.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[Default Accounts]] Default Accounts

## Commands Used


## Tools Used


## Tags

- [[password-reset]]
- [[account-takeover]]
- [[web]]
- [[credential-access]]
