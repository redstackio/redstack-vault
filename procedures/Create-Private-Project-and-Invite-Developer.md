---
id: proc-gitlab-create-project-001
tags:
  - gitlab
  - setup
  - project-creation
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
updated_at: '2025-12-14T17:32:11.104Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Private-Project-and-Invite-Developer

## Summary

This procedure sets up a private GitLab project and invites a target user with Developer role, establishing the foundation for testing access control changes.

## Description

In a GitLab environment, create a new private project to ensure visibility restrictions, then add a user as Developer via the project members interface. This simulates a collaborative development scenario where permissions can later be altered. Prerequisites include admin access to GitLab and a target user account. Expected outcome: User gains full read/write access to the project.

## Requirements

1. Admin privileges on GitLab instance
2. Target user email or username
3. Access to GitLab web UI

## Defense

Defensive measures and detection strategies:

- Monitor project creation and member invitations via GitLab audit logs
- Enforce role approval workflows for sensitive projects

## Objectives

1. Establish controlled private project environment
2. Grant initial elevated access to target user
3. Prepare for permission demotion testing

## Instructions

### Step 1: Create New Private Project

**Context**: Use GitLab UI to initiate a private repository.

Log in as admin, click 'New Project', select 'Create blank project', set visibility to Private, and name it (e.g., 'test-vuln-project').

> Project created with ID retrievable from URL (e.g., project_id=123).

### Step 2: Invite User as Developer

**Context**: Add the target user with Developer permissions.

Navigate to Project > Members > Invite Members, enter user email/username, select 'Developer' role, and send invitation.

> Invitation sent; user accepts to gain access.

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
- project-setup
