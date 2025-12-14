---
tags:
  - admin-access
  - impersonation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:57.961Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2ab40171-c22e-46d8-9bb6-f657e85121e9
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access Admin Features and Target Account

## Summary

As admin, view customer accounts and login to target like marten.mickos, preparing for 2FA bypass.

## Description

Admin panel allows impersonation; retrieve password from admin tab for marten.mickos, initiate login on app.bountypay.h1ctf.com/pay/ with app_style param for CSS exfil.

## Requirements

1. Admin privileges
2. Target username
3. 2FA bypass setup

## Defense

Defensive measures: Log all admin logins, require additional auth for impersonation; Detection: Alert on cross-account access.

## Objectives

1. Access admin dashboard
2. Impersonate target
3. Expected outcome: Target session start

## Instructions

### Step 1: Navigate Admin Panel

**Context**: View customers.

Login to admin features post-escalation.

> Expected output: List of accounts.

### Step 2: Initiate Target Login

**Context**: Use admin password.

Enter marten.mickos credentials from tab.

> Expected output: 2FA prompt for bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used


## Tools Used


## Tags

- admin-access
- impersonation
