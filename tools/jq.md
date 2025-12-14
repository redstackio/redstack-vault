---
id: tool-uuid-002
url: 'https://jqlang.github.io/jq/'
tags:
  - json
  - parse
  - cli
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.508Z'
validated: true
submitted: true
---
# jq

**Status**: Unverified

## Overview

Command-line JSON processor for extracting fields from API responses, used here to parse GitLab import_error for SSRF leaks.

## Description

Lightweight tool to query and manipulate JSON, ideal for piping curl output to extract specific keys like .import_error in security testing.

## Features

- Feature 1: Selectors like .field
- Feature 2: Filters and transformations
- Feature 3: Streaming for large JSON

## Installation

### Requirements

- Linux/Unix system

### Install Commands

```bash
# Ubuntu/Debian
sudo apt install jq
# Or from source
```

## Basic Usage

```bash
curl ... | jq .key
```

### Common Options

| Option | Description |
|--------|-------------|
| `.key` | Extract field |
| `-r` | Raw output |

## Examples

### Example 1: Basic Usage

```bash
echo '{"error":"test"}' | jq .error
```

### Example 2: Advanced Usage

```bash
curl api | jq '.projects[] | .import_error'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Data from Local System]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process: jq in ps aux
- Common in recon scripts

## Related Procedures

- [[procedures/Check-Import-Status-for-SSRF-Result]]

## Related Tools

- [[curl]]

## References

- Official: https://jqlang.github.io/jq/
