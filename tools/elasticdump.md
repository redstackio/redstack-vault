---
url: 'https://github.com/elasticsearch-dump/elasticsearch-dump'
tags:
  - elasticsearch
  - data-migration
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-30T00:00:00Z'
updated_at: '2025-12-14T17:31:19.263Z'
id: f452f43a-988e-48c0-9688-88f639b23527
validated: true
submitted: true
---
# elasticdump

**Status**: Unverified

## Overview

elasticdump is a tool for dumping and restoring Elasticsearch data, useful as an alternative for extracting indexes in security assessments of exposed instances.

## Description

It facilitates backup and transfer of Elasticsearch data via JSON exports, supporting unauthenticated access scenarios. In red teaming, it's used for mirroring data from vulnerable services like open port 9200 setups.

## Features

- Feature 1: Full index or mapping dumps
- Feature 2: Input/output to files or streams
- Feature 3: Support for multiple Elasticsearch versions

## Installation

### Requirements

- Node.js 10+

### Install Commands

```bash
npm install elasticdump -g
```

## Basic Usage

```bash
elasticdump --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `--input` | Source URL or file |
| `--output` | Destination file or URL |
| `--type` | data, mapping, or analyzer |

## Examples

### Example 1: Basic Usage

```bash
elasticdump --input=https://elasticsearch.example.com:9200/aim_high --output=data.json --type=data
```

### Example 2: Advanced Usage

```bash
elasticdump --input=https://elasticsearch.example.com:9200 --output=$ --type=mapping
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- HTTP requests to _bulk or _search from Node.js processes
- File artifacts like .json dumps

## Related Procedures

- [[procedures/Extract-Data-from-Elasticsearch-Index-with-estk]]

## Related Tools

- [[tools/estk]]

## References

- Official GitHub documentation
