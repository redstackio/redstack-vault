---
id: proc-uuid-1
name: Create-GitLab-Project-and-Init-README
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.897Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - gitlab
  - project-creation
commands: []
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Create-GitLab-Project-and-Init-README

## Summary

This procedure sets up a new GitLab project and initializes a basic README file, providing the foundation for injecting malicious content in subsequent steps of an XSS attack.

## Description

In the context of exploiting GitLab's RDoc XSS vulnerability, this step involves using a legitimate GitLab account to create a new repository. The process leverages GitLab's standard project creation features, which do not require elevated privileges beyond basic user access. Once created, an initial README is added to ensure the repository renders markup content, setting the stage for payload injection. Expected outcomes include a functional repository ready for editing, with no immediate alerts triggered.

## Requirements

1. Valid GitLab credentials with project creation permissions
2. Access to the GitLab web interface via a browser
3. Internet connectivity to the GitLab instance

## Defense

Defensive measures and detection strategies:

- Monitor for rapid project creation from new or suspicious accounts
- Implement rate limiting on project creation APIs
- Review audit logs for unusual repository activity

## Objectives

1. Establish a controlled environment for payload hosting
2. Prepare the repository for markup-based exploitation
3. Validate access to GitLab features without triggering defenses

## Instructions

### Step 1: Access GitLab Dashboard

**Context**: Log in to initiate project creation.

Navigate to your GitLab instance and sign in with valid credentials. Click the 'New Project' button on the dashboard.

### Step 2: Create Blank Project

**Context**: Set up an empty repository.

Fill in the project name, description (optional), and visibility settings. Select 'Create blank project' and confirm.

### Step 3: Initialize README

**Context**: Add the initial file to enable rendering.

In the new project, click 'New file', name it README, add basic content like '# Project README', and commit.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[project-setup]]
