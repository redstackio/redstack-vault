---
id: 601eb9ee-93d0-47ec-a76f-c3ae8d480c03
name: Bypass-Path-Traversal-Validation-with-Valid-Prefix
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T17:54:44.342511+00:00'
updated_at: '2023-05-26T18:24:52.530886+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - path-traversal
  - web-applications
  - file-inclusion
commands:
  - '[[commands/curl-download-file-valid-path]]'
  - '[[commands/curl-download-file-traversal]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Bypass-Path-Traversal-Validation-with-Valid-Prefix

## Summary

This procedure outlines how to bypass path traversal protections in web applications that validate only the beginning of a filename parameter. By prepending a legitimate file path (e.g., to an image in a web directory) and appending directory traversal sequences like '../', an attacker can access sensitive files outside the intended directory, such as /etc/passwd on Linux systems. This technique is useful during web vulnerability assessments to test for improper input sanitization in file download or inclusion features.

## Description

Path traversal vulnerabilities (also known as directory traversal) allow attackers to read arbitrary files on a server by manipulating path parameters to navigate up the directory structure. Some applications implement weak filters that check only if the path starts with an allowed prefix, such as '/var/www/images/', assuming any file beginning with that is safe. This procedure exploits that by starting with a valid, accessible file (e.g., '37.jpg') and then using '../' sequences to backtrack to root and reach restricted files like system configuration or password files. It targets web applications with file-serving endpoints, typically over HTTP/HTTPS, and requires no authentication if the endpoint is public-facing. Success reveals server file contents, potentially leading to further reconnaissance or exploitation. This maps to MITRE ATT&CK technique T1083 (File and Directory Discovery) under the Discovery tactic.

## Requirements

1. Network access to the target web application (e.g., via browser or proxy).
2. A proxy tool like [[tools/Burp-Suite]] for intercepting and modifying requests, or curl for direct HTTP testing.
3. Knowledge of the application's file download endpoint and expected valid paths (e.g., from prior reconnaissance).
4. Target running on a Unix-like system (e.g., Linux) for paths like /etc/passwd; adjust for Windows (e.g., C:\Windows\system32\drivers\etc\hosts).

## Defense

- Implement whitelisting for allowed file paths and extensions, validating the entire resolved path on the server side.
- Use absolute path resolution and chroot jails to restrict file access to a safe directory.
- Enable web application firewall (WAF) rules to detect '../' sequences and anomalous path patterns.
- Log and monitor file access attempts, alerting on requests for sensitive paths like /etc/.

## Objectives

1. Identify if the application filters only the path prefix, allowing traversal bypass.
2. Retrieve contents of a sensitive file, such as /etc/passwd, to confirm vulnerability.
3. Demonstrate the impact of weak input validation on file disclosure.

## Instructions

### Step 1: Establish Baseline with Valid Path

**Context**: Send a request with a known valid filename to confirm the endpoint works and observe the normal response. This verifies the parameter (e.g., 'filename') and establishes a baseline for modification. Use [[commands/curl-download-file-valid-path]] to simulate the request directly or intercept via Burp Suite.

**Command** ([[commands/curl-download-file-valid-path]]):
```bash
curl -X GET "http://target.com/download?filename=/var/www/images/37.jpg" -o output.jpg
```

> This command fetches a legitimate image file. If using Burp Suite, configure your browser proxy, navigate to the download page, and intercept the request. Forward it unchanged to see the image load successfully without errors.

### Step 2: Test Traversal Bypass

**Context**: Modify the filename parameter to start with the valid prefix but append traversal sequences to reach a sensitive file. The filter passes because it matches the start, but the full path resolves to /etc/passwd (adjust '../' count based on directory depth, e.g., four '../' to go from /var/www/images/ to /). Use [[commands/curl-download-file-traversal]] or modify the intercepted request in Burp's Repeater tab.

**Command** ([[commands/curl-download-file-traversal]]):
```bash
curl -X GET "http://target.com/download?filename=/var/www/images/../../../etc/passwd" -o sensitive.txt
```

> Send the modified request. In Burp, right-click the intercepted request, send to Repeater, edit the 'filename' parameter to '/var/www/images/../../../etc/passwd' (note: some filters block 'd' in 'passwd', so try '/var/www/images/../../../etc/passw*'), and forward. The response should contain the file contents if vulnerable.

### Step 3: Verify and Analyze Output

**Context**: Check the response for sensitive data indicators, such as user account lines in /etc/passwd (e.g., 'root:x:0:0:root:/root:/bin/bash'). If the output is garbled or error-free but not the expected file, adjust the traversal depth or encoding (e.g., URL-encode '../' as '%2e%2e%2f'). This step confirms exploitation success.

**Instructions**: Review the downloaded file or response body. Look for headers like 'root:x:0:0' to validate access to system files. If blocked, try variations like null-byte injection (%00) or double encoding.
