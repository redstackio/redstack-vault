---
id: proc-downgrade-role
tags:
  - role-revoke
  - access-control
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
  - '[[Account Access Removal]]'
updated_at: '2025-12-14T17:28:51.670Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Account Access Removal]]'
---
# Downgrade-User-Role-to-None

## Summary

This procedure revokes admin privileges from a user in the Omise team management, setting their role to none to test post-downgrade access enforcement.

## Description

Using owner credentials, access the team page at https://dashboard.omise.co/team and modify the target user's role from admin to none. This simulates privilege revocation without logging out the user. Expected outcome: Role updated immediately, but session may persist. Targets test dashboard; live environment may differ.

## Requirements

1. Owner credentials for Omise
2. Access to team management page
3. Target user already invited

## Defense

Defensive measures and detection strategies:

- Force session revalidation on role changes
- Log all role modifications with timestamps
- Notify users of role changes via email

## Objectives

1. Revoke admin access from user
2. Trigger potential backend revalidation test
3. Prepare for access bypass verification

## Instructions

### Step 1: Access Team Management

**Context**: Log in as owner and view team members.

No specific command; visit https://dashboard.omise.co/team.

> Locate the target user in the list.

### Step 2: Change Role to None

**Context**: Update role assignment.

No specific command; select user, change role dropdown to 'None', and save.

> Role updated; no immediate user notification in test env.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Account Access Removal]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- role-revoke
- access-control
