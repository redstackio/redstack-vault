---
url: ''
tags:
  - mruby
  - interactive-shell
type: tool
platforms:
  - Linux
description: Interactive shell for mruby scripting and testing
id: 796f8a1c-9dfa-4594-adc3-f14afa30b4ef
created_at: '2025-12-11T03:47:48.044Z'
updated_at: '2025-12-11T03:47:48.044Z'
verified: false
validated: true
submitted: true
---
# mirb

**Status**: Unverified

## Overview

mirb is an interactive REPL shell for mruby, allowing execution of Ruby-like code in an embedded environment, commonly used for testing vulnerabilities in mruby libraries.

## Description

mirb enables running PoC code like Decimal object creation and initialization to exploit assertions, making it essential for local testing of mruby-based vulnerabilities.

## Features

- Interactive code execution
- mruby script testing
- Integration with mruby extensions like mpdecimal

## Installation

### Requirements

- mruby compiled and installed
- Linux system

### Install Commands

```bash
# Assuming mruby is built, mirb is available in the bin directory
```

## Basic Usage

```bash
mirb
```

### Common Options

| Option | Description |
|--------|-------------|
| (none) | Starts interactive shell |

## Examples

### Example 1: Basic Usage

```bash
mirb
a = Decimal.new
```

### Example 2: Advanced Usage

```bash
mirb
a = Decimal.new
a.initialize a
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for mirb process launches in production
- Log unexpected mruby executions

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #irb
- [[Ruby]]

## References

- Official documentation: mruby GitHub
- Related resources: mruby documentation
