---
tags:
  - gitlab
  - import
  - arbitrary-file-read
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Cloud (GitLab.com)
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 3e19c2af-92c4-451d-9d0c-a0f4175892ca
created_at: '2025-12-11T03:47:56.791Z'
updated_at: '2025-12-11T03:47:56.791Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Import Malicious GitLab Export File

## Summary

This procedure involves using GitLab's project import feature to upload a specially crafted 'import.tar.gz' file that exploits an arbitrary file read vulnerability in the JSON schema validator and open-uri library.

## Description

The procedure targets the project import functionality in GitLab, where improper validation allows arbitrary file access during processing. This can lead to leaking sensitive data and SSRF attacks. It requires a valid GitLab account and is applicable to GitLab.com or self-hosted instances.

## Requirements

1. Valid GitLab account with project creation permissions
2. Specially crafted 'import.tar.gz' file exploiting the vulnerability
3. Network access to GitLab import endpoint

## Defense

Defensive measures and detection strategies:

- Monitor for unusual project imports and API queries
- Implement strict validation in JSON schema and open-uri usage

## Objectives

1. Trigger the vulnerability through file import
2. Initiate leakage of sensitive files
3. Enable potential SSRF access to internal resources

## Instructions

### Step 1: Upload Malicious File

**Context**: Use the import feature to upload the file as a GitLab export.

Navigate to GitLab's project import page and select the malicious 'import.tar.gz' file.

> This triggers the import process, exploiting the validator.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #gitlab
- #import
