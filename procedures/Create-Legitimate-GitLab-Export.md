---
tags:
  - gitlab
  - export
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-25T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:08.383Z'
sub_techniques: []
id: e4b4f4b2-c284-437c-961d-faacc0f9159b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Legitimate-GitLab-Export

## Summary

This procedure generates a standard GitLab project export file to serve as a template for subsequent modifications in symlink-based attacks.

## Description

In the context of exploiting GitLab's import feature, a legitimate export is created to analyze its structure, which includes files like VERSION, project.bundle, and project.json. This export is generated via the project's admin panel and downloaded as a tar.gz archive. The target environment is a GitLab instance where the user has project management permissions. Expected outcomes include obtaining a clean archive for tampering.

## Requirements

1. Valid GitLab account with project creation and export permissions
2. Access to the web interface
3. No special tools required beyond browser

## Defense

Defensive measures and detection strategies:

- Disable export/import for untrusted users
- Monitor project creation and import logs for unusual patterns
- Implement file validation on uploads to detect tampered archives

## Objectives

1. Obtain a baseline export for modification
2. Understand archive structure for symlink insertion
3. Prepare for vulnerability exploitation

## Instructions

### Step 1: Create Demo Project

**Context**: Set up a simple project to generate the export.

Log into GitLab and create a new empty project.

### Step 2: Trigger Export

**Context**: Use the admin panel to export the project.

Navigate to Project Settings > General > Export project, then download the generated tar.gz file.

**Expected Output**: tar.gz file containing VERSION (version string), project.bundle (git repo), and project.json (metadata).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[gitlab]]
- [[export]]
