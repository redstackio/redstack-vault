---
id: 2805b0f9-3294-4a2b-bff6-3785f1d8cb76
name: Burp Proxy
type: tool
verified: false
created_at: '2025-12-11T03:47:47.706Z'
updated_at: '2025-12-11T03:47:47.706Z'
platforms:
  - Windows
  - Linux
  - macOS
tags:
  - proxy
  - intercept
  - web
  - burp-suite
url: 'https://portswigger.net/burp'
description: >-
  A web proxy tool for intercepting and modifying HTTP/S traffic, commonly used
  in security testing.
validated: true
submitted: true
---

# Burp Proxy

**Status**: Unverified

## Overview

Burp Proxy is a component of Burp Suite that allows interception, inspection, and modification of web traffic, ideal for testing vulnerabilities like IDOR in GraphQL queries.

## Description

Enables man-in-the-middle proxying for HTTP/S requests, supporting features like request editing, repeating, and analysis. Used in offensive security for parameter tampering and exploit development.

## Features

- Feature 1: Real-time request interception
- Feature 2: Parameter modification interface
- Feature 3: Response analysis and data extraction

## Installation

### Requirements

- Java Runtime Environment
- Compatible OS (Windows, Linux, macOS)

### Install Commands

```bash
# Download from official site and run the installer
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
# Configure browser to proxy through 127.0.0.1:8080
```

### Example 2: Advanced Usage

```bash
# Use with intercept mode enabled for editing requests
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### Tactics

- [[Initial Access]]
- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual proxy headers in requests
- Detection method 2: Traffic routed through localhost ports

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Charles Proxy]]
- #mitmproxy

## References

- Official documentation: https://portswigger.net/burp/documentation
- Related resources: OWASP testing guides
