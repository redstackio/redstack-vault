---
id: proc-create-subdir-filecloud
tags:
  - directory-creation
  - persistence
  - filecloud
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:10.216Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Subdirectory-in-Shared-Folder

## Summary

This procedure uses the unauthenticated FileCloud UI to create a new subdirectory within a shared folder, establishing persistence for file uploads without authentication checks.

## Description

Once in public mode, the FileCloud file explorer allows directory creation via UI buttons, with no backend enforcement of user permissions. This affects shared paths like /SHARED/rpchllmd/CSAT, enabling attackers to organize uploaded content. The root cause is the lack of authentication and permission validation in public mode.

## Requirements

1. Successful access to the public mode UI from the prior procedure
2. Web browser session active on the target
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Disable directory creation in public/shared modes
- Require authentication for all write operations
- Audit logs for new folder creations in shared directories and correlate with IP/access patterns
- Use file integrity monitoring to detect unauthorized structures

## Objectives

1. Create a persistent storage location in the shared folder
2. Prepare for arbitrary file uploads
3. Expand control over the file system structure

## Instructions

### Step 1: Locate New Folder Option

**Context**: Identify the UI element for directory creation in the file explorer.

No command required.

In the FileCloud UI, look for the 'New Folder' or '+' icon in the toolbar.

> Expected output: Button is clickable and functional.

### Step 2: Create and Name Directory

**Context**: Input a name and confirm creation within the shared path.

No command required.

Click 'New Folder', enter a name (e.g., 'testdir'), and submit.

> The new directory appears immediately in the listing. Success if no permission errors occur.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- directory-creation
- persistence
- filecloud
