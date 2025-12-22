---
tags:
  - api-upload
  - gitlab
type: procedure
tools:
  - '[[tools/Nokogiri]]'
  - '[[tools/Faraday]]'
  - '[[tools/exp.rb]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f1fec366-7b8e-4294-a419-fbee5c105f87
created_at: '2025-12-11T03:47:39.826Z'
updated_at: '2025-12-11T03:47:39.826Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
---
# Upload Malicious NuPkg via GitLab API

## Summary

This procedure uploads the malicious .nupkg file to GitLab via the API, triggering the path traversal vulnerability during metadata extraction.

## Description

The upload uses the PUT /api/v4/projects/#{id}/packages/nuget/ endpoint, which processes the package and extracts metadata without validating paths, leading to arbitrary file creation in the filesystem.

## Requirements

1. GitLab API access token
2. Project ID
3. Malicious dummy.nupkg file

## Defense

Defensive measures and detection strategies:

- Sanitize version fields in update_package_from_metadata_service.rb
- Log and alert on suspicious API uploads

## Objectives

1. Trigger file creation with traversed paths
2. Set up for further exploitation

## Instructions

### Step 1: Perform API Upload

**Context**: Send the package to the GitLab endpoint.

Use an HTTP client to PUT the file to /api/v4/projects/#{id}/packages/nuget/.

> This exploits the lack of validation in metadata_extraction_service.rb.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- api-upload
- gitlab
