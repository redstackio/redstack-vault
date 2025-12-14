---
tags:
  - broken-access-control
  - bypass
  - web
  - hackerone
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
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:25:23.559Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 5ce5a753-c4d9-4838-8b3f-5098193805d0
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Bypass-Concealed-Team-Member-Restrictions

## Summary

This procedure tests and exploits broken access controls in HackerOne by allowing concealed team members to add/remove external reporters and post public comments, bypassing visibility restrictions.

## Description

HackerOne's concealed membership feature fails to enforce restrictions on certain actions, leading to unintended disclosures. Invite a concealed member and perform actions as them to verify. Requires admin access to invite.

## Requirements

1. Admin access to a HackerOne program/team to invite members
2. Ability to set visibility to concealed
3. Access to report UI for actions like adding users or posting comments

## Defense

Defensive measures and detection strategies:

- Enforce visibility flags consistently across all endpoints and UI actions
- Log actions by concealed users and alert on public-visible operations
- Implement role-based access control (RBAC) with granular permissions

## Objectives

1. Demonstrate unenforced restrictions for concealed members
2. Enable unauthorized management of report participants
3. Allow posting of public comments leading to information disclosure

## Instructions

### Step 1: Invite Concealed Team Member

**Context**: Add a team member with concealed visibility to the report.

No command; use HackerOne team management UI to invite and set visibility to concealed.

> Confirm invitation succeeds and member status is hidden from reporters.

### Step 2: Perform Restricted Actions

**Context**: As the concealed member, attempt add/remove external users and post public comments.

No command; use report UI to add/remove a test external reporter and post a comment marked as public.

> Expected: Actions succeed; removals trigger notifications, comments visible to reporters despite concealment.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[broken-access-control]]
- [[web]]
