---
id: e585edc6-c42a-45d5-b980-3fb9daeaa5e5
name: Detect-TRACE-HTTP-Method-with-Nmap
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T16:56:54.548865+00:00'
updated_at: '2023-05-26T01:12:32.342153+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - HTTP Methods
  - OWASP
  - OWASP Top 10
  - Trace Method
  - Web Applications
commands:
  - '[[commands/nmap-detect-http-trace]]'
platforms:
  - Web
tools:
  - '[[tools/Nmap]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Detect-TRACE-HTTP-Method-with-Nmap

## Summary

This procedure uses Nmap's http-trace script to scan a target web server and determine if the TRACE HTTP method is enabled. The TRACE method can pose a security risk as it may allow attackers to gather sensitive information, such as cookies or authentication headers, potentially leading to cross-site tracing (XST) attacks when combined with other vulnerabilities like XSS.

## Description

The TRACE method is an HTTP method intended for diagnostic purposes, allowing clients to see what servers receive. However, when enabled on production servers, it can expose internal headers and data, aiding in reconnaissance for further attacks. This procedure targets web applications running on standard HTTP ports (typically 80 or 443) and performs an active scan to check for TRACE support. It is useful during initial reconnaissance phases to identify misconfigurations in web servers like Apache or IIS. The scan assumes network access to the target and focuses on non-intrusive probing to avoid triggering alerts.

## Requirements

1. Network access to the target web server on port 80 (or 443 for HTTPS, though the script primarily targets HTTP).
2. Nmap installed on the attacking machine (version 7.0 or later recommended for script support).
3. Basic knowledge of target IP addresses or hostnames.
4. No special credentials required, as this is an external scan.

## Defense

Defensive measures include disabling the TRACE method at the web server level (e.g., via Apache's TraceEnable Off directive or IIS registry settings). Implement web application firewalls (WAFs) to block TRACE requests. Monitor access logs for unusual HTTP method usage and enable logging for all HTTP methods to detect scanning attempts.

## Objectives

1. Identify if the TRACE HTTP method is enabled on the target web server.
2. Gather evidence of the server's HTTP method configuration for vulnerability assessment.
3. Provide indicators for potential follow-up attacks if TRACE is enabled.

## Instructions

### Step 1: Identify Target and Prerequisites

**Context**: Before scanning, confirm the target's IP address or hostname and ensure Nmap is available. This step verifies the setup to avoid execution errors.

Run a basic connectivity check using ping or a simple Nmap host discovery to confirm the target is reachable.

**Command** ([[commands/nmap-host-discovery]]):
```bash
nmap -sn $_TARGET
```

> This command performs a ping scan to check if the host is up without port scanning. Replace $_TARGET with the IP or hostname.

### Step 2: Execute TRACE Method Detection Scan

**Context**: Use Nmap's http-trace script to send a TRACE request and analyze the response. This reveals if the server echoes back the request, indicating TRACE is enabled.

**Command** ([[commands/nmap-detect-http-trace]]):
```bash
nmap --script http-trace -p$_PORT $_TARGET
```

> Execute this on the target web server. The script sends a TRACE / HTTP/1.1 request and checks for a 200 OK response with echoed data. If TRACE is disabled, expect a 405 Method Not Allowed or similar error.

### Step 3: Interpret Results and Verify

**Context**: Review the scan output for indicators of TRACE enablement. If enabled, document for further testing, such as combining with XSS for XST.

Manually verify by using curl to send a TRACE request if Nmap confirms enablement.

**Command** ([[commands/curl-trace-request]]):
```bash
curl -X TRACE http://$_TARGET/
```

> Look for echoed headers in the response. A successful echo confirms the vulnerability. If the response is empty or errored, TRACE is likely disabled.

## Expected Output

Successful detection shows TRACE enabled, allowing reconnaissance of server configurations. If disabled, the procedure confirms a secure configuration.
