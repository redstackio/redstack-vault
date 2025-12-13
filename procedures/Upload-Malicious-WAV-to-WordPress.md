---
tags:
  - xxe
  - file-upload
  - wordpress
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - PHP 8
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f30d714e-1f6a-46c4-897c-688d69fba6b5
created_at: '2025-12-13T09:00:27.973Z'
updated_at: '2025-12-13T09:00:27.973Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload Malicious WAV to WordPress

## Summary

This procedure involves logging into WordPress as an author and uploading the crafted .wav file to trigger the XXE vulnerability in the Media Library.

## Description

Uploading the malicious .wav file causes WordPress to parse the embedded XML with LIBXML_NOENT, enabling entity substitution and exploitation for file access or other attacks.

## Requirements

1. WordPress author credentials
2. Prepared malicious xxe.wav file
3. Access to WordPress admin panel

## Defense

Defensive measures and detection strategies:

- Restrict media upload privileges
- Scan uploads for XML content
- Patch WordPress to remove LIBXML_NOENT flag

## Objectives

1. Trigger XXE during file parsing
2. Initiate exploitation chain

## Instructions

### Step 1: Login to WordPress

**Context**: Authenticate as author.

Navigate to WordPress login and enter credentials.

> Gains access to Media Library.

### Step 2: Upload WAV File

**Context**: Upload to Media Library.

Select and upload xxe.wav via the Media upload interface.

> Triggers vulnerable simplexml_load_string parsing.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- xxe
- file-upload
