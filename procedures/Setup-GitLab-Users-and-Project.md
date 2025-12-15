---
id: uuid-setup-users
tags:
  - gitlab
  - setup
  - users
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
updated_at: '2025-12-14T17:25:53.160Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-GitLab-Users-and-Project

## Summary

This procedure establishes the foundational environment for exploiting the GitLab GraphQL vulnerability by creating users, a project, and branches to simulate a realistic maintainer scenario.

## Description

In the attack scenario, an owner (User A) creates a project and grants maintainer access to User B. Branches are set up with differing file content to enable merge request creation. This targets GitLab instances (e.g., 12.10.0-ee) where maintainers have limited deletion permissions, setting up the type confusion exploit. Expected outcome: A prepared project ready for DiffNote creation and mutation execution.

## Requirements

1. Access to GitLab registration (self-hosted or SaaS)
2. Owner-level permissions for User A
3. Network access to GitLab UI

## Defense

Defensive measures and detection strategies:

- Enforce strict role-based access control (RBAC) audits
- Monitor user registrations and project invitations for anomalies

## Objectives

1. Create authenticated users with appropriate roles
2. Prepare project structure for vulnerability exploitation
3. Ensure maintainer cannot normally delete repositories

## Instructions

### Step 1: Register Users

**Context**: Create two separate accounts to simulate owner and attacker roles.

No specific command; use GitLab UI to register User A and User B.

> Log in as User A and User B to confirm accounts are active.

### Step 2: Create Project and Assign Role

**Context**: User A creates a project and invites User B as maintainer.

No specific command; in project settings, invite User B with Maintainer role.

> Verify User B can access the project with maintainer permissions but cannot delete the repository.

### Step 3: Create Branches with Differing Content

**Context**: Set up branches to enable merge request diffs.

No specific command; use GitLab UI or git CLI to create 'main' and 'feature' branches, add a file (e.g., test.txt) with different content in each.

> Commit and push branches; confirm differences visible in project repository view.

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
- setup
- users
