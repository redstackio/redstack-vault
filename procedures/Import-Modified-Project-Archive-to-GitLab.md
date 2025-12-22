---
tags:
  - gitlab
  - import-exploit
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
  - GitLab
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: e7448903-282c-4075-bd7c-d4bbf8d79bb9
created_at: '2025-12-11T03:47:39.601Z'
updated_at: '2025-12-11T03:47:39.601Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1190]]'
---
# Import Modified Project Archive to GitLab

## Summary

This procedure uploads the modified tar.gz archive to GitLab, exploiting the import feature to deploy the injected service template instance-wide.

## Description

The GitLab import process fails to validate the 'template' flag on services, allowing non-admins to create persistent malicious configurations that apply to all new projects, potentially exfiltrating repository data or mutating project attributes.

## Requirements

1. Modified project tar.gz archive
2. GitLab user access to import feature
3. No additional tools required

## Defense

Defensive measures and detection strategies:

- Add admin-only checks for template flags during import
- Log and alert on unusual service configurations in imports

## Objectives

1. Deploy injected service template
2. Achieve persistence across new projects
3. Compromise confidentiality and integrity

## Instructions

### Step 1: Upload Archive

**Context**: Import the modified file to trigger the vulnerability.

Navigate to GitLab's import feature and upload the service_template.tar.gz.

> Expected: Successful import without privilege errors, injecting the template.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used

## Tools Used

## Tags

- #gitlab
- #import-exploit
