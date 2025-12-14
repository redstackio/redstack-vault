---
id: proc-mopub-intercept-upload-001
tags:
  - file-upload
  - request-modification
  - xss
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:55:20.370Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-File-Upload-Request

## Summary

This procedure uses a proxy to intercept the MoPub app icon upload request, altering the filename extension to .html and Content-Type to text/html, allowing the server to store the malicious file without proper validation.

## Description

Targeting the POST /inventory/app_icon/upload/ endpoint on app.mopub.com, this step exploits the lack of server-side content validation. By modifying the request, the HTML file is uploaded to images.mopub.com/app_icons/[hash], where it can later be served as executable content. Prerequisites include an active upload attempt from the previous step.

## Requirements

1. Burp Suite or similar proxy intercepting traffic to app.mopub.com
2. Ongoing upload request from app settings
3. Knowledge of request structure (multipart/form-data)

## Defense

Defensive measures and detection strategies:

- Validate file content against MIME types on server-side
- Monitor for anomalous Content-Type changes in uploads
- Restrict uploads to authenticated users with rate limiting

## Objectives

1. Bypass server file type restrictions
2. Store arbitrary HTML on image domain
3. Obtain URL for payload execution

## Instructions

### Step 1: Set Up Interception

**Context**: Configure proxy to capture the upload.

In Burp Suite, enable interception for POST requests to /inventory/app_icon/upload/.

> Ensure browser traffic routes through the proxy.

### Step 2: Modify and Forward Request

**Context**: Alter key headers and parameters to force HTML acceptance.

Intercept the request, change filename="xssfileuploadcopy.jpg" to filename="xssfileuploadcopy.html", set Content-Type: text/html in the multipart body, then forward.

> Server responds with upload success and hashed URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- request-intercept
- content-type-bypass
