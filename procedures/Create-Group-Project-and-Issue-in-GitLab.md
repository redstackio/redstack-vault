---
id: uuid-create-resources
tags:
  - gitlab-ui
  - resource-creation
  - setup
type: procedure
tools: []
tactics: []
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-13T23:52:24.511Z'
sub_techniques: []
validated: true
---
# Create-Group-Project-and-Issue-in-GitLab

## Summary

This procedure uses the GitLab web interface to create a group, a project within it, and an issue, establishing the context where the injected XSS payload will be rendered in the group issue list.

## Description

Groups in GitLab aggregate projects, and issues are tracked per project but listed at the group level. The vulnerable Vue component displays assignee/author names (including full names) unsafely. This step simulates legitimate usage to store the payload. Prerequisites: Admin or user permissions in GitLab. Outcomes: Resources created, issue visible in group list for triggering.

## Requirements

1. GitLab user with create permissions
2. Running GitLab instance
3. Browser access to UI

## Defense

Defensive measures and detection strategies:

- Rate-limit resource creation to prevent abuse
- Validate inputs on group/project/issue forms
- Log creation events for anomaly detection

## Objectives

1. Build a minimal attack surface for payload display
2. Ensure the full name renders in the issue list
3. Prepare for victim navigation to the page

## Instructions

### Step 1: Create New Group

**Context**: Establish a top-level group to contain projects.

**Instructions**: Go to Groups > New Group, enter name (e.g., "VulnTestGroup"), visibility (private/public), and create.

### Step 2: Create Project in Group

**Context**: Add a project under the group for issue hosting.

**Instructions**: In the group, click New Project > Create blank project, name it (e.g., "VulnTestProject"), and create.

### Step 3: Create Issue in Project

**Context**: Generate an issue to appear in the group list, triggering name rendering.

**Instructions**: In the project, go to Issues > New Issue, add title (e.g., "Test Issue") and description, assign if needed, and submit.

> Expected output: Issue created, visible under Group > Issues. No errors in UI.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab-ui
- resource-creation
- setup
