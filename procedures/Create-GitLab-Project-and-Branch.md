---
tags:
  - gitlab
  - setup
  - project-creation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T00:11:09.124Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: cfe0529b-ac21-4e3d-83f5-494acd0b2269
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-GitLab-Project-and-Branch

## Summary

This procedure sets up a test project and branch in GitLab, providing the necessary environment for exploiting vulnerabilities in merge requests. It involves authentication, project creation, and branch generation using the standard GitLab UI workflow.

## Description

In the context of testing for Stored XSS in GitLab, this preparatory procedure authenticates a user, creates a public project named 'test-project', and branches 'test-branch' from 'master'. This establishes the source branch needed for the merge request injection. The process assumes access to a GitLab instance and uses browser-based interactions. Expected outcomes include a fully initialized repository ready for merge request creation, with no anomalous behavior to avoid detection.

## Requirements

1. Valid GitLab credentials (e.g., developer role)
2. Web browser with network access to the GitLab host
3. No special tools required for this setup phase

## Defense

Defensive measures and detection strategies:

- Monitor for rapid project creation patterns via GitLab audit logs
- Enforce role-based access controls to limit project creation
- Use web application firewalls to detect unusual UI interactions

## Objectives

1. Establish authenticated session and project infrastructure
2. Create a branch to serve as the source for the vulnerable merge request
3. Prepare environment without triggering security alerts

## Instructions

### Step 1: Authenticate and Access Dashboard

**Context**: Begin by signing into GitLab to gain access to project management features.

No specific command; use the login form at the GitLab instance URL.

> Enter username and password; upon success, the dashboard loads, confirming session establishment.

### Step 2: Initiate and Configure Project

**Context**: Create a new public project with initialization to mimic legitimate usage.

No specific command; interact with the UI:

- Click '[+]' > 'New Project'
- Enter 'test-project' as name
- Select 'Public' visibility
- Check 'Initialize repository with a README'
- Click 'Create project'

> Project creation succeeds, redirecting to the project page; verify by checking the project list.

### Step 3: Create Source Branch

**Context**: Generate a new branch from master to use in the merge request.

No specific command; navigate to branches page:

- Go to `/branches/new`
- Enter 'test-branch' as name
- Select 'master' as create from
- Click 'Create branch'

> Branch is created; success confirmed by its appearance in the branches list.

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
- [[project-setup]]
