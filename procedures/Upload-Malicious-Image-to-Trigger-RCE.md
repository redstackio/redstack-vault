---
tags:
  - file-upload
  - rce-trigger
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:17.721Z'
sub_techniques: []
id: ed3fe2a8-4f19-4002-aa7b-b036b3b35365
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
---
# Upload Malicious Image to Trigger RCE

## Summary

This procedure uploads the crafted PostScript payload as a logo image, causing ImageMagick to process it via Ghostscript and execute the embedded reverse shell command.

## Description

The Semrush logo upload endpoint processes uploaded images with vulnerable ImageMagick, invoking Ghostscript on PS content. Uploading test.jpg triggers the payload, leading to a reverse shell connection to the attacker's listener on port 8080. No additional tools needed beyond browser.

## Requirements

1. Access to upload form from previous step
2. Malicious test.jpg file
3. Active listener on attacker's side

## Defense

Defensive measures and detection strategies:

- Validate file types with magic bytes, not extensions
- Disable auto-processing of uploads
- Log and alert on ImageMagick errors

## Objectives

1. Submit payload to vulnerable endpoint
2. Initiate RCE execution
3. Establish shell connection

## Instructions

### Step 1: Select File

**Context**: Choose the disguised payload.

In the logo upload input, select test.jpg.

### Step 2: Submit Upload

**Context**: Trigger processing.

Click submit or apply to process the logo.

**Expected Output**: Upload completes; reverse shell connects.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- file-upload
- rce-trigger
