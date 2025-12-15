---
tags:
  - nextcloud
  - data-deletion
  - rce
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
  - '[[Data Destruction]]'
updated_at: '2025-12-14T17:29:57.036Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 64c32a41-2f78-4fd8-9801-94f1b70b072d
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Privilege Escalation]]'
  - '[[Data Destruction]]'
---
# Delete-User-to-Remove-Data-Directory

## Summary

Delete the specially created user in Nextcloud, triggering removal of the corresponding data/{username} directory and erasing arbitrary critical data, with potential for .htaccess removal leading to RCE under Apache.

## Description

User deletion in Nextcloud recursively removes the data/{user} directory without verifying its contents, allowing deletion of non-user data like app directories. Under Apache, this can remove .htaccess protections, exposing PHP files for direct execution as www-data. This step completes the exploit chain, causing data destruction and privilege escalation.

## Requirements

1. Active group admin session
2. The colliding user from previous step
3. Server access to verify filesystem changes (optional for validation)

## Defense

Defensive measures and detection strategies:

- Validate data/{user} contents before deletion to ensure only user files
- Monitor filesystem deletions in 'data' directory via audit logs
- Use immutable .htaccess files or non-Apache servers to prevent exposure

## Objectives

1. Remove target data directory
2. Achieve data destruction
3. Enable RCE if .htaccess affected

## Instructions

### Step 1: Select User for Deletion

**Context**: Locate the malicious user in the list.

No specific command; in Users UI:

- Search or filter for [username, e.g., files_external]

> User details load.

### Step 2: Execute Deletion

**Context**: Trigger the delete action.

No specific command; in UI:

- Click 'Delete user' or actions menu
- Confirm deletion prompt

> User removed; filesystem rmdir on data/{username} executes, deleting contents. Under Apache, check for exposed PHP access (e.g., curl direct to .php files).

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation
- [[Data Destruction]] Data Destruction

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[nextcloud]]
- [[user-deletion]]
