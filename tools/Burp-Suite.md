---
id: a07f2581-994b-4bf1-8382-143a03e29c9a
name: Burp Suite
type: tool
verified: false
created_at: '2025-12-11T06:10:40.633Z'
updated_at: '2025-12-11T06:10:40.633Z'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - proxy
  - interception
url: ''
description: >-
  Web vulnerability scanner and proxy for intercepting and modifying HTTP
  requests
validated: true
submitted: true
---

# Burp Suite

**Status**: Unverified

## Overview

Burp Suite is a comprehensive platform for web application security testing, primarily used for intercepting, analyzing, and modifying HTTP/S traffic.

## Description

It includes tools like a proxy, scanner, intruder, and repeater, commonly used in offensive security to test for vulnerabilities like authentication bypass by altering requests.

## Features

- Feature 1: HTTP proxy for traffic interception
- Feature 2: Automated vulnerability scanning
- Feature 3: Request modification and replay

## Installation

### Requirements

- Java Runtime Environment
- Compatible OS

### Install Commands

```bash
# Download from official site and install
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
burp-suite
```

### Example 2: Advanced Usage

```bash
burp-suite --proxy
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual proxy traffic
- Detection method 2: Modified request patterns

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Browser-Dev-Tools]]
- [[tools/Browser-Console]]

## References

- Official documentation: https://portswigger.net/burp
- Related resources
