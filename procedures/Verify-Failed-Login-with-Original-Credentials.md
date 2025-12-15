---
tags:
  - verification
  - authentication
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:24.313Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 49597bd3-bb1a-4896-a6de-e43f71d91d9a
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Verify-Failed-Login-with-Original-Credentials

## Summary

This verification procedure tests the success of the CSRF attack by attempting login with the victim's original password, confirming the unauthorized change has taken effect.

## Description

Post-CSRF execution, the password is reset, invalidating original credentials. Attempt login at default.asp to observe failure, indicating the profile update succeeded. This step validates the attack without alerting the victim prematurely.

## Requirements

1. Knowledge of victim's original username and password
2. Access to the login endpoint
3. Recent execution of the CSRF payload

## Defense

Defensive measures and detection strategies:

- Email alerts on password change attempts
- Rate-limit login failures to detect brute-force or verification probes
- Log all failed authentications with timestamps

## Objectives

1. Confirm password invalidation
2. Validate CSRF impact
3. Prepare for takeover login

## Instructions

### Step 1: Attempt Original Login

**Context**: Simulate victim login to check for changes.

Navigate to http://██████████/████████/default.asp and enter:

- Username: [victim_username]
- Password: [original_password]

Submit the form.

> Expected output: Error message like "Invalid username or password". No session established.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[verification]]
- [[authentication]]
