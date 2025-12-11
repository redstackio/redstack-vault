---
tags:
  - template-injection
  - json-modification
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
  - '[[Abuse Elevation Control Mechanism]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: e413b8ff-b104-4cb6-8c6f-7b8ed7717d60
created_at: '2025-12-11T06:10:28.928Z'
updated_at: '2025-12-11T06:10:28.929Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1548]]'
---
# Modify Project JSON to Inject Service Template

## Summary

This procedure details editing the exported project.json file to set a service as a template and change its type, enabling injection upon import.

## Description

By altering the JSON structure, attackers can bypass admin restrictions and create templated services like MockCiService, which apply to all new projects. This exploits improper access control in GitLab's import process.

## Requirements

1. Extracted project.json from a GitLab export.
2. Text editor for JSON modifications.
3. Knowledge of GitLab service structures.

## Defense

Defensive measures and detection strategies:

- Implement strict validation on imported JSON fields.
- Log and alert on template creations via imports.

## Objectives

1. Convert a service to a template.
2. Alter service type to malicious variant.
3. Prepare for repackaging.

## Instructions

### Step 1: Edit Template Flag

**Context**: Set the service as a template.

Replace "template":false with "template":true in the services array of project.json.

### Step 2: Change Service Type

**Context**: Modify to a mock or malicious service.

Replace CiService with MockCiService in the services array.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Abuse Elevation Control Mechanism]]

### Sub-Techniques

## Commands Used

## Tools Used

## Tags

- [[template-injection]]
- [[json-modification]]
