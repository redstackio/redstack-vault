---
url: null
tags:
  - download
type: tool
platforms:
  - Linux
description: Command-line tool to download files from the web.
id: 630e5c25-ce7f-483f-8b86-35bef71b6c42
created_at: '2025-12-13T09:01:22.044Z'
updated_at: '2025-12-13T09:01:22.044Z'
verified: false
validated: true
submitted: true
---
# wget

**Status**: Unverified

## Overview

wget is a non-interactive command-line tool for downloading files via HTTP, HTTPS, and FTP.

## Description

Used to fetch HAProxy source code.

## Features

- Recursive downloads
- Resume support
- Proxy support

## Installation

### Requirements

- Linux package manager

### Install Commands

```bash
apt install wget
```

## Basic Usage

```bash
wget url
```

### Common Options

| Option | Description |
|--------|-------------|
| `-O` | Output file |

## Examples

### Example 1: Basic Usage

```bash
wget https://example.com/file
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor download commands

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools



## References

- wget man page
