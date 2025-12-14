---
tags:
  - authentication
  - gitlab
  - project-creation
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:47:18.322Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: dbc3bb77-d3b6-4a23-aa1d-80c5de8c8d8b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-and-Create-GitLab-Project

## Summary

This procedure outlines signing into a GitLab instance with valid credentials and creating a new public project to serve as the foundation for injecting XSS payloads in issues.

## Description

In the context of exploiting stored XSS in GitLab, authentication provides the necessary access to create projects and issues. The procedure uses the web UI to create a public project named 'PoC', ensuring broad visibility for testing the vulnerability. This step assumes standard user permissions and targets GitLab's project management features, which do not sanitize inputs in subsequent issue fields.

## Requirements

1. Valid GitLab username and password
2. Web browser (Firefox or Chrome) with access to the GitLab URL
3. Network connectivity to the GitLab instance over HTTPS

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) for all users to limit unauthorized access
- Monitor login attempts and project creation logs for anomalous activity from new or suspicious IPs
- Use role-based access control (RBAC) to restrict project creation to trusted users

## Objectives

1. Establish authenticated session in GitLab
2. Create a test project for vulnerability exploitation
3. Prepare environment for issue-based attacks

## Instructions

### Step 1: Sign In to GitLab

**Context**: Authenticate to gain access to project creation features.

Open Firefox or Chrome and navigate to the GitLab login page. Enter valid credentials and submit the form.

> Successful login redirects to the dashboard, confirming session establishment.

### Step 2: Initiate Project Creation

**Context**: Access the navigation menu to start a new project.

Click the '+' icon in the top navigation bar, then select 'New Project' from the dropdown.

> The project creation form loads, ready for input.

### Step 3: Configure and Create Project

**Context**: Fill in project details to create a public repository.

Enter 'PoC' as the project name, set visibility to 'Public' by checking the checkbox, and click 'Create project'.

> Project is created and listed in the user's dashboard; note the project URL for subsequent steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- authentication
- gitlab
- project-setup
