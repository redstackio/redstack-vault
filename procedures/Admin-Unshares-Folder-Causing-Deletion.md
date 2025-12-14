---
tags:
  - nextcloud
  - file-sharing
  - deletion
  - data-loss
type: procedure
tools: []
tactics:
  - '[[Resource Development]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data Destruction]]'
updated_at: '2025-12-14T17:29:09.774Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 94af4181-35c7-4cda-b728-b01d8ce72cdb
validated: true
mitre_tactics:
  - '[[Resource Development]]'
mitre_techniques:
  - '[[Data Destruction]]'
---
# Admin-Unshares-Folder-Causing-Deletion

## Summary

This procedure exploits the core vulnerability by having the admin unshare the re-shared folder, resulting in the deletion of the original admin-owned folder in Nextcloud.

## Description

The final step in the privilege escalation involves the admin navigating to their 'Shared with you' section and unsharing the folder, which due to improper handling of re-sharing, deletes the original folder from the admin's home directory. This leads to unauthorized data loss without the admin's intent or awareness. Requires the prior sharing loop and admin credentials. Outcome is permanent folder deletion, potentially recoverable from recycle bin if enabled.

## Requirements

1. Valid admin account
2. Browser access to Nextcloud
3. Folder already re-shared from normal user to admin
4. No admin awareness of the sharing loop

## Defense

Defensive measures and detection strategies:

- Implement confirmation dialogs for unshare actions on owned folders
- Use ownership verification before deletion in sharing logic
- Enable recycle bin and backups for all users
- Log all unshare and deletion events for audit

## Objectives

1. Trigger the unshare action as admin
2. Exploit propagation to delete original folder
3. Achieve data destruction from low privilege

## Instructions

### Step 1: Log In as Admin

**Context**: Return to admin session to perform the triggering action.

Log in to Nextcloud with admin credentials.

> Access to Files and shared sections granted.

### Step 2: Navigate to Shared with You

**Context**: Locate the misleading shared folder.

Go to Files app > Shared with you, find 'sample_folder' listed as shared from normal user.

> Folder appears removable without ownership indication.

### Step 3: Unshare Folder

**Context**: Execute the vulnerable action leading to deletion.

Click the share icon or right-click and select 'Unshare' or remove the share.

> Unshare completes, but original folder in home directory is deleted unexpectedly.

## MITRE ATT&CK Mapping

### Tactics

- [[Resource Development]] Impact

### Techniques

- [[Data Destruction]] Data Destruction

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[file-sharing]]
- [[deletion]]
- [[data-loss]]
