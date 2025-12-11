---
id: a45ca4c9-9dc1-4c8d-b0fe-9edd8dc045d5
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:48:05.904Z'
updated_at: '2025-12-11T03:48:05.904Z'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - gitlab
  - import
commands: []
platforms:
  - Web
tools:
  - '[[tools/Flask]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1190]]'
---

# Initiate Malicious Group Import

## Summary

This procedure initiates the group import in GitLab using the ngrok URL and access token to trigger the extraction of the malicious tar file.

## Description

A personal access token is generated for authentication. A new group is created, and the import is started from the original group using the proxy URL, causing the UploadsPipeline to extract symlinks and enable file reads. This exploits the path traversal vulnerability in the bulk imports API.

## Requirements

1. GitLab account
2. Ngrok URL from proxy
3. Original group setup

## Defense

Defensive measures and detection strategies:

- Sanitize tar extractions to remove symlinks
- Log and alert on import failures or anomalies

## Objectives

1. Authenticate and initiate import
2. Inject malicious tar via proxy
3. Trigger vulnerability exploitation

## Instructions

### Step 1: Create Access Token

**Context**: Generate token via GitLab profile for authentication during import.

Navigate to GitLab profile and create a new personal access token.

> Token generated.

### Step 2: Create New Group and Import

**Context**: Use the ngrok URL and access token to initiate the group import.

Create a new group, choose to import from the original, provide ngrok URL, token, and new name.

> Import process started.

### Step 3: Complete Import

**Context**: Complete the import process, which triggers the UploadsPipeline to extract the malicious tar.

Select the original group and proceed.

> Import completed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #gitlab
- #import
