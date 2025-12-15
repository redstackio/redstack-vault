---
id: proc-17512-login-takeover
tags:
  - login
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
updated_at: '2025-12-14T17:33:06.438Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login with New Password

## Summary

This final procedure logs in to the compromised account using the target email and newly set password, achieving full unauthorized access.

## Description

Post-reset, the attacker uses the altered credentials to authenticate normally, gaining all privileges of the account, such as admin access for co-founder emails. This completes the takeover chain.

## Requirements

1. Target email and new password
2. Login endpoint access
3. No additional MFA (assumed absent)

## Defense

Defensive measures and detection strategies:

- Enable MFA for all accounts
- Alert on logins from new IPs post-reset
- Session invalidation on password changes

## Objectives

1. Authenticate with new credentials
2. Access account dashboard
3. Verify privilege level

## Instructions

### Step 1: Submit Login Form

**Context**: Enter credentials at login page.

Go to /login, input email and new password, submit.

> Expect redirect to dashboard; success: Session active.

### Step 2: Verify Access

**Context**: Confirm takeover.

Navigate to sensitive areas (e.g., settings, reports).

> Success: Full access without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[login]]
- [[account-takeover]]
