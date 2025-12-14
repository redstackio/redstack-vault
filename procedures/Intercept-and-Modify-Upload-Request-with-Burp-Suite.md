---
id: proc-002
tags:
  - intercept
  - modification
  - burp-suite
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
updated_at: '2025-12-14T05:32:22.962Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-Upload-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to intercept an HTTP file upload request during resume submission, allowing modification to bypass type restrictions and prepare for webshell injection.

## Description

With an authenticated session, submit a benign file (e.g., .jpg) via the upload form while proxying through Burp Suite. Capture the multipart/form-data POST request, then modify it in Repeater to alter the filename and content. This targets the weak validation in the ASP.NET upload handler on ecjobs.starbucks.com.cn.

## Requirements

1. Burp Suite configured as browser proxy
2. Authenticated session from prior login
3. Test file ready for upload

## Defense

Defensive measures and detection strategies:

- Validate file types server-side using MIME detection, not just extensions
- Log and alert on modified or proxied requests with unusual headers
- Use WAF rules to block common Burp Suite signatures

## Objectives

1. Capture upload request
2. Enable payload modification
3. Bypass client-side checks

## Instructions

### Step 1: Configure Proxy and Submit Test Upload

**Context**: Set up interception to capture the request.

Configure browser to use Burp proxy (default 127.0.0.1:8080), then submit a .jpg file via the resume upload form.

> Intercepted request shows Content-Type: multipart/form-data with filename=avatar.jpg and file contents.

### Step 2: Modify Request in Burp Repeater

**Context**: Alter the request to include space after extension for bypass.

In Burp Repeater, change filename to shell.asp<space> and update the file body if needed. Preserve headers and cookies.

> Modified request ready for forwarding; validation bypasses due to space ignoring the .asp extension check.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[modification]]
