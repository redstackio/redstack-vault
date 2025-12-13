---
url: null
tags:
  - build
type: tool
platforms:
  - Linux
description: Build automation tool to compile software from source.
id: 551213aa-59b3-4b81-925d-2ccd98d6f41d
created_at: '2025-12-13T09:01:22.035Z'
updated_at: '2025-12-13T09:01:22.035Z'
verified: false
validated: true
submitted: true
---
# make

**Status**: Unverified

## Overview

make is a build automation tool that controls the generation of executables from source code.

## Description

Used to compile HAProxy with TARGET=linux2628.

## Features

- Dependency tracking
- Parallel builds
- Makefile support

## Installation

### Requirements

- Linux

### Install Commands

```bash
apt install make
```

## Basic Usage

```bash
make
```

### Common Options

| Option | Description |
|--------|-------------|
| `TARGET` | Build target |

## Examples

### Example 1: Basic Usage

```bash
make TARGET=linux2628
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques



### Tactics



## Detection

Indicators and methods for detecting this tool's usage:

- Monitor compilation commands

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

- make documentation
