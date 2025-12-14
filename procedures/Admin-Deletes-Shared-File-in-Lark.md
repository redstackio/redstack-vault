---
tags:
  - setup
  - file-deletion
  - admin-action
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:09.938Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: 0769727e-2800-4d0a-b60a-737edcfd37f1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Admin-Deletes-Shared-File-in-Lark

## Summary

This procedure simulates the administrative action of deleting a shared file in Lark Technologies' platform, enforcing restrictions that should prevent further access by users. It serves as a prerequisite for testing bypass vulnerabilities in file handling.

## Description

In the Lark file sharing application, administrators can delete shared files to remove access for all users. This action is intended to permanently block downloads and usage, marking the file as inaccessible. However, this setup exposes potential flaws in related features like shortcuts. The procedure targets the web-based Lark interface and requires admin privileges. Expected outcome: The file is deleted, and direct access attempts fail, confirming the restriction is in place.

## Requirements

1. Admin credentials for Lark account
2. Access to a shared file that regular users have previously viewed
3. Web browser with JavaScript enabled for the Lark UI

## Defense

Defensive measures and detection strategies:

- Implement role-based access controls (RBAC) to log all admin deletion actions
- Monitor for unusual file access patterns post-deletion using audit logs
- Enforce multi-factor approval for sensitive file deletions

## Objectives

1. Remove shared file access to protect sensitive data
2. Verify deletion enforcement in the UI
3. Set up conditions for vulnerability testing

## Instructions

### Step 1: Navigate to Shared File

**Context**: Locate the target shared file in the Lark dashboard to prepare for deletion.

**Actions**:
- Log in to Lark as an admin.
- Go to the shared folders section and select the file.

> This positions the file for deletion; expect to see file details and sharing metadata.

### Step 2: Initiate Deletion

**Context**: Execute the deletion to enforce access restrictions.

**Actions**:
- Click the delete option in the file menu.
- Confirm the deletion in the prompted dialog.

> Deletion completes with a success message; the file disappears from shared views.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[file-deletion]]
- [[admin-action]]
