---
tags:
  - project-creation
  - privilege-assignment
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
updated_at: '2025-12-14T17:28:44.693Z'
sub_techniques: []
id: c0319ce7-bed7-4b23-9365-f433058d8ff3
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Create-Project-and-Assign-Privileges

## Summary

Creates a test project in Mavenlink and grants elevated privileges to a secondary user to enable invite functionality.

## Description

This leverages admin rights to set up a controlled environment where User B gains temporary Team Lead access, including invite permissions. The project creation UI allows role assignment during setup. This is crucial for the escalation, as it provides the initial high privilege before revocation. Expected: Project ready with User B empowered.

## Requirements

1. Active User A session with admin privileges
2. Project creation permissions
3. User B account details for invitation

## Defense

Defensive measures and detection strategies:

- Audit privilege assignments in projects
- Require approval for role changes
- Log all user additions to projects

## Objectives

1. Establish project for testing
2. Grant invite-capable role to User B
3. Prepare for session-based exploitation

## Instructions

### Step 1: Initiate Project Creation

**Context**: Use admin interface to build the test scenario.

In Browser X as User A, navigate to the projects section and click 'Create Project', filling in basic details like name and description.

### Step 2: Assign Role to User B

**Context**: Elevate User B to Team Lead.

In the user management tab during creation, search for User B, select 'Consultant' role, and set to Team Lead; save the project.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[project-creation]]
- [[privilege-assignment]]
- [[mavenlink]]
