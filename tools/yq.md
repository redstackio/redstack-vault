---
id: tool-2
url: 'https://github.com/mikefarah/yq'
tags:
  - yaml
  - parse
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.471Z'
validated: true
submitted: true
---
# yq

**Status**: Unverified

## Overview

yq is a lightweight YAML processor like jq for JSON, used to query and extract data from YAML files such as kOps state configs.

## Description

In offensive ops, yq parses structured data like keyset.yaml to pull base64 materials without full YAML loaders, aiding in credential extraction from cloud configs.

## Features

- Feature 1: jq-like syntax for YAML/JSON
- Feature 2: Evaluation and update modes
- Feature 3: Streaming input support

## Installation

### Requirements

- Go 1.13+

### Install Commands

```bash
# Snap
go install github.com/mikefarah/yq/v4@latest
# Or brew install yq
```

## Basic Usage

```bash
yq --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `e` | Evaluate expression |
| `r` | Raw output |

## Examples

### Example 1: Basic Usage

```bash
yq e '.key' file.yaml
```

### Example 2: Advanced Usage

```bash
cat file.yaml | yq e '.spec.keys[0].material' -
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials In Files]] Credentials In Files

### Tactics

- [[Collection]] Collection

## Detection

- Look for yq in process lists during data exfil
- Monitor YAML parsing in scripts
- Detect in container layers

## Related Procedures

- [[procedures/Extract-Kubernetes-CA-Keys-from-State-Bucket]]

## Related Tools

- [[tools/jq]]
- [[tools/kubectl]]

## References

- Official: https://mikefarah.gitbook.io/yq/
- jq compatibility docs
