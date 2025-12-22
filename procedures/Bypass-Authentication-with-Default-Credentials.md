---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567894
tags:
  - auth-bypass
  - default-credentials
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Default Accounts]]'
updated_at: '2025-12-14T17:31:19.630Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Default Accounts]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Default Accounts]]'
---
# Bypass-Authentication-with-Default-Credentials

## Summary

This procedure exploits unchanged default credentials in Tiny File Manager to gain unauthorized access, bypassing standard authentication.

## Description

Default credentials (user/12345) in Tiny File Manager allow immediate login if not modified, common in hastily deployed PHP tools. This grants admin-level access, enabling file operations on the server hosting the 'link your NIN' feature.

## Requirements

1. Access to the file manager login page
2. Knowledge of default credentials
3. No rate limiting on login attempts

## Defense

Defensive measures and detection strategies:

- Change default credentials immediately upon deployment
- Disable or remove exposed instances; monitor login logs for defaults

## Objectives

1. Achieve authenticated access without valid creds
2. Expected outcome: Admin dashboard

## Instructions

### Step 1: Enter Credentials

**Context**: Submit defaults to login form.

In the login interface, input username: user, password: 12345 (or ████/████).

> Submit the form; no additional verification should be needed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Default Accounts]]

### Sub-Techniques

- [[Default Accounts]]

## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[default-credentials]]
