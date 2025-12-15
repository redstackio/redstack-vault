---
tags:
  - 2fa-bypass
  - auth-bypass
  - linkedin
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:42.780Z'
sub_techniques: []
id: e9f81e67-6d4e-4162-b799-07a60152c7b0
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Bypass-2FA-Using-Merge-Accounts

## Summary

This procedure exploits a vulnerability in LinkedIn's merge-accounts feature to bypass two-factor authentication (2FA), allowing an attacker with the victim's credentials to gain full unauthorized access to the account without additional verification.

## Description

The merge-accounts functionality on LinkedIn is intended for combining duplicate profiles but fails to enforce 2FA checks when initiating a merge with a victim's credentials. An attacker logs into their own account, navigates to the merge process, and inputs the victim's email and password. The system authenticates the credentials but skips 2FA, effectively merging access and granting the attacker control over the victim's account. This leads to potential data exfiltration, account takeover, and further abuse. The vulnerability was reported and fixed by LinkedIn, but the technique highlights risks in account recovery flows.

## Requirements

1. Valid victim's LinkedIn credentials (email and password)
2. Attacker's own active LinkedIn account without 2FA enabled
3. Web browser with access to LinkedIn.com
4. Basic understanding of LinkedIn's account settings interface

## Defense

Defensive measures and detection strategies:

- Enforce 2FA on all account actions, including merges and recoveries
- Implement rate limiting and anomaly detection on account merge requests
- Monitor for unusual login patterns from merged accounts
- Require additional verification (e.g., email confirmation) for sensitive operations

## Objectives

1. Achieve unauthorized access to the victim's LinkedIn account
2. Bypass 2FA without alerting the victim
3. Demonstrate the impact of improper authentication in account management features

## Instructions

### Step 1: Log In to Attacker's Account

**Context**: Start by accessing your own LinkedIn account to reach the merge-accounts interface.

Navigate to https://www.linkedin.com and log in with your credentials. Ensure 2FA is not enabled on this account to avoid complications.

**Expected Output**: Successful login to the attacker's dashboard.

### Step 2: Initiate Merge-Accounts Process

**Context**: Use the account settings to start the merge process and input victim's credentials.

Go to Settings & Privacy > Account management > Merge or link accounts. Enter the victim's email address to begin the merge. When prompted, provide the victim's password. The system will authenticate without triggering 2FA.

**Expected Output**: The accounts are merged, and you gain access to the victim's profile.

### Step 3: Verify Access

**Context**: Confirm unauthorized access by checking victim-specific data.

Once merged, navigate to the victim's connections, messages, or posts. Perform a test action, such as viewing private messages.

**Expected Output**: Full access to victim's account features without logout or alerts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- 2fa-bypass
- auth-bypass
- linkedin
