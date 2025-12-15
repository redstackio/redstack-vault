---
id: tool-8
url: null
tags:
  - encode
  - decode
type: command
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.454Z'
validated: true
submitted: true
---
# base64

**Status**: Unverified

## Overview

base64 is a standard Unix utility for encoding/decoding base64 data, used to decode PKI materials from kOps YAML.

## Description

In extractions, pipes decoded output to files for PEM format, common in cloud config parsing.

## Features

- Feature 1: Encode stdin/stdout
- Feature 2: Decode with -d
- Feature 3: Wrap options

## Installation

### Requirements

- Coreutils

### Install Commands

```bash
# Usually pre-installed
apt install coreutils
```

## Basic Usage

```bash
base64 --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-d` | Decode |
| `-w 0` | No wrap |

## Examples

### Example 1: Basic Usage

```bash
echo 'data' | base64 -d
```

### Example 2: Advanced Usage

```bash
cat encoded.txt | base64 -d > decoded.pem
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Deobfuscate-Decode Files or Information]] Deobfuscate/Decode Files or Information

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

- Rare, as it's standard; monitor in pipelines with yq/gcloud

## Related Procedures

- [[procedures/Extract-Kubernetes-CA-Keys-from-State-Bucket]]

## Related Tools

- [[tools/openssl]] (base64 mode)

## References

- Man page: base64(1)
