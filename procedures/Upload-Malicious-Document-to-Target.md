---
tags:
  - file-upload
  - xxe
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/upload-document]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: bbd11d51-5351-4ac3-8788-b7b373f3e4c7
created_at: '2025-12-13T09:00:27.652Z'
updated_at: '2025-12-13T09:00:27.652Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload Malicious Document to Target

## Summary

This procedure covers uploading a crafted malicious document to a vulnerable web endpoint to trigger XXE processing and potential data exfiltration.

## Description

Uploading occurs via HTTP POST to the document processing service, exploiting improper XML handling. This step assumes the payload is ready and focuses on delivery to pu.vk.com.

## Requirements

1. Crafted malicious document file
2. Network access to the upload endpoint
3. curl or similar HTTP client

## Defense

Defensive measures and detection strategies:

- Validate and sanitize uploaded file contents
- Rate limit uploads and monitor for anomalous patterns

## Objectives

1. Deliver the payload to the target service
2. Trigger document processing
3. Avoid detection during upload

## Instructions

### Step 1: Perform Upload

**Context**: Send the file to the vulnerable endpoint.

**Command** ([[commands/upload-document]]):
```bash
curl -F 'file=@malicious.docx' https://pu.vk.com/upload
```

> This command uploads the file using multipart form data to the target URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/upload-document]]

## Tools Used



## Tags

- [[file-upload]]
- [[xxe]]
