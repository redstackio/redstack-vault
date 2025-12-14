---
id: tool-002
url: 'https://visualvm.github.io/'
tags:
  - memory-analysis
  - java
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:47.355Z'
validated: true
submitted: true
---
# VisualVM

**Status**: Unverified

## Overview

VisualVM is a visual tool for monitoring and profiling Java applications, including offline analysis of heap dumps to extract runtime data like credentials.

## Description

It supports loading heap dumps to browse memory, threads, and classes, making it suitable for post-exploitation analysis of leaked JVM memory from actuator endpoints.

## Features

- Feature 1: Live monitoring and offline dump analysis
- Feature 2: Heap walker for object inspection
- Feature 3: Plugin support for advanced queries

## Installation

### Requirements

- Java 8 or higher

### Install Commands

```bash
# Download and run
wget https://github.com/oracle/visualvm/releases/download/2.1.3/visualvm_213_linux.tar.gz
tar -xzf visualvm_213_linux.tar.gz
```

## Basic Usage

```bash
./bin/visualvm
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-J-Xmx` | Increase heap for large dumps |

## Examples

### Example 1: Basic Usage

```bash
./bin/visualvm
# Load heap dump via File > Load...
```

### Example 2: Advanced Usage

```bash
./bin/visualvm -J-Xmx4g
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Running visualvm process
- Access to .hprof files in temp directories

## Related Procedures


## Related Tools

- [[tools/Eclipse-Memory-Analyzer]]

## References

- Official documentation: https://visualvm.github.io/documentation.html
