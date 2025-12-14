---
id: proc-escalate-fake-admin
tags:
  - privilege-escalation
  - account-takeover
  - admin
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
updated_at: '2025-12-14T17:32:20.904Z'
skill_level: intermediate
impact_level: critical
detection_risk: high
sub_techniques:
  - '[[Default Accounts]]'
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Escalate Privileges Using Fake Admin Account

## Summary

This procedure logs in with the fake account now granted admin privileges via IDOR and uses it to escalate the original attacker's role to admin, then deletes the original owner to achieve full organization takeover.

## Description

Once the fake account is added as admin to the target org, it can manage memberships without restrictions. Log in to the console with the fake credentials, navigate to users/memberships, update the attacker's role, and remove the victim. This completes the takeover chain.

## Requirements

1. Fake account email and password (invited via previous step)
2. Access to Helium Console login
3. Target organization ID and attacker user ID

## Defense

Defensive measures and detection strategies:

- Require multi-factor approval for role changes and deletions
- Alert on rapid membership changes or admin additions from unknown IPs
- Implement audit trails for all organization actions

## Objectives

1. Promote original attacker to admin
2. Remove original owner
3. Secure persistent control over organization

## Instructions

### Step 1: Log In with Fake Account

**Context**: Use the invited email to log in and access the target org dashboard.

No specific command; use browser to login at https://console.helium.com/login with fake credentials.

> Verify admin access by viewing organization members.

### Step 2: Update Attacker Role and Delete Owner

**Context**: In the users section, edit the original attacker's membership to "admin" and delete the victim admin.

No CLI command; perform via UI: Navigate to /users, select attacker > Edit Role > Admin; Select owner > Delete.

> Confirm changes in membership list.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[Default Accounts]]

## Commands Used


## Tools Used


## Tags

- privilege-escalation
- account-takeover
- admin
