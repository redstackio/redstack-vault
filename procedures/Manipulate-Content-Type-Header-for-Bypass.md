---
tags:
  - header-manipulation
  - bypass
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-header-manipulate]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-13T23:52:25.266Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: e423a131-476f-4152-95f7-a972c7a060ff
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Manipulate-Content-Type-Header-for-Bypass

## Summary

This procedure manipulates the Content-Type header in the file upload request to bypass server-side validation, allowing an HTML file to be accepted as an image by using a mixed value like 'text/html; image/png'.

## Description

The vulnerability stems from the server's failure to strictly parse or validate the Content-Type header, accepting hybrid values that include both HTML and image MIME types. In the Booth.pm upload function, this allows uploading an HTML file containing JavaScript, which is then stored without proper sanitization. Prerequisites include access to the upload form from the previous procedure. The outcome is a successful bypass, enabling malicious file ingestion.

## Requirements

1. Captured or modifiable upload request (via proxy like Burp or dev tools)
2. Malicious HTML file prepared with JS payload
3. HTTP client capable of custom headers (e.g., curl)

## Defense

Defensive measures and detection strategies:

- Strictly parse Content-Type to allow only exact image MIME types (e.g., image/png without extras)
- Validate file content signature against declared type using libraries like libmagic
- Log and alert on anomalous Content-Type values in uploads

## Objectives

1. Craft a request that evades type checking
2. Ensure the server processes the file as valid
3. Set up for successful upload of non-image content

## Instructions

### Step 1: Prepare Malicious File

**Context**: Create an HTML file with embedded JavaScript to test XSS.

**Instructions**: Save the following as malicious.html: <html><body><script>alert(document.domain);</script></body></html>

> This payload will execute when loaded, demonstrating domain access.

### Step 2: Modify Upload Request

**Context**: Intercept the multipart upload and alter the Content-Type header.

**Command** ([[commands/curl-header-manipulate]]):
```bash
curl -X POST https://manage.booth.pm/design/edit/upload -H "Cookie: session=your_session_cookie" -H "Content-Type: text/html; image/png" --form "header_image=@malicious.html" -v
```

> This sends the file with a mixed Content-Type. Expected output: Server response 200 or redirect indicating success; check for no validation error.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques


## Commands Used

- [[commands/curl-header-manipulate]]

## Tools Used


## Tags

- [[header-manipulation]]
- [[bypass]]
