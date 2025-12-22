---
tags:
  - lfi
  - file-inclusion
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-upload-malicious-file]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T03:15:30.722Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: d9b5316c-35aa-49df-bfcc-5276556eb402
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Attempt Local File Inclusion via Uploaded Files

## Summary

This procedure attempts to chain the unrestricted file upload to Local File Inclusion (LFI) by uploading files with path traversal payloads, potentially allowing reading of server-side files like configuration or sensitive data in the helpdesk system.

## Description

Building on the upload vulnerability, LFI occurs if the system includes or processes uploaded files without sanitization, enabling traversal to local paths (e.g., /etc/passwd). This targets server-side inclusion flaws, leading to information disclosure. Requires authenticated upload access; outcomes include leaking server files for further compromise.

## Requirements

1. Successful prior upload access
2. Knowledge of server paths (e.g., Linux-based)
3. Tools for testing inclusion (browser or proxy)

## Defense

Defensive measures and detection strategies:

- Sanitize filenames and paths to prevent traversal (e.g., basename only)
- Run uploads in isolated environments or chroot jails
- Log and alert on suspicious path patterns in uploads

## Objectives

1. Upload file with traversal payload
2. Trigger inclusion to read local files
3. Disclose sensitive server information

## Instructions

### Step 1: Craft Traversal Payload

**Context**: Modify the uploaded file to include LFI payloads, e.g., filename with ../../etc/passwd.

**Command** ([[commands/curl-upload-malicious-file]]):
```bash
# Create file with traversal in name or content
echo '<html>Include: <?php include("/etc/passwd"); ?>' > lfi-payload.html
```

> Prepares a file that attempts PHP inclusion if processed server-side.

### Step 2: Upload and Test Inclusion

**Context**: Upload and attempt to include via system features (e.g., preview or attachment view).

**Command** ([[commands/curl-upload-malicious-file]]):
```bash
curl -X POST -F "file=@lfi-payload.html" -F "filename=../../etc/passwd" -H "Cookie: session=your_session" https://████████helpdesk/upload
```

> Expected output: If LFI works, viewing the file leaks contents like user lists. Otherwise, upload success but no leak.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-upload-malicious-file]]

## Tools Used


## Tags

- [[lfi]]
- [[file-inclusion]]
