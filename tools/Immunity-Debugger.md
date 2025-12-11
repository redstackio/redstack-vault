---
url: 'https://www.immunityinc.com/products/debugger/'
tags:
  - debugging
  - reverse-engineering
type: tool
platforms:
  - Windows
description: Debugger for analyzing Windows executables and crashes in exploit development.
id: 10954a4e-b579-4d65-b1dd-44cdc4a5b238
created_at: '2025-12-11T06:10:40.306Z'
updated_at: '2025-12-11T06:10:40.306Z'
verified: false
validated: true
submitted: true
---
# Immunity Debugger

**Status**: Unverified

## Overview

Immunity Debugger is a powerful tool for reverse engineering and exploit development, particularly for analyzing crashes and stack layouts in Windows applications.

## Description

It allows attaching to processes like Steam.exe to inspect buffer overflows, ROP gadgets, and memory protections during vulnerability research.

## Features

- Python scripting support
- Heap and stack visualization
- Anti-anti-debugging capabilities

## Installation

### Requirements

- Windows OS

### Install Commands

```bash
# Download and install from official site
```

## Basic Usage

```bash
immdbg.exe
```

### Common Options

| Option | Description |
|--------|-------------|
| `-attach` | Attach to process |

## Examples

### Example 1: Basic Usage

```bash
immdbg.exe -p Steam.exe
```

### Example 2: Advanced Usage

```bash
# Run script inside debugger
!mona find -s "pop pop ret" -m Steam.exe
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor debugger attachments to critical processes
- Look for Immunity Debugger installations

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Python]]

## References

- https://www.immunityinc.com/documentation/immdbg/
