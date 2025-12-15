---
url: 'https://stedolan.github.io/jq/'
tags:
  - json
  - parsing
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.543Z'
id: b5680139-f995-44eb-9653-9ca5edaf8c46
validated: true
submitted: true
---
# jq

**Status**: Verified

## Overview

jq is a lightweight command-line JSON processor, used for parsing, filtering, and transforming JSON data from API responses in security assessments.

## Description

jq excels at querying JSON structures with a simple syntax, enabling extraction of specific fields like IDs from leaked API data, which is crucial for analyzing information disclosure vulnerabilities.

## Features

- Feature 1: Filters like .data[] | .id for array traversal
- Feature 2: Support for conditional selects and outputs
- Feature 3: Streaming for large JSON files

## Installation

### Requirements

- Go or package manager access

### Install Commands

```bash
# On Ubuntu/Debian
apt update && apt install jq

# On macOS
brew install jq
```

## Basic Usage

```bash
jq --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-r` | Raw output strings |
| `-c` | Compact output |
| `--arg` | Pass variables |

## Examples

### Example 1: Basic Usage

```bash
jq '.name' input.json
```

### Example 2: Advanced Usage

```bash
jq '.data[] | select(.id > 100) | .id' api_response.json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]] Network Sniffing? No, more [[Data from Local System]] Data from Local System

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Process listings showing jq parsing JSON files
- Script logs with jq commands in recon workflows

## Related Procedures

- [[procedures/Expose-API-Identifiers-for-IDOR-Exploitation]]

## Related Tools

- [[tools/curl]]
- [[tools/Python]]

## References

- Official documentation: https://stedolan.github.io/jq/manual/
- Related resources: JSON parsing in pentesting guides
