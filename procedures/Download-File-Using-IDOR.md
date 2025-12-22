---
id: proc-download-idor
tags:
  - idor
  - download
  - pii
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Cloud (Salesforce)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Cloud Storage]]'
updated_at: '2025-12-14T17:31:43.131Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Cloud Storage]]'
---
# Download-File-Using-IDOR

## Summary

Use the extracted ContentDocument ID to construct and access a direct download URL, exploiting IDOR to retrieve sensitive files without authentication.

## Description

Salesforce's servlet.shepherd endpoint allows direct file access via ID without checks, leading to exposure of resumes, transcripts, and other PII attachments uploaded via the registration form.

## Requirements

1. Valid ContentDocument ID
2. Browser or HTTP client (e.g., curl)
3. Target instance URL

## Defense

Defensive measures and detection strategies:

- Implement ID validation and user-session binding on download endpoints
- Use signed URLs or temporary tokens for file access
- Monitor download logs for unauthenticated requests

## Objectives

1. Download individual sensitive files
2. Verify PII exposure
3. Repeat for bulk exfiltration

## Instructions

### Step 1: Construct Download URL

**Context**: Build the servlet URL with the ID.

No command; format as https://[instance].experience.[domain]/sfsites/c/sfc/servlet.shepherd/document/download/[ID].

> Example: https://example.experience.salesforce.com/sfsites/c/sfc/servlet.shepherd/document/download/069830000028KJdAAM.

### Step 2: Access URL for Download

**Context**: Retrieve the file content.

No command; paste URL in browser or use curl [[commands/curl-download]]:

```bash
curl -O https://[instance]/sfsites/c/sfc/servlet.shepherd/document/download/[ID]
```

> File saves locally (e.g., resume.pdf); inspect for PII like names and emails.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Data from Cloud Storage]] Data from Cloud Storage Object

### Sub-Techniques


## Commands Used

- [[commands/curl-download]]

## Tools Used


## Tags

- [[idor]]
- [[download]]
