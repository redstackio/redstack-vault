---
id: 123e4567-e89b-12d3-a456-426614174003
name: Protect-Branch-in-GitLab-Project
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.503Z'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Service Stop]]'
sub_techniques: []
tags:
  - gitlab
  - branch-protection
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Service Stop]]'
---

# Protect-Branch-in-GitLab-Project

## Summary

This procedure configures a branch as protected in a GitLab project, activating the vulnerable dropdown in the protected branches settings.

## Description

Protected branches require role-based permissions for merge/push, displayed via a dropdown that renders usernames without escaping. Protecting a branch like 'main' ensures the settings page loads the vulnerable component. This step is essential for the payload to appear and execute.

## Requirements

1. Maintainer access to the project
2. Existing repository with branches
3. Web browser

## Defense

Defensive measures and detection strategies:

- Regularly review protected branch configurations
- Sanitize all dropdown renders
- Use role-based access controls strictly

## Objectives

1. Enable protected branches feature
2. Populate the permission dropdowns
3. Set stage for XSS trigger

## Instructions

### Step 1: Access Repository Settings

**Context**: Navigate to branch protection options.

Go to Project > Settings > Repository > Protected Branches.

### Step 2: Add Protected Branch

**Context**: Select and protect a branch.

Click 'Add protected branch', choose 'main' or target branch, set permissions (e.g., Maintainers can merge), and save.

> This activates the 'Ability to Merge' and 'Ability to Push' dropdowns.

### Step 3: Verify Protection

**Context**: Confirm the setup.

The protected branches list should show the branch with configured rules.

**Expected Output**: Branch listed as protected.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Service Stop]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[branch-protection]]
