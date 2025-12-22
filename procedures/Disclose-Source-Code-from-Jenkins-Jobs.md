---
tags:
  - discovery
  - source-code
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Jenkins
techniques:
  - '[[File and Directory Discovery]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 37688e75-7b23-44ae-a3df-699a15b5bb29
created_at: '2025-12-11T03:47:56.624Z'
updated_at: '2025-12-11T03:47:56.624Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1083]]'
---
# Disclose Source Code from Jenkins Jobs

## Summary

This procedure accesses Jenkins job configurations to disclose source code of associated applications.

## Description

Authenticated users can view job details, workspaces, or configurations that may expose source code repositories or files, leading to intellectual property theft.

## Requirements

1. Authenticated access to Jenkins dashboard
2. Permissions to view jobs
3. Web browser

## Defense

Defensive measures and detection strategies:

- Restrict job visibility to authorized users
- Encrypt or protect sensitive configurations

## Objectives

1. Access job workspaces
2. Download or view source code
3. Identify sensitive information in code

## Instructions

### Step 1: Browse to Jobs

**Context**: List available Jenkins jobs.

Navigate to https://jenkins.target.com/view/all/.

### Step 2: Access Job Workspace

**Context**: View or download files from the workspace.

Select a job, go to 'Workspace', and browse files containing source code.

> Look for directories like 'src' or repository clones.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Browser]]

## Tags

- [[Discovery]]
- #source-code
