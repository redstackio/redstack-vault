---
url: 'https://www.npmjs.com/package/asar'
tags:
  - electron
  - extraction
type: tool
platforms:
  - macOS
  - Linux
  - Windows
description: Tool for handling Electron asar archives
id: 95e0b3f4-f3c7-4a06-b9eb-06ad9287dfb3
created_at: '2025-12-11T06:10:40.463Z'
updated_at: '2025-12-11T06:10:40.463Z'
verified: false
validated: true
submitted: true
---
# asar

**Status**: Unverified

## Overview

asar is a command-line tool for creating and extracting Electron's asar archives, essential for security researchers to unpack apps and discover embedded sensitive data like credentials.

## Description

Used in offensive security to extract contents from Electron apps, revealing files such as .env that may contain leaked tokens, as seen in credential exposure scenarios.

## Features

- Archive creation and extraction
- Listing archive contents
- Packing directories into asar

## Installation

### Requirements

- Node.js

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
| `extract` | Extract archive |
| `list` | List files |

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

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor asar command executions
- Detect file extractions in temp directories

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/npx]]
- [[electron]]

## References

- https://www.npmjs.com/package/asar
