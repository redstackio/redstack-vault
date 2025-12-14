---
id: 123e4567-e89b-12d3-a456-426614174003
name: HackerOne-Login-Bypassing-2FA
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:42.822Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques:
  - '[[T1078.004]]'
tags:
  - 2fa-bypass
  - login
  - account-takeover
  - hackerone
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---

# HackerOne-Login-Bypassing-2FA

## Summary

This procedure demonstrates logging into a HackerOne account post-deactivation and password reset, where the 2FA requirement is bypassed, granting full unauthorized access.

## Description

After deactivation and reset, the HackerOne login flow omits 2FA due to a flaw in state management. This web-based procedure assumes email access and prior steps, resulting in control over the account, including sensitive features like private program invites.

## Requirements

1. Newly set password from reset procedure
2. Victim's HackerOne email address
3. Web browser

## Defense

Defensive measures and detection strategies:

- Enforce 2FA re-verification on all logins after resets
- Log and alert on logins from new IPs post-deactivation
- Require reactivation with 2FA before full access

## Objectives

1. Achieve login without OTP
2. Access account dashboard and features
3. Compromise private data like program invites

## Instructions

### Step 1: Attempt Login

**Context**: Use the reset credentials to log in, observing the absence of 2FA.

Go to https://hackerone.com/login, enter the email and new password, submit.

> No OTP prompt appears; login proceeds directly.

### Step 2: Verify Access

**Context**: Confirm full account control post-login.

Upon success, navigate to dashboard; check access to private invites and settings.

> Expected: Full functionality without restrictions, indicating successful bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[T1078.004]] Cloud Accounts

## Commands Used


## Tools Used


## Tags

- [[2fa-bypass]]
- [[login]]
- [[account-takeover]]
- [[hackerone]]
