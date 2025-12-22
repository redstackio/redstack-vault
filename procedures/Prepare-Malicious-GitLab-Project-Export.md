---
tags:
  - gitlab
  - export-modification
  - service-injection
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
  - GitLab
techniques:
  - '[[Exploitation for Privilege Escalation]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: dc0c35c0-2804-4d61-ae2e-10c88a252dff
created_at: '2025-12-11T03:47:39.603Z'
updated_at: '2025-12-11T03:47:39.603Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1068]]'
---
# Prepare Malicious GitLab Project Export

## Summary

This procedure involves creating a GitLab project, enabling a service, exporting it, modifying the project.json to inject a templated malicious service, and repackaging the archive for import.

## Description

By exploiting improper access control in GitLab's import process, a standard user can modify the exported project.json to set a service as a template, normally requiring admin privileges. This allows injection of services like MockCiService that can exfiltrate or mutate data in new projects.

## Requirements

1. Standard GitLab user account
2. Access to GitLab UI for project creation and export
3. Tool: #tar for archive manipulation

## Defense

Defensive measures and detection strategies:

- Implement strict validation on imported project.json to prevent unauthorized template flags
- Monitor project imports for modifications to services array

## Objectives

1. Create a modified export with injected service template
2. Prepare for instance-wide service deployment
3. Enable data compromise in new projects

## Instructions

### Step 1: Create and Configure Project

**Context**: Set up a base project with a service enabled.

Sign in to GitLab, create a new project via UI, and enable CI service in Settings > Integrations.

> This establishes the service structure for modification.

### Step 2: Export and Extract Project

**Context**: Obtain the project archive and access JSON file.

Export the project using GitLab's export feature and download the tar.gz. Extract using #tar.

> Expected: project.json file becomes accessible for editing.

### Step 3: Modify project.json

**Context**: Inject the malicious template flag and service type.

Edit project.json: Change "template": false to "template": true in services array, and replace CiService with MockCiService.

> This sets the service as an instance-wide template.

### Step 4: Repackage Archive

**Context**: Create a new archive with modifications.

Execute [[commands/tar-create-archive]]:

```bash
tar -zcvf service_template.tar.gz project.json VERSION project.bundle
```

> Expected output: List of files added to the archive.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques

## Commands Used

- [[commands/tar-create-archive]]

## Tools Used

- #tar

## Tags

- #gitlab
- #service-injection
