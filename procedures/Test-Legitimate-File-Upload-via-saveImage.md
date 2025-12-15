---
tags:
  - file-upload
  - testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/saveimage-normal-post]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:08.081Z'
sub_techniques: []
id: 0e2f4f69-9591-4ad5-af2c-0b6d41fe2f50
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Legitimate-File-Upload-via-saveImage

## Summary

Test the saveImage.php endpoint with legitimate parameters to confirm file creation in the intended directory and understand the 'preview-' prefix behavior.

## Description

The endpoint processes POST requests with 'image' (content), 'filename' (base name), and 'extension' (e.g., png), creating files like preview-test.png in /var/www/html/view/data/image/. This step validates the lack of authentication and validation before attempting exploits.

## Requirements

1. HTTP client like curl
2. Public access to https://reverb.twitter.com
3. Basic image data (e.g., 'SomeContent' as placeholder stream)

## Defense

Defensive measures and detection strategies:

- Enforce authentication on all API endpoints
- Validate file parameters against whitelists
- Log and rate-limit upload attempts

## Objectives

1. Confirm endpoint functionality and directory
2. Identify file naming conventions
3. Verify public accessibility of created files

## Instructions

### Step 1: Send Legitimate POST Request

**Context**: Simulate normal image save to create a PNG file.

**Command** ([[commands/saveimage-normal-post]]):

```bash
curl -X POST https://reverb.twitter.com/api/actions/saveImage.php -d "image=SomeContent&filename=test&extension=png"
```

> Creates /var/www/html/view/data/image/preview-test.png; access at https://reverb.twitter.com/view/data/image/preview-test.png to verify.

### Step 2: Verify File Creation

**Context**: Check if the file is accessible and matches expected format.

Use browser or curl to GET the file URL.

> Expected: Image file loads without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/saveimage-normal-post]]

## Tools Used


## Tags

- [[file-upload]]
- [[web-vuln]]
