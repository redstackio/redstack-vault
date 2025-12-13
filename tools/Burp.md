---
url: null
tags:
  - proxy
  - scanner
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: >-
  Web vulnerability scanner and proxy for intercepting and modifying HTTP
  requests.
id: af86927f-74e2-4a51-a8f7-92b2713e5256
created_at: '2025-12-13T09:00:28.129Z'
updated_at: '2025-12-13T09:00:28.129Z'
verified: false
validated: true
submitted: true
---
# Burp

**Status**: Unverified

## Overview

Burp Suite is a platform for web application security testing, used to intercept, modify, and analyze HTTP traffic.

## Description

Primarily used for reproducing vulnerabilities like XXE by crafting requests in the Repeater tool.

## Features

- Feature 1: Request interception
- Feature 2: Vulnerability scanning
- Feature 3: Request modification

## Installation

### Requirements

- Java runtime

### Install Commands

```bash
# Download from official site and run
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
tool-name target
```

### Example 2: Advanced Usage

```bash
tool-name --option value target
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual proxy traffic
- Detection method 2: Log anomalies

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/curl]]

## References

- Official documentation
