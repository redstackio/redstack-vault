---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
url: null
tags:
  - rce
  - custom-script
  - injection
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:41.349Z'
validated: true
submitted: true
---
# RCE-Custom-Script

**Status**: Unverified

## Overview

A custom Python script designed to demonstrate remote code execution (RCE) by exploiting code injection vulnerabilities in web applications, such as the DoD website. It sends crafted payloads to trigger benign command execution on the target server, useful for vulnerability validation in penetration testing.

## Description

This tool is a bespoke script tailored for injecting code into vulnerable web endpoints that unsafely handle user input for command execution. It uses HTTP requests to deliver payloads like semicolon-chained commands, executing them server-side. Common use cases include ethical hacking reports, like the HackerOne disclosure, where it proves RCE without harm. Features include payload customization, response parsing for success indicators, and logging for analysis.

## Features

- Feature 1: Payload crafting for code injection (e.g., '; command')
- Feature 2: HTTP request automation with libraries like requests
- Feature 3: Response validation to confirm command output

## Installation

### Requirements

- Python 3.x
- requests library (pip install requests)

### Install Commands

```bash
# No installation needed; save as .py file
pip install requests
```

## Basic Usage

```bash
python rce_demo.py
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-t, --target` | Specify target URL |
| `-p, --payload` | Custom payload string |

## Examples

### Example 1: Basic Usage

```bash
python rce_demo.py -t https://dod-website.example/endpoint -p 'echo "Test"'
```

### Example 2: Advanced Usage

```bash
python rce_demo.py -t https://target.com/vuln -p '; id > /tmp/output && cat /tmp/output' --verbose
```

## Expected Output

Successful execution returns the command output in the response body, e.g., "uid=33(www-data) gid=33(www-data) groups=33(www-data)" for an 'id' command, confirming RCE.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Anomalous HTTP requests with suspicious payloads (e.g., semicolons, command keywords) in web logs
- Detection method 2: Unexpected file writes or command outputs on the server (e.g., /tmp/test.txt)

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[sqlmap]]

## References

- HackerOne Report #211381
- OWASP Code Injection Cheat Sheet
