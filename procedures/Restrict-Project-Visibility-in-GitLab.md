---
id: 61b6fe52-484e-4663-b38e-6a92d8468ea8
name: Restrict Project Visibility in GitLab
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:47.623Z'
updated_at: '2025-12-11T03:47:47.623Z'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - gitlab
  - access-control
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
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1078]]'
---

# Restrict Project Visibility in GitLab

## Summary

This procedure updates GitLab project settings to restrict visibility of features like issues and repositories to only project members, simulating a private environment for vulnerability testing.

## Description

GitLab allows fine-grained control over project feature visibility. This procedure navigates to the project settings and sets restrictions, which is crucial for demonstrating authorization bypass vulnerabilities where data can still be copied despite these settings. The target is GitLab EE, and success results in limited access for non-members.

## Requirements

1. Ownership or admin access to the GitLab project
2. Web access to GitLab instance
3. Existing project to modify

## Defense

Defensive measures and detection strategies:

- Regularly audit project visibility settings
- Use GitLab's access logging to detect unauthorized changes

## Objectives

1. Limit access to project data
2. Test for bypass vulnerabilities
3. Ensure only members can view sensitive features

## Instructions

### Step 1: Navigate to Settings

**Context**: Access the project's general settings.

Go to Settings > General in the project dashboard.

> This opens the visibility configuration options.

### Step 2: Set Visibility Restrictions

**Context**: Apply restrictions to features.

Set visibility for Issues, Repository, Wiki, and Snippets to 'Only Project Members'.

> Save the changes to enforce restrictions.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[commands/curl-gitlab-project-create]]
- #access-control
