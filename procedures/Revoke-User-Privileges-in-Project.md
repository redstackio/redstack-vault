---
tags:
  - privilege-revocation
  - access-control
  - mavenlink
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:28:44.686Z'
sub_techniques: []
id: 89393bc1-0086-4a0d-a3c2-2854da54fbb9
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Revoke-User-Privileges-in-Project

## Summary

Downgrades a user's role in a Mavenlink project to remove invite capabilities, testing if ongoing sessions respect the change.

## Description

Admin User A edits the project settings to reduce User B to Collaboration role, explicitly removing invite permissions. This simulates a security response like deranking a user. The flaw allows prior sessions to ignore this. Expected: Permissions updated system-wide, but not enforced on pending actions.

## Requirements

1. User A admin session
2. Active project with User B assigned
3. Edit permissions interface access

## Defense

Defensive measures and detection strategies:

- Propagate privilege changes immediately to all sessions
- Invalidate active dialogs on role updates
- Alert on privilege modifications

## Objectives

1. Enforce access control changes
2. Create condition for escalation test
3. Verify revocation in settings

## Instructions

### Step 1: Navigate to Project Settings

**Context**: Access admin controls for the project.

In Browser X as User A, open the project and go to settings or user management section.

### Step 2: Edit and Save User B Role

**Context**: Downgrade to block invites.

Select User B, change role to Collaboration, uncheck invite privilege if separate, and save changes.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[privilege-revocation]]
- [[access-control]]
- [[mavenlink]]
