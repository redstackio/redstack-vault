---
tags:
  - import
  - gitlab
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
id: bb11b403-60fd-4f35-bd0d-4771bddf5b32
created_at: '2025-12-11T03:47:56.925Z'
updated_at: '2025-12-11T03:47:56.925Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Import Tarball into GitLab

## Summary

This procedure uploads the malicious tarball to GitLab's project import feature, triggering the IDOR bypass and linking private issues.

## Description

Using GitLab's web interface, import the tarball to process the crafted JSON, exploiting insufficient validation. This step achieves the core vulnerability exploitation in a web environment.

## Requirements

1. GitLab account with import permissions
2. Prepared exploit.tar.gz
3. Web browser access to GitLab

## Defense

Defensive measures and detection strategies:

- Enhance import validation for nested attributes
- Audit import activities for suspicious patterns

## Objectives

1. Execute import to apply malicious relations
2. Bypass validation checks
3. Set up for verification of exposure

## Instructions

### Step 1: Navigate to Import

**Context**: Access GitLab's project import page.

Log in and go to New Project > Import Project.

> Select the tarball upload option.

### Step 2: Upload and Import

**Context**: Upload exploit.tar.gz and confirm import.

Upload the file and monitor for successful processing.

> Expected: Project imports without errors, applying the ID links.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #import
