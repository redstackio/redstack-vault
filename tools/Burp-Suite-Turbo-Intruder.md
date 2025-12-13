---
url: 'https://portswigger.net/burp'
tags:
  - web-testing
  - intruder
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: >-
  Burp Suite extension for automating custom HTTP requests, useful for
  exploiting vulnerabilities like request smuggling.
id: 66e66b0f-2a4c-4780-9513-9ea22c05cf60
created_at: '2025-12-13T09:01:26.074Z'
updated_at: '2025-12-13T09:01:26.074Z'
verified: false
validated: true
submitted: true
---
# Burp Suite Turbo Intruder

**Status**: Unverified

## Overview

Burp Suite Turbo Intruder is an extension for Burp Suite that automates the sending of customized HTTP requests, ideal for testing and exploiting web vulnerabilities such as HTTP Request Smuggling.

## Description

This tool extends Burp Suite's Intruder functionality for high-performance request automation, supporting scripts for complex attack patterns. It's commonly used in offensive security to probe endpoints with malformed requests.

## Features

- Feature 1: High-speed request automation
- Feature 2: Scriptable payloads for custom exploits
- Feature 3: Integration with Burp Suite for traffic analysis

## Installation

### Requirements

- Burp Suite Professional
- Java Runtime Environment

### Install Commands

```bash
# Install via Burp Suite BApp Store or manually load the extension JAR
```

## Basic Usage

```bash
turbo-intruder --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
turbo-intruder -request request.txt -script intruder.py
```

### Example 2: Advanced Usage

```bash
turbo-intruder -request smuggling.req -script intruder.txt -wordlist chars.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual HTTP traffic patterns in web server logs
- Detection method 2: Anomalous request volumes from single IP

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Burp Suite]]
- [[ZAP]]

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: HackerOne reports on request smuggling
