---
tags:
  - xss
  - file-upload
  - web-vulnerability
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-upload-malicious-file]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: a624ef88-07ae-48e0-b089-c7719d19c8a0
created_at: '2025-12-14T00:11:16.675Z'
updated_at: '2025-12-14T00:11:16.675Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Upload Malicious Files to TikTok Ads Video Function

## Summary

This procedure involves exploiting a stored XSS vulnerability by uploading MP4 or XML files containing embedded HTML and JavaScript code to the video upload function on ads.tiktok.com, bypassing content validation checks.

## Description

The attack targets the video upload endpoint, which fails to properly validate file contents, allowing malicious code to be stored and later executed. This can lead to arbitrary code execution in victims' browsers, potentially enabling session hijacking or data exfiltration. The procedure assumes access to a valid TikTok Ads account and requires preparing files with XSS payloads.

## Requirements

1. Valid credentials for ads.tiktok.com
2. Network access to the TikTok Ads platform
3. Tool: curl for handling HTTP uploads

## Defense

Defensive measures and detection strategies:

- Implement strict content validation and sanitization on file uploads
- Monitor upload logs for suspicious file types or payloads

## Objectives

1. Upload malicious file successfully
2. Bypass validation to store XSS payload
3. Prepare for execution in victim browsers

## Instructions

### Step 1: Prepare Malicious File

**Context**: Create an XML or MP4 file with embedded HTML/JS, such as <script>alert('XSS');</script>.

Save the file as malicious.xml.

> This step ensures the payload is ready for upload.

### Step 2: Upload File to Endpoint

**Context**: Send the file to the video upload function using an authenticated request.

**Command** ([[commands/curl-upload-malicious-file]]):
```bash
curl -X POST https://ads.tiktok.com/upload -H 'Authorization: Bearer YOUR_TOKEN' -F 'file=@malicious.xml' -F 'type=video'
```

> This command uploads the file; replace YOUR_TOKEN with a valid access token. Expect a success response if validation is bypassed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/curl-upload-malicious-file]]

## Tools Used

- [[tools/curl]]

## Tags

- [[xss]]
- [[file-upload]]
