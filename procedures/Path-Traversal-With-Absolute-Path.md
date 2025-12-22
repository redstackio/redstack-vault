---
id: 323f458f-ea3b-4a63-9a1d-df517ad24319
name: Path-Traversal-With-Absolute-Path
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T15:39:14.770226+00:00'
updated_at: '2023-05-26T01:37:47.891462+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Path Traversal]]'
  - '[[tags/Web Applications]]'
commands:
  - '[[commands/curl-send-path-traversal-request]]'
tools:
  - '[[tools/Burp-Suite]]'
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Path-Traversal-With-Absolute-Path

## Summary

This procedure exploits path traversal vulnerabilities in web applications by using absolute file paths to access sensitive internal files, such as /etc/passwd, bypassing potential filters or WAF rules that block relative traversal sequences like ../. It is useful when reconnaissance identifies endpoints that handle file parameters without proper sanitization.

## Description

Path traversal attacks allow attackers to read arbitrary files on the server by manipulating file path parameters in HTTP requests. In this variant, absolute paths (e.g., starting with /) are used instead of relative ones, which may evade detection mechanisms designed to block ../ patterns. This technique targets web applications misconfigured to resolve paths directly to the filesystem. It is commonly applicable to file viewer or download endpoints. Success depends on the server's file system permissions and the absence of path normalization. Expected outcomes include retrieval of configuration files, user databases, or system files, potentially leading to further exploitation like credential harvesting.

## Requirements

1. Network access to the vulnerable web application (e.g., HTTP/HTTPS endpoint).
2. Knowledge of target file paths (e.g., /etc/passwd on Linux servers).
3. Burp Suite for request interception and manipulation, or curl for direct HTTP requests.
4. No authentication required if the endpoint is public-facing; otherwise, valid session cookies or credentials.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to reject absolute paths and traversal sequences.
- Use path normalization libraries to resolve and validate file paths before access.
- Deploy WAF rules to block requests containing absolute paths or suspicious file extensions in parameters.
- Restrict web server processes to minimal filesystem permissions, using chroot or containers.
- Monitor access logs for requests to sensitive paths like /etc/ or /proc/.

## Objectives

1. Identify and confirm a vulnerable file-handling endpoint.
2. Retrieve contents of sensitive system files using absolute path manipulation.
3. Validate the vulnerability for potential escalation to data exfiltration or further attacks.

## Instructions

### Step 1: Identify and Intercept the Vulnerable Request

**Context**: Locate an endpoint that accepts a filename parameter (e.g., /view-details) and use Burp Suite to intercept a legitimate request. This establishes a baseline response before modification. If using curl, craft the initial request directly.

**Command** ([[commands/curl-send-path-traversal-request]]):
```bash
curl -X POST http://$_TARGET_URL/view-details -d "filename=$_FILENAME" -v
```

> This sends a POST request with a benign filename (e.g., normal.txt) to observe the normal response structure, such as file contents or error messages. The -v flag provides verbose output for debugging headers and status codes. Expected output includes a 200 OK response with the requested file's content or a success indicator.

### Step 2: Modify Parameter for Absolute Path Traversal

**Context**: Alter the filename parameter to an absolute path targeting a sensitive file, such as /etc/passwd. This bypasses relative traversal filters by directly specifying the full path from the root directory. Resend the request and inspect the response for file contents.

**Command** ([[commands/curl-send-path-traversal-request]]):
```bash
curl -X POST http://$_TARGET_URL/view-details -d "filename=/etc/passwd" -v
```

> Substitute /etc/passwd with other targets like /etc/shadow or application configs (e.g., /var/www/config.php). If the server is Windows-based, use paths like C:\Windows\System32\drivers\etc\hosts. Expected output is a successful response (200 OK) containing the raw file contents, confirming the traversal. If blocked, try URL encoding (e.g., %2Fetc%2Fpasswd) or check for additional filters.

### Step 3: Verify and Extract Data

**Context**: Confirm the retrieved data is valid and non-empty. If successful, document the contents for further analysis, such as parsing user accounts from /etc/passwd. If the response is truncated or errored, iterate with variations like null byte injection (%00) to terminate path resolution.

**Command** ([[commands/curl-send-path-traversal-request]]):
```bash
curl -X POST http://$_TARGET_URL/view-details -d "filename=/etc/passwd%00" -v | grep "root:x:0:0"
```

> The %00 appends a null byte to potentially bypass extensions. Pipe to grep for quick validation of known patterns (e.g., root user entry). Expected output includes lines like "root:x:0:0:root:/root:/bin/bash", indicating successful file read.
