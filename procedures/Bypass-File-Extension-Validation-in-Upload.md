---
id: p-bypass-extension-concrete
tags:
  - bypass
  - validation
  - ssrf
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/test-upload-bypass-curl]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:02.525Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass File Extension Validation in Upload

## Summary

This procedure bypasses the file type restrictions in Concrete CMS's remote upload feature by manipulating URL paths to disguise restricted content as allowed extensions, enabling SSRF on non-standard files.

## Description

The upload feature in Concrete CMS validates file extensions but can be tricked by appending allowed paths (e.g., /test.png) to endpoints like PHP scripts. The server fetches the full response from the base URL and ignores the appended path for content type, allowing arbitrary HTTP responses to be processed as uploads. This is key for SSRF as it permits fetching from script endpoints on internal servers. Prerequisites include access to the upload UI; outcomes enable uploading 'images' that are actually internal page dumps.

## Requirements

1. Access to the remote upload form in Concrete CMS
2. Knowledge of allowed extensions (e.g., .png, .jpg)
3. Target URL with a bypassable endpoint (e.g., index.php)

## Defense

Defensive measures and detection strategies:

- Enforce strict MIME type checking on fetched content, not just extensions
- Validate and sanitize URL paths to prevent appendage manipulation
- Log and alert on uploads from suspicious or internal-like URLs

## Objectives

1. Trick the validation to accept non-image content
2. Confirm bypass allows processing of HTTP 200 responses from any endpoint
3. Set up for private IP targeting

## Instructions

### Step 1: Prepare Bypass URL

**Context**: Construct a URL that ends with an allowed extension but points to a restricted resource.

Use a format like http://target.com/index.php/test.png, where index.php serves the real content.

### Step 2: Submit to Upload Feature

**Context**: Input the crafted URL into the remote upload field.

Execute [[commands/test-upload-bypass-curl]] to simulate or directly test via the UI form submission.

```bash
curl -X POST -F "remote_url=http://192.168.1.148/index.php/test.png" http://concrete-cms.example.com/dashboard/files/upload_remote
```

> This sends the URL to the CMS upload endpoint (adjust path as needed). Expected output: HTTP 200 with file processed, no extension error.

**Expected Output**: Upload succeeds, content saved as .png despite being PHP output.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/test-upload-bypass-curl]]

## Tools Used


## Tags

- [[bypass]]
- [[validation]]
