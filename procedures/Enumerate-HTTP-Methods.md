---
id: 8d4fe9d6-1762-4539-bd8b-c9aa93353ffe
name: Enumerate-HTTP-Methods
type: procedure
verified: true
submitted: true
created_at: '2020-07-19T06:50:16.874055+00:00'
updated_at: '2023-05-26T01:01:23.081346+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - '[[tags/Enumeration]]'
  - '[[tags/misconfiguration]]'
  - '[[tags/Web Applications]]'
commands:
  - '[[commands/nmap-enumerate-http-methods]]'
  - '[[commands/netcat-enumerate-http-methods]]'
platforms:
  - Web
tools:
  - '[[tools/Nmap]]'
  - '[[tools/Netcat]]'
validated: true
---

# Enumerate-HTTP-Methods

## Summary

This procedure enumerates the HTTP methods allowed on a target web server to identify potentially insecure configurations. By discovering methods like PUT, DELETE, TRACE, or OPTIONS, attackers can exploit them for actions such as resource creation/deletion, Cross-Site Tracing (XST), or information disclosure during the reconnaissance phase of an engagement.

## Description

HTTP methods define the actions a web server can perform, such as GET for retrieving data or POST for submitting forms. Misconfigurations often expose unnecessary methods, enabling attacks like uploading malicious files via PUT or reflecting input via TRACE for XST. This procedure uses automated tools like Nmap's NSE scripts or manual connections with Netcat to send OPTIONS requests, which prompt the server to list allowed methods. It is typically used early in web application testing to map the attack surface, focusing on ports 80 (HTTP) or 443 (HTTPS). Success reveals server capabilities without exploitation, aiding in planning subsequent steps like method-based vulnerabilities.

## Requirements

1. Network connectivity to the target web server (no firewall blocking outbound requests from your machine).
2. Installed tools: Nmap (with NSE scripts) or Netcat (nc).
3. Knowledge of the target hostname/IP and port (default: 80 for HTTP).
4. For HTTPS targets, additional handling like stunnel may be needed, but this procedure assumes HTTP.

## Defense

- Configure web servers (e.g., Apache, Nginx) to restrict methods to only necessary ones (GET, POST, HEAD) using directives like <LimitExcept> in Apache or limit_except in Nginx.
- Deploy Web Application Firewalls (WAFs) like ModSecurity to block or log unusual OPTIONS requests and disallowed methods.
- Enable HTTP method override protections and monitor server logs for anomalous method usage, integrating with SIEM for alerts on TRACE or PUT attempts.

## Objectives

1. Identify all HTTP methods permitted by the target server.
2. Detect insecure methods that could enable further attacks like file uploads or tracing exploits.
3. Gather intelligence on server configuration for targeted vulnerability assessment.

## Instructions

### Step 1: Enumerate Methods Using Nmap

**Context**: Leverage Nmap's http-methods NSE script to automatically send an OPTIONS request and parse the server's response, providing a structured output of supported methods. This is efficient for scanning multiple hosts or integrating into larger reconnaissance workflows.

**Command** ([[commands/nmap-enumerate-http-methods]]):
```bash
nmap --script http-methods $_TARGET_HOST
```

> The script connects to the web server on port 80 by default, issues an OPTIONS / request, and extracts the Allow header. Use this when you have Nmap available and want scripted, non-interactive enumeration. If the target uses HTTPS, add -p 443 and consider --script-args http-methods.ssl=true.

### Step 2: Manually Enumerate Methods Using Netcat

**Context**: Establish a raw TCP connection to the server and manually send an OPTIONS request to retrieve the allowed methods. This method is useful for understanding the protocol interaction or when Nmap is unavailable, allowing direct inspection of the HTTP response.

**Command** ([[commands/netcat-enumerate-http-methods]]):
```bash
nc $_TARGET_HOST $_TARGET_PORT
OPTIONS / HTTP/1.1
Host: $_TARGET_HOST
```

> After running nc to connect, type the OPTIONS request lines and press Enter twice to send. The server responds with the Allow header listing methods. This interactive approach helps verify responses manually and can be adapted for custom headers. Close the connection with Ctrl+C after receiving the output.
