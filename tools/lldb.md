---
id: 14ebeb8e-153b-406d-90a5-b2eedd90602c
name: lldb
type: tool
verified: false
created_at: '2025-12-11T03:47:48.097Z'
updated_at: '2025-12-11T03:47:48.097Z'
platforms:
  - macOS
tags:
  - debugging
  - analysis
url: null
description: Debugger for analyzing program crashes and backtraces.
validated: true
submitted: true
---

# lldb

**Status**: Unverified

## Overview

lldb is a high-performance debugger used to analyze segmentation faults, inspect backtraces, and read registers in crashed programs like mruby.

## Description

Part of the LLVM project, lldb provides detailed debugging capabilities for macOS and other platforms, configured here with target creation and run arguments.

## Features

- Backtrace inspection
- Register reading
- Target and argument configuration

## Installation

### Requirements

- macOS with Xcode

### Install Commands

```bash
xcode-select --install
```

## Basic Usage

```bash
lldb --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |

## Examples

### Example 1: Basic Usage

```bash
lldb executable
```

### Example 2: Advanced Usage

```bash
lldb executable arg
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for lldb process attachments
- Log debugger commands in development environments

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #mruby
- #sandbox

## References

- Official LLVM documentation
