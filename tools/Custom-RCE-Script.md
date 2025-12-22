---
id: tool-uuid-placeholder
url: null
tags:
  - rce
  - exploit
  - scripting
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:36.205Z'
validated: true
submitted: true
---
# Custom-RCE-Script

**Status**: Unverified

## Overview

A bespoke Python script designed to demonstrate remote code execution (RCE) by exploiting code injection vulnerabilities in web applications, such as the DoD website flaw associated with CVE-2013-2165. Its primary purpose is to send crafted payloads to vulnerable endpoints, executing benign commands on the server for proof-of-concept testing in security research.

## Description

This tool is a simple, custom-developed script using the requests library to automate HTTP requests with injected code payloads. It targets input parameters that the server interprets as executable commands, allowing researchers to verify RCE without causing harm. Commonly used in vulnerability discovery and reporting, it highlights risks in un-sanitized user inputs on public-facing web servers. Features include payload customization and response parsing for command output.

## Features

- Feature 1: Customizable payload injection for various commands (e.g., 'id', 'whoami')
- Feature 2: HTTP POST/GET support for different endpoint methods
- Feature 3: Basic response logging to capture executed command outputs

## Installation

### Requirements

- Python 3.x
- requests library (pip install requests)

### Install Commands

```bash
pip install requests
```

## Basic Usage

```bash
python custom_rce_script.py --url https://target-endpoint --payload '; id'
```

### Common Options

| Option | Description |
|--------|-------------|
| `-u, --url` | Target endpoint URL |
| `-p, --payload` | Injection payload (e.g., '; command') |
| `-v, --verbose` | Enable detailed logging |

## Examples

### Example 1: Basic Usage

```bash
python custom_rce_script.py -u https://dod-website/form -p '; id'
```

### Example 2: Advanced Usage

```bash
python custom_rce_script.py -u https://dod-website/api -p '| whoami' --verbose
```

## Expected Output

Description of what output to expect when the command runs successfully: HTTP response containing the executed command's result, e.g., 'uid=33(www-data) gid=33(www-data) groups=33(www-data)'.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous HTTP requests with semicolon or pipe characters in parameters
- Server logs showing unexpected command executions (e.g., 'id' in web context)
- Network traffic analysis for scripted POSTs to vulnerable endpoints

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[sqlmap]]

## References

- HackerOne Report: https://hackerone.com/reports/235605
- CVE-2013-2165 Details
