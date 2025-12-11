---
url: null
tags:
  - proxy
  - interception
type: tool
platforms:
  - Linux
  - Windows
  - Mac
description: Tool for intercepting and modifying HTTP requests
id: a5730b63-b14d-43ee-a003-18b01128f1fc
created_at: '2025-12-11T06:10:22.480Z'
updated_at: '2025-12-11T06:10:22.480Z'
verified: false
validated: true
submitted: true
---
# HTTP Proxy

**Status**: Unverified

## Overview

HTTP proxy tools like Burp Suite or ZAP are used to intercept and modify requests, such as changing filetypes in Slack API calls.

## Description

Enables man-in-the-middle for web traffic, crucial for editing requests in exploits like Slack HTML injection.

## Features

- Request interception: Capture and edit HTTP requests.
- Response modification: Alter server responses.
- Traffic analysis: View and manipulate data.

## Installation

### Requirements

- Java runtime for tools like Burp.
- Network configuration access.

### Install Commands

```bash
# Download and run Burp Suite or similar
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
burp
```

### Example 2: Advanced Usage

```bash
burp --proxy
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]
- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual proxy traffic.
- Anomalous request modifications.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/HTTPS-Enabled-Server]]

## References

- Burp Suite documentation
