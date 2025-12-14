---
id: tool-trurl-001
url: 'https://github.com/curl/trurl'
tags:
  - url
  - parse
  - manipulate
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.510Z'
configuration: Latest version (post-v0.8)
validated: true
submitted: true
---
# trurl

**Status**: Unverified

## Overview

trurl is a command-line tool built on libcurl's CURLU API for parsing, modifying, and extracting URL components; used here to demonstrate host/zone separation in IPv6 URLs.

## Description

Ideal for security testing URL handling; extracts fields like {host} and {zoneid}, showing libcurl's stripping behavior. Older versions (<v0.8) had issues, so use latest for accurate IPv6 support.

## Features

- Feature 1: URL templating and variable extraction.
- Feature 2: Supports percent-decoding and IPv6 literals.
- Feature 3: Non-interactive parsing for scripts.

## Installation

### Requirements

- libcurl and build tools.

### Install Commands

```bash
# From source
git clone https://github.com/curl/trurl.git
cd trurl
make
```

## Basic Usage

```bash
trurl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--get` | Output using template |
| `-s` | Set base URL |

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

- [[Exploit Public-Facing Application]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process lists showing trurl executions.
- URL manipulation logs.

## Related Procedures


## Related Tools

- [[tools/libcurl]]

## References

- Official documentation: https://github.com/curl/trurl
