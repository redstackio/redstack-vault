---
url: 'https://github.com/electron/asar'
tags:
  - extraction
  - electron
type: tool
platforms:
  - macOS
  - Linux
  - Windows
description: Tool for extracting and packing Electron ASAR archives.
id: 5d451b25-6c16-410c-855b-a45ef2864cd6
created_at: '2025-12-11T03:48:06.060Z'
updated_at: '2025-12-11T03:48:06.060Z'
verified: false
validated: true
submitted: true
---
# asar

**Status**: Unverified

## Overview

asar is a command-line tool for handling Electron's ASAR format, primarily used to extract app bundles for reverse engineering and security analysis.

## Description

It allows unpacking ASAR files to inspect contents, useful in identifying exposed credentials or vulnerabilities in Electron apps.

## Features

- Extract ASAR archives
- Pack directories into ASAR
- List archive contents

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm install -g asar
```

## Basic Usage

```bash
asar --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `extract` | Extract archive to directory |
| `pack` | Pack directory to archive |

## Examples

### Example 1: Basic Usage

```bash
asar extract app.asar out-dir
```

### Example 2: Advanced Usage

```bash
asar list app.asar
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]]

### Tactics

- [[Credential Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor npm installs of asar
- Check for ASAR extraction in temp directories

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- #curl
- #git

## References

- https://github.com/electron/asar
