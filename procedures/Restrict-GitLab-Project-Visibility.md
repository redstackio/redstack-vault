---
tags:
  - gitlab
  - visibility-restriction
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[T1213.003]]'
updated_at: '2025-12-14T17:29:36.658Z'
skill_level: intermediate
impact_level: medium
sub_techniques: []
id: 3e7476df-6d8d-4018-afc8-deb7e6c01d32
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[T1213.003]]'
---
# Restrict-GitLab-Project-Visibility

## Summary

This procedure applies visibility restrictions to a GitLab project and its CI pipelines, simulating a secure configuration where build information should only be accessible to authorized members.

## Description

Access the project settings in GitLab to change visibility level to 'Private' or 'Internal' (specifically 'Project Members Only'), and navigate to CI/CD settings to disable 'Public pipelines'. This ensures that non-members cannot view pipelines, setting up the conditions for testing unauthorized badge access. The restrictions apply across public, internal, and private projects.

## Requirements

1. Owner or Maintainer role in the GitLab project
2. Access to project settings via web interface
3. Existing project with CI configured

## Defense

Defensive measures and detection strategies:

- Regularly audit project visibility settings
- Enable GitLab's protected branches and merge request approvals
- Integrate with external identity providers for fine-grained access

## Objectives

1. Limit repository access to project members
2. Hide pipeline details from public view
3. Confirm restrictions prevent direct unauthorized access

## Instructions

### Step 1: Update Project Visibility

**Context**: Change the overall project access level.

Go to Project Settings > General > Visibility, project features, permissions, set 'Project visibility' to 'Private' (or 'Internal' for SaaS), and ensure 'Repository' is enabled but restricted.

### Step 2: Disable Public Builds in CI

**Context**: Restrict pipeline visibility specifically.

Navigate to Settings > CI/CD > General pipelines, uncheck 'Public pipelines' under 'Pipeline visibility', and save changes.

### Step 3: Verify Restrictions

**Context**: Test that non-members cannot access pipelines.

Log out or use an incognito browser to attempt viewing the project; confirm pipelines are not visible.

**Expected Output**: Error or limited view without pipeline details.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[T1213.003]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- visibility-restriction
