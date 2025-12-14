---
tags:
  - auth-bypass
  - twitter
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
impact_level: high
detection_risk: medium
sub_techniques: []
id: f88a49da-56d4-46ae-b8d9-4b135976da5c
created_at: '2025-12-14T17:33:06.119Z'
updated_at: '2025-12-14T17:33:06.119Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Old-Password-Reset-Link

## Summary

This procedure opens the previously generated password reset link from the old email after the account email has been updated, bypassing the new email requirement.

## Description

Post-email update, accessing the old link (from abcd@x.com) still grants reset access due to the token not being revoked. This step demonstrates the core vulnerability, allowing an attacker with old email access to proceed to takeover.

## Requirements

1. Unused reset link from abcd@x.com
2. Updated account email to efgh@x.com
3. Web browser

## Defense

Defensive measures and detection strategies:

- Expire reset tokens immediately on email changes
- Log token usage attempts and flag anomalies

## Objectives

1. Validate token persistence
2. Gain access to reset interface
3. Prepare for password modification

## Instructions

### Step 1: Log Out

**Context**: Ensure clean state before accessing link.

Log out of the account completely.

> This prevents session conflicts.

### Step 2: Open Reset Link

**Context**: Use the old email's link to reach the reset page.

Click the reset link from the earlier email in abcd@x.com.

> The page loads, allowing password entry despite email change.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[twitter]]
