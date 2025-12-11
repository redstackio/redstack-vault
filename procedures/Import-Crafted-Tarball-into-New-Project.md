---
tags:
  - gitlab
  - import
  - exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 123c5ea8-d910-4972-9810-29e72105aeb2
created_at: '2025-12-11T03:47:57.060Z'
updated_at: '2025-12-11T03:47:57.060Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Import Crafted Tarball into New Project

## Summary

This procedure covers importing a crafted malicious tarball into a new GitLab project to exploit the IDOR vulnerability and assign foreign objects.

## Description

By using GitLab's built-in import functionality, the malicious tarball is processed without validating foreign key assignments, resulting in the importation of private data from other projects. This step is critical for triggering the vulnerability in project_tree_restorer.rb.

## Requirements

1. GitLab account with permission to create new projects.
2. Crafted malicious tarball from prior step.
3. Access to GitLab web interface.

## Defense

Defensive measures and detection strategies:

- Enforce attribute exclusion during import processes.
- Log and alert on imports that reference non-owned object IDs.

## Objectives

1. Successfully import the tarball to hijack objects.
2. Bypass access controls via improper validation.
3. Prepare for data extraction in subsequent steps.

## Instructions

### Step 1: Navigate to Import

**Context**: Access the project import feature in GitLab.

Log into GitLab and go to the new project creation page with import option.

### Step 2: Upload Tarball

**Context**: Upload and initiate the import.

Select the crafted tarball and start the import process.

### Step 3: Monitor Import

**Context**: Ensure the import completes successfully.

Wait for GitLab to process the tarball and create the new project.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #gitlab
- #import
