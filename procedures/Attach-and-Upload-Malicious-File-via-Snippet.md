---
id: proc-uuid-3
tags:
  - file-upload
  - attachment
  - rce-trigger
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:14.950Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[Exploit Public-Facing Application]]'
---
# Attach-and-Upload-Malicious-File-via-Snippet

## Summary

Attach the prepared malicious DjVu file (disguised as .jpg) to a GitLab snippet description and submit to initiate processing by the vulnerable Workhorse component.

## Description

The upload endpoint in snippets processes attachments as images, invoking ExifTool to strip metadata. The malicious file's content triggers the DjVu parser, leading to code injection. This exploits the lack of strict MIME type enforcement.

## Requirements

1. Prepared malicious file from previous procedure
2. Open snippet creation form
3. No special permissions beyond basic upload access

## Defense

Defensive measures and detection strategies:

- Enforce server-side content-type validation
- Scan uploads for DjVu signatures in image files
- Block uploads with mismatched magic bytes vs. extensions

## Objectives

1. Successfully attach the file without client-side rejection
2. Submit to backend for ExifTool invocation
3. Avoid detection during upload phase

## Instructions

### Step 1: Select Attach File Option

**Context**: Locate the attachment UI in the description field.

In the snippet description, click 'Attach a file' button.

> Expected: File browser opens.

### Step 2: Choose Malicious File

**Context**: Select the renamed DjVu file.

Browse to and select echo_vakzz.jpg (or reverse_shell.jpg).

> Expected: File attached, previewed as image.

### Step 3: Submit Snippet

**Context**: Finalize and upload to trigger processing.

Enter a title like 'Test Snippet' and click 'Create snippet'.

> Expected: Snippet created; file processed in background.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- malicious-upload
- exiftool-trigger
