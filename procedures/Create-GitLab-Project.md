---
tags:
  - gitlab
  - setup
type: procedure
tools: []
tactics:
  - '[[TA0001]]'
commands:
  - '[[gitlab-move-quick-action]]'
platforms:
  - Web
  - GitLab
techniques: []
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 668699ba-4544-4cac-8e52-68390300993a
created_at: '2025-12-06T06:57:46.316Z'
updated_at: '2025-12-06T06:57:46.316Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
---
# Create GitLab Project

## Summary

This procedure outlines the steps to create a new project in GitLab, serving as the foundation for hosting issues and executing Quick Actions in attack scenarios.

## Description

Creating a project in GitLab is a prerequisite for many attacks involving issues and Quick Actions. It involves using the GitLab UI to set up a new repository where further actions like issue creation and command execution can occur. This step is low-risk and typically requires only a valid GitLab account.

## Requirements

1. Valid GitLab account with project creation permissions
2. Web browser access to GitLab
3. No additional tools required

## Defense

Defensive measures and detection strategies:

- Monitor for unusual project creation patterns
- Enforce role-based access controls on project creation

## Objectives

1. Establish a controlled environment for issue-based exploits
2. Gain a namespace for referencing other projects
3. Prepare for Quick Action execution

## Instructions

### Step 1: Navigate to Projects

**Context**: Access the GitLab dashboard to start project creation.

Log in to GitLab and click 'New project' in the UI.

> This opens the project creation form.

### Step 2: Configure and Create

**Context**: Fill in project details and submit.

Enter project name, visibility, and create the project.

> Project is created and ready for use.

## MITRE ATT&CK Mapping

### Tactics

- [[TA0001]]

### Techniques



### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[gitlab-move-quick-action]]
- [[setup]]
