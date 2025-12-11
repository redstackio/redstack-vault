---
tags:
  - gitlab
  - setup
type: procedure
tools:
  - '[[tools/HTTP-Proxy]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/gitlab-project-creation-post]]'
platforms:
  - Web
  - GitLab
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: de90a046-e844-4a54-9c16-7b5e7ee85f11
created_at: '2025-12-11T06:10:15.873Z'
updated_at: '2025-12-11T06:10:15.873Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Create Restricted Public Project in GitLab

## Summary

This procedure sets up a public GitLab project with restricted access to features like issues and repositories, simulating a target for authorization bypass exploits.

## Description

In GitLab, projects can be public but with features restricted to members only. This procedure creates such a project in a user-controlled group, which can then be targeted by template bypass vulnerabilities to copy sensitive data. It requires a standard GitLab user account and involves no special tools.

## Requirements

1. GitLab user account with group creation permissions
2. Access to the GitLab web interface
3. No elevated privileges needed

## Defense

Defensive measures and detection strategies:

- Monitor for unusual project creation patterns in logs
- Implement stricter namespace validation in custom template usage

## Objectives

1. Create a testable restricted project
2. Restrict sensitive features to members only
3. Prepare for exploitation testing

## Instructions

### Step 1: Create Group and Project

**Context**: Establish the base structure for the restricted project.

Sign in to GitLab, create a new group (e.g., ID 1), then create a project named 'test_project' within it.

> This sets up the namespace for the target project.

### Step 2: Restrict Project Features

**Context**: Apply restrictions to simulate protected data.

Navigate to Settings > General and set Issues, Repository, Wiki, and Snippets to 'Only Project Members'.

> This ensures non-members cannot access these features directly.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[commands/gitlab-project-creation-post]]
- [[setup]]
