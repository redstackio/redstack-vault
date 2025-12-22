---
tags:
  - gitlab
  - project-setup
  - initial-access
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - GitLab
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: aa7c425d-2805-4244-a616-d205f5e3e2be
created_at: '2025-12-14T17:32:10.409Z'
updated_at: '2025-12-14T17:32:10.409Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-and-Configure-Public-GitLab-Project

## Summary

This procedure sets up a public or internal GitLab project and enables the snippets feature, creating the environment for demonstrating the API disclosure vulnerability.

## Description

In the context of exploiting GitLab's snippet disclosure flaw, this procedure involves logging into a GitLab instance, creating a new project with public or internal visibility, and configuring it to support snippets. This mimics a victim's setup where sensitive private snippets are stored. The project ID is crucial for subsequent API interactions. Prerequisites include a valid GitLab account with project creation permissions.

## Requirements

1. Valid GitLab user account (e.g., Developer role)
2. Access to GitLab web UI
3. Network connectivity to the GitLab instance

## Defense

Defensive measures and detection strategies:

- Restrict project creation to trusted users via role-based access control (RBAC)
- Monitor project creation events in GitLab audit logs for anomalous activity

## Objectives

1. Establish a vulnerable project environment
2. Obtain project ID for API exploitation
3. Enable snippets feature without alerting defenses

## Instructions

### Step 1: Log In and Create Project

**Context**: Access the GitLab dashboard and initiate project creation to set up the target environment.

No command required; use the web UI to create a new project named e.g., "Test Project" with visibility set to Public or Internal. Note the assigned project ID (e.g., 1).

> After creation, verify the project in the dashboard and record the ID from the URL or API.

### Step 2: Enable Snippets

**Context**: Configure the project to allow snippet creation, which is necessary for the vulnerability.

Navigate to Project Settings > General > Visibility, project features, permissions. Check the box for "Snippets" and save changes.

> Confirm snippets are enabled by checking the project sidebar for the Snippets link.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- [[gitlab]]
- [[project-setup]]
