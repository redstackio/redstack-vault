---
tags:
  - rce
  - poc-preparation
  - file-crafting
type: procedure
tools:
  - '[[tools/ExifTool]]'
  - '[[tools/GitLab-Workhorse]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/perl-qx-execute-shell]]'
  - '[[commands/echo-write-file]]'
  - '[[commands/ruby-reverse-shell]]'
  - '[[commands/id-user-info]]'
  - '[[commands/hostname-alias]]'
  - '[[commands/ps-process-list]]'
platforms:
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 561cddc4-7904-41ff-9d1b-ec3126ce9341
created_at: '2025-12-11T06:10:22.455Z'
updated_at: '2025-12-11T06:10:22.455Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Download and Prepare Crafted DjVu PoC

## Summary

This procedure involves downloading and extracting a proof-of-concept zipped file containing a crafted DjVu image renamed as JPG, which embeds malicious Perl code for exploiting the GitLab ExifTool vulnerability.

## Description

The PoC is a DjVu file with annotations that inject arbitrary Perl code using backslash-newline escapes to close quotes and execute commands via insecure eval in ExifTool. This is the initial step for preparing the exploit payload targeting GitLab's image upload handling.

## Requirements

1. Access to download the PoC file (echo_vakzz.jpg.zip)
2. unzip tool installed on the local system
3. Basic file handling permissions

## Defense

Defensive measures and detection strategies:

- Monitor file uploads for unusual extensions or content types
- Update GitLab and ExifTool to patched versions

## Objectives

1. Obtain the malicious file for upload
2. Ensure the file is intact and ready for exploitation
3. Prepare for subsequent upload steps

## Instructions

### Step 1: Download PoC File

**Context**: Retrieve the zipped PoC from a reliable source.

Download echo_vakzz.jpg.zip.

> This file contains the crafted DjVu renamed as JPG.

### Step 2: Extract the File

**Context**: Unzip the archive to get the exploit file.

```bash
unzip echo_vakzz.jpg.zip
```

> Extracts echo_vakzz.jpg, ready for upload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- rce
- poc-preparation
