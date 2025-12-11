---
url: 'https://www.npmjs.com/package/npx'
tags:
  - npm
  - execution
type: tool
platforms:
  - macOS
  - Linux
  - Windows
description: Executes npm packages without global installation
id: 2bfe0a7e-0eb2-44cb-98ad-6b06f91821d4
created_at: '2025-12-11T06:10:40.472Z'
updated_at: '2025-12-11T06:10:40.472Z'
verified: false
validated: true
submitted: true
---
# npx

**Status**: Unverified

## Overview

npx is a tool for executing npm packages directly without installing them globally, commonly used to run one-off commands like asar extract in security testing for app dissection.

## Description

npx allows running packages from the npm registry or local paths, useful in offensive security for quick tool execution without setup, such as extracting Electron archives to find credentials.

## Features

- Executes packages without global install
- Supports local and remote packages
- Automatic installation if needed

## Installation

### Requirements

- Node.js installed

### Install Commands

```bash
npm install -g npx
```

## Basic Usage

```bash
npx --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--package` | Specify package to run |

## Examples

### Example 1: Basic Usage

```bash
npx asar extract app.asar out
```

### Example 2: Advanced Usage

```bash
npx --package=asar extract app.asar out
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor npm-related executions
- Log temporary package installations

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[npm]]
- [[tools/asar]]

## References

- https://www.npmjs.com/package/npx
