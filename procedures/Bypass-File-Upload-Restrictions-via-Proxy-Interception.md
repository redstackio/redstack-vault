---
id: proc-uuid-67890
name: Bypass-File-Upload-Restrictions-via-Proxy-Interception
tags:
  - unrestricted-file-upload
  - proxy-interception
  - bypass-validation
  - malware-upload
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
  - '[[Malicious File]]'
updated_at: '2025-12-14T05:32:13.096Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
  - '[[Malicious File]]'
---
# Bypass-File-Upload-Restrictions-via-Proxy-Interception

## Summary

This procedure demonstrates how to exploit unrestricted file upload vulnerabilities by intercepting and modifying HTTP requests in a web application's file submission form, specifically bypassing client-side only checks for extensions and sizes to upload malicious payloads like executables.

## Description

In scenarios like the DoD bug reporting feature, client-side JavaScript validates file types (e.g., only .txt allowed) and sizes (e.g., <5MB), but the server lacks corresponding checks. An attacker creates an account, prepares a form submission with a valid file, intercepts the multipart/form-data POST request using a proxy, alters the filename extension (e.g., to .exe) or inflates the content-length, and forwards it. If successful, the server stores the file, which support agents may open, leading to malware execution. This targets public-facing web apps without proper input sanitization.

## Requirements

1. Access to a proxy tool like Burp Suite configured between browser and target
2. Valid user account on the target web application
3. A malicious file prepared locally (e.g., renamed executable under or over size limits)
4. Network connectivity to the target (e.g., https://████████/bug-report endpoint)

## Defense

Defensive measures and detection strategies:

- Implement server-side validation for file extensions, MIME types, and sizes using whitelists
- Scan uploaded files with antivirus/malware detection tools before storage
- Monitor for anomalous upload patterns (e.g., unusual extensions, large sizes) via WAF logs
- Restrict file handling to sandboxed environments for support agents

## Objectives

1. Bypass client-side restrictions to upload disallowed file types or oversized files
2. Achieve server-side persistence of malicious payloads
3. Enable potential execution by tricking users into opening the files

## Instructions

### Step 1: Configure Proxy for Interception

**Context**: Set up a tool to capture and modify outgoing HTTP requests from the browser.

**Instructions**: Launch Burp Suite, configure the browser proxy to 127.0.0.1:8080, and enable interception on the target scope (e.g., https://████████/).

No specific command; use the tool's GUI to set proxy listener and turn on intercept.

> Expected output: Proxy is active, and browser traffic routes through it without errors.

### Step 2: Submit Form and Intercept Request

**Context**: Trigger the upload request to capture it for modification.

**Instructions**: With a valid file attached, submit the bug report form. The proxy will halt the request.

No specific command; interact with the web form.

> Expected output: Intercepted POST request visible, showing multipart/form-data with filename (e.g., test.txt) and Content-Length.

### Step 3: Modify Request and Forward

**Context**: Alter the request to evade validations, then release it to the server.

**Instructions**: In the proxy, edit the filename in the Content-Disposition header (e.g., change "filename*=UTF-8''test.txt" to "filename*=UTF-8''malware.exe" or increase body size). Drop and forward the request.

No specific command; use proxy editor.

> Expected output: Server responds with 200 OK or success message, indicating upload acceptance.

### Step 4: Verify Upload Success

**Context**: Confirm the malicious file was stored and is retrievable.

**Instructions**: Check the bug report dashboard or logs for the uploaded file reference.

No specific command; refresh the web interface.

> Expected output: Uploaded item listed without errors, potentially downloadable by agents.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[Malicious File]] User Execution: Malicious File

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[unrestricted-file-upload]]
- [[proxy-interception]]
- [[web-bypass]]
