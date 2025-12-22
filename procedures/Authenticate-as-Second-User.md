---
tags:
  - authentication
  - hackerone
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
updated_at: '2025-12-14T05:32:13.649Z'
sub_techniques: []
id: dabc3de2-1628-4ba8-8857-b8c8e69bb516
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-as-Second-User

## Summary

This procedure logs in to a secondary authenticated account on HackerOne that lacks access to the target scoping form, simulating an unauthorized attacker.

## Description

To demonstrate access bypass, switch from the form owner's account to a different valid user account. This leverages valid authentication but exploits the lack of form-specific authorization in the upload endpoint. No special privileges are needed beyond basic authentication.

## Requirements

1. Second valid HackerOne account (authenticated but without org/form access)
2. Web browser with session management
3. Knowledge of login credentials for the second account

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) for all accounts
- Monitor login events for cross-account activity patterns
- Implement IP/session binding to detect account switching

## Objectives

1. Establish an unauthorized session for exploitation
2. Confirm no direct access to the target form
3. Prepare for sending requests from the attacker perspective

## Instructions

### Step 1: Log Out of Owner Account

**Context**: Clear the current session to avoid interference.

**Command** (Manual):

Click the logout button in the HackerOne dashboard.

> Ensures clean separation between accounts.

### Step 2: Log In to Second Account

**Context**: Authenticate the unauthorized user.

**Command** (Manual):

Enter credentials at https://hackerone.com/login and submit.

> Verify successful login by checking the user profile or dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[hackerone]]
