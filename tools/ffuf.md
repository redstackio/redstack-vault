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
description: Fast web fuzzer for discovering content and vulnerabilities
id: 87d064d8-e62e-4007-ab1d-28f39ba7d94b
created_at: '2025-12-11T03:47:39.534Z'
updated_at: '2025-12-11T03:47:39.534Z'
verified: false
validated: true
submitted: true
---
# ffuf

**Status**: Unverified

## Overview

ffuf is a fast web fuzzer used for brute-forcing directories, subdomains, and parameters in web applications.

## Description

It supports customizable wordlists, filters, and matchers for efficient discovery in security testing.

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
| `-u` | URL to fuzz |

## Examples

### Example 1: Basic Usage

```bash
ffuf -u https://target.com/FUZZ -w wordlist.txt
```

### Example 2: Advanced Usage

```bash
ffuf -u https://target.com/FUZZ -w wordlist.txt -fc 404
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: High volume of HTTP requests
- Detection method 2: Unusual User-Agent strings

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #dirbuster
- [[Gobuster]]

## References

- Official GitHub repository
