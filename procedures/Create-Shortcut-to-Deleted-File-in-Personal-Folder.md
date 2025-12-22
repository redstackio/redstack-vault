---
tags:
  - authorization-bypass
  - shortcut-exploit
  - file-access
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
updated_at: '2025-12-14T17:29:09.935Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 7755174c-9a19-4d5b-a58c-2f23508fb11e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Shortcut-to-Deleted-File-in-Personal-Folder

## Summary

This procedure exploits the shortcut feature in Lark Technologies to create a reference to a deleted file within a user's personal folder, bypassing admin-imposed deletion restrictions and enabling indirect access.

## Description

The Lark application allows users to create shortcuts to files, but the mechanism does not validate the target file's deletion status. By referencing a recently deleted shared file's ID or path in a personal folder, a regular user can establish a persistent link. This targets the web/cloud-based file sharing system and requires a valid user session. Expected outcome: A functional shortcut in the personal folder that points to inaccessible content, setting up for data retrieval.

## Requirements

1. Regular user account in Lark with knowledge of the deleted file's ID
2. The file must have been shared with the user prior to deletion
3. Access to personal folders in the Lark UI

## Defense

Defensive measures and detection strategies:

- Validate shortcut targets against current file status during creation
- Log all shortcut creations with file ID references for anomaly detection
- Implement server-side checks to block shortcuts to deleted or restricted files

## Objectives

1. Establish an indirect reference to restricted deleted content
2. Bypass deletion validation in the shortcut system
3. Prepare for content retrieval via folder operations

## Instructions

### Step 1: Access Personal Folder

**Context**: Open the user's personal space to add the shortcut.

**Actions**:
- Log in to Lark as the regular user.
- Navigate to 'My Folders' or personal storage section.

> Personal folder loads, showing existing files; no errors expected.

### Step 2: Create Shortcut to Deleted File

**Context**: Use the UI to reference the deleted file, exploiting the lack of validation.

**Actions**:
- Select 'Create Shortcut' or 'Add Link' option.
- Enter the path or ID of the deleted shared file.
- Save the shortcut in the personal folder.

> Shortcut is added without rejection; it appears as a link in the folder view.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authorization-bypass]]
- [[shortcut-exploit]]
- [[file-access]]
