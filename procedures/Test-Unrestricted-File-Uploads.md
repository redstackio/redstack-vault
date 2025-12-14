---
id: p-test-file-uploads
tags:
  - file-upload
  - recon
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:10.324Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test Unrestricted File Uploads

## Summary

Probe a web endpoint for unrestricted file upload vulnerabilities by attempting to upload malicious files and analyzing error responses to infer processing mechanisms like XML parsing.

## Description

The endpoint was tested with PHP shells, revealing verbose errors about XML processing without file storage, indicating a non-standard upload handler tied to Microsoft Dynamics AX. This helps pivot to XML-based attacks.

## Requirements

1. Access to upload endpoint
2. Malicious file payloads (e.g., PHP shell)
3. HTTP client like curl

## Defense

- Validate and sanitize file types
- Store uploads outside web root
- Log upload attempts

## Objectives

1. Confirm upload processing
2. Identify XML handling
3. Rule out persistence

## Instructions

### Step 1: Attempt Malicious Upload

**Context**: Upload a PHP shell to test restrictions.

**Command** ([[commands/curl-upload-test]]):
```bash
curl -X POST -F "file=@shell.php" http://target-subdomain.example.com/upload
```

> Expected output: Error messages indicating XML parse failure, no file saved.

### Step 2: Analyze Response

**Context**: Review errors for backend clues.

Inspect response for XML references.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-upload-test]]

## Tools Used


## Tags

- file-upload
- xml
