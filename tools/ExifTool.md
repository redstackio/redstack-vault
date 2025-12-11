---
url: 'https://exiftool.org/'
tags:
  - metadata
  - image-processing
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: >-
  A platform-independent Perl library plus a command-line application for
  reading, writing, and editing meta information in a wide variety of files.
id: 482fb1c3-d088-4e9d-9c6f-4ffcdd4f8a55
created_at: '2025-12-11T03:47:57.632Z'
updated_at: '2025-12-11T03:47:57.632Z'
verified: false
validated: true
submitted: true
---
# ExifTool

**Status**: Unverified

## Overview

ExifTool is used for manipulating image metadata, but in this context, it's vulnerable to RCE when processing crafted DjVu files in GitLab uploads.

## Description

It determines file type by content, leading to eval of DjVu annotations with insufficient escaping, enabling code injection.

## Features

- Read/write metadata in images
- Supports multiple file formats
- Command-line interface

## Installation

### Requirements

- Perl installed

### Install Commands

```bash
sudo apt install libimage-exiftool-perl
```

## Basic Usage

```bash
exiftool --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-all=` | Remove all tags |

## Examples

### Example 1: Basic Usage

```bash
exiftool image.jpg
```

### Example 2: Advanced Usage

```bash
exiftool -all= image.jpg
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor Perl eval executions
- Check for unexpected file creations

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Perl]]

## References

- https://exiftool.org/
