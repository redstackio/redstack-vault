---
tags:
  - authentication-bypass
  - unverified-login
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 198bf43d-e36c-406a-be96-696d69d66444
created_at: '2025-12-14T17:24:48.435Z'
updated_at: '2025-12-14T17:24:48.435Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-Unverified-Account

## Summary

This procedure demonstrates logging into a newly registered account without completing email verification, bypassing standard authentication checks.

## Description

Vulnerable systems allow login with unverified emails, enabling attackers to access account features immediately after registration. In the context of this attack, this step grants the attacker control over the victim's email-associated account, paving the way for 2FA enablement.

## Requirements

1. Successful completion of account registration with victim's email
2. Web browser access to the login endpoint
3. Registered username and password

## Defense

Defensive measures and detection strategies:

- Require email verification before permitting login
- Log and alert on logins from unverified accounts
- Implement session checks for verification status

## Objectives

1. Access the account dashboard without verification
2. Confirm the bypass of email checks
3. Prepare for sensitive actions like 2FA setup

## Instructions

### Step 1: Navigate to Login Page

**Context**: Locate the authentication form.

Go to the target's login URL (e.g., https://target.com/login).

### Step 2: Enter Credentials and Submit

**Context**: Attempt login with unverified account details.

Input:
- Username: The one created during registration
- Password: The chosen password

Click login and observe no verification prompt.

**Expected Output**: Redirect to account dashboard; session established.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication-bypass]]
- [[unverified-login]]
