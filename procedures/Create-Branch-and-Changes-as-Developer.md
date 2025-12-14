---
id: proc-gitlab-create-branch-001
tags:
  - gitlab
  - branch
  - development
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - GitLab
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:11.102Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Branch-and-Changes-as-Developer

## Summary

This procedure involves creating a new branch and committing changes from a Developer account in GitLab, simulating normal development to set up for Merge Request creation.

## Description

Log in as the Developer user to the private project, create a feature branch, and perform a simple commit (e.g., add a file). This establishes content for the subsequent Merge Request. Target environment is GitLab web UI or Git client. Expected outcomes: Branch visible and changes committed.

## Requirements

1. Developer role in the project
2. Git client or web editor access
3. Project repository cloned locally if using CLI

## Defense

Defensive measures and detection strategies:

- Audit branch creation events in GitLab logs
- Implement branch protection rules

## Objectives

1. Generate development artifacts for MR testing
2. Ensure branch is pushable by Developer
3. Validate Developer permissions pre-demotion

## Instructions

### Step 1: Create New Branch

**Context**: Initiate a feature branch from master.

In GitLab UI or locally: git checkout -b test; or use web 'New branch' button naming it 'test'.

> Branch 'test' created from master.

### Step 2: Make and Commit Changes

**Context**: Add content to trigger MR relevance.

Create a new file (e.g., test.txt with 'test content') and commit: git add .; git commit -m 'Add test file'; git push origin test.

> Commit visible in branch history.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- gitlab
- branch-creation
