---
id: proc-gitlab-create-public-project
tags:
  - gitlab
  - project-creation
  - public-project
type: procedure
tools: []
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
updated_at: '2025-12-14T03:16:31.017Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Public-Project-in-GitLab

## Summary

This procedure outlines creating a new public project in GitLab to serve as a vector for hosting malicious integrations, enabling broad victim exposure in a persistent XSS attack.

## Description

In the context of exploiting GitLab's custom issue tracker, an attacker first creates a public project to ensure the vulnerable configuration is accessible to any user viewing the Issues page. This step requires a valid GitLab account but no elevated privileges. The public visibility level allows unauthenticated access, increasing the attack surface for payload delivery.

## Requirements

1. Valid GitLab user account with project creation permissions.
2. Web browser for navigation.
3. No network restrictions blocking GitLab access.

## Defense

Defensive measures and detection strategies:

- Enforce project visibility controls to limit public project creation.
- Monitor for anomalous project creations from low-privilege accounts.
- Implement rate limiting on project setup endpoints.

## Objectives

1. Establish a persistent, public project for payload hosting.
2. Ensure accessibility to lure victims without authentication.
3. Prepare foundation for integration configuration.

## Instructions

### Step 1: Navigate to Project Creation

**Context**: Access the GitLab interface to initiate project setup.

Log in to your GitLab account and navigate to `/projects/new` via the top menu (New Project > Create blank project).

### Step 2: Fill Project Form

**Context**: Provide details to create the project with public visibility.

Enter a project name (e.g., "Test Public Project"), description if needed, and set Visibility Level to "Public". Click "Create project".

**Expected Output**: Redirect to the new project's dashboard with public access confirmed.

### Step 3: Verify Public Access

**Context**: Confirm the project is publicly viewable.

Log out or use an incognito window to access the project URL; ensure the dashboard loads without login prompts.

**Expected Output**: Project accessible to unauthenticated users.

**Success Indicators**:
- Project created without errors.
- Public visibility active.

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
- [[project-creation]]
