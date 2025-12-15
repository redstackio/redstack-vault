---
tags:
  - nextcloud
  - file-sharing
  - re-share
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
updated_at: '2025-12-14T17:29:09.777Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: d9fa56d4-fe24-4163-acbf-4db91aee7de9
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Normal-User-Re-Shares-Folder-to-Admin

## Summary

This procedure describes how a normal user re-shares an admin-owned folder back to the admin in Nextcloud, creating a dependency that exploits the sharing vulnerability for privilege escalation.

## Description

As part of the attack, the low-privilege user logs in and accesses the shared folder from the admin. By re-sharing it back to the admin, a circular reference is formed, which causes the unshare action to incorrectly delete the original folder. This step requires the folder to already be shared to the normal user and uses the Nextcloud web UI. The outcome is the folder appearing in the admin's 'Shared with you' as if owned or shared by the normal user.

## Requirements

1. Valid normal user account (e.g., 'test') with access to the shared folder
2. Browser access to Nextcloud web interface
3. Prior share from admin to normal user
4. Admin user account details for re-sharing target

## Defense

Defensive measures and detection strategies:

- Disable re-sharing permissions for non-admin users
- Monitor share logs for unusual loops or re-shares
- Train admins to verify folder ownership before unsharing

## Objectives

1. Access the shared folder as normal user
2. Re-share to create misleading ownership
3. Position for deletion trigger

## Instructions

### Step 1: Log In as Normal User

**Context**: Switch to the attacker's perspective with low privileges.

Log in to Nextcloud using normal user credentials (e.g., 'test').

> Dashboard loads, showing access to shared items.

### Step 2: Locate Shared Folder

**Context**: Identify the admin-shared resource.

Navigate to Files or 'Shared with you', find 'sample_folder'.

> Folder displays with edit/share options enabled.

### Step 3: Re-Share to Admin

**Context**: Establish the circular share to confuse unshare logic.

Click the share icon on 'sample_folder', enter admin username, set basic share permissions, and confirm.

> Share succeeds, and admin sees it in their shared view.

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
- [[file-sharing]]
- [[re-share]]
