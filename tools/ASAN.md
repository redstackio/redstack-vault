---
url: ''
tags:
  - memory-analysis
type: tool
platforms:
  - macOS
description: Address Sanitizer for detecting memory errors
id: 24b07930-06c1-4787-879e-b6ffa1913fa0
created_at: '2025-12-11T03:47:47.969Z'
updated_at: '2025-12-11T03:47:47.969Z'
verified: false
validated: true
submitted: true
---
# ASAN

**Status**: Unverified

## Overview

Address Sanitizer (ASAN) detects memory corruption bugs like buffer overflows during compilation and runtime.

## Description

Enabled in builds to catch errors in mruby executions.

## Features

- Buffer overflow detection
- Use-after-free checks

## Installation

### Requirements

- Compiler with ASAN support

### Install Commands

```bash
# Enable during compilation: make with ASAN flags
```

## Basic Usage

```bash
# Run ASAN-enabled binary
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Runtime flags |

## Examples

### Example 1: Basic Usage

```bash
ASAN-enabled-mruby script.rb
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Account Access Removal]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- ASAN runtime logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #lldb

## References

- Clang ASAN documentation
