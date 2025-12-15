---
tags:
  - nextcloud
  - filesystem-abuse
  - user-creation
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:57.040Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 98c9b9c8-4be7-4014-b3fc-d73ea0666369
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Create-User-Matching-Data-Subdirectory

## Summary

Create a user in Nextcloud with a username that matches an existing subdirectory in the 'data' directory, exploiting the lack of path validation to set up for deletion-based data removal.

## Description

Nextcloud's user creation does not check if data/{username} already exists as a directory (e.g., data/files_external or data/appdata_{random}). This procedure uses the group admin session to create such a colliding user, preparing the filesystem for unintended deletion. Outcomes include potential overwrite or conflict, leading to data loss on deletion.

## Requirements

1. Active group admin session
2. Knowledge of target subdirectories (e.g., via prior recon or common paths like 'files_external')
3. Access to user management UI

## Defense

Defensive measures and detection strategies:

- Add validation in user creation to check for existing data/{uid} paths
- Audit user creation against filesystem inventory
- Block user names matching known sensitive paths

## Objectives

1. Collide username with critical data path
2. Bypass validation for setup
3. Enable deletion to remove arbitrary data

## Instructions

### Step 1: Identify Target Subdirectory

**Context**: Determine a sensitive path like 'files_external' from Nextcloud structure.

No specific command; manual recon:

- Review app configs or filesystem if accessible

> Common targets: 'files_external', 'appdata_{instance-id}'.

### Step 2: Create Colliding User

**Context**: Use UI to create user with matching name.

No specific command; in Users section:

- Click 'Add user'
- Username: [target-subdir, e.g., files_external]
- Set minimal password and groups
- Submit

> User created; data/{username} may conflict but proceeds.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[path-collision]]
