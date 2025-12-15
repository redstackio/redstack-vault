---
id: uuid-1
tags:
  - gitlab
  - external-user
  - setup
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
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:30:27.332Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Create-External-User-in-GitLab

## Summary

This procedure sets up an external user in GitLab, restricting their visibility to only invited projects and groups, as a prerequisite for testing privilege escalation via project tokens.

## Description

In GitLab, external users are intended to have limited access, but this setup allows testing how tokens created by such users can bypass restrictions. The process involves admin intervention to flag a user as external, simulating a scenario where an external maintainer escalates privileges. Expected outcome: User logs in with external status, seeing only personal or invited content.

## Requirements

1. Admin privileges on the GitLab instance
2. Access to the admin panel (e.g., https://gitlab.domain.com/admin)
3. Existing user account to modify

## Defense

Defensive measures and detection strategies:

- Monitor admin panel access logs for user status changes
- Implement role-based access controls to limit external user invitations
- Audit external user creations via GitLab audit events

## Objectives

1. Establish a test external user for escalation simulation
2. Verify external restrictions are applied
3. Prepare for maintainer invitation

## Instructions

### Step 1: Access Admin Panel

**Context**: Log in as admin and navigate to user management.

No command needed; use web UI at `/admin/users` to search for the target username.

> Locate the user and click edit.

### Step 2: Enable External Status

**Context**: Flag the user as external to limit visibility.

In the edit page `/admin/users/<username>/edit`, check the "External" box and save changes.

> User status updated; external users cannot see internal projects unless invited.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- external-user
- admin-setup
