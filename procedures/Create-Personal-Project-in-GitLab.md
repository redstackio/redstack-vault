---
tags:
  - gitlab
  - project-creation
type: procedure
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
updated_at: '2025-12-14T03:16:20.318Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 1da956b7-2cbc-4cc8-8826-15acb5afaff6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Personal-Project-in-GitLab

## Summary

This procedure creates a new personal project in GitLab under the user's namespace, which is necessary to associate the malicious username and trigger the XSS in the deletion modal.

## Description

Personal projects in GitLab are tied to the user's namespace and render user details like the username in administrative interfaces. This step sets up the environment for the vulnerability exploitation without using custom groups, ensuring the modal renders the stored payload.

## Requirements

1. Authenticated GitLab session
2. Permissions to create projects
3. Web browser

## Defense

Defensive measures and detection strategies:

- Limit project creation to verified users
- Audit new project creations for suspicious patterns
- Implement rate limiting on project operations

## Objectives

1. Establish a project linked to the malicious username
2. Enable access to deletion settings
3. Prepare for impact simulation on other users

## Instructions

### Step 1: Access Project Creation

**Context**: Navigate from the dashboard to start a new project.

Click the '+' icon or 'New project' button on the GitLab dashboard.

**Expected Output**: Project creation wizard opens.

### Step 2: Configure Personal Project

**Context**: Select personal namespace to avoid group-specific rendering differences.

Choose 'Create blank project', set visibility if needed, and ensure it's under your personal username namespace (not a group).

Click 'Create project'.

**Expected Output**: Project dashboard loads with the new repository.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[gitlab]]
- [[project-setup]]
