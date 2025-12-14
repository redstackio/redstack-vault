---
id: uuid-2
tags:
  - gitlab
  - invitation
  - maintainer
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
updated_at: '2025-12-14T17:30:27.330Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Invite-External-User-as-Maintainer

## Summary

Invites an external user to a GitLab project with maintainer privileges, enabling them to create project access tokens without admin involvement.

## Description

This step grants the external user sufficient permissions to access project settings and generate tokens. In the vulnerability, this leads to escalation because the token is tied to an internal bot user. Target environment: Any GitLab project. Prerequisites: Internal user with invite permissions.

## Requirements

1. Internal user account with project owner or maintainer role
2. External user account created
3. Project access via web UI

## Defense

Defensive measures and detection strategies:

- Restrict external user invitations to trusted roles
- Log all member additions and review for external users
- Use group-level policies to limit external maintainer access

## Objectives

1. Grant maintainer role to external user
2. Enable token creation capability
3. Confirm access without escalating visibility prematurely

## Instructions

### Step 1: Navigate to Project Members

**Context**: Access the project's member management.

Go to project dashboard > Settings > Members.

> Page loads with current members list.

### Step 2: Invite External User

**Context**: Add the external user with Maintainer role.

Click "Invite members", enter external username/email, select Maintainer, and send invitation.

> Invitation sent; external user accepts via email or UI, gaining access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- invitation
- maintainer-role
