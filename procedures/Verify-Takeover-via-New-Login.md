---
tags:
  - account-takeover
  - login-verification
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:57.801Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: b413ecca-c83b-4821-93ce-6243edc3868a
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
  - '[[Valid Accounts]]'
---
# Verify-Takeover-via-New-Login

## Summary

This procedure confirms account takeover by testing login failures with the old email and success with the new one.

## Description

Post-modification, this validates the exploit's success in Infogram by demonstrating the victim's loss of access and attacker's gain, highlighting the persistence achieved through email manipulation.

## Requirements

1. New email under attacker control
2. Knowledge of old email
3. Browser for login attempts

## Defense

Defensive measures and detection strategies:

- Failed login alerts to original email (if possible)
- Rate limiting on login attempts

## Objectives

1. Prove control transfer
2. Access victim data

## Instructions

### Step 1: Test Old Email Login

**Context**: Verify victim's access denial.

Navigate to login page and enter old email with any password.

> Expected: Error like "invalid email" or access denied.

### Step 2: Login with New Email

**Context**: Confirm attacker access.

Enter new email and victim's password (retained from session).

> Expected: Successful dashboard access.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Manipulation]]
- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[login-verification]]
