---
tags:
  - gitlab
  - project-creation
  - persistence
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.663Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: e074a1c3-5726-4eeb-b030-283f90a08f07
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create Project and Reference Emoji in File

## Summary

This procedure creates a project in the target group and embeds a reference to the malicious custom emoji in a README.md file, persisting the XSS payload for execution when viewed.

## Description

By referencing the emoji with ':xssreplace:' in a markdown file like README.md, the GitLab renderer processes the custom emoji, triggering the vulnerable emoji_image_tag function. This makes the payload stored and executable for any user accessing the file in a public or internal repository. The procedure relies on GitLab's markdown rendering pipeline and requires project creation permissions.

## Requirements

1. Access to the 'xss_target' group with project creation rights
2. GitLab web UI or API access
3. Malicious emoji already created

## Defense

Defensive measures and detection strategies:

- Scan repository files for suspicious emoji references during commits
- Restrict custom emoji usage in markdown rendering
- Implement preview sanitization for project files

## Objectives

1. Embed the emoji reference to trigger rendering
2. Make the payload accessible to multiple users
3. Ensure persistence across repository views

## Instructions

### Step 1: Create New Project

**Context**: Set up a project within the group to host the infected file.

**Command** (GitLab UI):
Click 'New project' in the group, name it (e.g., 'test-project'), and initialize with a README.

> Expected output: Project created and empty repository ready.

### Step 2: Add and Commit File with Reference

**Context**: Edit README.md to include the emoji syntax.

**Command** (GitLab UI):
In the web editor, add ':xssreplace:' to README.md and commit.

> Expected output: Commit successful, file shows emoji reference in preview.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- persistence
