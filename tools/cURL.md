---
id: t2u3v4w5-x6y7-8901-rstu-vw8901234567
url: 'https://curl.se/'
name: curl
tags:
  - http
  - testing
  - cli
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:33:24.170Z'
validated: true
submitted: true
---
# curl

**Status**: Unverified

## Overview

cURL is a command-line tool for transferring data with URLs, widely used for API testing and simulating HTTP requests in security assessments like SSRF exploitation.

## Description

In offensive ops, cURL sends custom HTTP requests to test web vulnerabilities, including POST payloads for SSRF via manipulated URLs to internal endpoints.

## Features

- Feature 1: Supports all HTTP methods and headers
- Feature 2: JSON data sending with -d
- Feature 3: Cookie and session handling

## Installation

### Requirements

- Standard on most Unix-like systems

### Install Commands

```bash
# On Ubuntu: sudo apt install curl
# On macOS: brew install curl
```

## Basic Usage

```bash
curl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-X` | Specify HTTP method |
| `-H` | Add headers |
| `-d` | POST data |

## Examples

### Example 1: Basic Usage

```bash
curl https://target.com
```

### Example 2: Advanced Usage

```bash
curl -X POST https://target.com/api -H 'Content-Type: json' -d '{"key":"value"}'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]
- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- cURL User-Agent in access logs
- High volume of POST requests from single IP

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
- [[tools/wget]]

## References

- Official documentation: https://curl.se/docs/manpage.html
- Related resources: HTTP protocol specs
