---
url: ''
tags:
  - file-extraction
type: tool
platforms:
  - Linux
  - Windows
  - macOS
description: A utility for extracting files from ZIP archives.
id: 6ac378e4-c34b-49a2-9e48-df3d35a37deb
created_at: '2025-12-11T03:47:57.591Z'
updated_at: '2025-12-11T03:47:57.591Z'
verified: false
validated: true
submitted: true
---
# unzip

**Status**: Unverified

## Overview

unzip is a standard tool for decompressing ZIP files, used here to extract PoC files for the GitLab exploit.

## Description

It extracts files from ZIP archives, preserving directory structures.

## Features

- Extract ZIP files
- List contents
- Test archives

## Installation

### Requirements

- None specific

### Install Commands

```bash
sudo apt install unzip
```

## Basic Usage

```bash
unzip --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-l` | List contents |
| `-v` | Verbose |

## Examples

### Example 1: Basic Usage

```bash
unzip file.zip
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]]

### Tactics

- [[Initial Access]]

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

- #zip

## References

- man unzip
