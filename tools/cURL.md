---
url: 'https://curl.se'
tags:
  - http-client
  - web-testing
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: 'Command-line tool for transferring data with URLs, useful for HTTP testing'
id: db541d87-02a7-4394-ad6e-cdc95ac652bc
created_at: '2025-12-11T06:10:40.600Z'
updated_at: '2025-12-11T06:10:40.600Z'
verified: false
validated: true
submitted: true
---
# cURL

**Status**: Unverified

## Overview

cURL is a versatile command-line tool for making HTTP requests, testing APIs, and verifying web vulnerabilities.

## Description

In security testing, cURL is used to send custom headers and payloads to exploit issues like request smuggling.

## Features

- Feature 1: Custom header support
- Feature 2: Protocol flexibility (HTTP/1.1, etc.)
- Feature 3: Data posting capabilities

## Installation

### Requirements

- Standard on most Unix systems
- Windows installer available

### Install Commands

```bash
# On Ubuntu
sudo apt install curl
```

## Basic Usage

```bash
curl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-H` | Add header |
| `-d` | Send data |
| `--http1.1` | Use HTTP/1.1 |

## Examples

### Example 1: Basic Usage

```bash
curl https://example.com
```

### Example 2: Advanced Usage

```bash
curl -H "Custom: value" -d "data" https://target.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Log unusual User-Agent
- Detection method 2: Monitor for crafted requests

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Burp-Suite]]
- [[wget]]

## References

- Official documentation: https://curl.se/docs/
