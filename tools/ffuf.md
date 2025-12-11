---
url: 'https://github.com/ffuf/ffuf'
tags:
  - fuzzing
  - recon
type: tool
platforms:
  - Linux
  - macOS
  - Windows
description: Fast web fuzzer for discovering hidden files and directories
id: d4875601-c1b6-43eb-980b-0f3c935c3391
created_at: '2025-12-11T06:10:16.220Z'
updated_at: '2025-12-11T06:10:16.220Z'
verified: false
validated: true
submitted: true
---
# ffuf

**Status**: Unverified

## Overview

ffuf is a fast web fuzzer used for brute-forcing and discovering hidden resources on web servers.

## Description

It supports customizable wordlists, filters, and multi-threading for efficient reconnaissance in offensive security.

## Features

- Feature 1: High-speed fuzzing
- Feature 2: Customizable filters
- Feature 3: Output formatting

## Installation

### Requirements

- Go installed

### Install Commands

```bash
go install github.com/ffuf/ffuf/v2@latest
```

## Basic Usage

```bash
ffuf --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-w` | Wordlist |

## Examples

### Example 1: Basic Usage

```bash
ffuf -u https://FUZZ.target.com -w wordlist.txt
```

### Example 2: Advanced Usage

```bash
ffuf -u https://FUZZ.target.com -w wordlist.txt -fc 404
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- High volume of requests from single IP
- Unusual URL patterns in access logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[dirbuster]]
- [[gobuster]]

## References

- https://github.com/ffuf/ffuf
