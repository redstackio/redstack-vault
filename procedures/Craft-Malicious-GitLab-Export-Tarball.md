---
tags:
  - gitlab
  - idor
  - tarball-craft
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
id: bb7b7bb1-bc7a-4eb9-a117-bc10e24aadf7
created_at: '2025-12-11T03:47:57.123Z'
updated_at: '2025-12-11T03:47:57.123Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Craft Malicious GitLab Export Tarball

## Summary

This procedure involves crafting a malicious GitLab export tarball by modifying the project.json file to include foreign issue IDs, enabling the theft of private objects during project import.

## Description

The procedure exploits an IDOR vulnerability in GitLab's import process where attributes like issue_ids are not validated, allowing arbitrary assignment of foreign keys. This can lead to stealing issues, merge requests, and sensitive data from other projects. It requires access to a GitLab instance and knowledge of target IDs, often obtained via brute-forcing incremental numbers.

## Requirements

1. Access to a GitLab account with project export/import permissions.
2. Basic file editing tools (e.g., text editor, tar utility).
3. Knowledge of target issue IDs for inclusion in project.json.

## Defense

Defensive measures and detection strategies:

- Implement strict validation and sanitization of imported attributes in GitLab.
- Monitor for unusual project imports and access patterns to private objects.

## Objectives

1. Create a tarball that hijacks foreign issues upon import.
2. Enable data theft without direct access to target projects.
3. Demonstrate IDOR exploitation in web applications.

## Instructions

### Step 1: Obtain Base Export

**Context**: Start with a legitimate GitLab project export or create a new one.

Export a project from GitLab and extract the tarball contents.

### Step 2: Modify project.json

**Context**: Edit the JSON to include foreign IDs.

Open project.json and add 'issue_ids': [27422144] (replace with target IDs; use increments for brute-force). Keep the issues array empty.

### Step 3: Repackage Tarball

**Context**: Reassemble the modified files into a tarball.

Use tar utilities to create the malicious export tarball.

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
- #idor
