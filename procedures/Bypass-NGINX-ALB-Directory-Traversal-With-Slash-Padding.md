---
id: a1c02ec2-8475-4cd5-b88c-275f83bbeb49
name: Bypass-NGINX-ALB-Directory-Traversal-With-Slash-Padding
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:57.940709+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/File and Directory Discovery|T1083 - File and Directory
    Discovery]]
sub_techniques: []
tags:
  - directory-traversal
  - nginx
  - alb
  - bypass
  - web-exploitation
commands:
  - '[[commands/curl-standard-directory-traversal]]'
  - '[[commands/curl-slash-padded-directory-traversal-bypass]]'
platforms:
  - Web
tools: []
validated: true
---

# Bypass-NGINX-ALB-Directory-Traversal-With-Slash-Padding

## Summary

This procedure demonstrates how to bypass directory traversal protections implemented in NGINX and Amazon Load Balancer (ALB) by padding the URL with multiple forward slashes before the traversal sequence (e.g., '../'). This technique allows unauthorized access to files and directories outside the web root, potentially leading to sensitive data exposure or further system compromise in web applications.

## Description

NGINX and ALB often include rules to block standard directory traversal attempts using sequences like '../' in URLs. However, these protections can be evaded by prepending multiple forward slashes (e.g., '////////') to the traversal path, which confuses the normalization process and allows the request to reach the backend application. This is particularly effective against misconfigured web servers hosting applications on Linux/Unix systems. The attack targets public-facing web endpoints and requires no authentication, making it a low-privilege entry point for discovery of configuration files, source code, or system details. Success depends on the absence of additional input sanitization in the application layer.

## Requirements

1. Network access to the target web server (e.g., via internet or internal network).
2. Knowledge of the target application's base URL and potential traversal points (e.g., file download or image endpoints).
3. A tool like curl for sending HTTP requests (pre-installed on most Linux systems).
4. Optional: A proxy like Burp Suite for intercepting and modifying requests in real-time.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and path normalization on the application side to canonicalize URLs and block any '..' sequences.
- Configure NGINX and ALB with comprehensive WAF rules to detect and block slash-padded traversal patterns (e.g., using mod_security or AWS WAF).
- Regularly audit and patch web server configurations, enabling logging for all HTTP requests to monitor for anomalous paths.
- Use file system permissions to restrict web server access to sensitive directories outside the root.

## Objectives

1. Traverse directory boundaries to access files outside the web root, such as /etc/passwd or application configs.
2. Exfiltrate sensitive data like credentials, source code, or system information.
3. Establish a foothold for further exploitation, such as chaining with RCE if sensitive files reveal vulnerabilities.

## Instructions

### Step 1: Test Standard Directory Traversal

**Context**: Begin by attempting a basic directory traversal to confirm if the target is vulnerable without bypasses. This establishes a baseline and verifies the endpoint's behavior.

**Command** ([[commands/curl-standard-directory-traversal]]):
```bash
curl "http://$_TARGET_HOST/$_TRAVERSAL_PATH"
```

> This sends a GET request with a standard '../' sequence. If blocked, expect a 403 Forbidden or normalized redirect; if vulnerable, it returns directory contents or file data. Replace placeholders with actual values, e.g., target host and path like '../../etc/passwd'.

### Step 2: Apply Slash-Padding Bypass for NGINX/ALB

**Context**: If the standard traversal fails due to NGINX/ALB filtering, modify the URL by adding multiple forward slashes before the traversal sequence. This disrupts the server's path normalization, allowing the request to bypass security rules and reach the backend.

**Command** ([[commands/curl-slash-padded-directory-traversal-bypass]]):
```bash
curl "http://$_TARGET_HOST////////$_TRAVERSAL_PATH"
```

> This crafts a request with slash padding (e.g., '////////../../etc/passwd'). Monitor the response for successful file access, such as readable content from sensitive files. Adjust slash count (8+ recommended) based on server behavior; use --verbose flag in curl for detailed headers.
