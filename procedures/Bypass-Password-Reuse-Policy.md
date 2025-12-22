---
tags:
  - password-bypass
  - policy-evasion
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:28.467Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 98e0eba6-ddf2-45c7-bc28-497d91a58e80
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-Password-Reuse-Policy

## Summary

This procedure takes advantage of the lack of password history enforcement in the MTN Group application, allowing immediate reuse of the old password after temporary password login, effectively bypassing change requirements.

## Description

After logging in with the temporary password, the app prompts for a new password without checking against recent history (e.g., the immediate old one). This weakens authentication by permitting stagnant credentials. The procedure assumes successful brute force or receipt of the temp password. Target environment is the post-reset login flow. Outcome: Account secured with weak, reused password, maintaining attacker access.

## Requirements

1. Valid temporary password (guessed or received)
2. Knowledge of the target's old password
3. Active session after temp login

## Defense

Defensive measures and detection strategies:

- Enforce password history (e.g., no reuse of last N passwords)
- Require new passwords to differ significantly (e.g., via checksumming)
- Audit password changes for reuse patterns

## Objectives

1. Log in with temporary password
2. Set new password to old one
3. Retain weak credentials

## Instructions

### Step 1: Authenticate with Temporary Password

**Context**: Use the obtained temp password to access the account.

Enter user ID and temporary password on the login form, submit.

> Redirects to new password prompt.

### Step 2: Enter Old Password as New

**Context**: Exploit lack of reuse checks.

In the new password fields, input the old password twice and confirm.

> No validation errors; password updates successfully.

### Step 3: Verify Access

**Context**: Confirm the bypass worked.

Log out and log back in with the reused password.

> Successful login indicates policy evasion.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[policy-bypass]]
- [[authentication]]
