---
id: p-use-token-admin-rce
name: Use-Stolen-Token-for-Admin-Access
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.229Z'
tactics:
  - '[[Privilege Escalation]]'
  - '[[Execution]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Windows Command Shell]]'
tags:
  - gitlab
  - privilege-escalation
  - rce
  - token-use
platforms:
  - Web
tools: []
commands: []
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Windows Command Shell]]'
---

# Use-Stolen-Token-for-Admin-Access

## Summary

This procedure uses the stolen authentication_token to access the GitLab admin panel, escalate privileges, execute remote code, and access private repositories and sensitive user data.

## Description

GitLab stores authentication tokens in plaintext in the database and exposes them via export. Appending the token to admin endpoints allows direct access without further validation, leading to full admin capabilities including RCE via Rails console or CI/CD pipelines, and viewing/modifying private repos, hashed passwords, and OTP secrets. Prerequisites: valid stolen token. Expected outcomes: complete compromise of the instance.

## Requirements

1. Stolen authentication_token from export
2. Access to GitLab instance URL
3. Browser or curl for API access

## Defense

Defensive measures and detection strategies:

- Rotate tokens immediately upon detection of leaks
- Implement token validation beyond simple parameter (e.g., IP whitelisting, expiration)
- Monitor admin panel access logs for anomalous token usage
- Use short-lived tokens and multi-factor auth

## Objectives

1. Gain admin panel access
2. Escalate to RCE
3. Exfiltrate sensitive data

## Instructions

### Step 1: Access Admin Panel

**Context**: Use token to authenticate to admin area.

No command; construct URL: https://gitlab-instance/admin/users?authentication_token=<stolen_token> and load in browser.

> Admin dashboard loads; user list and controls visible.

### Step 2: Escalate Privileges

**Context**: From admin panel, modify users or projects for higher access.

No command; navigate to Admin Area > Users, edit target or self to admin role if needed.

> Privileges elevated; full instance control.

### Step 3: Execute RCE

**Context**: Leverage admin access for code execution.

No command; go to Admin Area > Monitoring > Background Jobs or use Rails console via API with token to run commands like system('id').

> Command output confirms RCE, e.g., uid=33(www-data).

### Step 4: Access Sensitive Data

**Context**: View private repos and user secrets.

No command; browse Admin Area > Projects for private repos, or Users for hashed passwords/OTP.

> Data exposed; download or exfiltrate as needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation
- [[Execution]] Execution

### Techniques

- [[Valid Accounts]] Valid Accounts
- [[Windows Command Shell]] Windows Command Shell (adapted for Unix/RCE in Rails)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[privilege-escalation]]
- [[rce]]
- [[token-use]]
