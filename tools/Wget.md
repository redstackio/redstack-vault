---
id: tool-3
url: null
tags:
  - http
  - download
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.467Z'
validated: true
submitted: true
---
# wget

**Status**: Unverified

## Overview

GNU wget is a command-line tool for downloading files from HTTP/HTTPS, used here to query GCP metadata without curl.

## Description

In cloud attacks, wget fetches instance metadata tokens via the internal metadata server, requiring the Metadata-Flavor header for auth.

## Features

- Feature 1: Non-interactive downloads
- Feature 2: Header support for auth
- Feature 3: Output to file or stdout

## Installation

### Requirements

- Standard in most Linux distros

### Install Commands

```bash
# Ubuntu
apt install wget
# Or already present in Alpine
```

## Basic Usage

```bash
wget --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--header` | Custom headers |
| `-O` | Output file |
| `-q` | Quiet mode |

## Examples

### Example 1: Basic Usage

```bash
wget http://example.com/file.txt
```

### Example 2: Advanced Usage

```bash
wget --header 'Auth: token' http://internal/endpoint -O output
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[Cloud Instance Metadata API]] Cloud Instance Metadata API

### Tactics

- [[Command and Control]] Command and Control

## Detection

- Network logs for metadata.google.internal requests
- Process monitoring for wget with internal IPs
- Pod logs showing wget executions

## Related Procedures

- [[procedures/Retrieve-GCP-Metadata-Token-and-Bucket-Name]]

## Related Tools

- [[tools/curl]]
- [[tools/gcloud]]

## References

- Man page: wget(1)
- GNU docs
