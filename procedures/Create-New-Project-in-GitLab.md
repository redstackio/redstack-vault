---
tags:
  - project-creation
  - gitlab-ui
type: procedure
tools:
  - '[[tools/Git]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:44.378Z'
sub_techniques: []
id: ec515f66-c0e0-4144-8e4e-b434d77f6722
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-New-Project-in-GitLab

## Summary

This procedure creates a new project in the GitLab instance using the web UI, setting the stage for branch and merge request operations.

## Description

Access the GitLab dashboard to create a blank project repository. This provides the foundation for injecting the XSS payload via branches. No CLI needed; uses browser-based UI.

## Requirements

1. Access to GitLab UI as a user with create project permissions
2. Running GitLab instance
3. Browser for navigation

## Defense

Defensive measures and detection strategies:

- Limit project creation to trusted users via role-based access
- Audit project creation logs in GitLab
- Use project templates to enforce standards

## Objectives

1. Initialize a new repository
2. Prepare for Git operations
3. Ensure project visibility for MRs

## Instructions

### Step 1: Navigate to New Project

**Context**: Log in and access the project creation interface.

**Instructions**: Go to http://gitlab.example.com, click 'New project', select 'Create blank project', enter name/description, set visibility (private/public), and create.

> Expected output: Project page loads with empty repo and clone URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Git]]

## Tags

- project-creation
- gitlab-ui
