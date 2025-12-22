---
tags:
  - file-upload
  - bypass
  - web
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Remote File Copy]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 3a0106ec-b684-4ba9-b19f-2255f290e6e7
created_at: '2025-12-14T05:32:10.339Z'
updated_at: '2025-12-14T05:32:10.339Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Bypass-File-Upload-Signature-Checks

## Summary

This procedure exploits a file upload misconfiguration by altering a malicious file's structure to evade signature-based detection, allowing upload of dangerous types onto a server like the DoD website, potentially enabling further exploitation.

## Description

The DoD website's upload feature checked file signatures (e.g., via magic bytes) but failed against modified files. Attackers can prepare a payload (e.g., PHP shell in an image) and tweak non-essential parts to change the detectable signature while preserving functionality. This targets web platforms and results in file persistence, opening doors to code execution upon access.

## Requirements

1. Malicious file payload (e.g., webshell or executable)
2. Hex editor or proxy tool for file alteration
3. Access to the vulnerable upload endpoint

## Defense

Defensive measures and detection strategies:

- Enforce strict file type whitelisting and content normalization
- Scan uploads with antivirus or sandboxing before storage
- Monitor for file access patterns post-upload to detect exploitation

## Objectives

1. Successfully upload a dangerous file type undetected
2. Verify file persistence and accessibility on the server
3. Enable subsequent actions like remote code execution

## Instructions

### Step 1: Prepare Malicious File

**Context**: Select or create a payload file that can execute on the server (e.g., a PHP script embedded in a JPG).

Use a text editor to embed malicious code into a benign file format, ensuring the file remains functional for its cover type.

> Expected: A hybrid file that appears safe but contains executable content.

### Step 2: Alter File Signature

**Context**: Modify the file to evade signature detection without breaking the payload.

Open the file in a hex editor (e.g., HxD) and adjust bytes in the header (e.g., insert null bytes after the magic number or change metadata). Save and verify the alteration doesn't corrupt the embedded payload.

> Expected: File signature no longer matches known malicious patterns.

### Step 3: Upload Altered File

**Context**: Submit the modified file via the upload form, intercepting if necessary to adjust headers.

Use the web form to upload the file. If client-side checks interfere, disable JavaScript or use a proxy to bypass. Monitor the response for acceptance.

> Expected: Server stores the file without rejection.

### Step 4: Validate Upload

**Context**: Confirm the file is accessible and executable.

Attempt to access the uploaded file's URL or location. If it's a webshell, trigger it to execute a test command.

> Expected: File retrieval and potential code execution success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[file-upload]]
- [[bypass]]
- [[web]]
- [[Execution]]
