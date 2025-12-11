---
tags:
  - ssrf
  - json-modification
type: procedure
tools:
  - '[[tools/CarrierWave]]'
  - '[[tools/GitLab]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: cbe46a4f-9db5-4409-a41f-1d60a6bf2d85
created_at: '2025-12-11T03:47:39.486Z'
updated_at: '2025-12-11T03:47:39.486Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Modify Exported Project JSON for SSRF

## Summary

This procedure extracts and modifies the exported GitLab project.json to insert a malicious remote_attachment_url for SSRF exploitation.

## Description

By unpacking the tar.gz and editing the note hash in project.json, attackers can specify arbitrary URLs to internal services, bypassing validation during import due to flaws in AttributeCleaner.

## Requirements

1. Exported GitLab project tar.gz file.
2. Text editor for JSON modification.
3. Knowledge of target internal URLs (e.g., localhost metrics).

## Defense

Defensive measures and detection strategies:

- Sanitize imported attributes like remote_attachment_url.
- Log and alert on unusual import payloads.

## Objectives

1. Insert SSRF payload into project.json.
2. Prepare for import-triggered exploitation.
3. Target specific internal resources.

## Instructions

### Step 1: Extract Export

**Context**: Unpack the tar.gz to access project.json.

Use standard extraction tools like tar.

### Step 2: Add Remote Attachment URL

**Context**: Modify the note hash with a malicious URL.

Edit project.json to add 'remote_attachment_url' key with value like 'http://localhost:9090/metrics'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #ssrf
- #json-modification
