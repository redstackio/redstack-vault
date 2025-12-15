---
tags:
  - gitlab
  - setup
  - developer-role
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
updated_at: '2025-12-14T17:29:20.442Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: cb24c87b-1bcb-4d6c-9fbc-a5d7d92e0470
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Private-Project-and-Add-Developer-User

## Summary

This procedure sets up a test environment in GitLab by creating a private project and adding a user with Developer role, enabling simulation of the type confusion vulnerability exploitation.

## Description

In the context of the GitLab deleteAnnotation vulnerability, this initial setup creates a private project owned by User A and grants User B (developer) access. This mimics a real scenario where a developer has limited permissions but can exploit the flaw to delete higher-level resources. The environment uses GitLab's standard UI for project creation and member invitation. Prerequisites include admin or owner access to GitLab.

## Requirements

1. Authenticated access to GitLab as project owner or admin
2. Valid user accounts (User A as owner, User B as developer)
3. Network access to GitLab instance

## Defense

Defensive measures and detection strategies:

- Monitor project creation and member additions via audit logs
- Enforce role-based access controls strictly
- Use GitLab's permission auditing tools

## Objectives

1. Establish isolated test project for vulnerability demonstration
2. Assign developer permissions to simulate attacker
3. Prepare global IDs for exploitation

## Instructions

### Step 1: Create Private Project

**Context**: Log in as User A and create a new private project via the GitLab dashboard.

**Command** (GitLab UI):

Navigate to New Project > Create blank project, set visibility to Private, name it "Test Project", and create.

> Note the project ID from the URL or project settings.

### Step 2: Add Developer User

**Context**: Invite User B to the project with Developer role to grant limited permissions.

**Command** (GitLab UI):

Go to Project > Members > Invite member, enter User B's username/email, select Developer role, and invite.

> Expected output: Invitation sent and accepted, User B has Developer access.

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
- developer-role
