---
url: 'https://curl.se'
tags:
  - http
  - request
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: >-
  Command-line tool for transferring data with URLs, used for HTTP requests in
  exploits.
id: 3437752c-6be1-4757-b4b3-4bca2b12c817
created_at: '2025-12-13T09:01:26.615Z'
updated_at: '2025-12-13T09:01:26.615Z'
verified: false
validated: true
submitted: true
---
# Curl

**Status**: Unverified

## Overview

Curl is a versatile tool for making HTTP requests, uploading files, and testing web vulnerabilities like those in the Snapchat attack chain.

## Description

Supports various protocols and is commonly used in offensive security for crafting requests, testing redirects, and uploading payloads.

## Features

- Feature 1: HTTP/HTTPS support
- Feature 2: File uploads
- Feature 3: Header manipulation

## Installation

### Requirements

- Package manager like apt or brew

### Install Commands

```bash
sudo apt install curl  # On Debian-based systems
```

## Basic Usage

```bash
curl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-X` | Specify request method |
| `-F` | Multipart form data |

## Examples

### Example 1: Basic Usage

```bash
curl https://example.com
```

### Example 2: Advanced Usage

```bash
curl -X POST -F 'file=@path' https://upload.site
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Remote File Copy]]

### Tactics

- [[Initial Access]]
- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Command-line logs
- Detection method 2: Network traffic patterns

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
- [[Wget]]

## References

- https://curl.se/docs/
- Man pages
