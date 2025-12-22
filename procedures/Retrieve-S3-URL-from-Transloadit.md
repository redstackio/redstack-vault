---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - transloadit
  - s3
  - recon
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/transloadit-get-assembly-status]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:16:02.941Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Retrieve-S3-URL-from-Transloadit

## Summary

This procedure polls Transloadit's assembly endpoint to retrieve the S3 URL of the uploaded malicious file after processing, enabling the attacker to locate the stored payload.

## Description

After initiating an assembly upload, Transloadit processes the file asynchronously. Polling the assembly status with seq=0 returns the results, including the URL in the target S3 bucket. This step bridges the upload to exploitation by providing the direct link to the malicious content.

## Requirements

1. Assembly hash from previous upload step
2. HTTP client for GET requests
3. No authentication needed

## Defense

Defensive measures and detection strategies:

- Rate-limit polling requests to assembly endpoints
- Log and alert on uploads of non-image files
- Restrict S3 URLs to authenticated access only

## Objectives

1. Obtain location of stored malicious file
2. Confirm successful processing to S3
3. Prepare for proxy-based execution

## Instructions

### Step 1: Poll Assembly Status

**Context**: Use GET request to fetch the processed file's URL from Transloadit.

**Command** ([[commands/transloadit-get-assembly-status]]):

```bash
curl "https://isadora.transloadit.com/assemblies/[hash]?seq=0&callback="
```

> Replace [hash] with assembly ID. Expected JSON includes S3 URL in 'results' array.

### Step 2: Verify URL Accessibility

**Context**: Test if the S3 URL returns the HTML content.

Use curl to fetch:

```bash
curl "http://coursera-profile-photos.s3.amazonaws.com/[redacted]/stored_xss.html"
```

> Should return the HTML payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

-

## Commands Used

- [[commands/transloadit-get-assembly-status]]

## Tools Used

-

## Tags

- transloadit
- s3
- recon
