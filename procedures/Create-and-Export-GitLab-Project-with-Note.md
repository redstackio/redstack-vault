---
tags:
  - gitlab
  - project-setup
type: procedure
tools:
  - '[[tools/CarrierWave]]'
  - '[[tools/GitLab]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 3d514a1e-21ee-4674-9b31-77d4ca485f83
created_at: '2025-12-11T03:47:39.488Z'
updated_at: '2025-12-11T03:47:39.488Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Create and Export GitLab Project with Note

## Summary

This procedure sets up a basic GitLab project with an issue and note, then exports it for further modification in SSRF attacks.

## Description

In the context of exploiting SSRF in GitLab's import feature, this creates the foundation by generating exportable project data. It targets GitLab version 12.8.7-ee on Ubuntu 18.04, ensuring the note is present for later JSON manipulation.

## Requirements

1. Access to GitLab web interface with project creation permissions.
2. GitLab instance vulnerable to SSRF in project imports.
3. No special tools beyond the GitLab UI.

## Defense

Defensive measures and detection strategies:

- Monitor project export and import activities for anomalies.
- Implement strict validation on imported project data.

## Objectives

1. Create a project structure for export.
2. Include a note for attachment modification.
3. Obtain an export file for editing.

## Instructions

### Step 1: Create New Project

**Context**: Initiate a new project in GitLab to serve as the base.

Use GitLab UI to create a new project.

### Step 2: Create Issue

**Context**: Add an issue to associate notes with.

Create an issue in the project via GitLab UI.

### Step 3: Add Note to Issue

**Context**: Create a note on the issue for export.

Add a note to the issue using GitLab UI.

### Step 4: Export Project

**Context**: Export the project data into a tar.gz file.

Use GitLab's export feature to download the project as tar.gz.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/GitLab]]

## Tags

- [[tools/GitLab]]
- #project-setup
