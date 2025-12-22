---
tags:
  - archive-repackage
  - project-import
type: procedure
tools:
  - '[[tools/tar]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/tar-create-archive]]'
platforms:
  - Web
  - GitLab
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: cfe0ac90-8b78-47a0-b903-581e38826269
created_at: '2025-12-11T06:10:28.917Z'
updated_at: '2025-12-11T06:10:28.917Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1190]]'
---
# Repackage and Import Modified Project Archive

## Summary

This procedure covers repackaging the modified project files into a new archive and importing it into GitLab to inject the malicious template.

## Description

After editing, the files are archived using tar and uploaded via GitLab's import feature, exploiting the lack of validation to set instance-wide templates without admin access.

## Requirements

1. Modified project.json, VERSION, and project.bundle files.
2. tar tool for creating archives.
3. Access to GitLab import functionality.

## Defense

Defensive measures and detection strategies:

- Validate imported archives for unauthorized template settings.
- Monitor import activities for suspicious patterns.

## Objectives

1. Create a new tar.gz archive.
2. Import to inject the template.
3. Achieve persistence across new projects.

## Instructions

### Step 1: Repackage Files

**Context**: Create the modified archive.

Execute [[commands/tar-create-archive]]:

```bash
tar -zcvf service_template.tar.gz project.json VERSION project.bundle
```

> This compresses the files into a new importable archive.

### Step 2: Import Archive

**Context**: Upload and import to GitLab.

Use the GitLab UI to upload and import the service_template.tar.gz file.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used

- [[commands/tar-create-archive]]

## Tools Used

- [[tools/tar]]

## Tags

- [[archive-repackage]]
- [[project-import]]
