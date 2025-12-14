---
id: p-create-gitlab-project-invite
name: Create-GitLab-Project-and-Invite-Target
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.270Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - gitlab
  - initial-access
platforms:
  - Web
tools: []
commands: []
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Create-GitLab-Project-and-Invite-Target

## Summary

This procedure involves creating a temporary project on a GitLab instance and inviting a target user, such as an admin, to gain membership. This sets the stage for serializing the target's user object, including sensitive tokens, during a subsequent project export.

## Description

In the context of exploiting GitLab's project export vulnerability, an attacker with a low-privilege account creates a new repository and invites the target user via the UI. Once the target accepts, their full user object becomes part of the project data. Exporting the project serializes this data without redaction, exposing tokens. Prerequisites include a registered attacker account and knowledge of the target's username or email. Expected outcomes: target added to project, enabling token theft in next steps.

## Requirements

1. Registered low-privilege user account on the GitLab instance
2. Access to GitLab web UI (HTTPS on port 443)
3. Knowledge of target's username or email

## Defense

Defensive measures and detection strategies:

- Monitor project invitations for anomalous patterns (e.g., invites from new/low-priv users to admins)
- Implement rate limiting on project creation and member invites
- Educate users not to accept invites from unknown sources

## Objectives

1. Establish project membership with target user
2. Position for data serialization in export
3. Prepare for information disclosure

## Instructions

### Step 1: Register or Use Existing Account

**Context**: Ensure attacker has a valid account to create projects.

No command; use GitLab UI to log in or register a new user.

> Navigate to GitLab sign-up page and create account if needed.

### Step 2: Create Temporary Repository

**Context**: Initialize a new project to serve as the trap for the target.

No command; in GitLab UI, click "New Project" > "Create blank project", name it (e.g., "test-repo"), and initialize.

> Project created successfully; empty repo ready.

### Step 3: Invite Target User

**Context**: Add the target to project members to include their data in export.

No command; go to Project > Settings > Members > Invite Member, enter target's username/email, select role (e.g., Developer), and send invite. Wait for acceptance.

> Invitation sent; target must accept to proceed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[initial-access]]
