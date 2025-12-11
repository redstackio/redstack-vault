---
tags:
  - gitlab
  - verification
  - service-injection
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
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
id: 1b2440b7-cf30-4b50-a42b-f000924e0bec
created_at: '2025-12-11T03:47:39.597Z'
updated_at: '2025-12-11T03:47:39.597Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1068]]'
---
# Verify Injected Service Template in New Project

## Summary

This procedure tests the injection by creating a new project as another user and checking if the malicious service is automatically applied.

## Description

After injection, new projects inherit the templated service, allowing verification of the exploit's success through export and inspection of project.json.

## Requirements

1. Secondary GitLab user account
2. Access to create and export projects
3. Tool: #tar for extraction

## Defense

Defensive measures and detection strategies:

- Regularly audit service templates for unauthorized changes
- Monitor new project creations for anomalous services

## Objectives

1. Confirm instance-wide application of injected service
2. Validate data compromise potential
3. Assess exploit impact

## Instructions

### Step 1: Create New Project as Different User

**Context**: Simulate normal usage to trigger template application.

Sign in as another user and create a new project via UI.

> The project automatically inherits the injected template.

### Step 2: Export and Extract New Project

**Context**: Obtain files for inspection.

Export the new project, download the archive, and extract using #tar.

> Expected: Access to project.json.

### Step 3: Inspect project.json

**Context**: Verify presence of injected service.

Open project.json and check the services array for MockCiService with "template": true.

> Confirmation indicates successful injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Exploitation for Privilege Escalation]]

### Sub-Techniques

## Commands Used

## Tools Used

- #tar

## Tags

- #gitlab
- #verification
