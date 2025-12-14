---
id: proc-login-account
tags:
  - login
  - auth
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
updated_at: '2025-12-14T17:30:58.354Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login to Created Account

## Summary

This procedure authenticates into the newly created unauthorized HackerOne account using the chosen credentials, gaining initial access to the platform.

## Description

Post-verification, standard login is performed on hackerone.com. This leverages the bypassed account for valid session establishment. Prerequisites: Verified account. Outcome: Dashboard access, setting stage for SSO chaining.

## Requirements

1. Username and password from signup
2. Verified email
3. Browser access to hackerone.com

## Defense

Defensive measures and detection strategies:

- Enforce domain checks on login attempts for new accounts
- Log login from restricted domain accounts and trigger reviews
- Use anomaly detection for logins post-signup

## Objectives

1. Establish valid session on HackerOne
2. Confirm account functionality
3. Prepare for SSO to linked services

## Instructions

### Step 1: Submit Login Form

**Context**: Enter credentials on the HackerOne login page.

No command; manual:

Navigate to https://hackerone.com/users/sign_in, enter username and password, submit.

> Expected: Redirect to dashboard with user profile visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- login
- auth
