---
url: null
tags:
  - php
  - serialization
type: tool
platforms:
  - Linux
description: >-
  Custom script for generating serialized PHP objects with malicious XML for
  XXE.
id: 2600cf59-abef-47a4-b0b2-14ce3965193c
created_at: '2025-12-13T09:00:27.999Z'
updated_at: '2025-12-13T09:00:27.999Z'
verified: false
validated: true
submitted: true
---
# Custom PHP Script

**Status**: Unverified

## Overview

A custom PHP script designed to create serialized objects for exploiting PHP object injection vulnerabilities, particularly for embedding XXE payloads.

## Description

The script takes a URL as input and generates a serialized ConfigFile object containing malicious XML that triggers XXE when parsed. It's base64-encoded for upload.

## Features

- Generates serialized PHP objects
- Embeds custom URLs in XML entities
- Base64 encoding for payload delivery

## Installation

### Requirements

- PHP installed

### Install Commands

```bash
# No installation needed; run directly
```

## Basic Usage

```bash
php exploit.php --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `url` | Target URL for XXE entity |

## Examples

### Example 1: Basic Usage

```bash
php exploit.php http://localhost:1337
```

### Example 2: Advanced Usage

```bash
php exploit.php http://internal/update-status
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for PHP execution with unusual arguments
- Check logs for serialization patterns

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Netcat]]

## References

- HackerOne report: https://hackerone.com/reports/415501
