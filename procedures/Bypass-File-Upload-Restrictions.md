---
tags:
  - file-upload-bypass
  - web-exploitation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/intercept-http-request]]'
  - '[[commands/modify-upload-parameters]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: fc17a4fd-a260-42cc-8903-cea9b76d840b
created_at: '2025-12-13T23:56:20.136Z'
updated_at: '2025-12-13T23:56:20.136Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass File Upload Restrictions

## Summary

This procedure demonstrates bypassing file upload restrictions on upload.twitter.com by modifying the file extension to an unknown type during request interception, allowing unrestricted file serving without Content-Type headers.

## Description

The attack targets the Twitter Ads audience manager upload functionality. By intercepting the upload request and changing the blobstore_url to an unknown extension, the file is accepted and served in a way that enables further exploitation like XSS. This works because the server fails to reject unknown extensions, leading to browser sniffing and potential HTML rendering.

## Requirements

1. Access to Twitter Ads audience manager
2. HTTP interception tool like [[tools/Burp-Suite]]
3. Valid Twitter account credentials

## Defense

Defensive measures and detection strategies:

- Implement strict file extension whitelisting and validation
- Monitor for anomalous upload requests with unknown extensions

## Objectives

1. Successfully modify and upload a file with bypassed restrictions
2. Store the file on ton.twitter.com without Content-Type
3. Prepare for payload injection

## Instructions

### Step 1: Initiate Upload and Intercept

**Context**: Navigate to the upload interface and capture the request.

**Command** ([[commands/intercept-http-request]]):

```bash
# Use Burp Suite to intercept the POST request to upload.twitter.com
```

> This captures the upload request for modification.

### Step 2: Modify File Extension

**Context**: Change the blobstore_url to an unknown suffix.

**Command** ([[commands/modify-upload-parameters]]):

```bash
# In intercepted request: Change _blobstore_url_ to e.g., 1440354519600.test
```

> This bypasses extension checks, allowing the file to be served raw.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/intercept-http-request]]
- [[commands/modify-upload-parameters]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- file-upload-bypass
- web-exploitation
