---
id: proc-gitlab-demote-user-001
tags:
  - gitlab
  - role-demotion
  - permissions
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:11.098Z'
skill_level: basic
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Demote-User-to-Guest-Role

## Summary

This procedure demotes a Developer user to Guest role in a GitLab project, which enforces web UI restrictions but fails to revoke API access for assigned MRs.

## Description

Using admin privileges, navigate to project members and downgrade the user's role to Guest, simulating permission revocation. This highlights the discrepancy between UI and API enforcement. Expected outcome: Role changed, UI access limited.

## Requirements

1. Admin role in the project
2. Target user as current member
3. Access to members management UI

## Defense

Defensive measures and detection strategies:

- Log all role changes and notify affected users
- Implement API token revocation on role demotion

## Objectives

1. Trigger permission revocation for testing
2. Confirm UI restrictions post-demotion
3. Set up for API bypass validation

## Instructions

### Step 1: Access Project Members

**Context**: Locate user in members list.

Go to Project > Members, find the Developer user.

> User profile visible.

### Step 2: Change Role to Guest

**Context**: Apply demotion.

Click edit icon, select 'Guest' from role dropdown, and save.

> Role updated to Guest; confirm no Developer features in UI.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- access-control
