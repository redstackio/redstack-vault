---
url: ''
tags:
  - editor
  - reverse-engineering
type: tool
platforms:
  - Linux
  - Windows
description: 'Text editor for viewing and searching files, including binaries.'
id: ab2bef24-2ca8-432e-b35d-9d642addc712
created_at: '2025-12-11T06:10:17.274Z'
updated_at: '2025-12-11T06:10:17.274Z'
verified: false
validated: true
submitted: true
---
# Vim

**Status**: Unverified

## Overview

Vim is a powerful text editor used for searching and viewing string tables in binaries.

## Description

Assists in reverse engineering by navigating large binary files.

## Features

- Search and navigation
- Binary mode viewing

## Installation

### Requirements

- Any OS

### Install Commands

```bash
apt install vim
```

## Basic Usage

```bash
vim steam.exe
```

### Common Options

| Option | Description |
|--------|-------------|
| `/pattern` | Search |

## Examples

### Example 1: Basic Usage

```bash
vim steam.exe
/search steam://
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[User Execution]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for vim on binaries

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Binary-Grep]]

## References

- https://www.vim.org/
