---
id: proc-gitlab-create-project-invite
tags:
  - gitlab
  - project-setup
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:36.648Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Private-Project-and-Invite-Maintainer

## Summary

This procedure sets up a private GitLab project and grants maintainer access to a target user, establishing the foundation for testing permission-based access controls.

## Description

In the context of GitLab authorization testing, create a new private project as the owner (User A) and invite another user (User B) with maintainer permissions. This allows User B full access initially, including the ability to add the project to security features. The private visibility ensures sensitive data is not publicly accessible, simulating a real internal project scenario. Expected outcome: User B can interact with the project as a maintainer before any permission changes.

## Requirements

1. GitLab account with permissions to create projects (e.g., free tier on GitLab.com)
2. Email or username of the target user (User B)
3. Web browser access to GitLab interface

## Defense

Defensive measures and detection strategies:

- Enforce role-based access control (RBAC) audits regularly
- Monitor project member invitations via GitLab audit logs

## Objectives

1. Establish controlled environment for permission testing
2. Grant initial high-level access to simulate insider threat
3. Prepare project for security scanning integration

## Instructions

### Step 1: Log In and Create Project

**Context**: Access GitLab as the project owner and initiate a new private project.

Navigate to GitLab.com, log in as User A, click "New project", select "Create blank project", name it (e.g., "Test-Private-Project"), set visibility to "Private", and create it.

> This creates an isolated project where only invited members can access.

### Step 2: Invite Maintainer

**Context**: Add User B with elevated permissions to enable dashboard setup.

Go to Project > Settings > Members, click "Invite members", enter User B's username or email, select "Maintainer" role, and send invitation.

> User B accepts the invite and gains maintainer access, allowing project configuration.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[project-setup]]
