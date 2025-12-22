---
url: ''
tags:
  - debug
  - analysis
type: tool
platforms:
  - Linux
description: >-
  Tool for inspecting variables and execution during code generation to identify
  root causes
id: d2fc30d9-d09c-4c1d-81b3-6dae06b2e32d
created_at: '2025-12-11T03:47:47.816Z'
updated_at: '2025-12-11T03:47:47.816Z'
verified: false
validated: true
submitted: true
---
# debugger

**Status**: Unverified

## Overview

A debugging tool (e.g., gdb) used to inspect mruby's code generation process and identify bugs like unpopped contexts.

## Description

Enables stepping through C code in mruby to analyze loop contexts and jump calculations.

## Features

- Variable inspection
- Breakpoints
- Stack tracing

## Installation

### Requirements

- C development tools

### Install Commands

```bash
sudo apt install gdb
```

## Basic Usage

```bash
gdb --args mruby script.rb
```

### Common Options

| Option | Description |
|--------|-------------|
| `-q` | Quiet mode |

## Examples

### Example 1: Basic Usage

```bash
gdb mruby
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor debugger attachments to processes

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

## References

- gdb documentation
