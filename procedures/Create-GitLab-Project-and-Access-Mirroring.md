---
id: proc-create-gitlab-project
tags:
  - gitlab
  - project-creation
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T04:09:00.706Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
---

# Create GitLab Project and Access Mirroring

## Summary

This procedure authenticates to GitLab, creates a new project, and navigates to the repository mirroring settings to prepare for payload injection.

## Description

As an authenticated user, create a project to access the mirroring feature, which is vulnerable to SSRF and CRLF injection. This step requires a valid GitLab account with project creation permissions and assumes web access to the instance.

## Requirements

1. Valid GitLab username/password or session
2. Web browser access to GitLab UI
3. Permissions for project creation

## Defense

Defensive measures and detection strategies:

- Limit project creation to trusted users
- Audit logs for new project creations
- Rate-limit UI actions

## Objectives

1. Establish a project for mirroring exploitation
2. Reach the vulnerable mirroring configuration
3. Prepare for request interception

## Instructions

### Step 1: Sign In to GitLab

**Context**: Authenticate to gain session.

**Command** (browser action, no CLI):
No CLI command; use web UI to login at /users/sign_in.

> Enter credentials. Expected output: Dashboard access.

### Step 2: Create New Project

**Context**: Initiate project creation.

**Command** (browser action):
Click 'New Project' > 'Create blank project'.

> Fill name/namespace. Expected output: Project page loads.

### Step 3: Navigate to Mirroring Settings

**Context**: Access the vulnerable endpoint.

**Command** (browser action):
Go to Settings > Repository > Mirroring repositories.

> Expected output: Form for adding mirrors visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[project-creation]]

