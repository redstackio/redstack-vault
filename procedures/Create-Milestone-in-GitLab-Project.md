---
id: proc-gitlab-create-milestone-001
tags:
  - gitlab
  - milestone
  - setup
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:32:29.123Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Create-Milestone-in-GitLab-Project

## Summary

This procedure adds a milestone to a GitLab project, which can contain sensitive timeline information, setting up content that should be protected from non-member access.

## Description

Milestones in GitLab track project deadlines and can include descriptions with confidential details like security patch schedules. This step uses the UI to create one in a restricted project, ensuring it's hidden from non-members in the UI but testable via API. Expected outcomes include milestone creation with an internal ID, in a GitLab environment requiring project owner access.

## Requirements

1. Ownership or maintainer role in the target GitLab project
2. Access to project milestones UI
3. Web browser for interaction

## Defense

Defensive measures and detection strategies:

- Restrict milestone creation to trusted roles
- Audit milestone content for sensitive data before creation
- Implement API rate limiting on milestone-related endpoints

## Objectives

1. Introduce sensitive data via milestone
2. Verify UI restrictions on the new milestone
3. Prepare for API access testing

## Instructions

### Step 1: Access Milestones Section

**Context**: Navigate to the project's milestones page as a project member.

Go to https://gitlab.com/<namespace>/<project>/-/milestones and click 'New milestone'.

### Step 2: Define Milestone Details

**Context**: Enter title and description to simulate sensitive content.

Set title to 'milestone' and description to 'milestone' (or include mock sensitive info like 'Security release due next week'). Save the milestone.

**Expected Output**: Milestone listed in the project with iid (e.g., 1) and creation timestamp.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- milestone-creation
