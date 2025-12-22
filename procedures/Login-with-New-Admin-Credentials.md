---
id: proc-login-new-admin
tags:
  - auth-bypass
  - access-gain
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
updated_at: '2025-12-14T17:30:07.536Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-with-New-Admin-Credentials

## Summary

This procedure authenticates into the DoD web application using newly created admin credentials to achieve full administrative control and potential site-wide modifications.

## Description

After receiving credentials via email, return to the main login page and use the username/password to log in. This grants access to all admin functions, including user privilege changes, leading to complete compromise.

## Requirements

1. Received username and password from email
2. Access to the main login page
3. Stable network connection

## Defense

Defensive measures and detection strategies:

- Implement session timeouts and IP whitelisting for admin logins
- Monitor for logins from unusual IPs or with new accounts
- Require MFA for all admin access

## Objectives

1. Authenticate as admin
2. Verify elevated privileges
3. Access sensitive controls

## Instructions

### Step 1: Navigate to Login

**Context**: Return to the original login endpoint.

**Command** (Manual Login):
Visit https://target-dod-app.com/login.

> Login form appears.

### Step 2: Enter Credentials

**Context**: Submit the new admin details.

**Command** (Form Input):
Username: [received username], Password: [received password]; click login.

> Successful login redirects to admin dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[access-gain]]
