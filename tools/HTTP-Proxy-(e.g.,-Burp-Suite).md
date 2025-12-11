---
url: 'https://portswigger.net/burp'
tags:
  - interception
  - proxy
type: tool
platforms:
  - Web
  - Linux
  - Windows
  - macOS
description: >-
  An HTTP proxy tool for intercepting and manipulating web traffic, commonly
  used in security testing to exploit timing-based vulnerabilities.
id: eaf7a605-7050-468a-8d9f-56d847bbfe56
created_at: '2025-12-11T03:47:56.668Z'
updated_at: '2025-12-11T03:47:56.668Z'
verified: false
validated: true
submitted: true
---
# HTTP Proxy (e.g., Burp Suite)

**Status**: Unverified

## Overview

Burp Suite is a comprehensive platform for web application security testing, including proxy capabilities for intercepting, inspecting, and modifying HTTP/S traffic.

## Description

This tool allows attackers to capture and delay requests, essential for exploiting race conditions in web applications like Shopify's email verification process.

## Features

- Feature 1: Traffic interception and modification
- Feature 2: Request replay and timing control
- Feature 3: Integration with other testing tools

## Installation

### Requirements

- Java Runtime Environment
- Compatible OS

### Install Commands

```bash
# Download and run from official site
```

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
# Launch Burp Suite and configure browser proxy
```

### Example 2: Advanced Usage

```bash
# Use Intruder for timing attacks
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual proxy traffic patterns
- Detection method 2: Anomalies in request timing

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #zaproxy

## References

- Official documentation: https://portswigger.net/burp/documentation
