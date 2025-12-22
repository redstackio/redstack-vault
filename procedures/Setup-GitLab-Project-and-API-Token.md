---
tags:
  - gitlab
  - setup
  - authentication
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:26:27.998Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: b3b614cc-bd07-4e2c-878e-7613cbd4a0a3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Setup-GitLab-Project-and-API-Token

## Summary

This procedure prepares a GitLab instance for exploitation by enabling the package registry, creating a project, and generating a personal access token for API authentication.

## Description

In the context of exploiting GitLab's path traversal vulnerability, initial setup is required to enable the package registry feature (if disabled) and create an authenticated project. A personal access token with 'api' and 'write_package_registry' scopes is generated to allow subsequent API requests for package uploads. This step assumes attacker has developer-level access to the GitLab instance.

## Requirements

1. Access to GitLab UI as a user with admin or maintainer privileges
2. Enabled package registry at instance level (Admin Area > Settings > Packages)
3. Network access to GitLab web interface on port 80

## Defense

Defensive measures and detection strategies:

- Disable package registry if unused
- Monitor token creation events in GitLab audit logs
- Enforce least-privilege for API scopes

## Objectives

1. Enable package registry for the target project
2. Create a project to host the exploit
3. Generate and store API token securely

## Instructions

### Step 1: Enable Package Registry

**Context**: Activate the package registry feature instance-wide to make the vulnerable endpoint available.

Navigate to GitLab Admin Area > Settings > General > Visibility and access controls, and ensure 'Packages' is enabled.

### Step 2: Create Project

**Context**: Set up a new project where package registry can be used.

In GitLab UI, create a new project (e.g., via /projects/new). Package registry is enabled by default once the feature is active.

**Expected Output**: Project created with ID (e.g., 2), visible in dashboard.

### Step 3: Generate API Token

**Context**: Create a personal access token for authenticating API requests.

Go to User Settings > Access Tokens, name the token (e.g., 'exploit'), select scopes 'api' and 'write_package_registry', and generate. Save the token to a file named 'token'.

**Expected Output**: Token string saved to 'token' file.

**Success Indicators**:
- Token authenticates a test API call (e.g., GET /api/v4/user)

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
- [[setup]]
