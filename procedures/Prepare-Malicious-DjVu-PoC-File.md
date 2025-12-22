---
tags:
  - poc-preparation
  - file-crafting
type: procedure
tools:
  - '[[tools/ExifTool]]'
  - '[[tools/Ruby]]'
  - '[[tools/Perl]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 4d6c782f-9d87-4cde-9431-29162b048cf9
created_at: '2025-12-11T03:47:58.550Z'
updated_at: '2025-12-11T03:47:58.550Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Prepare Malicious DjVu PoC File

## Summary

This procedure involves downloading and extracting a proof-of-concept DjVu file renamed as .jpg to exploit ExifTool's content-based parsing in GitLab image uploads.

## Description

The PoC file contains malicious metadata that injects Perl code via DjVu annotations. This is the initial step for triggering RCE when uploaded to GitLab, targeting the improper escaping in ExifTool's eval function.

## Requirements

1. Access to the PoC ZIP file (echo_vakzz.jpg.zip)
2. unzip tool installed
3. Local Linux or compatible environment

## Defense

Defensive measures and detection strategies:

- Monitor for unusual file uploads in GitLab
- Update ExifTool to patched versions

## Objectives

1. Extract crafted DjVu file for upload
2. Prepare payload for RCE injection
3. Ensure file is ready without modifications

## Instructions

### Step 1: Download and Unzip PoC

**Context**: Extract the malicious DjVu file from the ZIP archive.

**Command** ([[commands/unzip-poc-file]]):
```bash
unzip echo_vakzz.jpg.zip
```

> This extracts echo_vakzz.jpg, which is parsed as DjVu by ExifTool based on content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/unzip-poc-file]]

## Tools Used

- #unzip

## Tags

- #poc-preparation
- #file-crafting
