---
tags:
  - project-linking
  - xss-persistence
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.386Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 82401065-c6de-4720-befb-a45ddecc77a2
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Add-File-as-Project-in-Conversation

## Summary

This procedure links the malicious file as a project in the Nextcloud Talk conversation, persisting the XSS payload in the projects tab display.

## Description

Projects in Talk conversations allow linking external files, but the filename is echoed without encoding when hovered, enabling the XSS. This step embeds the payload in a collaborative context the victim is likely to interact with.

## Requirements

1. Active conversation with victim invited
2. Shared malicious file accessible
3. Permissions to add projects in the conversation

## Defense

Defensive measures and detection strategies:

- Encode all user-input filenames in project displays
- Disable or restrict project linking from untrusted shares
- Log and alert on project additions with suspicious content

## Objectives

1. Associate the malicious file with the conversation
2. Ensure the filename is displayed in the projects tab
3. Set up for victim interaction without immediate execution

## Instructions

### Step 1: Access Projects Tab

**Context**: Open the conversation and navigate to project management.

Join the conversation and click on the 'Projects' section.

### Step 2: Link the Malicious File

**Context**: Add the shared file as a project link.

Click 'Add a project' > 'Link to a file', browse to the shared malicious file, and confirm the addition.

**Expected Output**: File appears in the projects list with its original filename.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[projects]]
- [[spreed]]
