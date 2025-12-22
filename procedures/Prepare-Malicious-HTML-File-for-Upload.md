---
id: proc-mopub-prep-upload-001
tags:
  - file-upload
  - xss
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-13T23:55:20.372Z'
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
# Prepare-Malicious-HTML-File-for-Upload

## Summary

This procedure involves creating an HTML file with a JavaScript payload and renaming it with a .jpg extension to attempt upload in MoPub's app icon settings, initiating the stored XSS attack vector.

## Description

In the context of MoPub's app management at app.mopub.com, attackers with authenticated access can exploit weak client-side validation by preparing a file that appears as an image but contains executable HTML/JS. This step sets up the upload attempt, which will be intercepted in the next phase. The expected outcome is the generation of an upload request that can be manipulated server-side.

## Requirements

1. Authenticated session to app.mopub.com
2. Text editor to create HTML file
3. Proxy tool like Burp Suite configured for interception

## Defense

Defensive measures and detection strategies:

- Implement client-side file type checks with content inspection
- Log all file upload attempts with metadata

## Objectives

1. Bypass initial file selection validation
2. Prepare payload for server-side exploitation
3. Generate interceptable upload request

## Instructions

### Step 1: Create Malicious File

**Context**: Craft an HTML file with XSS payload and disguise it as an image.

Create a file named 'xssfileuploadcopy.jpg' with content:

```html
<html><body><script>alert('XSS')</script></body></html>
```

> This file will be selected for upload but modified during transmission.

### Step 2: Initiate Upload

**Context**: Navigate to upload interface and select the file.

Log in to app.mopub.com, go to App settings, and select the prepared file for app icon upload.

> The request will be captured by the proxy for modification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- file-upload
- xss-prep
