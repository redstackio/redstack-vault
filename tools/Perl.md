---
url: 'https://www.perl.org/'
tags:
  - programming
  - eval-injection
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: 'A high-level, general-purpose programming language known for text processing.'
id: a1c0c6f4-e196-43a8-94b3-e2ddebf3e829
created_at: '2025-12-11T03:47:57.548Z'
updated_at: '2025-12-11T03:47:57.548Z'
verified: false
validated: true
submitted: true
---
# Perl

**Status**: Unverified

## Overview

Perl executes the vulnerable eval on DjVu annotations in ExifTool, allowing code injection.

## Description

Used in ExifTool for processing, with qx for command execution.

## Features

- Text manipulation
- Eval capabilities
- System command execution

## Installation

### Requirements

- None specific

### Install Commands

```bash
sudo apt install perl
```

## Basic Usage

```bash
perl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-w` | Enable warnings |
| `-e` | Execute code |

## Examples

### Example 1: Basic Usage

```bash
perl -e 'print "Hello\n"'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Windows Command Shell]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor Perl eval usages in logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Ruby]]

## References

- https://www.perl.org/
