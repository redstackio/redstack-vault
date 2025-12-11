---
tags:
  - idor
  - json-craft
  - bypass
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
id: 3c303c14-5848-4d0f-a563-e3815fd2b36d
created_at: '2025-12-11T03:47:56.943Z'
updated_at: '2025-12-11T03:47:56.943Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Craft Malicious Project JSON

## Summary

This procedure involves manually editing a project.json file to indirectly set restricted '_ids' attributes like 'issue_ids' within the 'attributes' field, bypassing GitLab's validation checks and enabling linkage to private issues.

## Description

In GitLab's project import, direct setting of '_ids' fields is blocked, but indirect setting via 'attributes' allows exploitation. This IDOR vulnerability permits attackers to associate arbitrary private issues with an imported project, exposing them. The procedure targets web-based GitLab environments and requires basic JSON editing skills. Expected outcome is a malicious JSON that survives import validation.

## Requirements

1. Text editor for JSON modification
2. Knowledge of target issue IDs (e.g., via enumeration)
3. Access to a base project.json template from a legitimate export

## Defense

Defensive measures and detection strategies:

- Implement strict validation on all nested fields in import data
- Monitor import logs for unusual relation modifications

## Objectives

1. Bypass IDOR fix to set issue relations
2. Prepare JSON for tarball packaging
3. Enable exposure of private resources post-import

## Instructions

### Step 1: Modify JSON Attributes

**Context**: Edit the project.json to include indirect 'issue_ids' setting.

Modify the file to add: {'attributes': {'issue_ids': [29279725], 'description': 'Set from attributes[description]'}}.

> This bypasses direct '_ids' validation while achieving the same relation modification.

### Step 2: Validate JSON Structure

**Context**: Ensure the JSON is valid and matches GitLab's expected format.

Use a JSON validator to check for syntax errors before proceeding.

> Expected: Valid JSON without direct '_ids' fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #idor
- [[procedures/Craft-Malicious-Project-JSON]]
