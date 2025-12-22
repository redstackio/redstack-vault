---
id: 700c5c07-42f5-41c1-8c33-b6f9d2447f9d
name: Java-Jar-Protocol-SSRF-Bypass
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.751967+00:00'
updated_at: '2023-04-10T20:23:55.812605+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Bypassing filters]]'
  - '[[tags/Bypassing using jar protocol (java only)]]'
  - '[[tags/Server-Side Request Forgery]]'
  - ssrf
  - java
  - bypass
commands:
  - '[[commands/curl-basic-ssrf-test]]'
  - '[[commands/curl-jar-ssrf-http]]'
  - '[[commands/curl-jar-ssrf-https]]'
  - '[[commands/curl-jar-ssrf-ftp]]'
platforms:
  - Web
  - Java
tools: []
validated: true
---

# Java-Jar-Protocol-SSRF-Bypass

## Summary

This procedure outlines how to exploit server-side request forgery (SSRF) vulnerabilities in Java applications by leveraging the JAR protocol to bypass URL filters, enabling unauthorized access to internal network resources such as localhost services, metadata endpoints, or private servers.

## Description

Java applications often use the JAR protocol (jar:) to load resources from JAR archives over network protocols like HTTP, HTTPS, or FTP. In SSRF scenarios, attackers can construct URLs like 'jar:http://internal-ip!/' to trick the application into making requests to filtered internal destinations. This bypasses common blacklists that block direct IP access (e.g., 127.0.0.1 or 10.0.0.0/8) because the filter sees 'jar:' as a benign protocol. The technique is particularly effective against Java web apps like those built with Spring or Tomcat, where user-supplied URLs are processed without proper validation. Successful exploitation can lead to data exfiltration, port scanning, or lateral movement by accessing internal APIs, databases, or cloud metadata services.

## Requirements

1. A confirmed SSRF vulnerability in a Java-based web application, typically an endpoint that accepts and fetches user-controlled URLs (e.g., image loaders, webhooks, or resource importers).
2. Network access to the target application from an external position.
3. Tools like curl or Burp Suite for crafting and sending requests.
4. Knowledge of internal targets, such as localhost ports (e.g., 8080 for admin panels) or private IPs.

## Defense

- Implement comprehensive URL parsing and validation to block or strip non-standard protocols like 'jar:', restricting inputs to whitelisted schemes (http/https only).
- Deploy web application firewalls (WAFs) with rules to detect and block JAR protocol usage or anomalous internal requests.
- Segment the network to prevent application servers from accessing sensitive internal resources, using firewalls or VPC controls.
- Enable application-level logging for all outbound requests and monitor for connections to localhost or private IPs.

## Objectives

1. Confirm SSRF vulnerability and bypass protocol filters using JAR URLs.
2. Access and retrieve data from internal services or hosts.
3. Facilitate further attacks like internal reconnaissance or privilege escalation via pivoted access.

## Instructions

### Step 1: Verify Basic SSRF Vulnerability

**Context**: Before attempting bypasses, confirm the endpoint can make internal requests by testing with a direct localhost URL. This establishes the vulnerability baseline and identifies any basic IP blocking.

**Command** ([[commands/curl-basic-ssrf-test]]):
```bash
curl -X POST http://target.com/ssrf-endpoint -d 'url=http://127.0.0.1:80/'
```

> This sends a simple HTTP request to localhost port 80. If the response includes internal content (e.g., a 200 OK from an internal web server) or a timeout indicating connection, SSRF is confirmed. If blocked, proceed to JAR bypass. Why: Validates the attack surface without revealing advanced techniques.

### Step 2: Bypass with JAR HTTP Protocol

**Context**: Use the JAR protocol over HTTP to wrap the internal URL, evading filters that block direct internal IPs. This step targets HTTP-based internal services.

**Command** ([[commands/curl-jar-ssrf-http]]):
```bash
curl -X POST http://target.com/ssrf-endpoint -d 'url=jar:http://127.0.0.1:8080!/' --proxy http://127.0.0.1:8080
```

> Expected output: The application fetches the JAR resource, resulting in a response containing internal HTTP content (e.g., admin page HTML) or an error revealing internal access. If successful, the '!' separator tricks the parser into requesting the internal host. Why: JAR allows protocol chaining, common in Java's URL handler.

### Step 3: Test JAR HTTPS for Secure Internal Services

**Context**: For internal services using HTTPS, adapt the JAR payload to handle SSL. This extends the bypass to encrypted endpoints.

**Command** ([[commands/curl-jar-ssrf-https]]):
```bash
curl -X POST http://target.com/ssrf-endpoint -d 'url=jar:https://127.0.0.1:443!/' --proxy http://127.0.0.1:8080
```

> Expected output: Internal HTTPS response data, such as certificate details or secured API output, confirming bypass. Decision point: If TLS errors occur, the app may not support HTTPS in JAR; fall back to HTTP. Why: Demonstrates versatility against mixed-protocol environments.

### Step 4: Exploit with JAR FTP for File Access

**Context**: Target file-based internal services like FTP servers to exfiltrate data. This is useful for reading sensitive files on internal hosts.

**Command** ([[commands/curl-jar-ssrf-ftp]]):
```bash
curl -X POST http://target.com/ssrf-endpoint -d 'url=jar:ftp://internal-ftp-server/files!/sensitive.txt' --proxy http://127.0.0.1:8080
```

> Expected output: Contents of the internal file or FTP directory listing in the response. Success criteria: Non-empty data or FTP-specific errors indicating connection. Why: JAR FTP enables direct file reads, escalating from recon to exfiltration.

### Step 5: Analyze and Pivot

**Context**: Review responses for further opportunities, such as chaining to other vulns or extracting tokens.

> No specific command; manually inspect outputs for internal headers, IPs, or data. If access granted, use tools like [[tools/Burp-Suite]] to chain requests. Decision point: If blocked, try variations like 'jar:file:...' for local files.
