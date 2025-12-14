---
id: 123e4567-e89b-12d3-a456-426614174002
name: Create-GitLab-Project
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.880Z'
tactics:
  - '[[Initial Access]]'
techniques: []
sub_techniques: []
tags:
  - gitlab
  - project-setup
commands: []
platforms:
  - Web
tools:
  - '[[tools/GitLab]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---

# Create-GitLab-Project

## Summary

This procedure creates a new project in GitLab to serve as the foundation for configuring the ZenTao integration in the XSS attack chain.

## Description

Creating a project allows access to integration settings where the malicious ZenTao server URL can be configured. This step assumes authenticated access and targets self-hosted GitLab with premium features.

## Requirements

1. Authenticated session in GitLab
2. Premium subscription for integrations
3. Project naming and visibility preferences

## Defense

Defensive measures and detection strategies:

- Audit project creation logs for suspicious activity
- Limit project creation to trusted users
- Enable notifications for new projects

## Objectives

1. Establish a project for integration setup
2. Ensure integration options are available
3. Prepare for ZenTao configuration

## Instructions

### Step 1: Navigate to Projects

**Context**: From the dashboard, access the new project creation interface.

No command; click 'New project' button.

> Select 'Create blank project' and fill in name, description, visibility.

### Step 2: Confirm Creation

**Context**: Save and verify the project exists.

No command; submit form.

> Expected: Redirect to project overview page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/GitLab]]

## Tags

- [[tools/GitLab]]
- [[project-setup]]
