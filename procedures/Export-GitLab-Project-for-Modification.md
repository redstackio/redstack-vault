---
tags:
  - gitlab
  - project-export
type: procedure
tools:
  - '[[tools/tar]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/tar-create-archive]]'
platforms:
  - Web
  - GitLab
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: eb400902-9cb8-40b2-b74d-cd044eef3004
created_at: '2025-12-11T06:10:28.937Z'
updated_at: '2025-12-11T06:10:28.937Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Export GitLab Project for Modification

## Summary

This procedure outlines the steps to create and export a GitLab project with an enabled service, preparing it for modification to inject a malicious template.

## Description

In this attack scenario, an attacker uses a standard user account to set up a project with CI integration, exports it, and extracts the archive to access editable files like project.json. This is the initial step in exploiting the import vulnerability for template injection in GitLab.

## Requirements

1. Authenticated access to GitLab as a standard user.
2. Ability to create projects and enable integrations.
3. tar tool for archive extraction.

## Defense

Defensive measures and detection strategies:

- Monitor project export/import activities for anomalies.
- Restrict export features to trusted users.

## Objectives

1. Prepare a project export for JSON modification.
2. Enable a service that can be converted to a template.
3. Extract files for editing.

## Instructions

### Step 1: Create and Configure Project

**Context**: Authenticate and set up a new project with CI enabled.

Sign in as any user, create a new project via GitLab UI, and enable CI through Settings > Integrations.

### Step 2: Export Project

**Context**: Download the project archive.

Use the GitLab export feature to download the project archive.

### Step 3: Extract Archive

**Context**: Unpack the archive to access project.json.

Execute the extraction:

```bash
tar -zxvf project_export.tar.gz
```

> This extracts project.json, VERSION, and project.bundle for modification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used

## Tools Used

- [[tools/tar]]

## Tags

- [[gitlab]]
- [[project-export]]
