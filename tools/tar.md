---
url: null
tags:
  - archive
type: tool
platforms:
  - Linux
description: Tool to extract and create tar archives.
id: 3f0427d0-94e2-44d8-b3c5-a3eb64d575e7
created_at: '2025-12-13T09:01:22.040Z'
updated_at: '2025-12-13T09:01:22.040Z'
verified: false
validated: true
submitted: true
---
# tar

**Status**: Unverified

## Overview

tar is a utility for archiving files, often used with compression like gzip.

## Description

Used to extract HAProxy tarball.

## Features

- Create archives
- Extract files
- Compression support

## Installation

### Requirements

- Standard on Linux

### Install Commands

```bash
# Built-in
```

## Basic Usage

```bash
tar xvf file.tar
```

### Common Options

| Option | Description |
|--------|-------------|
| `x` | Extract |
| `z` | Gzip |

## Examples

### Example 1: Basic Usage

```bash
tar zxvf file.tar.gz
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques



### Tactics



## Detection

Indicators and methods for detecting this tool's usage:

- Monitor archive operations

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools



## References

- tar man page
