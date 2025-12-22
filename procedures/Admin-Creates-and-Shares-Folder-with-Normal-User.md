---
tags:
  - nextcloud
  - file-sharing
  - setup
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
updated_at: '2025-12-14T17:29:09.781Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 7b9de03c-f3f3-4ca2-8f3b-d8f546012ce3
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
---
# Admin-Creates-and-Shares-Folder-with-Normal-User

## Summary

This procedure outlines how an admin user creates a folder in Nextcloud and shares it with a normal user, enabling subsequent manipulation in a privilege escalation attack.

## Description

In the context of exploiting a vulnerability in Nextcloud's file sharing, the admin inadvertently sets up the attack by creating a folder in their home directory and sharing it with a low-privilege user with 'can share' permissions. This allows the normal user to access and re-share the folder, leading to unintended consequences during unsharing. The procedure assumes access to a running Nextcloud instance and requires admin credentials. Expected outcome is the folder being visible and shareable by the recipient.

## Requirements

1. Valid admin account in Nextcloud
2. Access to the web interface via browser
3. Normal user account (e.g., 'test') already created and active
4. No additional tools; uses built-in Nextcloud UI

## Defense

Defensive measures and detection strategies:

- Restrict sharing permissions to 'view only' for sensitive folders
- Enable admin notifications for all share actions
- Regularly audit shared folders and ownership chains

## Objectives

1. Create a target folder owned by admin
2. Share it with normal user to enable re-sharing
3. Set up conditions for privilege escalation

## Instructions

### Step 1: Log In as Admin

**Context**: Gain access to the admin account to perform privileged actions.

Log in to the Nextcloud web interface using admin credentials at the login page.

> Successful login redirects to the dashboard or Files section.

### Step 2: Create Folder

**Context**: Establish the target resource in the admin's home directory.

Navigate to the Files app, click the '+' icon or 'New folder' button, and name it 'sample_folder'. Confirm creation.

> The folder appears in the file list with admin as owner.

### Step 3: Share Folder

**Context**: Grant the normal user access to initiate the sharing chain.

Right-click the 'sample_folder', select 'Share', enter the normal user 'test', and set permissions to 'Can edit' and 'Can share'. Send the share.

> Share confirmation appears, and the folder is listed in the normal user's 'Shared with you'.

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
- [[setup]]
