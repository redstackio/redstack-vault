---
url: ''
tags:
  - proxy
  - intercept
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: Tool for intercepting and modifying HTTP requests
id: 9fbe5a98-b4c1-4ed3-8dda-42941a1ec86a
created_at: '2025-12-13T09:01:26.295Z'
updated_at: '2025-12-13T09:01:26.295Z'
verified: false
validated: true
submitted: true
---
# Proxy Tool

**Status**: Unverified

## Overview

A proxy tool like Burp Suite or ZAP used to intercept and manipulate HTTP traffic, essential for capturing and modifying SAML requests.

## Description

This tool allows man-in-the-middle interception of web requests, enabling extraction and editing of parameters like SAMLResponse during authentication flows.

## Features

- Request interception
- Parameter modification
- Traffic logging

## Installation

### Requirements

- Java runtime (for tools like Burp)

### Install Commands

```bash
# Download and run from official site (e.g., Burp Suite)
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
# Set as system proxy and browse to target
```

### Example 2: Advanced Usage

```bash
# Intercept specific endpoint
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual proxy configurations
- Anomalous traffic patterns

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Python3]]

## References

- PortSwigger Burp Suite documentation
