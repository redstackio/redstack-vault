---
id: proc-gitlab-add-to-dashboard
tags:
  - gitlab
  - security-dashboard
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
updated_at: '2025-12-14T17:29:36.624Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Add-Project-to-Personal-Security-Dashboard

## Summary

This procedure allows a maintainer to integrate a private project into their personal GitLab security dashboard for monitoring vulnerabilities.

## Description

As a maintainer (User B), access the personal profile's security dashboard feature in GitLab and add the target private project. This links the project's security scans to the user's dashboard, enabling visibility into issues like dependency vulnerabilities. In a vulnerability scenario, this setup persists even after permission changes, leading to unauthorized access. Prerequisites include maintainer role; expected outcome is the project appearing in the dashboard with scan data.

## Requirements

1. Maintainer access to the private project
2. GitLab instance with security dashboard enabled (default on GitLab.com)
3. Web access to user profile

## Defense

Defensive measures and detection strategies:

- Review dashboard project additions in user activity logs
- Implement automatic dashboard cleanup on role changes

## Objectives

1. Enable personal tracking of project security posture
2. Expose project vulnerabilities in user-specific view
3. Set up for post-demotion access testing

## Instructions

### Step 1: Access Personal Security Dashboard

**Context**: Navigate to the user's security overview.

Log in as User B, go to profile avatar > Security & analysis > Security dashboard.

> This opens the personal dashboard interface.

### Step 2: Add the Project

**Context**: Select and integrate the target project.

In the dashboard, click "Add projects", search for and select the private project, then confirm addition.

> The project now tracks security scans in the personal view.

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
- [[security-dashboard]]
