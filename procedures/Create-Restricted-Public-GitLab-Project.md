---
id: proc-gitlab-create-restricted-project-001
tags:
  - gitlab
  - setup
  - project-creation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:29.128Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Restricted-Public-GitLab-Project

## Summary

This procedure sets up a public GitLab project with all features restricted to project members only, creating a test environment where non-members should be denied access to internal elements like milestones.

## Description

In GitLab, public projects can be configured to limit visibility of features such as issues, merge requests, and milestones to authenticated project members. This procedure involves creating such a project via the UI, which is a prerequisite for demonstrating access control flaws in the API. The target environment is any GitLab instance, and outcomes include a project ID usable for further testing. Prerequisites include a GitLab account with project creation rights.

## Requirements

1. GitLab account with permissions to create projects
2. Access to GitLab UI (e.g., https://gitlab.com)
3. No special tools needed beyond a web browser

## Defense

Defensive measures and detection strategies:

- Enforce consistent access controls across UI and API endpoints
- Monitor API calls for anomalous searches on restricted projects
- Use role-based access control (RBAC) auditing tools to verify permissions

## Objectives

1. Establish a controlled public project with member-only restrictions
2. Obtain project ID for API testing
3. Simulate a real-world restricted project setup

## Instructions

### Step 1: Create New Public Project

**Context**: Log in to GitLab and initiate project creation to set visibility to public.

Navigate to https://gitlab.com/projects/new and fill in project details, setting visibility level to 'Public'.

### Step 2: Configure Restrictions

**Context**: Access project settings to disable features for non-members.

Go to project settings at https://gitlab.com/<namespace>/<project>/edit and under 'Permissions and group features', set all options (Issues, Merge Requests, Milestones, etc.) to 'Only Project Members + Authenticated Users' or stricter.

**Expected Output**: Settings saved, confirmation message in UI.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- project-setup
