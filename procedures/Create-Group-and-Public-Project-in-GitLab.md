---
id: ded707e6-61b1-48a0-b6e9-ee075ce2fe75
name: Create Group and Public Project in GitLab
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:47.627Z'
updated_at: '2025-12-11T03:47:47.627Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - gitlab
  - setup
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---

# Create Group and Public Project in GitLab

## Summary

This procedure sets up a group and a public project in GitLab as the initial step for testing or exploiting project template vulnerabilities, enabling the creation of a controlled environment for restricted data.

## Description

In GitLab, groups and projects form the basis for organizing repositories and data. This procedure involves signing in as a user, creating a group, and then adding a public project to it. It's used in attack scenarios to prepare a target project with restricted access for later exploitation via template imports. The target environment is a GitLab EE instance, and the expected outcome is a functional group and project ready for visibility restrictions.

## Requirements

1. Authenticated GitLab user account
2. Access to GitLab web interface
3. No special tools required

## Defense

Defensive measures and detection strategies:

- Monitor group and project creation logs for unusual activity
- Implement role-based access controls to limit group creation

## Objectives

1. Establish a group for project organization
2. Create a public project to host data
3. Prepare for access restriction and exploitation testing

## Instructions

### Step 1: Sign In and Create Group

**Context**: Authenticate and create the group structure.

Sign in as a normal user and create a group with ID 1 via the GitLab dashboard.

> This sets up the namespace for the project.

### Step 2: Create Public Project

**Context**: Add a project to the group.

Create a public project within the group, naming it 'test_project'.

> The project will be used to store data for later restriction.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[commands/curl-gitlab-project-create]]
- #setup
