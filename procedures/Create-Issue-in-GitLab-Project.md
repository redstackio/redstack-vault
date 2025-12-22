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
id: 576c89d7-1be2-4d86-89fc-870a026f874a
created_at: '2025-12-06T06:57:46.323Z'
updated_at: '2025-12-06T06:57:46.323Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
---
# Create Issue in GitLab Project

## Summary

This procedure details how to create a new issue within a GitLab project, enabling the use of comments for Quick Actions in exploitation scenarios.

## Description

Issues in GitLab provide a mechanism for discussions and Quick Actions. This step sets up an issue where comments can be posted to trigger vulnerabilities like information disclosure via the /move command.

## Requirements

1. Existing GitLab project
2. Permissions to create issues
3. Web access to GitLab

## Defense

Defensive measures and detection strategies:

- Audit issue creation in sensitive projects
- Limit Quick Action usage via permissions

## Objectives

1. Create a platform for submitting exploitative comments
2. Enable Quick Action execution
3. Prepare for data exposure

## Instructions

### Step 1: Navigate to Issues

**Context**: Go to the project's issues section.

In the project dashboard, click 'Issues' > 'New issue'.

> Opens the issue creation form.

### Step 2: Submit Issue

**Context**: Enter details and create the issue.

Fill in title, description, and submit.

> Issue is created and ready for comments.

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
