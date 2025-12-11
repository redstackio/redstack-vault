---
tags:
  - verification
  - data-exfiltration
type: procedure
tools:
  - '[[tools/tar]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/tar-create-archive]]'
platforms:
  - Web
  - GitLab
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 478fc2f4-9647-4a05-b25b-daee7d6eaa11
created_at: '2025-12-11T06:10:28.878Z'
updated_at: '2025-12-11T06:10:28.878Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1190]]'
---
# Verify Injected Service Template in New Project

## Summary

This procedure verifies the successful injection by creating a new project and checking its exported JSON for the malicious service.

## Description

After injection, new projects automatically inherit the template, allowing exfiltration of data like commits and issues. This step confirms the attack's impact on the GitLab instance.

## Requirements

1. Injected template via import.
2. Secondary user account.
3. tar for extraction.

## Defense

Defensive measures and detection strategies:

- Regularly audit project templates and services.
- Detect anomalous service configurations in exports.

## Objectives

1. Confirm template application.
2. Validate potential for data compromise.
3. Assess instance-wide impact.

## Instructions

### Step 1: Create New Project

**Context**: Test inheritance with another user.

Sign in as another user and create a new project.

### Step 2: Export and Extract

**Context**: Download and unpack the new project's export.

Export the project, download the archive, and extract:

```bash
tar -zxvf new_project_export.tar.gz
```

### Step 3: Observe Injected Service

**Context**: Check project.json.

Verify that project.json contains the injected MockCiService as a template.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used

## Tools Used

- [[tools/tar]]

## Tags

- [[verification]]
- [[data-exfiltration]]
