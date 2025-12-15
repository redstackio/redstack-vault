---
id: proc-identify-lfi-sony-param
tags:
  - lfi
  - web
  - parameter-testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-lfi-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:22.184Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-LFI-Vulnerable-URL-Parameter

## Summary

This procedure tests a URL parameter in a web endpoint for Local File Inclusion (LFI) vulnerabilities by injecting traversal paths to access local files, confirming if the application fails to sanitize inputs.

## Description

In the context of the Sony endpoint, the procedure involves sending HTTP requests with manipulated URL parameters to include paths like ../../etc/passwd. If successful, it reveals the application's inability to validate inputs, allowing directory traversal and file reading. This is typically performed on public-facing web applications without authentication, leading to information disclosure.

## Requirements

1. Network access to the target endpoint (e.g., http://www.████)
2. Basic HTTP client like curl or a browser
3. Knowledge of common file paths on Linux systems (/etc/passwd for testing)

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization on URL parameters to block path traversal
- Use web application firewalls (WAF) to detect and block LFI payloads like ../ sequences
- Monitor server logs for anomalous file access patterns or unusual HTTP parameters

## Objectives

1. Confirm LFI vulnerability in the URL parameter
2. Validate file inclusion by retrieving known file contents
3. Assess potential for broader system enumeration

## Instructions

### Step 1: Prepare Test Payload

**Context**: Construct a URL with a traversal payload targeting a known sensitive file to test inclusion.

**Command** ([[commands/curl-lfi-test]]):
```bash
curl "http://www.████?param=../../etc/passwd" -v
```

> This command sends a GET request to the Sony endpoint with the parameter set to a path traversal string. The -v flag provides verbose output to inspect headers and response. Expected output includes the contents of /etc/passwd if vulnerable, such as root:x:0:0:root:/root:/bin/bash.

### Step 2: Analyze Response

**Context**: Review the HTTP response body for signs of file inclusion versus error messages.

**Command** ([[commands/curl-lfi-test]]):
```bash
curl "http://www.████?param=../../etc/passwd" | grep -i "root"
```

> Pipe the output through grep to check for user entries like 'root'. Success is indicated by matching lines; failure shows 404 or application errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-lfi-test]]

## Tools Used


## Tags

- [[lfi]]
- [[web]]
- [[parameter-testing]]
