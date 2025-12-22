---
url: null
tags:
  - extraction
  - file-handling
type: tool
platforms:
  - Windows
  - Linux
  - macOS
description: Utility for extracting compressed archives
id: 27449129-fa8f-4e33-83f2-f9c4654790af
created_at: '2025-12-14T00:11:25.201Z'
updated_at: '2025-12-14T00:11:25.201Z'
verified: false
validated: true
submitted: true
---
# Unzipping Tool

**Status**: Unverified

## Overview

Generic tool for unzipping files, used here to extract CS:GO Panorama UI files from code.pbin.

## Description

Tools like unzip or 7-Zip are used to decompress archives for analysis in security research.

## Features

- Archive extraction
- Support for multiple formats
- Command-line interface

## Installation

### Requirements

- OS-specific package

### Install Commands

```bash
# On Linux
apt install unzip
```

## Basic Usage

```bash
unzip --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-d` | Extract to directory |

## Examples

### Example 1: Basic Usage

```bash
unzip code.pbin
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Data from Local System]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor file extraction events

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/7zip]]

## References

- Unzip documentation
