---
id: proc-gitlab-demote-to-guest
tags:
  - gitlab
  - permission-change
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
updated_at: '2025-12-14T17:29:36.612Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Demote-User-to-Guest-Access

## Summary

This procedure reduces a user's role in a GitLab project from maintainer to guest, simulating a permission revocation that should limit access but exposes a bypass in security features.

## Description

As the project owner (User A), modify member roles in the private project settings to downgrade User B from maintainer to guest. Guest role typically allows only read-only access to public info, but in this vulnerability, it fails to revoke security dashboard visibility. This step is crucial for demonstrating the authorization flaw. Expected outcome: Role updated, direct access restricted, but dashboard access persists.

## Requirements

1. Owner or maintainer role in the project (User A)
2. Target user listed as member
3. Access to project settings

## Defense

Defensive measures and detection strategies:

- Audit role changes via GitLab events API
- Enforce re-validation of dashboard permissions on role updates

## Objectives

1. Revoke elevated permissions to test access controls
2. Simulate insider threat demotion scenario
3. Highlight failure in permission enforcement

## Instructions

### Step 1: Access Project Members

**Context**: Open the members management interface.

Log in as User A, navigate to Project > Manage > Members.

> Displays current members and roles.

### Step 2: Change Role to Guest

**Context**: Downgrade the target user's permissions.

Click the pencil icon next to User B, select "Guest" from the role dropdown, and save changes.

> Role updated; User B notified of change.

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
- [[permission-change]]
