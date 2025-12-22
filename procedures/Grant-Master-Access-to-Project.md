---
tags:
  - access-control
  - gitlab
type: procedure
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:16:20.315Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[Default Accounts]]'
id: ca03f5f0-a771-475f-bc15-b9b80cf512e1
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Grant-Master-Access-to-Project

## Summary

This optional procedure invites another user to the personal project and grants them Master access, simulating a victim who can trigger the XSS in their browser session.

## Description

Master access allows full control, including deletion, which renders the project owner's username in the modal. This step expands the attack surface to other authenticated users.

## Requirements

1. Ownership of the project
2. Email or username of target user
3. Project members management access

## Defense

Defensive measures and detection strategies:

- Require approval for role changes
- Log all access grants and review for anomalies
- Use role-based access control (RBAC) with least privilege

## Objectives

1. Simulate multi-user impact
2. Enable victim to reach deletion modal
3. Demonstrate scoped JavaScript execution

## Instructions

### Step 1: Navigate to Members Settings

**Context**: Access the project members page to add users.

In the project, go to Project information > Members.

**Expected Output**: Members list loads.

### Step 2: Invite and Assign Role

**Context**: Add the user and set permissions to Master.

Click 'Invite members', enter the username/email, select 'Master' role, and send invitation.

**Expected Output**: Invitation sent; user gains access upon acceptance.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[Default Accounts]]

## Commands Used

-

## Tools Used

-

## Tags

- [[access-grant]]
- [[gitlab]]
