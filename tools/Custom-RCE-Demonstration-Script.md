---
url: ''
tags:
  - rce
  - exploit
  - custom-script
  - apache-struts
type: tool
verified: false
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.243Z'
id: 085bab81-af87-4acc-bd26-6ce81348c0ca
validated: true
submitted: true
---
# Custom-RCE-Demonstration-Script

**Status**: Unverified

## Overview

A bespoke script developed to demonstrate remote code execution by exploiting CVE-2017-5638 in Apache Struts on a DoD website, executing a benign command to validate the vulnerability without harm. Primarily used in ethical hacking reports for proof-of-concept.

## Description

This tool is a custom Python or Java script that crafts and sends a deserialization payload to the vulnerable Struts endpoint. It targets the Jakarta Multipart Parser flaw, injecting code to run commands on the web server. In offensive security, it's used for vulnerability validation in web applications, focusing on safe, non-destructive testing.

## Features

- Feature 1: Payload generation for CVE-2017-5638 using tools like ysoserial.
- Feature 2: HTTP request crafting to target specific endpoints.
- Feature 3: Benign command execution for proof without escalation.

## Installation

### Requirements

- Python 3.x or Java runtime.
- Libraries: requests (Python) or Apache HttpClient (Java).

### Install Commands

```bash
# For Python version
pip install requests

# For Java, compile with dependencies
javac -cp . CustomRCE.java
```

## Basic Usage

```bash
python custom_rce_demo.py --target https://dod-website.gov --payload benign_echo
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-t, --target` | Specify the vulnerable URL |
| `-p, --payload` | Define the command payload |

## Examples

### Example 1: Basic Usage

```bash
python custom_rce_demo.py -t https://dod-website.gov/upload
```

### Example 2: Advanced Usage

```bash
python custom_rce_demo.py -t https://dod-website.gov -p "echo 'proof' > /tmp/test.txt" --verbose
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic with encoded deserialization payloads in HTTP POST requests.
- Server logs showing unexpected file writes in /tmp from remote triggers.

## Related Procedures

- [[procedures/Demonstrate-RCE-with-Custom-Script]]

## Related Tools

- [[ysoserial]]

## References

- HackerOne Report: https://hackerone.com/reports/213069
- CVE-2017-5638 Details: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-5638
