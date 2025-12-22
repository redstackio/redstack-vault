---
url: null
tags:
  - smuggling
  - testing
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.485Z'
id: c63d212d-6c95-439a-9ba8-d8672c16ec06
validated: true
submitted: true
---
# smuggler

**Status**: Unverified

## Overview

Smuggler is a custom open-source tool for detecting HTTP Request Smuggling vulnerabilities by sending various payloads to test server parsing behaviors.

## Description

Designed for offensive security, it automates tests for CL.TE, TE.CL, and other variants, including edge cases like spaces in headers. Commonly used in bug bounty hunting to identify desyncs in load-balanced web apps.

## Features

- Feature 1: Exhaustive payload testing including 'space1' for CL.TE
- Feature 2: Detailed reporting of vulnerable vectors
- Feature 3: Support for HTTPS targets

## Installation

### Requirements

- Go 1.16+
- Git

### Install Commands

```bash
# Clone and build
go install github.com/defparam/smuggler@latest
```

## Basic Usage

```bash
smuggler --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-u, --url` | Target URL |
| `-v, --verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
smuggler -u https://slackb.com
```

### Example 2: Advanced Usage

```bash
smuggler -u https://target.com -t space1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network scans with smuggling payloads
- Anomalous HTTP requests in WAF logs

## Related Procedures


## Related Tools

- [[tools/Burp-Suite]]

## References

- GitHub repo for smuggler
