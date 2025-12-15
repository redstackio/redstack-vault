---
id: proc-uuid-1
tags:
  - group-management
  - hackerone
  - setup
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:48.173Z'
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
# Create-HackerOne-Group

## Summary

This procedure creates a new group within a HackerOne enterprise program, serving as the initial setup for exploiting the group management vulnerability.

## Description

In the context of testing HackerOne's enterprise features, creating a group via the web interface allows subsequent addition of members and modifications that trigger the infinite loop. The group is managed through the program's settings and can be accessed via API endpoints like /groups.json. Prerequisites include authenticated access to the program with group management permissions.

## Requirements

1. Valid HackerOne account with access to the target enterprise program
2. Permissions to manage groups in the program settings
3. Web browser for interface navigation

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls (RBAC) to limit group creation to authorized users
- Monitor for unusual group creation patterns in audit logs

## Objectives

1. Establish a controllable group for the exploit chain
2. Verify group creation via API to ensure persistence
3. Prepare for member addition without triggering alerts

## Instructions

### Step 1: Access Group Management

**Context**: Log in to HackerOne and navigate to the target program's group management section to initiate group creation.

No specific command required; use the web UI at https://hackerone.com/[PROGRAM]/groups.

> Click 'Add Group' and provide a name like 'Testing'. Save the group.

### Step 2: Verify Creation

**Context**: Confirm the group exists and is retrievable via API.

Access https://hackerone.com/[PROGRAM]/groups.json in the browser or via API client.

> Expected: JSON array including the new group with its ID and name.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- group-management
- hackerone
