---
tags:
  - gitlab
  - setup
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: c1b7de22-6aef-4973-8e38-2a1ec61912ff
created_at: '2025-12-11T03:47:56.731Z'
updated_at: '2025-12-11T03:47:56.731Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Create GitLab Project and Issue

## Summary

This procedure sets up a new project and issue in GitLab to prepare for uploading and referencing designs, serving as the initial access point for exploiting vulnerabilities in design handling.

## Description

In GitLab, projects and issues provide contexts for uploading designs and rendering markdown. This setup is necessary for exploiting stored XSS via design references. The procedure assumes a valid GitLab account and targets web-based GitLab instances like gitlab.com.

## Requirements

1. Valid GitLab account
2. Web browser access to GitLab
3. No special tools required

## Defense

Defensive measures and detection strategies:

- Monitor for unusual project creation patterns
- Implement rate limiting on project and issue creation

## Objectives

1. Establish a project for vulnerability exploitation
2. Create an issue to host designs
3. Prepare for subsequent upload and injection steps

## Instructions

### Step 1: Create New Project

**Context**: Navigate to GitLab dashboard and initiate project creation.

Go to gitlab.com and click 'New project' to create a new project.

### Step 2: Create New Issue

**Context**: Within the project, create an issue for design uploads.

Navigate to the project and select 'New issue' to create one.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- gitlab
- setup
