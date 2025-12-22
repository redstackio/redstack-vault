---
url: 'https://github.com/target/estk'
tags:
  - elasticsearch
  - recon
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-30T00:00:00Z'
updated_at: '2025-12-14T17:31:19.267Z'
id: cc6969d6-e304-43e1-8753-8fcdff6d2197
validated: true
submitted: true
---
# estk

**Status**: Unverified

## Overview

estk is a command-line tool for interacting with Elasticsearch instances, primarily used in security testing to list indexes, dump data, and verify insecure configurations like missing authentication.

## Description

Designed for quick probing of Elasticsearch endpoints, estk supports version detection, index enumeration, and data extraction over HTTP/HTTPS. In offensive ops, it's ideal for confirming exposed services and exfiltrating data from unauthenticated instances like version 2.7.0 on port 9200.

## Features

- Feature 1: Automatic version detection for Elasticsearch
- Feature 2: Index listing with doc counts and sizes
- Feature 3: Full index dumping in JSON

## Installation

### Requirements

- Go 1.16+ installed

### Install Commands

```bash
go install github.com/target/estk@latest
```

## Basic Usage

```bash
estk --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--url` | Target Elasticsearch URL |

## Examples

### Example 1: Basic Usage

```bash
estk --url=https://elasticsearch.example.com:9200 list
```

### Example 2: Advanced Usage

```bash
estk dump --url=https://elasticsearch.example.com:9200 --index=aim_high
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network logs showing _cat/indices or _search requests from unknown IPs
- Process monitoring for 'estk' binary

## Related Procedures

- [[procedures/Enumerate-Elasticsearch-Indexes-with-estk]]
- [[procedures/Extract-Data-from-Elasticsearch-Index-with-estk]]

## Related Tools

- [[tools/elasticdump]]

## References

- GitHub repository for estk
