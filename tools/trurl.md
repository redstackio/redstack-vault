---
id: tool-trurl
url: 'https://github.com/curl/trurl'
tags:
  - url
  - parse
  - cli
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.025Z'
validated: true
submitted: true
---
# trurl

**Status**: Unverified

## Overview

trurl is a command-line tool frontend to libcurl's CURLU API for URL parsing and manipulation, used here to test and demonstrate extraction of IPv6 zone IDs.

## Description

Facilitates testing libcurl behaviors like separating {host} and {zoneid} in URLs. Ideal for verifying the zone omission flaw in a CLI context without full app integration.

## Features

- Feature 1: Template-based output for URL components
- Feature 2: Supports percent-encoded elements
- Feature 3: IPv6 literal handling

## Installation

### Requirements

- libcurl development files

### Install Commands

```bash
# Build from source
git clone https://github.com/curl/trurl.git
cd trurl && make
```

## Basic Usage

```bash
trurl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--get` | Output using template |
| `-s` | Set URL source |

## Examples

### Example 1: Basic Usage

```bash
trurl --get '{host}' 'http://example.com'
```

### Example 2: Advanced Usage

```bash
trurl --get 'Host: {host} Zone: {zoneid}' 'http://[fe80::1%25eth0]/'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Process name 'trurl' in logs
- URL parsing patterns in command history

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/libcurl]]

## References

- Official documentation: https://github.com/curl/trurl
- Related resources: libcurl docs
