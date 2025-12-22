---
tags:
  - xxe
  - file-upload
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Upload-Scanner]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/post-upload-image]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: f71880d2-bd18-4257-a725-c03ea9d28c8c
created_at: '2025-12-13T09:00:33.729Z'
updated_at: '2025-12-13T09:00:33.729Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Detect XXE in File Upload

## Summary

This procedure uses automated scanning to identify XXE vulnerabilities in file upload endpoints by injecting payloads into image metadata.

## Description

The procedure targets web applications that parse XML-based metadata in uploaded files, such as XMP in JPEGs, without disabling external entities. It leverages Burp Suite extensions to automate detection, suitable for penetration testing of Java-based servlets.

## Requirements

1. Access to Burp Suite Professional
2. Upload Scanner extension installed
3. Target upload endpoint URL

## Defense

Defensive measures and detection strategies:

- Configure XML parsers to disable external entity resolution
- Monitor for unexpected outbound network requests

## Objectives

1. Detect XXE vulnerability
2. Confirm payload injection point
3. Prepare for manual exploitation

## Instructions

### Step 1: Scan Upload Endpoint

**Context**: Intercept and scan the upload request.

**Command** ([[commands/post-upload-image]]):
```bash
POST /edit-profile-avatar!uploadImage.jspa HTTP/1.1
Host: target.com
```

> This uploads a JPEG with injected XXE payload in XMP metadata, triggering the scan.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used

- [[commands/post-upload-image]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Upload-Scanner]]

## Tags

- [[xxe]]
- [[file-upload]]
