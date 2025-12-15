---
id: proc-uuid-1
tags:
  - rce
  - djvu
  - exiftool
  - perl-injection
type: procedure
tools:
  - '[[tools/ExifTool]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:24:14.960Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Prepare-Malicious-DjVu-File-for-ExifTool-RCE

## Summary

This procedure involves obtaining or crafting a DjVu file with malicious metadata that exploits ExifTool's insecure eval in the DjVu parser, allowing arbitrary Perl code injection when the file is processed for metadata stripping.

## Description

ExifTool determines file types by content, not extension. By renaming a DjVu file to .jpg and embedding a backslash-newline sequence in annotation metadata, the DjVu module's eval on tokens can be bypassed to inject code like qx{command}. This targets GitLab Workhorse's use of ExifTool during uploads. Prerequisites include access to PoC files from the vulnerability report.

## Requirements

1. Download PoC ZIP from vulnerability disclosure (e.g., echo_vakzz.jpg.zip)
2. Unzip tool or command-line access
3. Basic understanding of file metadata manipulation

## Defense

Defensive measures and detection strategies:

- Update GitLab to patched versions (post-13.10.2)
- Disable or sandbox ExifTool processing for uploads
- Monitor for anomalous file uploads with mismatched extensions
- Log ExifTool invocations and scan for eval errors

## Objectives

1. Prepare a file that triggers Perl eval during ExifTool parsing
2. Ensure payload executes arbitrary commands as the processing user
3. Validate file disguises as a standard image

## Instructions

### Step 1: Download PoC Archive

**Context**: Obtain the pre-crafted malicious DjVu file from the vulnerability report.

No command needed; use browser to download echo_vakzz.jpg.zip or reverse_shell.jpg.zip from https://hackerone.com/reports/1154542 attachments.

> Expected: ZIP file downloaded.

### Step 2: Extract Malicious File

**Context**: Unzip to get the renamed DjVu file ready for upload.

```bash
unzip echo_vakzz.jpg.zip
```

> This extracts echo_vakzz.jpg, a DjVu file with metadata like /INFO 0 "\nqx{echo vakzz >/tmp/vakzz}" to bypass escaping and inject code.

### Step 3: Verify File Content

**Context**: Confirm the file is DjVu despite .jpg extension.

Use file command:

```bash
file echo_vakzz.jpg
```

> Expected output: DjVu image data, not JPEG.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Windows Command Shell]] Command and Scripting Interpreter: Perl

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/ExifTool]]

## Tags

- rce
- djvu
- metadata-injection
