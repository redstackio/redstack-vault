---
url: null
tags:
  - editor
  - analysis
type: tool
platforms:
  - Web
description: Text editor used for pasting and analyzing URLs to observe protocols
id: 30f2ca3f-7557-494c-a0b9-1dac0d038292
created_at: '2025-12-11T06:10:15.801Z'
updated_at: '2025-12-11T06:10:15.801Z'
verified: false
validated: true
submitted: true
---
# Sublime Text

**Status**: Unverified

## Overview

Sublime Text is a sophisticated text editor for code, markup, and prose, often used in security workflows for inspecting and editing text-based data like URLs.

## Description

In security testing, it's employed to paste and examine links, configurations, or scripts without executing them, helping identify issues like insecure protocols.

## Features

- Syntax highlighting
- Multi-platform support
- Plugin ecosystem

## Installation

### Requirements

- Compatible OS
- Download from official site

### Install Commands

```bash
# Install via package manager or direct download
```

## Basic Usage

```bash
subl file.txt
```

### Common Options

| Option | Description |
|--------|-------------|
| `-n` | Open new window |
| `-a` | Add to existing window |

## Examples

### Example 1: Basic Usage

```bash
subl
# Paste link inside editor
```

### Example 2: Advanced Usage

```bash
subl -n link.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- File access logs
- Process monitoring

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[VS Code]]
- [[Notepad++]]

## References

- https://www.sublimetext.com/
