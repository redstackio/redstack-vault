---
url: null
tags:
  - proxy
  - interception
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: >-
  Web vulnerability scanner and proxy for intercepting and modifying HTTP
  requests.
id: 67d8693e-2516-42cd-b619-92b03120ba4e
created_at: '2025-12-13T23:56:20.333Z'
updated_at: '2025-12-13T23:56:20.333Z'
verified: false
validated: true
submitted: true
---
# Burp

**Status**: Unverified

## Overview

Burp Suite is a comprehensive platform for web application security testing, used for intercepting requests, identifying vulnerabilities like XSS, and token interception.

## Description

Includes proxy, scanner, repeater, and intruder tools for manual and automated testing of web apps.

## Features

- Request interception and modification
- Vulnerability scanning
- Payload injection and testing

## Installation

### Requirements

- Java Runtime Environment

### Install Commands

```bash
# Download from official site and run
```

## Basic Usage

```bash
burp --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
burp
```

### Example 2: Advanced Usage

```bash
burp --project-file project.burp
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]
- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual proxy traffic
- Modified User-Agent headers

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/CyberChef]]

## References

- https://portswigger.net/burp
