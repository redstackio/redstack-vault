---
id: proc-uuid-1
tags:
  - gitlab
  - setup
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:28.227Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Private-Group-and-Project-in-GitLab

## Summary

This procedure sets up a private group and a nested private project in GitLab, simulating a sensitive target namespace that will be exploited for unauthorized access.

## Description

In a GitLab environment, create a new private group to isolate resources, then add a private project within it. This establishes the target for IDOR exploitation, where the group ID (e.g., 7) becomes the key parameter for tampering. Prerequisites include admin or creator-level access to the GitLab instance. Expected outcomes: A fully private namespace inaccessible to unauthorized users initially.

## Requirements

1. Access to GitLab as a user with group creation privileges
2. Web browser for navigation
3. Knowledge of GitLab UI paths

## Defense

Defensive measures and detection strategies:

- Enforce strict role-based access control (RBAC) for group creation
- Monitor for unusual group/project creation patterns via audit logs

## Objectives

1. Establish isolated private resources
2. Obtain group ID for exploitation targeting
3. Verify privacy before attack simulation

## Instructions

### Step 1: Create Private Group

**Context**: Navigate to the groups creation page and set visibility to private.

No command; use GitLab UI: Visit http://gitlab-instance/groups/new, enter name (e.g., 'private-group'), set visibility to Private, and create.

> Note the generated group ID (e.g., 7) from the URL or API.

### Step 2: Create Project in Private Group

**Context**: Nest a private project within the new group.

No command; use GitLab UI: Go to http://gitlab-instance/projects/new?namespace_id=7, name it 'secret-project', set visibility to Private, and create.

> The project is now hidden from non-members.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[setup]]
